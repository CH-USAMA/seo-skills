# Combining Ghulam Ali's playbook with BeyondSEO and seo-site-audit

BeyondSEO (v2.11.0 installed at `~/.claude/skills/beyondseo`, by Muhammad Tahir Ashraf) is an executable toolkit: native crawler, audit, competitor discovery, backlink and reputation checks, branded reports, 30/60/90-day plans, and a 206-entry backlink and posting library. It is evidence-first and deliberately **does not** promise rankings.

Ghulam Ali's material is opinionated tactics: what to rank for, in which order, and what to copy. They answer different questions.

## Division of labour

| Question | Use |
|---|---|
| What is actually wrong with this site? | BeyondSEO `crawl` then `audit` (or Search Console data) |
| Who are the real competitors and what do they do? | BeyondSEO `discover` and `competitors`, then [competitor-reverse-engineering.md](competitor-reverse-engineering.md) for interpretation |
| Which keywords and pages should we build first? | [keyword-research.md](keyword-research.md) and [topical-mapping-and-intent.md](topical-mapping-and-intent.md) |
| How do we write the pages? | [on-page-and-semantic-content.md](on-page-and-semantic-content.md) plus BeyondSEO's AEO writing persona and `topical-authority.md` |
| Are there hidden technical issues? | [technical-seo-audit.md](technical-seo-audit.md) as the checklist, BeyondSEO crawl as the proof |
| How do we get AI citations? | [geo-aeo-playbook.md](geo-aeo-playbook.md) priorities, BeyondSEO `playbooks/aeo-geo/` for execution |
| Which links to chase? | [backlinks-and-offpage.md](backlinks-and-offpage.md) for strategy, BeyondSEO `backlink-system/` and `backlinks` for scoring and sources |
| Does this break Google's rules? | `seo-site-audit` / Google Search Essentials, final say |

## Where they overlap (agree)

Answer-first content, structured data, entity clarity, E-E-A-T, crawlability, freshness, internal links, topical authority, relevance over volume of links, "no promises".

## Where they differ (decide consciously)

| Topic | BeyondSEO | Ghulam Ali | Resolution |
|---|---|---|---|
| Promises | Never guarantees ranking or citations | Shows speed demos (7 minutes to page 3) | Treat his demos as one-off case studies, follow BeyondSEO's no-guarantee rule |
| Authority numbers | Its own Reputation Score, explicitly not DR | Relies on Ahrefs DR | Use DR only as a rough screen, rely on indexing, traffic and relevance |
| Link sources | Evaluates and scores sources, flags toxic | Sells cheap guest posts as a warning example | Follow BeyondSEO's toxic-link rules |
| Tool access | Native tools, no API keys needed | Ahrefs, Surfer, NeuronWriter | Use free or user-owned subscriptions only |
| llms.txt | Neutral | Calls it hype | Optional, no promises |

## What this skill adds that BeyondSEO does not have

- The untapped-keyword filter and SERP test with numeric thresholds
- The competitor "copy the strategy" workflow and the DR-versus-referring-domains sanity check
- A semantic-content process driven by a term list from a content tool, with an AI-writing acceptance checklist
- The 8 hidden technical checks as a short list, including server log analysis and per-template speed
- A week-by-week new-site plan that leads with GEO in week 3
- A decision scorecard for choosing sites or skills to invest in

## Suggested combined workflow for any site

1. `beyondseo doctor`, then `beyondseo crawl URL --include-www --out RUN/site` (read BeyondSEO's `SKILL.md` for the full audit sequence).
2. Pull Search Console data if available: queries on positions 8 to 30 and pages with impressions but few clicks.
3. Run the 8-point technical list on the crawl evidence.
4. Build the keyword and page plan from the user's queries plus competitor pages found by `beyondseo competitors`.
5. Choose actions in this order: indexing and crawl problems, intent mismatches, internal links, near-win pages (refresh), new topical pages, then links, then GEO layers.
6. Report using BeyondSEO's `present` command, labelling each recommendation as evidence-backed, Google guidance or Ghulam Ali method.

## Maintenance note

Do not edit `~/.claude/skills/beyondseo`. Its updates would overwrite edits. Keep all Ghulam Ali content in this folder.
