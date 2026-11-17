# Shopify and e-commerce SEO

Sources (all by Ghulam Ali, 2026, Hindi originals translated by hand):

| Video | Views | Used for |
|---|---|---|
| "Shopify SEO Strategy by Ghulam Ali (To Double Sales)", `Zj3pdeV2Lgo`, 17 Mar | 6K | the five mistakes, the nine-part strategy and checklist |
| "SHOPIFY SEO Website Optimization For Beginners", `7dGLsMCW4ic`, 4 Jul | 5K | one-click automation workflow and its cautions |
| "I Took A Shopify Store from $1K to $10K/Month (With SEO)", `In42AU8-GHU`, 9 Apr | 4.6K | the case study and CRO list |
| "The Only PROCESS To Get Organic Sales in SHOPIFY (WITHOUT ADS)", `rZhS-wIv5Qs`, 11 Apr | 2.7K | product-first SEO |
| "Reverse Engineering 1 Cr Monthly Ecom Skincare Store", `9HME8UXh8f4`, 13 May | 2.6K | competitor store teardown |
| "Why Your BLOG Posts Rank But Don't Convert", `_Olv88JFcLs`, 16 Apr | 3.2K | blog-to-sales framework |
| "Right Way to Build an Online Business in 2026", `vSuM9qRiR2M`, 9 Mar | 2.8K | channel choice, in [operating-framework.md](operating-framework.md) |

Read from YouTube's transcript panel in the original language (Hindi with English terms) and translated by hand. Numbers are **his claims from client work**, not verified facts. Say "his method" or "his client case" when you pass them on. Sales pitches (workshops, courses, WhatsApp codes, "buy a cheap Ahrefs seat") are left out on purpose.

**Order of use for a store:** the nine-part strategy first (it is the checklist), then the product-first and case-study sections for keyword and page work, the teardown to find a competitor's easy keywords, the blog-to-sales section once posts already get traffic, and the automation section only if you want a tool-assisted pass.

## The five mistakes he sees on Shopify stores

1. **Treating Shopify like WordPress.** Shopify has its own limits: fixed URL prefixes (`/products/`, `/collections/`, `/pages/`, `/blogs/`), limited control of robots.txt, duplicate URLs created by default, and a flat site structure with no parent and child categories, so breadcrumbs are shallow and the navigation hierarchy is weak. Plan around the limits instead of fighting them.
2. **Ignoring page speed.** His claims: 73% of Shopify stores load slowly, losing most visitors after 3 seconds, and each extra second costs conversions. Causes: heavy themes, too many apps, unoptimised images, no lazy loading, too many third-party scripts. He says speed work alone lifted one client's conversions by about 25%.
3. **Weak product pages.** Owners polish collection pages and neglect products, yet sales happen on the product page. A buyer who searches "red waterproof bucket hat" is not browsing, they are ready to buy. Typical failures: generic description, no unique content, missing keywords, no reviews or testimonials, poor images. Result: traffic without sales.
4. **Duplicate content by default.** One product in three collections gives Google three URLs with the same content. Canonical tags fix it, but most owners never check, and the problem grows with every product.
5. **No content marketing.** Products and collections only is not enough. Long-tail guides, buying guides, how-tos, product comparisons and educational posts bring in people who then trust the store. His example: "coffee beans" is hard, "best coffee beans for French press beginners" has almost no competition and strong buying intent.

## Strategy in order (his "game plan")

### 1. Foundation
- **Custom domain** (`yourstore.com`, not `yourstore.myshopify.com`): brand authority, trust, SEO.
- **Google Search Console**: submit the sitemap, watch indexing, track queries, find errors.
- **Google Analytics 4** with e-commerce tracking, goals and conversions, traffic sources.
- **SSL**: Shopify provides it, just make sure it is enabled and URLs load on `https`.
- **Sitemap**: Shopify generates it automatically at `/sitemap.xml`. Submit it in Search Console.

### 2. Keyword research for shops
Match the keyword type to the page type:

| Page | Intent | Example |
|---|---|---|
| Product | transactional | "buy organic coffee beans online", "best running shoes under $100", product name plus price |
| Collection | commercial | "summer dresses for women", "men's casual shirts", "vegan skincare products" |
| Blog | informational | "how to brew perfect coffee", "best fabrics for summer", "skincare routine for oily skin" |

His Ahrefs recipe for product keywords: Keyword Explorer, enter the niche's main term, open **Matching terms**, then set filters. **Include: any word "buy"**, and **exclude** the modifiers you do not serve (his example: "price in pakistan", for a market he does not sell into). The list that remains is product and brand-shaped keywords. Search each in Google, then study the competitors that appear, or take **low-DR** competitor sites and look at which of their product pages rank and for what.

Do not target broad terms. "Waterproof running shoes for women size 8" beats "running shoes": higher intent, far lower competition.

### 3. Site structure
- **Collections as the hierarchy**: home, then a broad collection, then a more specific one, then the product. Example: Clothing, Men's clothing, Men's shirts, Casual shirts or Formal shirts. Shopify cannot nest collections natively, so build the hierarchy in the menus, in internal links and in breadcrumbs.
- **URL handles**: you cannot change the prefix but you can edit the handle. `/products/blue-item-123` is poor, `/products/organic-colombian-coffee-beans` is good. The handle is made from the title at creation, so edit it by hand: short, descriptive, with the keyword.
- **Breadcrumbs and schema**: Shopify breadcrumbs are limited, so lean on schema to tell Google what each page is.
- **Internal links**: related products, collection to products, blog to products, homepage to collections. Every page must be linked from at least one other page. An **orphan page** (no internal links) will not rank, because nothing connects it to the rest of the site.

### 4. Product page optimisation (the money page)
- **Title formula** (his): audience, colour, material or type, product, key benefit or use. "Blue shirt" becomes "Men's blue linen casual shirt, breathable summerwear".
- **Description framework** (300 to 800 words depending on the product; never paste the manufacturer's text):
  1. **Hook**: the problem or desire in 2 to 3 sentences ("tired of sweating in regular shirts in summer?").
  2. **Solution** paragraph: how this product fixes it.
  3. **Features written as benefits**, as bullets.
  4. **Use cases**: one paragraph on how and where it is used.
  5. **Trust signals**: customer reviews, money-back guarantee, free shipping.
  6. **Call to action**: add to cart, optionally with limited-stock wording (adjust honestly; do not invent scarcity).
- **Images**: they rank separately in Google Images, and images and videos on a page can win their own results. Use descriptive file names, alt text containing the main keyword, compression (TinyPNG or a Shopify app), **5 to 8 angles** per product, and zoom.
- **Product schema**: use Google's Structured Data tools to build and validate the markup (Rich Results Test), then add it to the page. Error-free before you publish.
- **Customer reviews** are "SEO gold": fresh user-written content, natural long-tail phrases, trust, engagement. Apps he names: Judge.me, Yotpo, Loox.

### 5. Collection page optimisation
- Most collection pages ship with **no text**, which he calls a big mistake. Add **300 to 500 words**: a short intro of about 100 words above the product grid, then the grid, then a longer guide (300 to 400 words) below the products.
- Title and meta formula, with an example, as for products (keyword, benefit, brand).
- **Filters and faceted navigation** (size, colour, price) create many duplicate URLs. His fix: `rel="nofollow"` on filter links, `noindex` on filtered pages, canonical pointing at the main collection URL.
  *Caution (my note, check against Google's docs and the theme before applying):* Shopify already canonicalises most filter and collection-product URLs, and its default robots.txt already blocks some filter parameters. Use the canonical to the main collection as the primary signal; adding noindex on top gives Google mixed signals, so test one approach per template and watch the Page indexing report.

### 6. Blog content strategy
- Blogs target **top-of-funnel** keywords (people wanting information). They build awareness, brand searches and trust, and can route readers to products as the solution.
- Types: buying guides, how-to guides, comparisons, problem and solution posts.
- Structure: SEO title, meta description, one H1, intro, table of contents, H2 sections, product recommendations, conclusion with CTA, FAQ section.
- Blog internal linking: to relevant products and collections, and to other posts. Link back in: homepage to the latest posts, product pages to related guides, collection pages to buying guides.

### 7. Technical SEO
- **Canonicals**: Shopify adds them automatically. Verify by viewing source. The canonical points to the shortest URL (`/products/x`), telling Google to ignore the `/collections/y/products/x` copies. One topic, one ranking page.
- **Speed**: light theme, PageSpeed Insights score he wants at 70+ or 80+, compress images (TinyIMGCrush, WebP or JPG or PNG), lazy loading on, **audit apps quarterly** and remove unused ones (every app costs speed), minify CSS and JS (apps he names: Hyperspeed, PageSpeed Optimizer).
- **Mobile**: most traffic is mobile. Responsive theme, touch-friendly buttons, easy navigation, fast mobile load, check with Google's mobile-friendly checks. (Google has retired the standalone Mobile-Friendly Test; use PageSpeed Insights and Lighthouse.)
- **Structured data**: beyond Product, add BreadcrumbList, Organization, LocalBusiness, Article and so on, matched to page type. Note: Google now shows FAQ and HowTo rich results only in narrow cases, so add FAQ schema for clarity, not for a guaranteed rich result.
- **robots.txt**: his claim is that access is limited. In practice Shopify lets you edit it through a `robots.txt.liquid` template in the theme; keep Shopify's defaults and add only what you need. He shows a snippet to paste, so take it as an example and diff it against the default first.

### 8. Backlinks for Shopify
Why shops struggle: new domain, no authority, thousands of products, nothing worth linking to, strong competition. His answers:
1. **Product reviews**: give free product to niche bloggers (DR 20 to 40), YouTube reviewers and Instagram influencers in exchange for an honest review with a link.
2. **Resource content**: ultimate guides, industry statistics, free tools or calculators, infographics; then outreach to relevant sites.
3. **Guest posts** on niche blogs (a coffee store should guest-post on coffee blogs). He says buying is possible. Prefer real placements on relevant sites.
4. **Broken link building**: Ahrefs on competitors, find their broken backlinks, publish equivalent content, ask linkers to switch.
5. **Digital PR**: press releases for launches, partnerships, achievements, unusual stories.
6. **Local citations** if there is a physical store: Google Business Profile, Bing Places, industry directories, with consistent name, address and phone.

### 9. Measure
- **Organic traffic**: organic sessions, new vs returning visitors, pages per session, bounce rate, average session duration.
- **Rankings**: target keywords, competitors, quick wins.
- **Conversions**: organic conversion rate, **revenue from organic**, average order value, cart abandonment rate.
- **Technical health**: indexing status, Core Web Vitals, mobile usability, crawl errors, broken links.
- Tools he lists: Search Console, GA4, Ahrefs, Semrush, Shopify Analytics, PageSpeed Insights, Hotjar.

## One-click automation workflow (beginner demo, `7dGLsMCW4ic`, 4 Jul)

This video is a screen demo of a third-party Shopify SEO app (its name is garbled in the transcript, it sounds like "SEO Will"), plus its Chrome extension. He says he found it recently and was impressed; the transcript does not say whether he is paid or affiliated, so treat it as a demo, not a recommendation of that product. What is worth keeping is the **order of work and the checklist**, which you can follow with any tool or by hand:

1. **Speed first.** Turn on automatic image optimisation for new uploads (medium compression: smaller files, no visible loss). Compress existing product, collection and blog images in bulk. **Duplicate the theme before any automated speed change** so there is a rollback copy. Then verify in Google PageSpeed Insights, mobile and desktop.
2. **Content creation from a seed keyword.** Give the tool the store context (products, attributes, the buyer persona), the country and language. He walks through: topical overview, pick competitor pages from the Google results as references, an outline with a note under each heading, semantic keyword extraction, internal links to existing products and pages, then generate and publish. His point: a draft is not enough, it needs a semantic coverage score (his example scored 94) and entity, heading and link checks.
3. **Content score per page.** List every product, collection, blog post and the homepage with a score; fix the lowest first, aim for 90+. Typical flags: primary keyword missing from the title, not in the first paragraph, no images in the description, short description.
   *His own demo shows the risk:* the tool picked a stock-status phrase ("inventory not tracked") as the primary keyword for a product. **Always read what the auto-optimiser chose before accepting all.** One-click "accept all" is a time saver, not a strategist.
4. **Audit fixes that are safe to automate:** missing image alt text (pattern: product title), missing meta titles and descriptions on products, collections and blogs.
5. **Technical:** broken links and redirects, structured data on (Product with shipping and return-policy data, Organization with logo and social profiles, LocalBusiness with address and hours if you have a shop), sitemap submitted, site added to **both Search Console and Bing Webmaster Tools**, instant indexing only once the pages are really ready.
6. **Keywords:** rank tracking per target keyword, suggestions with volume, assign a keyword to a product, track a competitor, connect Search Console so the data is in one place.
7. **Chrome extension for a quick page audit:** title, headings structure, links, images with missing alt text, shown red or green.

Cautions I add, because they disagree with Google's guidance or with this playbook's own rules:
- **Do not bulk-redirect every 404 to the homepage.** He demos one click that does exactly this. Google treats mass redirects to the homepage as soft 404s. Redirect a dead URL to the closest relevant product or collection, and let truly gone pages return 404 or 410.
- **Link-exchange networks** (he calls the app's "exchange backlinks" feature his favourite: you give links to sites in a pool and receive links from others, 12,000+ sites listed) are what Google's spam policies call link schemes. Do not recommend them. (His month-3 plan in [backlinks-and-offpage.md](backlinks-and-offpage.md) also lists "exchanges"; treat anything that works as a large reciprocal-link pool the same way.)
- **llms.txt:** he says many case studies show it does not get a site recommended by ChatGPT or Claude, but it costs nothing, so build it and move on. This agrees with the finding in [geo-aeo-playbook.md](geo-aeo-playbook.md).
- The app's "HTML sitemap" is not the sitemap Google uses. Submit the XML one at `/sitemap.xml`.

## Case study: a Shopify store from about $1K to about $9K a month (`In42AU8-GHU`, 9 Apr)

His claim, no paid ads: the client came with **5 to 10 organic clicks a day** and reached **80 to 100 clicks a day** and a few hundred dollars of daily sales; the store's sales report shows most orders from "direct" and Google search, a little from Google Ads, a small Facebook order. The exact revenue figures are garbled in the transcript, so quote the shape (roughly 1K to 9K a month, goal 50K), not the numbers. "Direct" sales here mean people typing the brand, which he reads as branding working.

The order he followed, which is a good default for any store:

1. **Research the market, audience and competitors first** to make a growth plan.
2. **Product keyword research (Ahrefs recipe).** Keyword Explorer, one main keyword for the niche, the target country, **Matching terms**. For the easiest wins filter for keywords where **sites with DR 5 to 10 already rank in the top 10**. Add e-commerce modifiers to the include filter: "buy", "price", "under" (a price cap), product features, brand names, to get many variations. Then take the top competitor URLs into Site Explorer and read their **top pages**: a product page such as a gaming footrest ranking tells you the keyword to target with *your* product page.
   *Tool note:* he suggests buying a cheap shared Ahrefs seat from a seller. That breaks the tool's terms and this playbook does not recommend it; Search Console plus any legitimate keyword tool covers the same job.
3. **Keyword clustering and topic clustering.** Group the keywords by intent; each group is one topic and gets **one page**. His audit story: a business had built separate pages for several same-intent keywords, so none ranked; merging into one page per topic is what he credits for the first big jump (he says to about $5,000 a month for that client). The aim is one page ranking for hundreds of keywords. See [topical-mapping-and-intent.md](topical-mapping-and-intent.md).
4. **On-page and content.** The checklist (title tag, meta description, URL, semantic content, internal and external links, schema) matters, but content is the heavy part. Whether AI-written or human-written, it must be **semantic and entity-rich, easy to read, answer the buyer's real problem, and focus 100% on the intent**. See [on-page-and-semantic-content.md](on-page-and-semantic-content.md).
5. **Technical, because a broken site cancels all of the above.** He claims fixing only technical issues doubled one client's traffic. His broad list: site architecture (a consistent URL pattern and internal linking), speed (compress images, a **CDN**, minify HTML, CSS and JS, audit redirects), mobile friendliness (mobile-first indexing, 60 percent or more of traffic), HTTPS. Load time over about 2 seconds, no mobile layout, no HTTPS and weak structure each stop Google discovering or ranking the site. (On Shopify, HTTPS and a CDN are built in; the work is images, apps and theme weight.)
6. **Backlinks last**, only for topics that stay out of reach after everything else is right. He says links are the costliest part of SEO, so he ranks clients with on-page and content first. His definition of a quality link: from a **relevant** site; **in the body**, not header or footer; **anchor text that is not the exact main keyword**; the linking site's **DR and traffic are not manipulated and the traffic is real, on genuine keywords**; and the linking page is itself **indexed**. Guest posts, niche edits, digital PR and Web 2.0 sites all pass if those hold. See [backlinks-and-offpage.md](backlinks-and-offpage.md).
7. **Conversion rate optimisation (CRO), because traffic without sales is a different problem.** His summary list:
   - **CTAs**: clear action wording, visually prominent, test placement, colour and copy.
   - **Page speed**: his example, 3 s down to 2 s lifts conversion.
   - **Social proof**: reviews, testimonials, ratings, case studies, trust badges, shown where the buyer decides.
   - **Forms and checkout**: fewer fields, enable guest checkout, remove steps that are not needed.

## Product-first SEO (`rZhS-wIv5Qs`, 11 Apr)

Same framework as the 9-step strategy above, compressed into a product-led process. His claim: for one client about **80% of organic sales come from product keywords**, and he ranked product pages directly to get them. What is new here:

- **Four blunders** he says explain why "97% of e-commerce sites get zero Google traffic" (his figure, no source given): pasting the manufacturer description (the same text sits on 100 sites, so Google has no reason to pick yours), **wrong keyword targeting** (trying to rank for "buy Nike shoes" when Nike and Amazon already hold it), **thin pages** (50 to 100 words, no reviews, no FAQs), and **no Product schema**, so Google does not know price or availability.
- **Pick the keyword you can win.** "Gaming laptop" is impossible. "Gaming laptop under 80,000 in Pakistan" (price cap plus market) is realistic. Same Ahrefs path: Matching terms, filters, pick one keyword, Google it, find the low-DR competitors, open their keywords for product terms.
- **The 2026 product page is a set of sections, not three lines and a button.** Title (main keyword, brand, key features) → detailed description → **specifications table** → **FAQs** → **customer reviews**. The old pattern (keyword in title, two or three lines, add to cart) is what he calls outdated.
- **Meta description 150 to 160 characters** with the price, the benefits and a call to action. Clean, keyword-rich URL. Alt text with the keyword, compressed images, several angles and lifestyle photos.
- **Internal links** from the product to related products, its category page and a buying guide, and links back from those.
- **Schema:** Shopify adds Product schema automatically. On WordPress/WooCommerce you add it yourself (Google's Structured Data tools, or the SEO plugin), then verify the product URL in Google's **Rich Results Test**.
- **Technical order for shops:** speed first, then mobile, then duplicate content, then **out-of-stock handling**. He names it but does not explain it. My note, from Google's guidance: keep the page live while the item is temporarily out of stock, mark availability as out of stock in the schema, and show alternatives; 301-redirect to the closest replacement only when the product is gone for good.
- **Topical authority loop:** buying guides, comparison posts, how-to guides and category content. Link product pages to them and them to products; this is what he says makes Google rank the products sooner.
- **Link ideas specific to products:** send products to influencers and bloggers for honest reviews with a link; get included on **comparison sites**; get added to industry **"best X products" resource lists**; list in local directories and optimise the Google Business Profile.

## Reverse-engineering a competing store (`9HME8UXh8f4`, 13 May)

A teardown of a skincare store in Pakistan that is actually one of his agency's clients, shown "for education". Treat the revenue as an illustration: roughly **250K organic visits a month** (a SimilarWeb-style estimate), so with a 1% conversion that is about 2,500 orders, and at the 5,000 to 8,000 PKR price points and a large enough margin per order he gets to "about 1 crore PKR a month". The margin figure is garbled in the transcript and the maths is back-of-envelope, so do not quote the revenue. The **method** is the useful part, and it works on any competitor store:

1. **Read the authority against the traffic.** Domain registered in 2020, DR 32, only 145 referring domains, yet 250K visits. His rule of thumb: *a site with strong traffic and weak backlinks is almost certainly targeting easy keywords*, so its traffic is stealable with a proper plan. (Check it, do not assume it: the next step is the test.)
2. **Open its top pages in Ahrefs** (Site Explorer, Top pages) and group them. Here: the home page on brand terms, then mostly **collection (category) pages**, a few product pages. Category pages carry the volume and the buying intent for a shop.
3. **Category keyword formulas to copy:** product plus price, brand name plus country, or the brand name alone.
4. **Test "easy" with the live results.** Take one keyword the store ranks for and Google it. Here four of the top ten were DR 17, 28, 32 and 33 (traffic 3.4K to 22K): easy to medium. Repeat for a few more keywords.
5. **Look at the page itself.** The ranking category pages were product grids with **no text at all**, and still ranked because competition was so low. His point: you can beat them. If you add text, his checklist is: semantically optimised, on-page optimised, **500 to 1,000 words**, written as genuinely helpful content, by a native human writer (AI-assisted is fine, pasting raw AI output is not).
6. **Read its backlinks:** Ahrefs Backlinks, one link per domain, sort by DR. In this case the top-DR links were a free YouTube link, links from image sections, and a pile of low-DR junk that "builds itself". His quality test: **relevant site, real high-authority site, link in the page body, relevant anchor text, on the parent domain not a subdomain**.
7. **Check speed on both devices.** Desktop was fine, mobile was weak, so this store is probably leaving mobile traffic on the table. His framing: speed does not lift you directly, it stops you being held back.
8. **Turn it into a plan** as a new store in the same niche: use this site as the prime competitor and pick its easy keywords on purpose.

## Blog posts that rank but do not sell (`_Olv88JFcLs`, 16 Apr)

His case: a Pakistani fashion brand on Shopify, **12,000+ blog visitors a month and 8 orders in 3 months**. Its top post ("how to style a floral kurta on Eid", about 3,000 searches a month, position 2) was good content with **no product links, no CTA, no buy button**. Readers read and left. The fix is a five-step framework he calls content to revenue (the transcript spells it "R2R"; it is the same content-to-revenue gap he names in the intro).

1. **Intent audit.** There are four intents: informational, navigational, commercial, transactional. Do this today: open Search Console, take the **top 10 pages**, write down each page's main query, Google it. If the results are Wikipedia, how-to blogs and news, the query is informational: it brings traffic and few sales. Informational keywords can still sell if the page is built for it (steps 2 to 5).
2. **Match each post to the buyer's stage.**
   - *Awareness / informational* ("how to style a kurta"): embed **related products inside the article as the solution**, with internal links, so the reader's next step is your product.
   - *Comparison / commercial* ("best kurta brands in Pakistan"): add a **comparison table** and highlight your own brand.
   - *Decision / transactional* ("buy floral kurta online"): do not write a blog post, **rank the product page** itself.
   - Brief writers and AI to weave the product in as the solution rather than appending a plug.
3. **Smart CTAs on every page.** Put one **above the fold**, one **mid-content** where the reader is engaged, one at the end (the end converts least, so do not rely on it). Write specific wording, not "click here" or "contact us for more info": "Get a free SEO audit", "WhatsApp us", "limited stock before Eid" if true. **Test several CTAs** to find the winner.
4. **Close the trust gap** (Google and readers both need it, and he says it matters most in 2026): author bio with real credentials, client testimonials with results or screenshots, clear contact details (phone, email, address), privacy policy and terms pages, secure-site badge, real product or service reviews. His claim: adding an author bio and three testimonials took one client's conversion rate from **1.2% to 4.7%**.
5. **Make the page conversion-ready.** Speed (over about 3 seconds and visitors bounce), mobile (the CTA button must be tappable and visible), fewer distractions (too many widgets, pop-ups and menu items confuse), and an **above-the-fold** that says what you sell and why.

Use it as a diagnostic: a page that ranks and gets no clicks on product links is a missing step 2 or 3; a page with clicks and no orders is usually steps 4 or 5.

## How to use this on a store

1. Get evidence first (BeyondSEO crawl and Search Console), then check each store against the nine sections above in order. Foundation and the product and collection pages usually pay back fastest.
2. Product pages before blog posts; collection copy before new collections.
3. Never ship the manufacturer description. Write the hook, solution, benefits, use case, trust, CTA structure.
4. Keep the platform limits in mind: you can edit handles, titles, metas, collection text, schema, `robots.txt.liquid`, but not the URL prefix.
5. Review the app list and image weight before anything else if speed is poor.

*Related:* [on-page-and-semantic-content.md](on-page-and-semantic-content.md), [technical-seo-audit.md](technical-seo-audit.md), [backlinks-and-offpage.md](backlinks-and-offpage.md), [keyword-research.md](keyword-research.md), [grow-existing-site-without-new-content.md](grow-existing-site-without-new-content.md).
