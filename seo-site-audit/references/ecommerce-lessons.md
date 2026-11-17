# Online shops: lessons from a real audit (WooCommerce, Oct 2026)

Read this before auditing or advising any shop. Everything here happened on a small WordPress/WooCommerce store
selling EUR 1 to 19 gifts. The examples are specific; the patterns are general.

## 1. Product data must match what checkout charges

- Product JSON-LD (`Offer`) carries `shippingDetails` and `hasMerchantReturnPolicy`. If it says shipping is EUR 5 and
  checkout charges EUR 7, Google can flag a mismatch later. After any rate change, update the markup.
- **Prove it with a cart simulation, not the settings screen.** In WP-CLI, inside `wp eval-file`:
  `wc_load_cart(); WC()->cart->empty_cart(); WC()->customer->set_shipping_country('IE'); WC()->cart->add_to_cart($id);
  WC()->cart->calculate_totals(); WC()->shipping()->reset_shipping();
  foreach (WC()->shipping()->calculate_shipping(WC()->cart->get_shipping_packages()) as $p) { /* $p['rates'] */ }`.
  Test one item, two items, a "free postage" class item, and each destination (home country, EU, rest of world).
- Flat rate "per class" **adds** class costs: item A (class 1, EUR 6) plus item B (no class, EUR 7) costs EUR 13. A
  tempting tweak (moving one product into a cheaper class) can raise mixed baskets. Simulate before and after, and
  revert if any realistic basket gets dearer. "Most expensive class" calculation avoids the trap.
- Every priced `UnitPriceSpecification` needs `validFrom` (Google's non-critical "missing validFrom" warning).
- **Search Console merchant emails often name pages deleted weeks ago.** Open the example URL first: if it now
  redirects or 404s, the fix is already done; validate and wait. Then confirm the live products all pass with a script
  that fetches each product page and parses its JSON-LD.
- SEO plugins (Rank Math) build a product's meta description from its short description when none is set. A
  170-character short description produced an over-long meta description; keep short descriptions under about 150
  characters or set the description explicitly, and re-run the audit after bulk-writing short descriptions.
- Grep product descriptions, FAQ and delivery pages for prices whenever rates change; stale text ("EUR 5 flat rate")
  outlives the setting.

## 2. Theme layout traps that look like content problems

- Featured images in a fixed-height band with `object-fit: cover` slice square product photos. Either supply wide
  images (about 2.5:1) or show square ones whole on white for low-ratio images.
- A drop-down menu and a post image can share the same z-index; the later element wins and covers the menu.
  Prove it with `document.elementsFromPoint(x, y)` over each menu item, then raise the menu's z-index (9999).
- Test at desktop width, 1280, and 375 (phone) with DOM measurements (`getBoundingClientRect`, `scrollWidth`),
  because screenshots in automation tools time out or catch the page before images paint.
- Demo pages from a purchased theme (`/home-2/`, `/home-3/`, "Sample page") still get clicks from Google. Noindex is
  slow; add a 301 to the real page.

## 3. Content that earns impressions

- From Search Console: short posts (under about 250 words) are almost never shown; one long, specific post got most
  impressions. Write 500+ words that answer one real question, link to relevant products and sibling posts, and
  add a "related" line to older posts so new ones are reachable.
- Time seasonal posts (feast days, Advent, First Communion) 4 to 6 weeks ahead; keep a steady cadence (one good post
  every 1 to 2 weeks) rather than bursts.
- Report growth with real counts ("4 to 14 clicks, about 134 to 868 impressions"), not percentages from a tiny base,
  and never promise orders.

- Search Console's "crawled, currently not indexed" and similar lists lag behind. Before acting on an example URL, run URL
  Inspection on it: it may already read "URL is on Google". Most of such a list on a WordPress shop is RSS feed URLs, add-to-cart
  links and wp-admin, which are correct; send feeds `X-Robots-Tag: noindex, follow` to tidy the report. Request indexing has a small
  daily quota ("Quota exceeded"), so spend it on new posts and retry the rest the next day.

## 4. Before recommending paid ads, do the unit economics

1. Measure from the store: median price, share of items under EUR 5, average order, shipping paid by the customer,
   free-shipping threshold, margin (ask the owner; if unknown, use a range such as 40%, 60%, 75%).
2. Profit per order after payment fees = order value x margin - fees (about 1.5% + EUR 0.25 for EU cards).
3. Cost to win an order = click price / purchase conversion rate. Planning ranges for a small store: clicks EUR 0.40
   to 1.50 (Ireland), conversion 1% to 2.5% for a new store with baskets under EUR 25.
4. If cost to win an order is above profit per order in every realistic cell, **do not advertise yet**. Say so
   plainly, with the table. Benchmarks that count "any conversion" (WordStream's 4% for gifts) are not purchase rates.
5. A small test teaches little: 190 clicks at a true 2% purchase rate can show anything from 1 to 10 orders. If the
   owner insists, cap it (about EUR 100 for 3 weeks), narrow it to a few high-intent phrases, set a stop rule, check
   real volumes in Keyword Planner first (free), and let the owner enter their own card on Google's page.
6. What fits low-value baskets better: face-to-face sales (judge a paid stall by orders needed per day: a EUR 500 a day
   stand at EUR 6 profit per order needs about 80 orders), marketplace listings (Etsy about 14% of a EUR 13 order, only when
   it sells), partners sharing the shop, bigger baskets (bundles), and finding best sellers from people who sell
   (shop staff, marketplace best-seller lists).
7. A printed card or ad should carry a QR code with a tagged URL (`?utm_source=card&utm_medium=qr`) so Analytics can
   count scans. Use vector SVG for print, error correction level Q, quiet zone of 4 modules, at least 20 mm square;
   check it decodes after shrinking.

## 5. Brand and logos

- Use the organisation's own official artwork (a charity's vector logo or the file they send). Do not redraw or
  recolour it. If a logo is white on a brand colour, give it that exact colour behind it. A third party's logo on a
  commercial card (for example a sanctuary's TV logo) needs the owner's confirmation that use is allowed.

## 6. Client safety habits that paid off

- Show a draft and send only after "send"; never repeat or store passwords or card numbers; tell owners never to give
  a stranger (including an ad rep) their social-media password, and to get free-offer terms in writing (length, price
  after, auto-renewal). Prefer partner access over shared logins.
- Keep a changelog, a script index and the working notes in the project folder, because the working folder of an
  assistant session is temporary.
