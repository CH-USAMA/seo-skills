#!/usr/bin/env python3
"""
seo_audit.py - generic on-page and technical SEO auditor. Standard library only (Python 3.8+).

What it does
  1. Finds the pages to audit: robots.txt -> sitemap(s) -> every URL (falls back to crawling from the homepage).
  2. Fetches each page WITHOUT following redirects (so redirected sitemap URLs show up) and parses the HTML.
  3. Checks titles, meta descriptions, H1s, canonicals, robots directives, images, links, structured data,
     placeholder/demo text, mixed content, language, duplicates across pages.
  4. Checks site-level hygiene: robots.txt, sitemap quality, http/https/www variants, soft-404 behaviour,
     broken internal links.
  5. Writes a JSON file (raw data + issues) and a Markdown report, and can diff against an earlier run.

Usage
  python seo_audit.py https://example.com
  python seo_audit.py https://example.com --out audit.json --md audit.md --max-urls 400
  python seo_audit.py https://example.com --baseline before.json      # shows fixed / new issues since last run
  python seo_audit.py https://example.com --urls-file urls.txt        # audit only these URLs

Severity:  P0 broken or harmful  |  P1 should fix  |  P2 worth fixing  |  P3 minor / informational
It is read-only: it only makes GET requests, politely (low concurrency, small delay).
"""
import argparse
import gzip
import html
import json
import random
import re
import string
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser

UA = 'Mozilla/5.0 (compatible; seo-site-audit/1.0; read-only audit)'

PLACEHOLDER_RE = re.compile(
    r'lorem ipsum|dolor sit amet|sed ut perspiciatis|consectetur adipiscing|placeholder text|your text here|'
    r'click here to edit|just another wordpress site|hello world!|sample page|demo content|john doe|'
    r'123 main st|205 middle road|\+ ?012 345 678',
    re.I)
GENERIC_ANCHORS = {'here', 'click here', 'read more', 'learn more', 'more', 'link', 'this', 'this link', 'click', 'details',
                   'view', 'view more', 'continue reading', 'go', 'read', 'see more'}
FILENAME_ALT_RE = re.compile(r'(?i)(\.(jpe?g|png|gif|webp|svg|avif)$)|^(img|dsc|image|photo|screenshot|untitled)[ _-]?\d*$|'
                             r'chatgpt|gemini[_ -]generated|\d{6,}|^[a-z0-9_-]+\d{3,}[a-z0-9_-]*$')


# ----------------------------------------------------------------------------- fetching
class Resp:
    def __init__(self, status=0, headers=None, body=b'', url='', error=''):
        self.status, self.headers, self.body, self.url, self.error = status, headers or {}, body, url, error

    def header(self, name, default=''):
        for k, v in self.headers.items():
            if k.lower() == name.lower():
                return v
        return default

    def text(self):
        ctype = self.header('Content-Type')
        m = re.search(r'charset=([\w-]+)', ctype, re.I)
        enc = m.group(1) if m else 'utf-8'
        try:
            return self.body.decode(enc, 'replace')
        except LookupError:
            return self.body.decode('utf-8', 'replace')


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def fetch_retry(url, tries=2, **kw):
    """fetch(), but try again after a short pause when the request itself failed (status 0): transient network errors
    and rate limiting are not 'broken pages'."""
    r = fetch(url, **kw)
    for _ in range(tries - 1):
        if r.status != 0:
            break
        time.sleep(1.5)
        r = fetch(url, **kw)
    return r


def fetch(url, follow=False, timeout=30, max_bytes=3_000_000, delay=0.0):
    if delay:
        time.sleep(delay)
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(_NoRedirect)
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Encoding': 'gzip',
                                               'Accept': 'text/html,application/xml;q=0.9,*/*;q=0.8'})
    try:
        r = opener.open(req, timeout=timeout)
        status, headers, final = r.status, dict(r.headers), r.geturl()
        body = r.read(max_bytes)
    except urllib.error.HTTPError as e:
        status, headers, final = e.code, dict(e.headers), url
        try:
            body = e.read(max_bytes)
        except Exception:
            body = b''
    except Exception as e:  # DNS, timeout, TLS ...
        return Resp(0, {}, b'', url, str(e)[:120])
    if any(k.lower() == 'content-encoding' and 'gzip' in v.lower() for k, v in headers.items()) or body[:2] == b'\x1f\x8b':
        try:
            body = gzip.decompress(body)
        except Exception:
            pass
    return Resp(status, headers, body, final)


# ----------------------------------------------------------------------------- HTML parsing
class PageParser(HTMLParser):
    SKIP = {'script', 'style', 'noscript', 'template', 'svg'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = ''
        self.title = ''
        self.in_title = False
        self.meta = {}
        self.links = []          # (rel, href, hreflang)
        self.headings = []       # (level, text)
        self._h_stack = None
        self.imgs = []           # attr dicts
        self.anchors = []        # dict(href, text, rel)
        self._a_stack = None
        self.jsonld = []
        self._in_ld = False
        self.words = 0
        self.resources = []      # (tag, url) for mixed-content checks
        self.dup_attrs = []      # (tag, attr)
        self._skip = 0
        self._in_body = False
        self._ld_buf = []

    def handle_starttag(self, tag, attrs):
        names = [k for k, _ in attrs]
        for n in set(names):
            if names.count(n) > 1:
                self.dup_attrs.append((tag, n))
        a = {k: (v if v is not None else '') for k, v in attrs}
        if tag == 'html':
            self.lang = a.get('lang', '')
        elif tag == 'body':
            self._in_body = True
        elif tag == 'title' and not self.title:
            self.in_title = True
        elif tag == 'meta':
            key = (a.get('name') or a.get('property') or a.get('http-equiv') or '').lower()
            if key and key not in self.meta:
                self.meta[key] = a.get('content', '')
        elif tag == 'link':
            rel = a.get('rel', '').lower()
            self.links.append((rel, a.get('href', ''), a.get('hreflang', '')))
            if 'stylesheet' in rel and a.get('href'):
                self.resources.append(('link', a['href']))
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self._h_stack = [int(tag[1]), []]
        elif tag == 'img':
            self.imgs.append(a)
            for k in ('src', 'data-src'):
                if a.get(k):
                    self.resources.append(('img', a[k]))
        elif tag == 'a':
            self._a_stack = {'href': a.get('href', ''), 'rel': a.get('rel', '').lower(), 'aria': a.get('aria-label', ''), 'text': [], 'img_alt': ''}
        elif tag == 'script':
            if a.get('type', '').lower() == 'application/ld+json':
                self._in_ld = True
                self._ld_buf = []
            elif a.get('src'):
                self.resources.append(('script', a['src']))
        elif tag in ('iframe', 'source', 'video', 'audio', 'embed') and a.get('src'):
            self.resources.append((tag, a['src']))
        if tag in self.SKIP:
            self._skip += 1
        if tag == 'img' and self._a_stack is not None:
            self._a_stack['img_alt'] = a.get('alt', '')

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6') and self._h_stack:
            self.headings.append((self._h_stack[0], re.sub(r'\s+', ' ', ''.join(self._h_stack[1])).strip()))
            self._h_stack = None
        elif tag == 'a' and self._a_stack is not None:
            st = self._a_stack
            st['text'] = re.sub(r'\s+', ' ', ''.join(st['text'])).strip()
            self.anchors.append(st)
            self._a_stack = None
        elif tag == 'script' and self._in_ld:
            self._in_ld = False
            self.jsonld.append(''.join(self._ld_buf))
        if tag in self.SKIP and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._in_ld:
            self._ld_buf.append(data)
            return
        if self.in_title:
            self.title += data
        if self._skip:
            return
        if self._h_stack is not None:
            self._h_stack[1].append(data)
        if self._a_stack is not None:
            self._a_stack['text'].append(data)
        if self._in_body:
            self.words += len(data.split())


def jsonld_types(blobs):
    types, invalid = set(), 0
    for b in blobs:
        try:
            data = json.loads(b)
        except Exception:
            invalid += 1
            continue
        stack = [data]
        while stack:
            x = stack.pop()
            if isinstance(x, dict):
                t = x.get('@type')
                if isinstance(t, str):
                    types.add(t)
                elif isinstance(t, list):
                    types.update(str(i) for i in t)
                stack.extend(x.values())
            elif isinstance(x, list):
                stack.extend(x)
    return sorted(types), invalid


# ----------------------------------------------------------------------------- discovery
def parse_sitemap(url, delay, seen=None, depth=0):
    """Return (page_urls, sitemap_files). Follows sitemap indexes (max depth 3)."""
    seen = seen if seen is not None else set()
    if url in seen or depth > 3:
        return [], []
    seen.add(url)
    r = fetch(url, follow=True, delay=delay)
    if r.status != 200 or not r.body:
        return [], [(url, r.status, 0)]
    txt = r.text()
    locs = re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', txt)
    if '<sitemapindex' in txt:
        pages, files = [], [(url, 200, len(locs))]
        for child in locs:
            p, f = parse_sitemap(child, delay, seen, depth + 1)
            pages += p
            files += f
        return pages, files
    return [html.unescape(u) for u in locs], [(url, 200, len(locs))]


def crawl_discover(base, limit, delay):
    host = urllib.parse.urlparse(base).netloc
    todo, seen, found = [base], {base}, []
    while todo and len(found) < limit:
        u = todo.pop(0)
        r = fetch(u, follow=True, delay=delay)
        if r.status != 200 or 'html' not in r.header('Content-Type', 'html').lower():
            continue
        found.append(u)
        p = PageParser()
        try:
            p.feed(r.text())
        except Exception:
            pass
        for a in p.anchors:
            h = urllib.parse.urldefrag(urllib.parse.urljoin(u, a['href']))[0]
            if urllib.parse.urlparse(h).netloc == host and h not in seen and not re.search(r'\.(jpe?g|png|gif|pdf|zip|css|js|webp|svg)$', h, re.I):
                seen.add(h)
                todo.append(h)
    return found


# ----------------------------------------------------------------------------- analysis
def norm(u):
    return u.rstrip('/') if u.count('/') > 3 else u


def analyse(url, base_host, delay, title_max):
    r = fetch_retry(url, delay=delay)
    page = {'url': url, 'status': r.status, 'location': r.header('Location'), 'issues': []}
    add = lambda sev, code, msg: page['issues'].append({'sev': sev, 'code': code, 'msg': msg})
    if r.status == 0:
        add('P0', 'STATUS_ERROR', 'request failed: ' + r.error)
        return page
    if 300 <= r.status < 400:
        add('P1', 'REDIRECTS', f'returns {r.status} to {r.header("Location")}')
        return page
    if r.status >= 400:
        add('P0', 'STATUS_ERROR', f'returns HTTP {r.status}')
        return page
    if 'html' not in r.header('Content-Type', 'text/html').lower():
        page['non_html'] = True
        return page
    p = PageParser()
    try:
        p.feed(r.text())
    except Exception as e:
        add('P2', 'PARSE_WARNING', 'HTML parse issue: ' + str(e)[:80])
    title = re.sub(r'\s+', ' ', p.title).strip()
    desc = re.sub(r'\s+', ' ', p.meta.get('description', '')).strip()
    robots = (p.meta.get('robots', '') + ' ' + r.header('X-Robots-Tag')).lower()
    canon = [h for rel, h, _ in p.links if rel == 'canonical']
    h1s = [t for lv, t in p.headings if lv == 1]
    types, bad_ld = jsonld_types(p.jsonld)
    page.update({'title': title, 'description': desc, 'h1': h1s, 'canonical': canon[0] if canon else '',
                 'robots': robots.strip(), 'noindex': 'noindex' in robots, 'lang': p.lang, 'words': p.words,
                 'schema': types, 'imgs': len(p.imgs), 'headings': Counter(lv for lv, _ in p.headings),
                 'internal_links': []})

    # titles
    if not title:
        add('P1', 'TITLE_MISSING', 'no <title>')
    else:
        if len(title) > title_max:
            add('P1', 'TITLE_LONG', f'{len(title)} chars (> {title_max}): {title[:70]}')
        elif len(title) < 20:
            add('P1', 'TITLE_SHORT', f'{len(title)} chars: {title}')
    # description
    if not desc:
        add('P1', 'DESC_MISSING', 'no meta description')
    elif len(desc) > 160:
        add('P1', 'DESC_LONG', f'{len(desc)} chars')
    elif len(desc) < 70:
        add('P1', 'DESC_SHORT', f'{len(desc)} chars: {desc}')
    # headings
    if not h1s:
        add('P1', 'H1_MISSING', 'no <h1>')
    elif len(h1s) > 1:
        add('P2', 'H1_MULTIPLE', f'{len(h1s)} h1 elements')
    # canonical
    if not canon:
        add('P1', 'CANONICAL_MISSING', 'no rel=canonical')
    elif norm(canon[0]) != norm(url) and not page['noindex']:
        add('P1', 'CANONICAL_OTHER', f'canonical points to {canon[0]}')
    # robots
    if page['noindex']:
        add('P3', 'NOINDEX', 'page is noindex')
    # language / viewport / social
    if not p.lang:
        add('P2', 'LANG_MISSING', '<html lang> not set')
    if 'viewport' not in p.meta:
        add('P2', 'VIEWPORT_MISSING', 'no viewport meta (mobile)')
    if 'og:image' not in p.meta:
        add('P3', 'OG_IMAGE_MISSING', 'no og:image (poor link previews)')
    # structured data
    if not types:
        add('P3', 'NO_STRUCTURED_DATA', 'no JSON-LD found')
    if bad_ld:
        add('P2', 'JSONLD_INVALID', f'{bad_ld} JSON-LD block(s) fail to parse')
    # images
    no_alt = [i for i in p.imgs if 'alt' not in i]
    bad_alt = [i for i in p.imgs if i.get('alt', '').strip() and FILENAME_ALT_RE.search(i['alt'].strip())]
    no_dim = [i for i in p.imgs if not (i.get('width') and i.get('height')) and (i.get('src') or i.get('data-src'))]
    if no_alt:
        add('P2', 'IMG_NO_ALT', f'{len(no_alt)} of {len(p.imgs)} images have no alt attribute (use alt="" if decorative)')
    if bad_alt:
        add('P2', 'IMG_ALT_FILENAME', f'{len(bad_alt)} alt text(s) look like filenames, e.g. "{bad_alt[0]["alt"][:50]}"')
    if no_dim:
        add('P3', 'IMG_NO_DIMENSIONS', f'{len(no_dim)} images lack width/height (layout shift risk)')
    # anchors
    generic, empty = [], []
    internal = set()
    for a in p.anchors:
        txt = (a['text'] or a['img_alt'] or a['aria']).strip().lower().rstrip(' >→')
        href = a['href']
        if not href or href.startswith(('#', 'mailto:', 'tel:', 'javascript:')):
            continue
        absu = urllib.parse.urldefrag(urllib.parse.urljoin(url, href))[0]
        if urllib.parse.urlparse(absu).netloc == base_host and 'nofollow' not in a['rel']:
            internal.add(absu)
        if not txt:
            empty.append(href)
        elif txt in GENERIC_ANCHORS:
            generic.append(txt)
    page['internal_links'] = sorted(internal)
    if generic:
        add('P2', 'ANCHOR_GENERIC', f'{len(generic)} links with vague text such as "{generic[0]}"')
    if empty:
        add('P2', 'ANCHOR_EMPTY', f'{len(empty)} links with no text, alt or aria-label')
    # placeholder / demo text (visible text only, so scripts and styles do not trigger it)
    visible = re.sub(r'(?is)<(script|style|noscript|template|svg)\b.*?</\1>', ' ', r.text())
    visible = re.sub(r'(?s)<[^>]+>', ' ', visible)
    m = PLACEHOLDER_RE.search(visible) or PLACEHOLDER_RE.search(desc) or PLACEHOLDER_RE.search(title)
    if m:
        add('P0', 'PLACEHOLDER_TEXT', f'placeholder/demo text found: "{m.group(0)}"')
    # mixed content
    if url.startswith('https://'):
        mixed = [u for _, u in p.resources if u.startswith('http://')]
        if mixed:
            add('P0', 'MIXED_CONTENT', f'{len(mixed)} http:// resources on an https page, e.g. {mixed[0][:70]}')
    # duplicated attributes (e.g. loading="lazy" twice) are sloppy markup
    if p.dup_attrs:
        c = Counter(f'{t}[{a}]' for t, a in p.dup_attrs)
        add('P3', 'DUPLICATE_ATTR', 'repeated attributes: ' + ', '.join(f'{k} x{v}' for k, v in c.most_common(3)))
    # nearly empty page
    if p.words < 50:
        add('P3', 'VERY_LITTLE_TEXT', f'only {p.words} words of text (informational; Google has no word-count rule)')
    return page


# ----------------------------------------------------------------------------- site-level checks
def site_checks(base, host, delay):
    out = []
    add = lambda sev, code, msg: out.append({'sev': sev, 'code': code, 'msg': msg, 'url': ''})
    scheme = urllib.parse.urlparse(base).scheme
    # robots.txt
    rb = fetch(f'{scheme}://{host}/robots.txt', follow=True, delay=delay)
    sitemaps_in_robots = []
    if rb.status == 200:
        txt = rb.text()
        sitemaps_in_robots = re.findall(r'(?im)^\s*sitemap:\s*(\S+)', txt)
        agent_all, rules = False, []
        for line in txt.splitlines():
            line = line.split('#')[0].strip()
            if re.match(r'(?i)user-agent:\s*\*', line):
                agent_all = True
            elif re.match(r'(?i)user-agent:', line):
                agent_all = False
            elif agent_all and re.match(r'(?i)disallow:', line):
                rules.append(line.split(':', 1)[1].strip())
        if '/' in rules:
            add('P0', 'ROBOTS_BLOCKS_ALL', 'robots.txt has "Disallow: /" for all crawlers')
        assets = [x for x in rules if re.search(r'(wp-includes|wp-content/(themes|plugins)|\.css|\.js|/assets/|/static/)', x)]
        if assets:
            add('P1', 'ROBOTS_BLOCKS_ASSETS', 'robots.txt blocks CSS/JS-style paths (Google needs them to render): ' + ', '.join(assets[:3]))
        if not sitemaps_in_robots:
            add('P2', 'ROBOTS_NO_SITEMAP', 'robots.txt does not list a Sitemap: line')
    elif rb.status == 404:
        add('P2', 'ROBOTS_MISSING', 'no robots.txt (fine, but a Sitemap: line there helps discovery)')
    else:
        add('P1', 'ROBOTS_ERROR', f'robots.txt returned {rb.status}')
    # host / protocol variants
    bare = host[4:] if host.startswith('www.') else host
    variants = [f'http://{bare}/', f'http://www.{bare}/', f'https://{bare}/', f'https://www.{bare}/']
    ok_variants = []
    for v in variants:
        r = fetch(v, delay=delay)
        if r.status == 200:
            ok_variants.append(v)
        elif r.status in (301, 308):
            pass
        elif r.status in (302, 303, 307):
            add('P2', 'TEMP_REDIRECT_VARIANT', f'{v} uses a {r.status} (temporary) redirect; use 301')
    if len(ok_variants) > 1:
        add('P1', 'HOST_VARIANTS_DUPLICATE', 'several host/protocol variants answer 200 instead of redirecting to one: ' + ', '.join(ok_variants))
    if not ok_variants:
        add('P2', 'HOST_NO_DIRECT_200', 'none of the four host variants returns 200 directly (check the preferred one redirects cleanly)')
    if scheme != 'https':
        add('P0', 'NOT_HTTPS', 'site is audited over http; serve and redirect to https')
    # soft 404
    junk = ''.join(random.choice(string.ascii_lowercase) for _ in range(14))
    probe = f'{scheme}://{host}/{junk}-not-a-real-page/'
    s = fetch(probe, delay=delay)
    # Follow a few hops: sites that strip (or add) the trailing slash answer the probe with a 308 to the
    # other form, which then returns a real 404. That is fine. A redirect that lands on a 200 page (often
    # the homepage) is a soft 404; one that loops or ends anywhere else is still worth a look.
    hops, url = [], probe
    while s.status in (301, 302, 303, 307, 308) and len(hops) < 3:
        loc = next((v for k, v in s.headers.items() if k.lower() == 'location'), '')
        if not loc:
            break
        url = urllib.parse.urljoin(url, loc)
        hops.append(s.status)
        s = fetch(url, delay=delay)
    via = f' (after {"/".join(map(str, hops))} redirect to {url})' if hops else ''
    if s.status == 200:
        add('P0', 'SOFT_404', f'a nonsense URL returns 200 instead of 404{via} (soft 404s waste crawl and confuse indexing)')
    elif s.status in (301, 302, 303, 307, 308):
        add('P1', 'SOFT_404_REDIRECT', f'a nonsense URL keeps redirecting ({"/".join(map(str, hops + [s.status]))}) instead of returning 404')
    elif s.status not in (404, 410):
        add('P1', 'SOFT_404_REDIRECT', f'a nonsense URL returns {s.status or "no response"}{via} instead of 404')
    return out, sitemaps_in_robots


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('url', help='site root, e.g. https://example.com')
    ap.add_argument('--out', default='seo-audit.json')
    ap.add_argument('--md', default='seo-audit.md')
    ap.add_argument('--max-urls', type=int, default=250)
    ap.add_argument('--concurrency', type=int, default=4)
    ap.add_argument('--delay', type=float, default=0.1, help='seconds to wait before each request')
    ap.add_argument('--title-max', type=int, default=60)
    ap.add_argument('--urls-file', help='text file with one URL per line (skips discovery)')
    ap.add_argument('--no-link-check', action='store_true', help='skip checking internal links that are not in the sitemap')
    ap.add_argument('--baseline', help='earlier JSON output to compare against')
    a = ap.parse_args()
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    base = a.url if a.url.startswith('http') else 'https://' + a.url
    base = base.rstrip('/') + '/'
    host = urllib.parse.urlparse(base).netloc
    print(f'Auditing {base}')

    site_issues, robots_sitemaps = site_checks(base, host, a.delay)

    # discovery
    sitemap_files, in_sitemap = [], set()
    if a.urls_file:
        urls = [l.strip() for l in open(a.urls_file, encoding='utf-8') if l.strip()]
        mode = 'urls-file'
    else:
        cands = robots_sitemaps or [base + 'sitemap_index.xml', base + 'sitemap.xml', base + 'wp-sitemap.xml']
        urls = []
        for c in cands:
            pgs, files = parse_sitemap(c, a.delay)
            sitemap_files += files
            urls += pgs
            if pgs:
                break
        mode = 'sitemap'
        if not urls:
            mode = 'crawl'
            site_issues.append({'sev': 'P1', 'code': 'NO_SITEMAP', 'msg': 'no working sitemap found; pages were discovered by crawling', 'url': ''})
            urls = crawl_discover(base, a.max_urls, a.delay)
        in_sitemap = set(urls)
    seen, ordered = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            ordered.append(u)
    dupes = len(urls) - len(ordered)
    if dupes:
        site_issues.append({'sev': 'P3', 'code': 'SITEMAP_DUPLICATE_URLS', 'msg': f'{dupes} URL(s) are listed more than once across the sitemaps', 'url': ''})
    ordered = ordered[:a.max_urls]
    print(f'{len(ordered)} URLs to audit ({mode}); site-level findings so far: {len(site_issues)}')

    with ThreadPoolExecutor(max_workers=max(1, a.concurrency)) as ex:
        pages = list(ex.map(lambda u: analyse(u, host, a.delay, a.title_max), ordered))

    # cross-page checks
    indexable = [p for p in pages if p.get('status') == 200 and not p.get('noindex') and 'title' in p]
    for field, code, label in (('title', 'TITLE_DUPLICATE', 'title'), ('description', 'DESC_DUPLICATE', 'meta description')):
        groups = defaultdict(list)
        for p in indexable:
            if p.get(field):
                groups[p[field]].append(p)
        for val, grp in groups.items():
            if len(grp) > 1:
                for p in grp:
                    p['issues'].append({'sev': 'P1', 'code': code, 'msg': f'same {label} as {len(grp) - 1} other page(s): {val[:60]}'})
    if mode == 'sitemap':
        for p in pages:
            if p.get('noindex'):
                p['issues'].append({'sev': 'P0', 'code': 'NOINDEX_IN_SITEMAP', 'msg': 'page is noindex but listed in the sitemap'})
    # broken / redirected internal links (limited sample outside the audited set)
    if not a.no_link_check:
        audited = set(ordered)
        linked = Counter()
        for p in pages:
            for l in p.get('internal_links', []):
                linked[l] += 1
        extra = [l for l in linked if l not in audited and '?' not in l and not re.search(r'\.(jpe?g|png|gif|webp|svg|css|js|pdf|zip|ico|xml|woff2?)$', l, re.I)][:150]
        if extra:
            with ThreadPoolExecutor(max_workers=max(1, a.concurrency)) as ex:
                statuses = list(ex.map(lambda u: (u, fetch_retry(u, delay=a.delay).status), extra))
            for u, s in statuses:
                if s == 0:
                    site_issues.append({'sev': 'P2', 'code': 'LINK_CHECK_FAILED', 'msg': f'could not fetch (timeout or network error, retried): {u}', 'url': u})
                elif s >= 400:
                    site_issues.append({'sev': 'P1', 'code': 'BROKEN_INTERNAL_LINK', 'msg': f'linked from {linked[u]} page(s) but returns {s}: {u}', 'url': u})
                elif 300 <= s < 400:
                    site_issues.append({'sev': 'P2', 'code': 'INTERNAL_LINK_REDIRECTS', 'msg': f'linked from {linked[u]} page(s) but redirects ({s}): {u}', 'url': u})
        # orphans: audited pages nobody links to
        inbound = Counter(l for p in pages for l in p.get('internal_links', []))
        for p in pages:
            if p['url'].rstrip('/') != base.rstrip('/') and inbound.get(p['url'], 0) == 0 and p.get('status') == 200:
                p['issues'].append({'sev': 'P3', 'code': 'NO_INTERNAL_LINKS_IN', 'msg': 'no other audited page links here (orphan)'})

    # summary
    sev_count, code_count, examples = Counter(), Counter(), defaultdict(list)
    for p in pages:
        for i in p['issues']:
            sev_count[i['sev']] += 1
            code_count[(i['sev'], i['code'])] += 1
            if len(examples[i['code']]) < 5:
                examples[i['code']].append((p['url'], i['msg']))
    for i in site_issues:
        sev_count[i['sev']] += 1
        code_count[(i['sev'], i['code'])] += 1
        if len(examples[i['code']]) < 5:
            examples[i['code']].append((i.get('url') or '(site)', i['msg']))

    result = {'site': base, 'mode': mode, 'audited': len(pages), 'sitemaps': sitemap_files, 'site_issues': site_issues,
              'summary': {f'{s}:{c}': n for (s, c), n in sorted(code_count.items())}, 'severity_totals': dict(sev_count),
              'pages': pages, 'generated': time.strftime('%Y-%m-%d %H:%M:%S')}
    with open(a.out, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=1, default=lambda o: dict(o) if isinstance(o, Counter) else str(o))

    # markdown
    sev_order = {'P0': 0, 'P1': 1, 'P2': 2, 'P3': 3}
    names = {'P0': 'P0 broken or harmful', 'P1': 'P1 should fix', 'P2': 'P2 worth fixing', 'P3': 'P3 minor / informational'}
    lines = [f'# SEO audit: {base}', '', f'Audited **{len(pages)}** URLs (discovery: {mode}) on {result["generated"]}.', '',
             '| Severity | Issues |', '|---|---|'] + [f'| {names[s]} | {sev_count.get(s, 0)} |' for s in ('P0', 'P1', 'P2', 'P3')] + ['']
    if sitemap_files:
        lines += ['## Sitemaps', ''] + [f'- {u} (HTTP {s}, {n} entries)' for u, s, n in sitemap_files] + ['']
    for sev in ('P0', 'P1', 'P2', 'P3'):
        rows = sorted([(c, n) for (s, c), n in code_count.items() if s == sev], key=lambda x: -x[1])
        if not rows:
            continue
        lines += [f'## {names[sev]}', '']
        for code, n in rows:
            lines.append(f'### {code} ({n})')
            for u, m in examples[code]:
                lines.append(f'- `{u.replace(base.rstrip("/"), "") or "/"}`: {m}')
            if n > len(examples[code]):
                lines.append(f'- ... and {n - len(examples[code])} more')
            lines.append('')
    if not sev_count:
        lines.append('No issues found.')

    if a.baseline:
        try:
            old = json.load(open(a.baseline, encoding='utf-8'))['summary']
            new = result['summary']
            keys = sorted(set(old) | set(new))
            diff = [(k, old.get(k, 0), new.get(k, 0)) for k in keys if old.get(k, 0) != new.get(k, 0)]
            lines += ['## Change since baseline', '', '| Issue | Before | Now |', '|---|---|---|'] + [f'| {k} | {o} | {n} |' for k, o, n in diff]
            if not diff:
                lines.append('| (no change) | | |')
            lines.append('')
        except Exception as e:
            lines.append(f'(could not read baseline: {e})')
    open(a.md, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')

    print(f'P0={sev_count.get("P0", 0)}  P1={sev_count.get("P1", 0)}  P2={sev_count.get("P2", 0)}  P3={sev_count.get("P3", 0)}')
    print(f'wrote {a.out} and {a.md}')
    return 1 if sev_count.get('P0') else 0


if __name__ == '__main__':
    sys.exit(main())
