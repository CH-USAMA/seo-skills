# Google SEO Starter Guide: distilled

Source: https://developers.google.com/search/docs/fundamentals/seo-starter-guide (read 10 Oct 2026, paraphrased).
The guide changes over time. If a decision hinges on a detail, re-fetch it. Google's wider rules live in "Search Essentials" and the spam policies.

Contents: how search works / timing / helping Google find content / organising the site / making content useful / how the site appears / images and video / promotion / what not to focus on / structured data / next steps.

## How search works and timing
- Crawlers find pages (mostly through links from pages they already know), render them, and add them to an index. Usually, publishing is enough; nothing guarantees inclusion or a ranking.
- Changes can take hours to months to appear. Wait a few weeks before judging an edit. Not every change is visible in results. Iterate if the business allows.

## Helping Google find content
- Check indexing with a `site:example.com` search. If pages show, they are indexed.
- Sitemaps are optional but harmless: a file listing the URLs you care about. Promotion and links matter more for discovery.
- Do not hide CSS or JavaScript users need; Google must render the page. Googlebot generally crawls from the US, so check location-dependent content.
- Use the URL Inspection tool in Search Console to test a page. Use the documented methods (noindex, access control) to keep content out of Search. robots.txt controls crawling, not indexing.

## Organising the site
- Do not reorganise hastily. Descriptive URLs with real words help users (and breadcrumbs in results); avoid random identifiers.
- Large sites (thousands of URLs): group similar topics in directories so Google learns how often areas change.
- **Duplicate content**: not a spam violation or manual action, but it hurts users and wastes crawl. Make each piece of content reachable through one URL; 301 non-preferred URLs to the preferred one; if you cannot redirect, use `rel="canonical"`. Google will pick a canonical itself if you do not.

## Making the site interesting and useful (the biggest factor)
- Readable, naturally written, well organised (paragraphs, sections, headings), no spelling or grammar errors.
- Original: do not copy or merely rehash others. Keep content current; update or remove outdated pages.
- Helpful, reliable, people-first; show expertise (cite experts or experience).
- Anticipate how newcomers search (they use different words than experts); Google's language matching covers many variations.
- Do not let ads or interstitials distract from the content.
- Links: help users and Google find and corroborate content. Use **descriptive anchor text**. Link only to resources you trust; use `nofollow` or similar for untrusted ones and for user-generated links (make the CMS do it automatically).

## How the site appears in results
- **Title links** come from the `<title>` and other on-page text. Good titles are unique to the page, clear, concise and accurate. Consider the business name, location and what the page offers.
- **Snippets** usually come from page content; occasionally from the meta description, which should be short, unique to the page, and summarise the most relevant points in one or two sentences.
- Images: sharp, high quality, near relevant text, with descriptive alt text (or the CMS description field).
- Videos: high quality, embedded on a standalone page near relevant text, descriptive titles and descriptions.

## Promotion
- Social media, community engagement, advertising, offline (URL on business cards, letterhead, posters, permission-based newsletters). Word of mouth is the most effective and lasting. Over-promotion tires audiences and manipulation can break spam policies.

## What the guide says not to focus on
- Meta keywords tag: Google does not use it.
- Keyword stuffing (even variations): tiring for users and a spam violation.
- Keywords in the domain name or URL path: little effect beyond breadcrumbs.
- TLD choice (.com, .guru ...): only matters for country targeting, and then little.
- Content length: no minimum or maximum word count.
- Subdomains vs subdirectories: choose for business reasons.
- PageRank: one of many signals.
- Duplicate content "penalty": none (copying others' content is different and is spam).
- Heading order or count: helps screen readers, not Google Search.
- E-E-A-T: stated plainly as not a ranking factor.

## Structured data
- Valid structured data makes pages eligible for enhanced features (review stars, carousels, breadcrumbs). It must reflect what is visible on the page.

## Next steps
- Set up Search Console to monitor performance. Read the guidance on site moves and multilingual sites when relevant. Follow the Search Central blog and help forum.
