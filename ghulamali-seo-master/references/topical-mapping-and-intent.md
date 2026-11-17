# Topical mapping and search intent

Source: "Stop Chasing Backlinks - This Google Traffic Method Works Faster", "How to Never Fail in SEO", "Give me 9min...", "The Only Video You Need to Watch".

## Why it matters

"Google now favours topics rather than keywords." One page built around a topic ranks for many keyword variants. Ghulam Ali shows a single page ranking for about 1,300 keywords, some of which do not even appear in its text. This is why a 100-search keyword can deliver far more than the 50 clicks position one would suggest.

Consequence: **never create separate pages for keywords that share an intent.** They compete with each other (cannibalisation) and neither ranks properly.

## The four intents and what to build

| Intent | Searcher goal | Example | Page type that fits |
|---|---|---|---|
| Informational | Learn something | how to clean a keyboard | Guide, how-to, explainer |
| Navigational | Reach a known site | amazon login | Rarely worth targeting unless it is your brand |
| Commercial | Compare before buying | best gaming laptop, MacBook review | Comparison / listicle with pros and cons for 5 to 10 options (affiliate sites live here) |
| Transactional | Buy now | iPhone price in Pakistan, buy iPhone | Product or service page: price, availability, buy button. E-commerce and local service sites live here |

His two failure examples:

- Product grid with 5 to 10 products and little information on a "best gaming laptop" page. The searcher needs comparison reasoning, so the page is useless to them and does not sell.
- A 5,000-word review for "gaming laptop price in Pakistan". The searcher only wants a price, so long reviews do not convert.

**Rule:** decide intent first, then page type. Check the live SERP: if the top results are all listicles, a product page will not win.

## Topical mapping procedure

1. Export all keywords from research.
2. For each pair, ask: would the same page satisfy both searchers? If yes, same cluster.
   - best gaming laptop / best budget gaming laptop / best gaming laptops 2026 = **one page**.
   - best laptop for graphic design / best video-editing laptop / best laptop for office work = **different pages** (different audiences).
3. Name each cluster by its main topic. That is one page, one primary keyword, the rest as supporting terms.
4. Arrange clusters into a site structure: parent topics, subtopics, pillar pages, then internal links between them (see [on-page file](on-page-and-semantic-content.md)).
5. Write each page as **semantic content on the topic**, not by repeating the keyword (see the on-page file).

## Structure from competitor evidence

In "The Only Video You Need to Watch" the structure itself comes from a competitor: a printing company had a Services menu with parents (vinyl sticker printing) and children (window graphics), and audience pages (printing for hotels in London). Each became its own page. See [competitor-reverse-engineering.md](competitor-reverse-engineering.md).

## Site architecture rules (`pFtYbWx1GSk`, "Website Architecture Playbook", 2026)

A short video on why most businesses fail to rank: **a poor structure**, meaning how the pages are organised and linked. Fix it and the site helps both search engines and visitors. Read from the transcript panel and translated by hand.

**Why it matters (his three reasons):**
1. Google discovers pages by **following internal links**. A page that no other page links to, an **orphan**, will not be indexed properly, and a page that is not indexed earns nothing.
2. Links **pass authority**: link from your strong pages to your weak ones so the "link juice" flows, and the **anchor text** tells Google how the two pages relate.
3. Visitors move from page to page through a clear structure, and you can **walk someone to the buying page** through internal links.

**The three rules of a good structure:**
- **Flat:** every page reachable within **three clicks** of the homepage.
- **Grouped:** one broad **pillar page** with the narrow pages linking to it. This builds topical authority and makes the site easy for Google to understand.
- **No orphans:** a page nothing links to is ignored and not prioritised.

**Building it:**
- Choose the structure for your site type: an online shop uses categories; a publisher uses topics.
- Short URLs that describe the page.
- **Predictable navigation:** main categories in the header; policies, contact and about in the footer; a separate mobile menu if you want one.
- **Breadcrumbs on every page** (a trail back to where the visitor came from).
- Everything goes in the **sitemap**, which you submit in Search Console.

**Repairing an existing site:** run a crawl with Semrush, Ahrefs or Screaming Frog and look for **orphan pages, broken internal links and pages found only after five to seven clicks**. See [technical-seo-audit.md](technical-seo-audit.md) for what to do with each orphan.

**His proof:** he shows an agency client's site that he says grew to a monthly revenue figure (the number is shown on screen, not in the captions) from structure and high-quality content alone. Treat it as a claim. The online-shop version of this, where Shopify cannot nest collections, is in [shopify-seo.md](shopify-seo.md).

## Quick checks for an existing site

- Search `site:yourdomain.com` plus the keyword to spot two pages targeting one intent.
- In Search Console, filter by a query and look at the Pages tab. More than one page getting impressions for the same query is a cannibalisation sign: merge, redirect or differentiate.
- Make sure category/listing pages are written for Google (short, clear) while blog, product and service pages are written for both the user and Google. He says users do not read category pages.
