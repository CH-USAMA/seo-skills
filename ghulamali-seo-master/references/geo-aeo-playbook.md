# GEO / AEO playbook (getting cited by AI search)

Source: "I Spent 2,000 Hours Learning GEO/AEO For This" (12K views), "How to start SEO+GEO from ZERO in 2026" (14K), "The 30-Day SEO+GEO Roadmap" (9K). Statistics below are his citations, not independently verified; each is marked where it matters.

## Position: SEO is the floor, GEO the second floor

- "SEO is dead, GEO is the future": both wrong.
- **SEO gets clicks. GEO gets you quoted.** SEO is being the book on the shelf; GEO is being the answer the librarian speaks. AI answers may mention you without sending a click.
- About **80% of GEO is ordinary SEO** (crawlability, speed, clean architecture, content, authority, E-E-A-T). The new 20% is below.
- AI Overviews and AI Mode are grounded in Google's index. Rankings are "the guest list". He cites ChatGPT citing number-one results about 3.5 times more often, but also that only about 7% of ChatGPT citations overlap with Google's top 10. So rank to enter the pool, then win the seat with GEO tactics.

## How the engines pick sources (RAG in four stages)

1. **Query rewrite / fan-out.** The engine splits your question into many sub-queries. Cover definitions, comparisons, edge cases, objections and the "what next" inside one piece, because your page is tested against the whole fan of questions.
2. **Chunk retrieval.** It retrieves **passages, not pages**, turning each into an embedding. A best answer buried in a 400 to 500 word paragraph will not be picked. Messy structure gives a messy "fingerprint".
3. **Ranking survivors** by relevance, clarity, trust, and **freshness**.
4. **Writing the answer** from the selected chunks.

Three outcomes: selected, integrated into the answer, **named**. The bad one is absorbed without credit. The goal is to climb to "named".

## The four layers

### Layer 1: Content (how every page is written)
- **Answer first**: a complete, self-contained answer in the first **40 to 60 words** of each section, then expand. (Claim: about 44% of cited passages come from the first third of a page, so front-load value.)
- **One idea per section**, own heading, clean passage. Do not mix definition, how-to and case study.
- The Princeton and Georgia Tech GEO study (2023) found three tactics lifting AI visibility by up to about 40%:
  1. **Add statistics**: replace vague claims with hard numbers. One meaningful stat every roughly 100 to 200 words.
  2. **Add quotations**: attributed quotes from named, credible experts.
  3. **Cite sources**: link primary studies, government data, original sources directly (not blog summaries). Helps small sites most.
- **Real FAQs**: 5 to 7 self-contained question and answer pairs on important pages.
- **Formats that get cited**: listicles, "best X", "X vs Y", tables and bullets. (Claim: listicles get about 25% more citations than opinion posts.)
- Write for a smart, busy person first, then add the structure that makes it liftable. No thin content.

### Layer 2: Entity and authority (the AI judges you, not only pages)
- Be a **recognisable entity**: consistent brand and author names everywhere, a clean About page.
- **Schema**: Organization, Article, FAQ, Author, and `sameAs` links to verified profiles. Schema cannot force a citation but removes ambiguity.
- **E-E-A-T**: real author bios with credentials, visible publish and update dates, transparent sourcing. Anonymous content loses.

### Layer 3: Technical (can the machine reach you?)
- **Let AI crawlers in.** Check robots.txt for user agents: GPTBot, OAI-SearchBot (OpenAI), ClaudeBot, Claude-User (Anthropic), PerplexityBot, Google-Extended (Google). The captions garble his sentence about which to allow. The sound reading: **do not block the search and retrieval bots** if you want citations; blocking pure training bots is a separate business choice that does not stop live citations.
- **Speed and clean HTML**, content must render without JavaScript.
- **llms.txt is hype.** He cites that only about 10% of sites using it get fetched, one test found 100 fetches across 500 million sites, and Google says it does not use it. It costs nothing, so add it if you like, but expect nothing.
- **Freshness is real.** Claim: pages updated within 30 days get cited about 3 times more. Keep dates visible in both text and schema, refresh stats, prioritise pricing, comparisons, regulations.

### Layer 4: Off-site (what the web says about you)
Independent, consistent third-party descriptions of your brand matter more than 500 articles on your own domain. Earn mentions in authoritative publications and communities (Reddit, Quora, Facebook groups, directories, "best of" roundups), digital PR, helpful presence. Linked or unlinked both count.

## The strongest move: original proprietary data

Publish data nobody else has (an audience survey, an honest analysis of your own numbers). It cannot be copied, other sites cite it, trusted outlets point to it, and the AI then sees your brand as the origin and starts associating you with the topic. He calls this the one move competitors are too lazy to copy.

## Measuring GEO (do not use visits)

- **AI share of voice**: write 50 to 100 prompts real customers would type, run them on ChatGPT, Gemini, Perplexity and Claude, and record the percentage of answers that mention you. (28 mentions in 100 = 28%.) In the 30-day roadmap he uses a smaller starter list of **10 to 20** prompts.
- **Citation frequency**, **citation quality** (passing mention, paraphrase, named and linked), **sentiment and accuracy**, **referral quality** (few clicks but they convert well).
- AI answers are volatile: never judge from one run; track trends over weeks.
- Reverse-engineer whoever is cited instead of you: copy their format, schema and answer structure.
- Free start: run the prompt list by hand and log it in a sheet.

## What not to overclaim

- Do not say "add llms.txt and you will get citations".
- Do not promise citations. BeyondSEO's own guidance is the same.
- The big stats above are from his video; verify before using them in client deliverables.

## Case study: replacing a local business's ads with organic (`cMD6HkvHvik`, 15 Jul)

"Laziest Way to Get Customers From Google (Without Ads)", 4K views, read from the transcript panel and translated by hand. His agency promised a local service business, which was spending about $3,000 a month on ads at rising cost per lead, that **within 120 days organic sales would replace the ad sales**. Claims, not verified facts:

- **What went wrong:** traditional SEO alone, **no results in the first month**, and ads had been **switched off at the same time**, so the client's business slowed and he asked to turn ads back on. *My note:* do not cut paid ads until organic leads are arriving; taper them. The risky pitch cost them a month of trust.
- **What he found by studying every source AI cited for the client's topics** (AI breaks one question into many small searches, the "query fan-out" above, so you cannot see or track the hidden searches; the question is whether you appear in what the machine reads):
  1. cited businesses had the **same name, address and phone on every directory and platform**; inconsistency makes the machine ignore you;
  2. competitors had **structured factual articles and press-release-style pieces** that language models pick up easily;
  3. their links came from **relevant sites in the same field or area, not big sites**: relation matters more than size;
  4. competitors collected **fresh, real reviews every week**;
  5. a **gap list**: every question where competitors are recommended and the client is not.
- **What they did, in order:** (1) **third-party mentions**, linked and unlinked, on authority publications, review sites, Reddit, forums, Wikipedia-type sources and industry lists; (2) **content structure**: clear Q&A style, definitive statements, a concise summary at the top of the page, FAQs, comparison tables, specific numbers and features, each answer in a **self-contained passage** rather than scattered; (3) **technical access**: no crawler blocked (Google, ChatGPT, Perplexity), schema in place; (4) **topical authority**: cover the niche from every angle with original data and expertise.
- **His result:** in about 6 weeks one page reached number one for one keyword (a very low competition one), and within 2 weeks of that the first customer arrived; the customer's intake form showed they had come from ChatGPT. Google rankings were already on page one or two for low-competition keywords.
- **His conclusions:** Google rankings and AI citations are closely correlated (as rankings rose, citations rose); ChatGPT click-through is very low and most people using AI never click a site, so it helps **branding**, while **Google is still the best traffic source**; AI visibility is "a shiny object": organic traffic is dented, but abandoning search traffic to chase AI alone is self-harm.
- **To use:** the five-point list is a good template for an AI-visibility audit of any local or service business; run it before spending on more content. See also [local-seo-keywords.md](local-seo-keywords.md).

## How BeyondSEO fits

It already ships `playbooks/aeo-geo/` (AEO writing, generative-engine optimisation, citations and source-worthiness, topical authority, AI-overview opportunity audit, entity SEO). Use those for execution and structure, and this file for his priorities, the four-layer order, and the measurement approach. See [combining-with-beyondseo.md](combining-with-beyondseo.md).
