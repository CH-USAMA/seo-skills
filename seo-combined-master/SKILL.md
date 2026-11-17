---
name: seo-combined-master
description: One entry point that runs BeyondSEO (evidence - crawl, audit, competitors, backlinks, reports), the Ghulam Ali playbook (priorities and tactics) and seo-site-audit (Google's rules, WordPress/WooCommerce/Shopify fixes) together on any website. Use whenever the user wants to improve, audit, plan or grow a website's SEO or AI-search visibility, start work on a new client's site, "do SEO on this site", read Google Search Console data, rewrite titles and descriptions, find pages stuck near page one, plan content, internal links or backlinks, or repeat the method used on one site on another. Trigger on "SEO", "audit my site", "Search Console", "rank", "GEO", "AEO", "another website", "new client site", "BeyondSEO", "Beyond Tahir", "Ghulam Ali", even if no skill is named.
metadata:
  version: 0.1.0
  built-from: beyondseo (Muhammad Tahir Ashraf), ghulamali-seo-master, seo-site-audit, and field lessons from marianholyart.com
---

# Combined SEO master

This skill is the **conductor**. It does not replace the three skills it uses; it fixes the order they are used in, so a site gets evidence first, priorities second, safe changes third and a measured follow-up last.

| Layer | Where it lives | Use it for |
|---|---|---|
| Evidence | `~/.claude/skills/beyondseo` (do not edit it; its updater refuses edited files) | Crawl, audit, competitor discovery, backlink and reputation checks, branded reports, 30/60/90-day plans |
| Priorities | `~/.claude/skills/ghulamali-seo-master` (SKILL.md routes to 18 references) | What to do first and why: keywords, topical maps, content, internal links, GEO, local SEO, new-site plans |
| Rules | `~/.claude/skills/seo-site-audit` | Google Search Essentials, Rank Math/Yoast, sitemaps, schema, redirects, shop and theme bugs |
| Method | this folder | The workflow below, a Search Console triage script, field lessons, a per-site notes template |

Resolve `~` to the user's home folder. Read the other skills' files by path when a step needs them; do not paste their content here.

## Step 0: preflight

1. List `~/.claude/skills`. If `beyondseo`, `ghulamali-seo-master` or `seo-site-audit` is missing, say which one and carry on with the others. Never pretend a missing layer ran.
2. BeyondSEO needs a runtime check before crawling: `python3 ~/.claude/skills/beyondseo/scripts/run.py doctor` (Windows: `py -3`). If it fails, use `--mode http` or supplied evidence and say that JavaScript content was not verified.
3. Get only what blocks the work: the URL, the goal, the platform (WordPress, Shopify, other), what you may change, and who has Search Console. Everything else you can look up.
4. **Read-only by default.** Crawling public pages and reading Search Console is fine. Any change to the live site, any message, any indexing request waits for the user's yes on a specific list (Step 3).
5. Look for the site's own notes (a `CLAUDE.md`, `README` or `SITE-NOTES.md`) and follow its rules (for example "no em dashes", "do not name the pope", "shipping changes wait"). If none exists, create `SITE-NOTES.md` from `assets/site-notes-template.md` in the site's project folder.

## Step 1: evidence

1. **BeyondSEO.** For "audit this site" run its complete audit checklist (`beyondseo/SKILL.md`, section "Complete audit checklist"). For a narrow request keep the narrow scope. Record how many pages were actually crawled: a partial crawl undercounts inbound links, so check the live page before calling a link missing.
2. **Search Console** is the best evidence for a site that already has impressions. Pull the Pages and Queries reports (see [references/search-console-triage.md](references/search-console-triage.md) for the three ways to get them), then run:
   ```
   python -I <this skill>/scripts/sc_triage.py --pages Pages.csv --queries Queries.csv
   ```
   It sorts pages into "fix the snippet", "needs ranking help, not a new title", "probably zero-click", "seasonal" and "skip", and prints the thresholds it used. Treat its output as a screen, then read the pages.
3. **Platform checks** from `seo-site-audit` (titles, descriptions, H1, schema, sitemaps, robots, redirects, demo or template pages, theme bugs that create 404 URLs).

## Step 2: prioritise

Choose actions in this order, and stop adding items when the list is long enough to finish:

1. Indexing and crawl problems (noindex by mistake, 404 patterns, redirects, blocked pages)
2. Wrong page for the intent, or two pages competing for one query
3. Snippet fixes (title, description) **only where the query data supports them**
4. Internal links to pages that deserve more weight
5. Near-win refresh: pages at positions 8 to 20 get the query's wording covered in the text, answer-first sections and, where the platform allows, visible Q&A with matching FAQ schema
6. New topical pages from content gaps
7. Links from relevant, real sources
8. GEO layers (chunkable answers, entities, third-party mentions)

Route the details through the Ghulam Ali SKILL.md table (keywords, topical mapping, on-page, local, new site, tool sites, why a site does not rank, growing an existing site). For an established shop or business site start with `grow-existing-site-without-new-content.md`; for a new site start with `new-site-30-day-roadmap.md`.

Label every recommendation with where it comes from: **evidence** (crawl or Search Console), **Google guidance**, or **Ghulam Ali method** (his claim, not verified). Google's documented behaviour wins any disagreement. BeyondSEO's no-guarantee rule applies: never promise rankings, traffic or AI citations.

## Step 3: propose before changing

Show a table the user can approve line by line: page, change, before and after text, the query or number that justifies it, risk, and how it is undone. Long text (new sections, Q&A) goes in a draft file for review first. Say plainly what you are leaving alone and why (a title that already holds position 7, a page changed this week and still settling).

## Step 4: apply safely

1. Back up first (database dump or the platform's equivalent) and keep every old value in a clearly named backup field or file.
2. Change only what was approved. Run content writes as an administrator on platforms that strip markup for lesser users (WordPress `unfiltered_html`; Elementor data).
3. Read back what was saved and stop on any difference.
4. Purge the page cache as well as the object cache, then **verify on the live HTML**: title, description, canonical, schema, the new links, HTTP 200. Look at layout changes (tables, new blocks) in a real browser on desktop and phone.
5. Respect the client's content rules from their notes. Facts in new text come only from the same page or the client, never from memory.

Platform specifics are in `seo-site-audit`; recurring traps are in [references/field-lessons.md](references/field-lessons.md).

## Step 5: measure and keep notes

- Re-pull the same Search Console reports after 2 to 4 weeks with the same date length and compare per page. Do not claim a change worked inside the first two weeks; seasonal pages move with the calendar, not only with edits.
- Append to `SITE-NOTES.md`: what changed, the old values' location, the evidence, the next check date, what the user still has to do.
- A lesson that would help on the next site goes into `references/field-lessons.md` here.

## Honesty rules

- Say what was and was not checked (pages crawled, date range, sources unavailable). A partial result is labelled partial.
- Ghulam Ali's numbers are his claims. CTR is not a direct Google ranking signal; a better snippet earns more clicks from the same position, and that is the honest reason to improve one.
- Skip his sales pitches, shared tool accounts and cheap guest-post bundles.
- No shared or borrowed credentials, no entering passwords for the user, no bypassing sign-in, CAPTCHAs or rate limits.

## Files

- [references/search-console-triage.md](references/search-console-triage.md): pulling the data, reading it, thresholds and caveats
- [references/field-lessons.md](references/field-lessons.md): generalised lessons from real work on a WooCommerce site
- `scripts/sc_triage.py`: Search Console Pages/Queries triage (CSV export or text copied from the report)
- `assets/site-notes-template.md`: per-site notes file
- `examples/`: tiny sample inputs for the script
