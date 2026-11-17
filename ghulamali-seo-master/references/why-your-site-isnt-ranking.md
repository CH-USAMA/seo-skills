# Why a website is not ranking: his diagnostic order

Source: "Why Your Website isn't Ranking in Google ( & How to Rank it )" (18K views, about 8 minutes). Read from YouTube's transcript panel in the original language and translated by hand.

**His frame:** a site may not rank because content is duplicated, keywords are too competitive, the site was hacked, it is not being crawled or indexed, it is technically broken, or competitors are very strong. Whatever the reason, you can find it, fix it and rank. His image: fixing Search Console issues is like treating the body from outside. If the body is damaged inside, you need the detailed audits as well.

## Part 1: Search Console audit (three things, about 30 to 60 minutes of fixes)

| Report | What to look at | What it means |
|---|---|---|
| **Core Web Vitals** | Mobile and desktop tabs: how many URLs are "Poor" | Poor URLs are not eligible to rank well on that device because of speed. Export the list. Then run each URL through **PageSpeed Insights**; the reasons differ per site and tell you what to fix. |
| **Pages (indexing)** | Reasons pages are not indexed: Not found (404), Page with redirect, Excluded by noindex tag, and others | He calls these very straightforward fixes. Work down the list of reasons. |
| **Crawl stats** (Settings, then Crawl stats) | Crawl requests per day on the graph | Higher means Google visits the site more and the site can rank faster; a low number means Google is not visiting. |

**What raises crawl rate** (he says he did exactly this on a client site and crawl rate "went through the roof" while traffic almost doubled): fast hosting (he names SiteGround), a lightweight theme, a strong internal linking structure, a steady page publishing frequency, and backlinks.

His claim that fixing only Core Web Vitals and indexing issues on one client produced a visible traffic climb is a single case study.

## Part 2: the five detailed audits

Even with a clean Search Console, a site struggles if any of these are bad: internal or external duplicate content, wrong-intent keywords, highly competitive keywords, on-page mistakes, spammy backlinks.

### 1. Keyword audit
Take every keyword already targeted and sort it into easy, medium and high competition. **Never trust a tool's difficulty score alone; confirm manually.** For each keyword:

- Look at the top five results (he uses the Ahrefs toolbar to show DR in the results).
- Is the exact keyword in their titles?
- What DR do they have? A very high DR means competitive; if the third and fourth results have very low DR, that is a weakness and an easy target.
- Even where Ahrefs shows KD 0, still check manually.

Then do new research the same way and **map topically** so a page covers a topic, not one keyword ([topical-mapping-and-intent.md](topical-mapping-and-intent.md)).

### 2. Content audit
- **External duplication:** check with Copyscape. Cause: a poor writer copies other sites. Always ask the writer for a plagiarism report.
- **Internal duplication:** mostly e-commerce, when product variations get separate pages with the same text. Fix with canonicalisation.
- **Quality checklist:** semantically optimised, user-first, covers the topic fully, no language mistakes, written in the reader's native language, active voice. If all boxes are ticked, fine; otherwise fix.

### 3. On-page audit
Check each page for: keyword in the title, in the first paragraph, in an H2, in image alt text; no schema errors; internal links; external links; semantically optimised content. Tools he names for finding issues: Screaming Frog, Semrush, Ahrefs, and an on-page tool he calls "POP".

### 4. Technical audit
Speed no more than 3 seconds; no insecure (mixed) content; responsive; mobile not mismanaged; robots.txt correct; no broken URL structure; no 404 pages; no large numbers of redirects. Tools: Website Auditor (Link-Assistant), Screaming Frog (his recommendation, "the best one"), Ahrefs, Semrush, JetOctopus.

### 5. Backlink audit
- Anchor text ratio.
- Dofollow versus nofollow ratio.
- Low-quality, spammy links; negative link building by competitors.
- **Backlink gap** between you and your competitors: how many links they rank with versus you.

Use a backlink tool; mark spammy and negative links and remove or disavow them with care (see BeyondSEO's toxic-link guidance).

## His decision point and what to ignore

He ends by asking the viewer whether they have time to do all this themselves ("if yes, stop the video and implement it") and then pitches an 80% discounted, done-with-you SEO plan (two-hour strategy call, audit, research sheet, an AI content masterclass, technical and backlink audit, six-month plan) with discount code and email. Skip the offer and the code. The audit order itself is the value.

## How to use it

Run it in this order for any site that "does not rank":

1. Search Console: Core Web Vitals, Pages, Crawl stats. (BeyondSEO `crawl` plus Search Console data covers the same ground; see [combining-with-beyondseo.md](combining-with-beyondseo.md).)
2. Keyword audit (manual SERP check), then content, on-page, technical, backlinks.
3. Rank fixes by effort: indexing and speed fixes first (cheap, "straightforward"), content and keyword changes next, link work last.
4. Compare with [technical-seo-audit.md](technical-seo-audit.md) for the hidden technical checks this video does not mention.
