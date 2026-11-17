# Local service business playbook (proven patterns)

Use this for sites of local service businesses (taxis, trades, clinics, tour operators, removals and the like), especially when the owner also runs Google Ads. These patterns come from a site with strong organic traffic (a 24/7 taxi company with route, tour and event pages); treat them as the default target, then audit against them.

Contents: page structure / titles, descriptions, H1 / conversion and tracking / ads landing pages / schema and NAP / caching with ads / AI search / technical baseline / checks to run.

## 1. Page structure that wins local searches

- **One page per real search intent.** A service page for each service (airport transfers, minibus, wheelchair-accessible, courier, hospital transport) and a page for each route or area people actually search ("Shannon Airport to Galway taxi", "Knock Airport to Galway taxi"). Do not spin near-identical city pages; each page needs real, specific content (distance, typical fare or how fares work, journey time, what is included, how to book).
- **Seasonal and event content** (local festivals, races, Christmas, New Year, exam season, airport strikes) earns traffic every year. Update the year and details each season instead of publishing duplicates.
- **How-to and decision content** that answers booking questions ("How to book a taxi in X", "Taxi vs bus to the hospital", "Do taxis run on Christmas Day?") pulls in people close to booking and is what AI answers quote.
- **Internal links:** every blog post links to its matching service or route page with descriptive anchor text, and service pages link to their best supporting posts. Check for orphans (the auditor's `NO_INTERNAL_LINKS_IN`); a blog index alone is not enough because older posts drop off its first page.

## 2. Titles, descriptions and H1 (formulas that work)

- **Title:** `Service + Place | Key selling point | Brand`, at most 60 characters. Example: `Taxi Galway | 24/7 Cabs & Fixed Fares | Five Stars Taxis` (56). Pick **one** short brand suffix and use it on every page; mixed suffixes ("Brand", "Brand Galway", "Brand Taxis") look sloppy and push titles over the limit.
- **Meta description:** what the visitor gets, plus a call to action **with the phone number**, 120 to 155 characters. Example: `Book a Galway taxi in seconds, 24/7. Local licensed drivers, fixed fares, no surprises. Tap to call 091 399 999 or book your ride online.` Every page unique; conversion pages (book, contact, quote) deserve the best ones, never a 27-character stub.
- **H1:** one visible H1 naming the service and place (`Galway Taxi Service, Available 24/7`).

## 3. Conversion and tracking

- **Tap-to-call** `tel:` links in the header, in the hero and near every call to action, using the same number everywhere. Consider a WhatsApp link if the business uses it.
- A **booking or quote page** plus an instant price tool (fare or quote calculator) if prices are predictable. Tools convert better than "contact us for a price".
- **Track micro-conversions** with Google Tag Manager dataLayer events (for example `fare_check`, `fare_call_click`, `fare_enquire_open`, `fare_enquiry_submit`) and import the call-click and enquiry events into Google Ads as conversions, so bidding optimises for bookings, not visits.
- Contact forms: confirm submissions actually email someone (SPF covers the web server) and store a copy (for example a CF7 database add-on).

## 4. Google Ads landing pages

- **Match the landing page to the ad group.** "Airport taxi" ads go to the airport route page, "minibus" ads to the minibus page. Sending everything to the homepage lowers Quality Score and raises cost per click.
- Landing pages must load fast **with the ad parameters attached** (see section 6) and must not be blocked to Google's ad checker (security firewalls sometimes block AdsBot; check Google Ads, Policy manager, for "Destination not working").
- Above the fold: the service, the place, the phone button and the booking button. No pop-up before the visitor has seen the offer.

## 5. Structured data and NAP consistency

- Mark the business up as **LocalBusiness** (the closest subtype the SEO plugin offers) with name, address, phone, geo coordinates, opening hours and areas served, matching the visible page. A plain `Organization` misses local signals. Never add ratings or reviews that are not real and visible.
- A contact page should not be typed `Article`; use `ContactPage` or the plugin's page default with the LocalBusiness entity.
- **NAP consistency:** business name, address and phone must be written the same way everywhere: header, footer, contact page, schema, Google Business Profile, `llms.txt`, directory listings. Even formatting variants of the same number (`+353 91 399 999` vs `+353 9139 9999`) should be unified.
- Keep the Google Business Profile in sync (hours, phone, website URL, categories) and link to it from the site.

## 6. Page caching must ignore ad and tracking parameters

Every ad click arrives with a unique `gclid` (plus `gad_source`, `gad_campaignid`, `gbraid`, `wbraid`; Microsoft adds `msclkid`; Facebook `fbclid`; email tools `utm_*`; Google Shopping `srsltid`). Many page caches treat each unique query string as a new page, so **paid visitors always get the slow, uncached page**. Measured on a real site: 1.75 s for ad clicks vs 0.5 s for normal visits, fixed to 0.5 s.

- **WP Super Cache:** Settings, Advanced, "Tracking parameters": tick "Ignore tracking parameters" and add the list above. In `wp-content/wp-cache-config.php` this is `$wpsc_ignore_tracking_parameters = 1;` and `$wpsc_tracking_parameters = array( ... );`.
- **LiteSpeed Cache:** Cache, Advanced, "Drop Query String": add the same keys.
- **WP Rocket:** it ignores common UTM and click IDs by default; add `gad_source`, `gad_campaignid`, `gbraid`, `wbraid`, `srsltid` with the `rocket_cache_ignored_parameters` filter.
- **Cloudflare:** a Cache Rule that ignores those query parameters in the cache key.
- Analytics still works: the tags read the parameters from the browser URL, not from the cached HTML.

Test (compare time to first byte):
```bash
curl -s -o /dev/null -w "plain %{time_starttransfer}\n" https://example.com/
curl -s -o /dev/null -w "ad    %{time_starttransfer}\n" "https://example.com/?gad_source=1&gclid=test$RANDOM"
```
Also confirm a real query (for example `/?s=test`) is still not served from cache.

## 7. AI search visibility

- Publish **`/llms.txt`**: a short Markdown summary (one-paragraph description, business facts: name, phone, email, address, hours, areas served, booking and payment options), then linked lists of the key pages (booking, services, routes, tours, about, contact) and an "Optional" section (blog). Use only facts already on the site. Keep its links in sync with the sitemap (all must return 200) and re-upload after edits.
- Make sure AI crawlers are **allowed by robots.txt and by the host's firewall** (WAFs such as Imunify360 often return 403 to them): OAI-SearchBot, ChatGPT-User, GPTBot (OpenAI), PerplexityBot, Perplexity-User, ClaudeBot, Claude-User, Claude-SearchBot (Anthropic), Bingbot. Check server logs for 403s against those user agents; the host must allow them, the site owner cannot override a server WAF.
- Submit the site to **Bing Webmaster Tools** (import from Search Console) because ChatGPT search and Copilot lean on Bing's index, and enable **IndexNow** (Rank Math "Instant Indexing" or the IndexNow plugin).
- Google AI Overviews and Gemini use the normal Google index: good structure, LocalBusiness data and FAQ-style answers are what they quote.

## 8. Technical baseline (all were in place on the reference site)

- One canonical host: `http://` and non-`www` 301 to `https://www.` (or the reverse), no chains.
- `robots.txt` with only `/wp-admin/` disallowed (plus `admin-ajax.php` allowed) and a `Sitemap:` line; sitemap with only 200, indexable, canonical URLs.
- `<html lang>` matching the audience (`en-GB` or `en-IE` for Ireland); alt text on every content image; width and height on images; lazy loading only below the fold.
- A working page cache (and the right cache plugin for the server: LiteSpeed Cache only caches on LiteSpeed servers; on Apache or nginx use WP Super Cache, WP Rocket or the host's cache).
- After any hosting change or hosting-tool "setup" action, re-check the rendered `<title>`: hosting tools can rewrite the WordPress site name, which silently changes every SEO title that uses `%sitename%`.

## 9. Extra checks to run on these sites

1. Rendered title, description and H1 of the homepage and every ad landing page.
2. Ad-parameter cache test (section 6).
3. External scripts on the homepage: anything not from the site, Google or a known vendor is a red flag (injected malware loads remote scripts and shows fake "verify you are human" pop-ups):
   `curl -s https://example.com/ | grep -oiE '<script[^>]*src="[^"]+' | grep -vi example.com`
4. NAP: grep the homepage and contact page for every phone format and the postcode; they must agree with the schema and the Google Business Profile.
5. `/llms.txt` returns 200 and its links are all in the sitemap.
6. Search Console URL Inspection, "Test live URL" on the homepage (Googlebot allowed), and Google Ads Policy manager (landing pages reachable).
