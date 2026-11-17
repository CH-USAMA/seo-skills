# Search Console: what only the owner can do (and how to read what it says)

An assistant can fix the site, but several steps need the owner's Google login. List the ones that apply in the report, with the exact clicks.

## One-time setup
1. **Verify ownership** at https://search.google.com/search-console. A *Domain* property (verified by a DNS record) covers every protocol and subdomain and is preferred. A *URL-prefix* property for `https://example.com/` also works. To let a helper see the data, the verified owner adds them under Settings, Users and permissions.
2. **Submit the sitemap**: Indexing, Sitemaps, enter `sitemap_index.xml` (or `sitemap.xml`), Submit. Status should read "Success".
3. Optional but useful: link Google Analytics; connect the SEO plugin's analytics to the right property (in Rank Math: Analytics settings, choose the property from the Site dropdown, Save); add the same sitemap in Bing Webmaster Tools (it can import from Search Console).
4. For a local business, claim and complete the Google Business Profile, with the same name, address and phone as the website.

## After you change things
- **URL Inspection**: paste a changed URL, "Test live URL" to see what Google would render, then "Request indexing". Do this for the homepage, contact page, new or rebuilt pages and anything whose old snippet is stale. There is a daily quota, so prioritise.
- In the **Pages** (indexing) report, open each "Why pages aren't indexed" reason and use "Validate fix" once the cause is gone. Validation takes days to weeks; a "some fixes failed" email usually means a few URLs still 404 or redirect.

## Reading the Pages report
| Reason | Usual meaning and fix |
|---|---|
| Not found (404) | A URL Google remembers is gone. 301 it to the closest live page, or leave it if truly gone. Also hunt for the *source*: broken internal links, templates linking to IDs or old paths |
| Page with redirect | Normal for old URLs. Make sure internal links and sitemaps point to the final URL |
| Excluded by noindex | Fine if intended (cart, account, archives); a problem if a real page |
| Duplicate without user-selected canonical / Alternate page with proper canonical | Duplicate URLs. Add canonicals or 301s so one URL wins |
| Crawled, currently not indexed | Google saw it and was not convinced: improve the page (unique, useful), link to it internally, wait |
| Discovered, currently not indexed | Known but not crawled yet: internal links, sitemap, patience |
| Soft 404 | The page looks empty or error-like but returns 200: fix the content or return a real 404 |
| Blocked by robots.txt | Only intended for non-pages |

## Reading a Performance export (Search results, Last 3 to 28 days)
- Files: Chart (daily), Queries, Pages, Countries, Devices, Search appearance, Filters. Data lags 2 to 3 days, so recent edits are not in it yet.
- Compare **impressions per day**, not totals, across periods of different length.
- Pages with impressions but a dead or redirected URL: redirect or fix. Pages ranking 4 to 12 with low CTR: improve title and description. Queries with impressions but no matching page: a content opportunity. Position 50+: Google barely shows it.
- Product snippets, breadcrumbs and other enhancements appear under "Search appearance" and "Enhancements".

## Things that should always be empty
Manual actions and Security issues. If either has an entry, stop and deal with it before anything else.
