# Grow traffic from pages you already have (no new content)

Source: "5 Easiest Ways to Increase Organic Traffic to Website" (19K views, about 5 minutes), plus the thin-content and category-page remarks in "My SEO Strategy to Rank a website Fast ( SAAS, eCommerce, Business )". Read from YouTube's transcript panel in the original language and translated by hand.

This is the most directly useful file for an **established site or shop** such as marianholyart.com: every item works on pages that already exist and each is checkable in Search Console. His framing: the five ways agencies use to grow client traffic without writing new content.

## The five ways

### 1. Refresh the meta title and description (raise click-through rate)
His case: a client's CTR climbed after meta changes, and a higher CTR is a way to move up. (Google's own position is that clicks are not a direct ranking signal, but a better snippet earns more clicks from the same position, which is a gain either way. Say so to the user.)

Tactics:
- **Use numbers:** "Best LinkedIn Tools of 2026" becomes "The Best 12 LinkedIn Tools in 2026".
- **Use authority words**, in the pattern competitors use. Look at the other results for your keyword, spy on how they write titles, mimic the pattern, do not copy.
- Make sure the title contains the exact keyword that shows in Search Console, the one you want to rank for.

### 2. Hunt for high impressions and low CTR
In Search Console, filter for pages with **many impressions but few clicks**. Google is showing you to people and nobody clicks. Updating the meta data may help. If it does not, one of two reasons applies: the page is not well optimised for those queries (covered in item 4), or the page lacks the authority to climb.

### 3. Build internal links with the right anchors
An under-rated practice: it connects pages for users and passes authority around the site. In most sites each URL has one or two internal links and many have zero. The fix is simple: **add links pointing to pages that are missing internal links.** Warning from him: overdo it and the site "burns" quickly, so keep it natural.

How to find pages with no or few internal links (Ahrefs Site Audit, internal pages report): open the audit, go to the **Most internally linked pages** view; it lists target pages with the total number of internal links, and a drop-down lists the pages linking to each. Sort and export to decide. BeyondSEO's crawl gives the same internal-link data without Ahrefs; see [technical-seo-audit.md](technical-seo-audit.md) for orphan-page handling.

### 4. Refresh your content
"The oldest trick in SEO": freshness. Google likes it and LLMs like it even more. In practice:

- Take the exact queries in Search Console where impressions are high and clicks are low. They are the starting point because Google is signalling them.
- If the page ranks for a word or phrase that **is not in the content**, cover it. Most people stuff the query into the text as is. Instead write **semantically optimised content around** those words, even if it is only one paragraph, and add it to the page. That quickly brings traffic from those keywords.
- He publishes prompts for this on his own site; use the ordinary rules in [on-page-and-semantic-content.md](on-page-and-semantic-content.md).

### 5. Strengthen topical authority (content gap)
"Hands down the best SEO concept": the **topical map**, the whole map of your content structure, which gives Google a picture of how much you know about a topic. Aim to cover your chosen topic more fully than your competitors.

How (Ahrefs): Site Explorer, then **Content gap**. It shows competitors with common keywords and the keywords **you have missed but relevant competitors target**. Pick the relevant ones, and that list shows where your gaps are. Fill them, and note this does mean some new pages or sections, so it sits at the edge of "no new content".

## Thin content and category pages (from the SaaS/e-commerce video)

- Claim: a client's traffic nearly doubled just by **updating the content of category pages.**
- His rule of thumb: pages below about **300 words get a "thin content" penalty.** Treat this as his heuristic. Google has no minimum word count; "thin" means pages with little unique value. Use word count only as a prompt to ask whether a page answers the query completely. He adds that ranking may need 1,000 or 2,000 words, depending on the keyword.
- The reason content must serve the visitor: Google measures what visitors do after clicking; if the page does not serve them it drops, even if AI content got it ranking first.

## For the user's WooCommerce or WordPress site

Order of work, cheapest first: items 2 and 1 (Search Console report, then rewrite titles and descriptions on the highest-impression pages), then item 3 (internal links from stronger pages to the weak ones), then items 4 and 5 (content refresh and gaps). Re-check Search Console after a few weeks. This is what the 17 Nov 2026 pass on marianholyart.com did for the paged archives, the Quick answers blocks and the Lourdes Live title; see that project's changelog.
