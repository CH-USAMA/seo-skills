# Field lessons (from real work on a WooCommerce and WordPress shop, Oct and Nov 2026)

Generalised so they help on the next site. Add to this file whenever a lesson would have saved time.

## Reading data
- A partial crawl undercounts inbound internal links. Check the live page before saying a link is missing.
- "High impressions, low CTR" often returns false alarms: zero-click questions ("when is X this year") and mid-page-one or page-two positions where a low CTR is normal. Check position and query type first.
- One seasonal page can hold most of a young site's impressions. Look at the share, and plan what the visitors do next (links to the following season's pages).
- Search Console shows no query-to-page pairs in the two summary reports; do not invent them.

## Titles, descriptions and content
- Write titles keyword first, the year for date-driven topics, under about 60 characters, plus the brand. Do not touch a title that already holds a good position for its main query.
- Match the words people type: "holy day" and "2026" in the title when queries carry them, but only if the page truly answers it.
- A visible Q&A block ("Quick answers": answer first, built only from facts already on the page) lifts thin posts and answers the many variants of a question. Generate the FAQ schema from the visible text so the markup and the page cannot disagree.
- Paged archives (blog page 2, 3) need their own titles and descriptions ("Page N"), or they duplicate page 1.
- Date or season in a URL (`.../22-november/`) goes wrong the next year. Prefer year-free URLs for recurring events, or plan the redirect.

## Technical traps
- A theme can print links that crawlers turn into 404 URLs (for example a quick-view magnifier whose href is a bare product ID). Look at the example URLs of a Search Console "Not found" group before assuming old pages.
- Theme demo or template pages (home-2, lorem ipsum, builder tags) should be redirected or noindexed; check what is actually returned (301, 404 plus noindex).
- Fixes that live in a theme file are lost on update. Put permanent fixes in a must-use plugin or the child theme.

## Safe changes on WordPress
- Back up the database first. Keep each old value in a backup meta key or file.
- Save content as an administrator (`wp eval-file ... --user=<admin>`), or markup, styles and scripts get stripped silently. Builder data (Elementor) has the same trap.
- Backups written to meta must be slashed (`wp_slash`) or they are corrupted on read.
- Clear the page cache (LiteSpeed: `wp litespeed-purge all`) as well as the object cache, or the old HTML keeps serving.
- Read back after saving, then fetch the live page and check title, description and the new links.
- Some hosts block `wp db export` and shell functions; use the host's dump tool and the platform's scheduler.

## Search Console actions
- Request Indexing via URL Inspection is flaky. One request per URL, then leave it; Google recrawls on its own.
- Do not press "Validate fix" on 404 groups that are meant to stay 404.
- Pulling reports through the user's signed-in Chrome needs the window in front.

## Working with people
- Put the client's rules in a notes file and read it first (writing style, names to avoid, what waits for their say-so).
- Show proposed copy and get a yes before it goes live; keep a draft file the client can read.
- Say plainly when your own earlier suggestion turned out wrong (for example a "missing" link that existed).
