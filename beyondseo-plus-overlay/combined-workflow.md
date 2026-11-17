# Combined workflow: BeyondSEO evidence plus the Ghulam Ali strategy layer

Use this for any website. It fixes the order of work so a site gets evidence first, priorities second, safe changes third and a measured follow-up last. BeyondSEO's own commands and evidence rules (see [SKILL.md](../../SKILL.md)) are unchanged; the playbook in [../ghulam-ali/](../ghulam-ali/README.md) says what to do and why.

## Step 0: preflight

1. Run the runtime check from SKILL.md (`python3 scripts/run.py doctor`, Windows `py -3 scripts/run.py doctor`). If it fails, use `--mode http` or supplied evidence and say JavaScript content was not verified.
2. If the `seo-site-audit` skill is installed, use it for Google's rules and platform fixes (WordPress, WooCommerce, Shopify, Rank Math). If it is not, Google Search Essentials is the tie-breaker. Say which one you used.
3. Get only what blocks the work: URL, goal, platform, what you may change, who has Search Console. Look up everything else.
4. **Read-only by default.** Crawling public pages and reading Search Console is fine. Any change to a live site, any message, any indexing request waits for the user's yes on a specific list (Step 3).
5. Look for the site's own notes (`CLAUDE.md`, `README`, `SITE-NOTES.md`) and follow their rules (for example "no em dashes", "shipping changes wait"). If none exist, create `SITE-NOTES.md` from [the template](../../assets/site-notes-template.md) in the site's project folder.

## Step 1: evidence

1. **BeyondSEO.** For "audit this site" run the [complete audit checklist](../../SKILL.md#complete-audit-checklist). A narrow request keeps its narrow scope. Record how many pages were actually crawled: a partial crawl undercounts inbound links, so check the live page before calling a link missing.
2. **Search Console** is the best evidence for a site that already has impressions. Pull the Pages and Queries reports ([three ways](../../references/search-console-triage.md)), then run `python -I scripts/sc_triage.py --pages Pages.csv --queries Queries.csv`. It sorts pages into "fix the snippet", "needs ranking help, not a new title", "probably zero-click", "seasonal" and "skip" and prints the thresholds it used. Treat it as a screen, then read the pages.
3. **Platform checks** (titles, descriptions, H1, schema, sitemaps, robots, redirects, demo or template pages, theme bugs that create 404 URLs) from `seo-site-audit` when available.

## Step 2: prioritise

Choose actions in this order and stop when the list is long enough to finish:

1. Indexing and crawl problems (noindex by mistake, 404 patterns, redirects, blocked pages)
2. Wrong page for the intent, or two pages competing for one query
3. Snippet fixes (title, description) **only where the query data supports them**
4. Internal links to pages that deserve more weight
5. Near-win refresh: pages at positions 8 to 20 get the query's wording covered in the text, answer-first sections and, where the platform allows, visible Q&A with matching FAQ schema
6. New topical pages from content gaps
7. Links from relevant, real sources
8. GEO layers (chunkable answers, entities, third-party mentions)

Route the details through the [playbook index](../ghulam-ali/README.md). For an established shop or business site start with [grow-existing-site-without-new-content](../ghulam-ali/grow-existing-site-without-new-content.md); for a new site start with [new-site-30-day-roadmap](../ghulam-ali/new-site-30-day-roadmap.md). Where the two sources overlap or differ, see [combining-with-beyondseo](../ghulam-ali/combining-with-beyondseo.md).

Label every recommendation with where it comes from: **evidence** (crawl or Search Console), **Google guidance**, or **Ghulam Ali method** (his claim, not verified). Google's documented behaviour wins any disagreement. BeyondSEO's no-guarantee rule applies: never promise rankings, traffic or AI citations.

## Step 3: propose before changing

Show a table the user can approve line by line: page, change, before and after text, the query or number that justifies it, risk, and how it is undone. Long text (new sections, Q&A) goes in a draft file for review first. Say plainly what you are leaving alone and why (a title that already holds position 7, a page changed this week and still settling).

## Step 4: apply safely

1. Back up first (database dump or the platform's equivalent) and keep every old value in a clearly named backup field or file.
2. Change only what was approved. Run content writes as an administrator on platforms that strip markup for lesser users (WordPress `unfiltered_html`; Elementor data).
3. Read back what was saved and stop on any difference.
4. Purge the page cache as well as the object cache, then **verify on the live HTML**: title, description, canonical, schema, the new links, HTTP 200. Look at layout changes (tables, new blocks) in a real browser on desktop and phone.
5. Respect the client's content rules from their notes. Facts in new text come only from the same page or the client, never from memory.

Recurring traps are in [field lessons](../../references/field-lessons.md).

## Step 5: measure and keep notes

- Re-pull the same Search Console reports after 2 to 4 weeks with the same date length and compare per page. Do not claim a change worked inside the first two weeks; seasonal pages move with the calendar, not only with edits.
- Append to `SITE-NOTES.md`: what changed, where the old values are, the evidence, the next check date, what the user still has to do.
- A lesson that would help on the next site goes into `references/field-lessons.md`.

## Honesty rules

- Say what was and was not checked (pages crawled, date range, sources unavailable). A partial result is labelled partial.
- Ghulam Ali's numbers are his claims. CTR is not a direct Google ranking signal; a better snippet earns more clicks from the same position, and that is the honest reason to improve one.
- Skip his sales pitches, shared tool accounts and cheap guest-post bundles.
- No shared or borrowed credentials, no entering passwords for the user, no bypassing sign-in, CAPTCHAs or rate limits.
