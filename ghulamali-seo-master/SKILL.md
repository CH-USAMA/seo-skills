---
name: ghulamali-seo-master
description: Practitioner SEO + GEO/AEO playbook distilled from Ghulam Ali's most-watched 2026 YouTube videos (GMS Digitals), meant to sit on top of the BeyondSEO and seo-site-audit skills. Use whenever the user wants to decide WHAT to do for a website and in what order - untapped keyword research, topical mapping, competitor reverse-engineering, semantic content, technical SEO secrets, backlink quality, the 30-day SEO+GEO roadmap, getting cited in ChatGPT/Gemini/Perplexity, local SEO keywords, Google Business Profile and the map pack, real-estate and restaurant sites, a 30-day plan, why a site is not ranking, growing traffic from existing pages, Shopify and e-commerce stores (product pages, collections, filters, blog posts that sell, competitor store teardown), or ideas for new sites (tool sites, AdSense). Load it together with `beyondseo` whenever BeyondSEO is used for an audit, competitor study, content plan or backlink plan, because BeyondSEO supplies the evidence and this skill supplies the priorities. Trigger on "what should we do for my site", "plan SEO", "SEO strategy", "audit my site", "keyword research", "rank faster", "new website SEO", "Search Console", "GEO", "AEO", "get recommended by ChatGPT", "Shopify SEO", "online store", "product pages", "WooCommerce", "Google Business Profile", "map pack", "local SEO", "Ghulam Ali", even if no skill is named.
metadata:
  version: 0.5.0
  source: youtube.com/@ghulamaliseo, most-watched 2026 videos (see sources/)
---

# Ghulam Ali SEO master playbook

This skill is the **"what to do and why"** layer. It does not crawl anything itself.

| Layer | Skill | What it does |
|---|---|---|
| Evidence | `beyondseo` (installed in `~/.claude/skills/beyondseo`) | Crawls, audits, finds competitors and backlink evidence, writes reports |
| Rules | `seo-site-audit` | Google Search Essentials / Starter Guide checks, WordPress and Shopify fixes |
| **Strategy** | **this skill** | Opinionated, practitioner-tested priorities and tactics, new-site ideas |

Working order for any site: get evidence first (BeyondSEO crawl or Search Console data), then use this skill to choose and sequence the actions, then apply the Google rules in `seo-site-audit` as the tie-breaker. Details in [references/combining-with-beyondseo.md](references/combining-with-beyondseo.md).

## How to read this playbook honestly

- The source is one practitioner (10 years in SEO, agency with 100+ ranked clients). Numbers such as "7 minutes to page 3" or "40% crawl budget wasted" are **his claims, not verified facts**. When you pass them on to the user, say "Ghulam Ali's method" or "his case study", not "SEO fact".
- Transcripts are machine translations from Urdu. Known mis-hearings are in [references/glossary.md](references/glossary.md). Read it before quoting any term.
- Where he contradicts himself or Google, the reference file says so. Google's documented behaviour wins.
- Skip his sales pitches (course batches, WhatsApp codes) and one recurring item: **cheap shared Ahrefs seats from a "trusted seller"** and **cheap spammy guest-post bundles**. Do not recommend either. Shared tool accounts break the tool's terms, and he himself describes low-quality guest posts as nearly worthless.

## Route by task

| The user wants | Read |
|---|---|
| Find keywords that rank fast, judge difficulty | [keyword-research.md](references/keyword-research.md) |
| Group keywords into pages, avoid cannibalisation | [topical-mapping-and-intent.md](references/topical-mapping-and-intent.md) |
| Copy what competitors do without copying content | [competitor-reverse-engineering.md](references/competitor-reverse-engineering.md) |
| Write or rewrite a page, brief a writer or an AI | [on-page-and-semantic-content.md](references/on-page-and-semantic-content.md) |
| Technical audit beyond the basics | [technical-seo-audit.md](references/technical-seo-audit.md) |
| Backlinks, internal links as authority, link quality | [backlinks-and-offpage.md](references/backlinks-and-offpage.md) |
| ChatGPT / Gemini / Perplexity / AI Overviews visibility | [geo-aeo-playbook.md](references/geo-aeo-playbook.md) |
| A brand-new site, step by step | [new-site-30-day-roadmap.md](references/new-site-30-day-roadmap.md) (weekly plan with GEO), [new-website-step-by-step.md](references/new-website-step-by-step.md) (full order of work: research, content, on-page, technical, links) |
| "Why do projects fail", consistency, choosing a skill or business, SEO vs ads vs social vs email as a channel | [operating-framework.md](references/operating-framework.md) |
| A site that does not rank, step by step diagnosis | [why-your-site-isnt-ranking.md](references/why-your-site-isnt-ranking.md) |
| More traffic from pages that already exist (titles, CTR, internal links, refresh, content gaps), good for an established shop | [grow-existing-site-without-new-content.md](references/grow-existing-site-without-new-content.md) |
| Rank without leaning on backlinks, worked keyword example | [rank-without-backlinks.md](references/rank-without-backlinks.md) |
| An online shop (Shopify, also WooCommerce): product and collection page copy, filters and duplicate URLs, store keyword research, blog posts that rank but do not sell, copying a competitor store's easy keywords, CRO basics, link ideas for products | [shopify-seo.md](references/shopify-seo.md) |
| Local business keywords (neighbourhood, near me, landmarks, competitor names, mobile) | [local-seo-keywords.md](references/local-seo-keywords.md) |
| Google Business Profile / map pack: categories, name rules that avoid suspension, reviews, engagement signals, why a competitor outranks you | [google-business-profile.md](references/google-business-profile.md) |
| A real-estate or restaurant client: keyword types, content kinds, location pages, citations, schema | [local-industry-playbooks.md](references/local-industry-playbooks.md) |
| A day-by-day plan for the first 30 days (keyword filter, foundation, content, on-page, links, AI search), as an agency would run it | [agency-30-day-plan.md](references/agency-30-day-plan.md) |
| Seven lessons from ten years, realistic timeline (3 to 6 months), five SEO myths, the one-page keyword test | [seven-lessons-and-timeline.md](references/seven-lessons-and-timeline.md) |
| Tool websites and AdSense: niche, AI-built tool, SEO, a teardown of a "$10K a month" tool site, the site he sold | [tool-sites-and-adsense.md](references/tool-sites-and-adsense.md) |
| Beginner end-to-end: intent types, keyword sweet spot, money pages, 30-day plan | [beginner-blueprint-2026.md](references/beginner-blueprint-2026.md) |

## The ten rules that run through all his material

1. **Pick keywords you can already win.** Low competition first. A weak new site cannot rank for strong keywords, whatever else it does right.
2. **A page ranks for a topic, not one keyword.** One page per intent cluster. A page built for a 100-search keyword can collect traffic from hundreds of variants.
3. **Match search intent before anything else.** Right keyword, wrong page type earns traffic and no sales.
4. **Write semantically.** Cover the whole topic, use the entity and term list from a content tool, answer first, structure for scanning.
5. **Internal links behave like backlinks.** Link new pages from older, stronger pages before paying for anything external.
6. **Link quality beats link count.** Relevant, in-body, on a page that is itself indexed and ranking.
7. **Technical SEO is mostly hidden things.** Log files, JavaScript rendering, orphan pages, link-equity leaks, per-template speed, render-blocking, schema gaps, mobile UX.
8. **SEO is the floor, GEO the second floor.** About 80% of GEO is ordinary good SEO; the extra 20% is chunkable answers, stats, quotes, citations, entity clarity, freshness and third-party mentions.
9. **Consistency wins.** Projects that get steady, intentional attention do not fail; abandoned ones do.
10. **Measure, then loop.** Search Console for pages on positions 8 to 20, a fixed prompt list for AI visibility, then refresh the near-misses.

## Output conventions

- Give the user a ranked action list: what, which URL, why, how to check it worked. Label each recommendation as *evidence-backed* (BeyondSEO or Search Console data), *Google guidance*, or *Ghulam Ali method*.
- Never promise first place or guaranteed AI citations.
- For the user's own sites (for example marianholyart.com, a WooCommerce store), prefer the low-risk items first: indexing and sitemap health, internal links, intent fit of product and category pages, answer-first rewrites of existing pages. Anything that edits a live site goes through the user first.
