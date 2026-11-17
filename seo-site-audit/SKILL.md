---
name: seo-site-audit
description: Audit and fix on-page and technical SEO for any website (WordPress, WooCommerce, Shopify, Next.js, static HTML), following Google's SEO Starter Guide and Search Essentials. Use whenever the user asks to improve SEO or rankings, audit a site, fix Search Console problems (404s, page indexing, duplicates, noindex, merchant listings or product structured data emails), write or repair titles, descriptions, H1s, alt text, schema, sitemaps, robots.txt, canonicals or redirects, prepare a launch, or find out why pages are not in Google. Also use for Rank Math or Yoast, demo or template pages still live, local service businesses and NAP consistency, Google Ads landing pages, AI search visibility (llms.txt, AI crawlers, Bing), and online shops: shipping or price mismatches between markup and checkout, whether Google Ads or paid social will pay back (unit economics), blog and product content strategy, and theme layout bugs that crop images or hide menus.
metadata:
  version: "1.3.0"
  source: "Google SEO Starter Guide (developers.google.com/search/docs/fundamentals/seo-starter-guide), plus lessons from real audits"
---

# SEO site audit and fix

Google's own starter guide is clear about priorities, and this skill follows them: the biggest lever is **useful, original, accurate content that people want**; everything else is hygiene that lets Google find the pages, understand them and present them well. Technical polish on thin or wrong content does not rescue it, and chasing myths wastes the owner's money and trust. So audit for real problems, fix the high-impact ones first, prove each fix with a measurement, and be honest about what only time (weeks) will show.

Fetch the guide when details matter (it is short): https://developers.google.com/search/docs/fundamentals/seo-starter-guide . A distilled copy is in `references/google-seo-starter-guide.md`.

## Workflow

1. **Scope and safety** (before any change)
2. **Audit** (script plus manual checks)
3. **Triage** (fix in severity order)
4. **Fix** (rules below)
5. **Verify** (re-measure, on the live site)
6. **Report** (plain language, with the owner-only steps)

### 1. Scope and safety

Establish: the site URL, the platform, how changes get made (CMS admin, SSH or WP-CLI, a git repo), who approves wording, and any brand rules (tone, banned punctuation, claims that need sign-off). Then:

- The audit is read-only. **Fixes change a live site**, so take a backup first (database dump, export, or a git branch) and keep the original of anything you overwrite (a backup meta field or file). Prefer reversible actions (redirects, noindex, settings) to deletion. Do not hard-delete user content or data without the owner's say-so; move it to trash or spam instead.
- Use only facts that are already on the site or that the owner gave you for addresses, prices, policies, dates and claims. Never invent reviews, ratings, awards, statistics or contact details. When two pages disagree (for example two different addresses), do not pick silently: show the owner both and ask which is right.
- Do not send messages or publish to third parties as part of an audit unless asked.

### 2. Audit

Run the bundled auditor (Python 3.8+, standard library only, makes polite GET requests):

```bash
python <this-skill>/scripts/seo_audit.py https://example.com --out audit.json --md audit.md
# later, to measure progress:
python <this-skill>/scripts/seo_audit.py https://example.com --out audit2.json --md audit2.md --baseline audit.json
```

It discovers URLs from robots.txt and sitemaps (or crawls if there is no sitemap), does not follow redirects (so redirected sitemap entries show up), and reports by severity: **P0** broken or harmful, **P1** should fix, **P2** worth fixing, **P3** informational. Read `audit.md`, then do the checks a script cannot:

- **What Google actually has.** Search `site:domain.com`, and ask the owner for Search Console data (Pages report, Sitemaps, Performance export, URL Inspection). Search Console is the ground truth for indexing; exports lag 2 to 3 days. If search results still show old content, that is a stale snapshot: the fix is a recrawl (URL Inspection, Request indexing), not more edits.
- **Read the key pages as a visitor would** (home, contact, about, shop or services, policies, FAQ): placeholder or demo text, fake contact details, contradictory facts, outdated labels ("September update" in October), claims that need verification.
- **Template leaks into the HTML.** Buttons written as `<a href="1058">` (an ID, which crawlers follow as `/1058`), footer anchors like `#about` that go nowhere from other pages, `http://` assets on https pages, repeated attributes, text hidden with CSS.
- **Archives that duplicate other pages.** A blog index and a category archive that list the same posts; tag, author and date archives; internal search; parameter URLs; pagination.
- **User-generated content.** Open comments, pingbacks (a CMS can turn every internal link into a "pingback" comment), contact forms, spam links.
- **Performance sanity** (a page-experience signal, not the main event): slow first byte, huge images, layout shift, lazy images that never load.

### 3. Triage

| Tier | Examples | Why first |
|---|---|---|
| P0 | placeholder or demo content live; fake NAP; 4xx/5xx or noindex in the sitemap; robots.txt blocking everything; soft 404s; mixed content | misleads users or hides the site |
| P1 | missing, duplicate, or over-long titles and descriptions; no or wrong H1; canonical missing or pointing elsewhere; redirected sitemap URLs; broken internal links; duplicate content at several URLs; http/https/www variants all answering 200 | directly shapes what Google indexes and shows |
| P2 | missing alt; vague anchor text; invalid structured data; no `lang`; internal links that redirect; open comments | quality and accessibility |
| P3 | image dimensions, og:image, duplicate attributes, tiny pages | polish |

### 4. Fix: the rules

- **Titles.** Unique per page, accurate, concise. Keep to about 60 characters or fewer so they are not cut off. Lead with what the page is about, put the brand last, include the place or business type where natural ("Irish Catholic Gifts from Knock and Lourdes | Brand"), no keyword stuffing. A site called only its brand name on the homepage is a missed opportunity.
- **Meta descriptions.** One or two sentences, roughly 70 to 155 characters, unique, summarising what the visitor gets. Google may rewrite them; they still help. A placeholder (lorem ipsum) description is P0.
- **Headings.** One visible H1 that names the page. Heading order and count are not a ranking factor, but a missing H1 hurts clarity and accessibility. If the theme prints post titles as H4 or H2, change the visible title's tag to H1 and restyle it to look identical. A visually hidden H1 is a last resort and must match the visible title.
- **URLs and duplicates.** Descriptive words, lowercase and hyphens, stable. Each piece of content should be reachable at one URL: fix duplicates with a 301 redirect first, `rel=canonical` second, noindex for archives that only repeat other pages. Never change a live URL without a 301. Make sure http, https, www and non-www collapse to one address with 301s.
- **Sitemap.** Only canonical, indexable, 200-status URLs. Exclude redirects, noindex pages, demo pages and duplicate archives. Reference it in robots.txt and submit it in Search Console. Regenerate or clear the plugin's cache after changing settings.
- **robots.txt.** Do not block CSS, JS or images (Google must render pages). Do not use it to hide pages; use noindex for that. Include the `Sitemap:` line.
- **Internal links.** Descriptive anchor text (never "click here" or "read more" alone, and cards that wrap a title are fine). Footer and menu links must work from every page (absolute or root-relative, not bare `#anchors`). Link to important pages from the homepage; avoid orphan pages. Add `nofollow` to untrusted and user-posted links.
- **Images.** Alt text that describes the image in context (`alt=""` when purely decorative), sharp images placed near the relevant text, `width` and `height` set, modern formats, lazy-load only below the fold. Do not write `loading="lazy"` by hand on a platform that adds it, or you get it twice.
- **Structured data.** Valid JSON-LD that matches visible content: Organization, WebSite, BreadcrumbList, Article or BlogPosting, Product with offers, LocalBusiness. Mark up only what is on the page. Never fabricate ratings or reviews.
- **Content.** People-first, original, accurate, readable, kept current. Answer the visitor's real questions (a shop needs real delivery, returns, FAQ and contact pages). Remove or rewrite outdated and demo pages; do not copy other sites; do not stuff keywords; word count is not a rule. Respect the owner's voice and any banned phrasing or punctuation.
- **Locale.** `<html lang>` should match the audience (`en-IE` for Ireland). Use hreflang only for genuinely multilingual sites.
- **Comments and UGC.** If nobody uses comments, close them (spam comments and self-pingbacks are only liabilities). Otherwise moderate and nofollow.
- **Consistency.** Business name, address and phone must be identical everywhere they appear (footer, contact page, policies, schema).

Platform specifics (WordPress with Rank Math or Yoast, WooCommerce, Elementor, Shopify, Next.js and static sites) are in `references/platforms.md`. Read it before editing a site on those platforms.

**Local service businesses** (taxis, trades, clinics, tours) and **any site running Google Ads**: also read `references/local-business-playbook.md`. It holds patterns proven on a high-traffic local site (page structure per service and route, title and description formulas with the phone number, call tracking, matched ad landing pages, LocalBusiness schema and NAP consistency, making the page cache ignore `gclid`/`gad_source` so ad clicks are not served uncached, and AI-search visibility with `llms.txt`, AI crawler access and Bing). Audit against it and run its extra checks.

**Online shops** (WooCommerce, Shopify, any catalogue with prices): also read `references/ecommerce-lessons.md`. It covers keeping product structured data (shipping, returns, `validFrom`) equal to what checkout charges (with a cart-simulation method), triaging Search Console merchant emails, theme layout traps (cropped featured images, menus hidden under images), content that earns impressions, and the **paid-ads profitability check you must do before recommending any ad spend**: profit per order versus click price divided by conversion rate. If every realistic case loses money, say so with the table instead of building a campaign.

### 5. Verify

- Re-run the auditor with `--baseline` and show the before and after counts. P0 should be zero.
- Check the **live** HTML, not the CMS preview: purge page caches (LiteSpeed, WP Rocket, Cloudflare), then fetch the URL with a cache-busting query string.
- Redirects must be 301 (not 302) and not chained. A nonsense URL must return 404.
- Test lazy-loaded images by scrolling to them in a real browser; do not force them to load, or you hide the bug.
- Be straight about timing: Google says changes can take hours to months to show; judge after a few weeks.

### 6. Report

Plain language, no jargon dump. Use this shape:

1. **What I found** (the few things that matter, most serious first).
2. **What I fixed** (each with evidence: before and after numbers, a URL).
3. **What I left alone and why** (judgement calls, things that need the owner's decision).
4. **What only the owner can do** (see `references/search-console.md`: submit the sitemap, request indexing for key pages, validate fixes, verify the property, connect analytics).
5. **Next ideas** (content to write, links to earn, pages to improve).

If something conflicts or is uncertain (two addresses, a claim without a source), say so and ask rather than choosing.

## What not to spend time on

Google says these do not matter or are myths: the meta keywords tag, keyword stuffing, keywords in the domain or URL, which TLD you use, a minimum or maximum word count, heading order or number of headings for rankings, subdomain versus subfolder, a "duplicate content penalty" (duplicates waste crawl and confuse; they are not penalised as such, but copying other sites is spam), and E-E-A-T as a direct ranking factor. Promotion (word of mouth, community, putting the URL on printed material, social) is the most durable growth, but over-promotion or manipulation backfires.

## Hard-won pitfalls

- **Demo and template leftovers are the most damaging and the most overlooked**: a FAQ page of Latin filler, a Contact page with a fake city and phone number, a "Sample Page". Scan for them first, and rebuild or redirect them.
- Code that generates HTML from a command line or cron job often builds `http://` URLs (it does not know the site is https). Force `https` and check the output.
- Many platforms add `loading="lazy"` themselves. A hand-written second one is a duplicate attribute.
- A lazy image with `width:auto; height:auto` has a 0 by 0 box before it loads and may never load. Give logos and icons a definite box.
- A category that contains every post duplicates the blog index. Noindex it and drop it from the sitemap.
- Theme "quick view", "wishlist" and "compare" buttons often use the product ID as `href`. Crawlers follow them into 404s and redirect chains. If the theme's JavaScript needs the `href`, keep it, add `rel=nofollow` and an accessible name, and 301 the stray numeric URLs to the real page.
- Footer links written as bare `#anchors` work on the homepage only. Make them absolute.
- A custom title set in an SEO plugin overrides the template everywhere; always check the final rendered `<title>`.
- Pending "comments" in a CMS are often pingbacks from your own posts, or order notes. Look before deleting.
- Sitemaps from SEO plugins are cached; clear the cache after changing settings. Page caches serve stale HTML; purge them before verifying.
- On Windows, run Python with `-X utf8` (and `-I` ignores `PYTHONIOENCODING`) so pages with emoji or accents print correctly.
- Sequence matters: fix redirects and duplicates before polishing titles, and fix facts before fixing wording.
- A Search Console "merchant listings" or "page indexing" email often lists pages that were deleted weeks earlier. Open the example URL before changing anything; if it already redirects or 404s, validate the fix and wait.
- Shipping or price figures in structured data, FAQ text and product descriptions go stale when rates change. Simulate carts to learn the real charge, then update markup and text together.
- "Per class" shipping adds class costs, so moving one product into a cheaper class can make mixed baskets dearer. Simulate realistic baskets before and after; revert if any gets worse.
- Theme layout can hide things that look like content problems: a fixed-height `object-fit: cover` header slices square product photos, and equal z-index lets a post image cover a drop-down menu. Prove menus with `elementsFromPoint`, test at desktop, 1280 and 375 widths by measurement, and fix with a more specific selector rather than editing the theme.
- Growth numbers from a new site are tiny. Report counts, not percentages from a tiny base, and never promise orders.
- Do not recommend paid ads for low-value baskets without the unit-economics table (see `references/ecommerce-lessons.md`). A full-page free directory ad or a trade-show stall should be judged the same way: orders needed per day versus profit per order.
- Use an organisation's official logo files as supplied; do not redraw or recolour them, and confirm permission before putting a third party's logo on a commercial item.
- **Redirecting demo posts is not enough.** Their category, author, date and tag archives, the RSS feed and the on-site search can still list them with their Latin excerpts, and a sitemap-based crawl never sees those URLs. Open `/category/<old>/`, `/author/<login>/` (also reached via `?author=1`, which leaks admin logins), `/YYYY/MM/`, `/feed/` and `/?s=<demo word>`. Redirect the archives and exclude the demo IDs from feeds and search.
- **Hosting "AI tools" write a static `/llms.txt` once and never update it.** After a redesign or a change of business it can describe a different company. Read it during every audit, and prefer generating it from live data.
- **Empty taxonomy archives** (old product tags or categories with no items) return 200 with an empty list, and Search Console reports them as soft 404s. Return a real 404 when a term has no items.
- **A static homepage can keep the old page builder's text in `post_content`** even though the theme never prints it. It still shows up in search excerpts and the REST API. Clear it, but keep the builder's own meta if a rollback depends on it.
- **Search Console access:** the property may belong to another Google account in the same browser, so check each `/u/N/` slot before saying there is no access, and never sign in for the owner. Direct `/inspect?` links can 404; use the "Inspect any URL" bar. Request indexing allows about 10 to 12 URLs a day, so do the most important first.
- **Scheduled posts** return 404 until their date. Link only to posts already live on the linking post's date.
- **On Windows, URL lists written by Python end in `\r\n`.** Strip `\r` before passing them to curl, or every check fails with status 000.
