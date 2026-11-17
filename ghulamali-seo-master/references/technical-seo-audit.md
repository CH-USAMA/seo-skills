# Technical SEO: the hidden things

Source: "Auditing 500 Websites Taught Me These Technical SEO Secrets" (8K views, 10 years, 500+ audits), with crawling and indexing basics from "Give me 9min...". Numbers (for example "40% of crawl budget") are his case-study claims.

## Basics he says everyone already does

Fix 404s, remove duplicate meta descriptions, improve page speed, SSL, mobile responsive, no hacked pages, few redirects, no orphan pages, no cannibalisation, correct canonicals, proper schema. Skipping these wastes all other work. The "secrets" below are the things that are usually skipped.

## Crawl, process, index (why this is the first thing)

1. **Discover**: XML sitemap, backlinks, URL submitted in Search Console, internal links.
2. **Crawl**: Google downloads the page. Robots.txt controls which pages may be crawled.
3. **Process and index**: Google reads text, detects language, extracts keywords and entities.
4. **Rank**: the indexed page is compared with other pages on that topic.

If discovery, crawl or indexing fails, nothing else matters.

## The 8 hidden checks

### 1. Log file analysis
Server logs show how Googlebot really behaves: pages crawled, crawl budget wasted, crawl errors Search Console never shows, bot traffic, redirect effects.
His case: thousands of products, indexing problems. Logs showed **40% of crawl budget burned on faceted-navigation URLs**, and product pages were crawled once every 90 days. Fix: disallow the parameter URLs in robots.txt, configure URL parameter handling, strengthen internal links to the product pages. Result: indexed within a week, traffic up 34% in six months.
*Note:* Search Console's URL Parameters tool has been retired by Google, so use robots.txt, canonicals and noindex instead.

### 2. JavaScript rendering
Looks fine in a browser does not mean Googlebot sees it. Content, navigation and internal links injected after the first render may be missed, and render-heavy sites get less crawl budget.
Check: Search Console URL Inspection, **Test Live URL**, **View rendered HTML**, compare with the real page.
Fix: server-side render or keep critical content, navigation and anchor tags in static HTML.

### 3. Orphan pages
Pages with no internal links. Find them by crawling the site with Screaming Frog, then comparing the crawled list against the XML sitemap. For each orphan: valuable, then link to it; outdated but strong URL, then 301 to the new page; useless, then return **410**.

### 4. Internal link equity waste
Authority flows through internal links, and many sites leak it into pagination, tag pages, archives, weak category pages, author pages and internal search results.
Audit: crawl, export the internal links report, sort by inlinks descending, look at the top 50. If low-value pages top the list, fix it. Make tag, author and pagination pages **noindex,follow**, noindex faceted URLs, and build a deliberate internal-link plan to the commercial pages.

### 5. Page performance per template, not the homepage
"Where every developer cheats you": a homepage score of 92 while product pages load in 7.4 s and checkout in 5.9 s.
Audit: test home, category, product, blog post, checkout and login separately, 3 to 4 URLs per type, in PageSpeed Insights. Use the Search Console **Core Web Vitals** report for site-wide real-user data.

### 6. Render-blocking resources
Typical offenders: 12 separate CSS files that could be one, eight JavaScript libraries where half are unused, custom fonts loading before content, analytics in the head, third-party widgets (chat, popups, social feeds).

### 7. Schema gaps
Most sites have only Organization, WebSite and Article. Add what matches the content: FAQ, HowTo, Video, Review, BreadcrumbList, Speakable. Method: take the top 10 competitors' pages, check their schema in the Schema.org validator or Rich Results Test, then implement the types that fit, in **JSON-LD**. He claims rich results can lift click-through rate a lot (his numbers "30% to 80%" are unverified).
*Note:* Google has reduced FAQ and HowTo rich results in recent years. Keep them for machine readability and AI extraction, but do not promise a snippet.

### 8. Mobile viewport and UX
Mobile-first indexing means the mobile version is the one that is ranked. Responsive is not enough. Look for tiny text, buttons too close together, horizontal scroll, intrusive interstitials, fixed elements covering content.
His thresholds: **body text at least 16 px on mobile, tap targets at least 48x48 px, no full-screen popups on mobile, sticky elements under 15% of screen height**. Check Search Console, PageSpeed mobile tab, and a real phone.

## How BeyondSEO fits

`beyondseo crawl` and `beyondseo audit` produce the evidence for items 2 to 8 (raw vs rendered, schema, internal links, orphans via sitemap coverage, blocked requests). Items 1 (server logs) and the live Core Web Vitals field data need the user's own logs and Search Console or a Lighthouse JSON, which BeyondSEO can review once supplied. See [combining-with-beyondseo.md](combining-with-beyondseo.md).
