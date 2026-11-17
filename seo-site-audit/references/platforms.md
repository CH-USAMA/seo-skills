# Platform notes for SEO fixes

Contents: WordPress core and tooling / SEO plugins (Rank Math, Yoast) / Elementor / WooCommerce / caching / Shopify / Next.js and static sites / JavaScript-rendered sites.

Principle: change the smallest thing that fixes the problem, on the layer that owns it (setting before plugin before theme code), keep a backup of what you overwrite, and verify on the live HTML.

## WordPress: working method
- **Run PHP through WP-CLI files, not one-liners.** Over SSH, nested quotes in `wp eval '...'` break in confusing ways. Write a `.php` file, upload it (scp, pscp), run `wp eval-file /tmp/file.php`, then delete it. Lint it first (`php -l`).
- **Line endings.** Files written on Windows have CRLF; normalise on the server (`sed -i 's/\r$//' file.php`) before copying into `mu-plugins`.
- **mu-plugins** (`wp-content/mu-plugins/*.php`) load automatically, survive theme and plugin updates, and are easy to delete to undo a change. Put each fix in its own small, documented file (header comment saying what and why).
- **Make scripts idempotent** (safe to run twice): look up by slug or meta before inserting; store the original in a `_backup_...` postmeta only if it does not exist yet.
- **URLs built in CLI context are `http://`** (the request is not SSL). Wrap with `set_url_scheme( $url, 'https' )` or build from `home_url()` of a secure option, and re-check the live HTML.
- **Editing the theme is a last resort** (updates overwrite it). To change theme markup you cannot filter, use an output buffer in a mu-plugin: `add_action( 'template_redirect', function () { ob_start( function ( $html ) { /* regex or DOM edits */ return $html; } ); }, 0 );` Skip admin, AJAX, REST, feeds and page-builder preview requests, and return the buffer unchanged if `</body>` is absent.
- **Redirects.** For a handful, a `template_redirect` map with `wp_safe_redirect( $target, 301 ); exit;` in a mu-plugin is enough. For many, use the SEO plugin's redirect module or the Redirection plugin. Always 301, avoid chains.
- **Comments and pings.** Options: `default_comment_status`, `default_ping_status`, `default_pingback_flag`; close existing with `UPDATE wp_posts SET comment_status='closed', ping_status='closed' WHERE post_type IN ('post','page')`. Self-pingbacks (a comment created for every internal link) are stopped with `add_action( 'pre_ping', function ( &$links ) { foreach ( $links as $i => $l ) { if ( 0 === strpos( $l, home_url() ) ) { unset( $links[ $i ] ); } } } );`. Use `wp_spam_comment` and `wp_trash_comment` (reversible), not hard deletes. WooCommerce order notes are stored as comments; leave them.
- **Language tags.** `add_filter( 'language_attributes', fn( $o ) => str_replace( 'en-US', 'en-IE', $o ), 20 );` and the SEO plugin's og:locale filter. WordPress has no `en_IE` locale pack, so filter the output.
- **Menus.** `wp_update_nav_menu_item( $menu_id, 0, [ 'menu-item-title' => ..., 'menu-item-object' => 'page', 'menu-item-object-id' => $page_id, 'menu-item-type' => 'post_type', 'menu-item-status' => 'publish', 'menu-item-position' => n ] )`. A custom link's URL lives in postmeta `_menu_item_url`.
- **Demo content.** Themes ship demo pages (FAQ, About, Contact, Sample Page, Home 2, Home 3, Wishlist, Categories). Find them with `wp post list --post_type=page --fields=ID,post_name,post_modified` (old modified dates), then rebuild, redirect or noindex. Also check the demo menus and footers for links to the theme vendor's site.

## SEO plugins
**Rank Math** (option names use hyphens: `rank-math-options-titles`, `rank-math-options-sitemap`, `rank-math-options-general`)
- Per post, page or product (postmeta): `rank_math_title`, `rank_math_description`, `rank_math_focus_keyword`, `rank_math_robots` (an array such as `['noindex']`), `rank_math_facebook_image`, `rank_math_facebook_image_id`.
- Per term (term meta, same keys): category and product category descriptions and robots.
- Sitemap options (`rank-math-options-sitemap`): `pt_<type>_sitemap`, `tax_<taxonomy>_sitemap` (`'on'` or `'off'`), `exclude_posts` (comma-separated IDs), `exclude_terms`. After changing, clear the cache: `RankMath\Sitemap\Cache::invalidate_storage();`. Noindex posts drop out of the sitemap automatically. Product categories (`tax_product_cat_sitemap`) are often **off by default**: switch on if the categories are indexable and have products.
- Sitemap index: `/sitemap_index.xml`. The WP core sitemap at `/wp-sitemap.xml` is replaced when the plugin's sitemap is on.
- Custom titles set here override the title template site-wide; always verify the rendered `<title>`.

**Yoast SEO**: `_yoast_wpseo_title`, `_yoast_wpseo_metadesc`, `_yoast_wpseo_focuskw`, `_yoast_wpseo_meta-robots-noindex` (`1` for noindex), `_yoast_wpseo_canonical`. Sitemap `/sitemap_index.xml`. Confirm key names against the installed version before bulk-writing.

## Elementor
- Page content is JSON in postmeta `_elementor_data` (and often mirrored in `post_content`). To edit safely: back up the meta, `json_decode( $raw, true )`, walk the tree recursively and change string values, then `update_post_meta( $id, '_elementor_data', wp_slash( wp_json_encode( $data ) ) )`. Then `delete_post_meta( $id, '_elementor_element_cache' )`, `delete_post_meta( $id, '_elementor_css' )`, `wp elementor flush_css`, and purge page caches.
- A clean content page: set `_wp_page_template` to `elementor_header_footer`, `_elementor_edit_mode` to `builder`, `_elementor_template_type` to `wp-page`, and make `_elementor_data` one container holding one `text-editor` widget (`settings.editor` = your HTML). Minify the HTML (no newlines between tags) so `wpautop` does not insert stray `<p>` and `<br>`.
- A dynamic section (for example latest posts) is a `shortcode` widget (`settings.shortcode` = `[your_shortcode]`) backed by a mu-plugin that returns the HTML.
- Theme colours often override paragraph colour; give your own CSS `!important` on text colour when it renders paler than intended.

## WooCommerce
- Cart, checkout and account pages are noindex by default; keep them out of sitemaps. Product schema (price, availability, shipping, returns) is generated automatically; check it is valid and matches the visible price.
- Product tag and attribute archives are usually thin: noindex. Product category pages deserve titles, descriptions and indexing.
- Shop owners need real **Delivery, Returns, FAQ and Contact** pages that state their actual policies. Build FAQs only from policy text already published on the site.
- "Quick view", "wishlist" and "compare" buttons often print the product ID as `href` (`<a href="1058">`); see the pitfall in SKILL.md.
- Store address (WooCommerce, General) should match the address on the site.

## Caching
Purge after every change before you verify: LiteSpeed `wp litespeed-purge all`; WP Rocket `wp rocket clean --confirm`; WP object cache `wp cache flush`; stale transients `wp transient delete --all`; Cloudflare "Purge everything" in its dashboard. Verify with a cache-busting query string (`?cb=123`), which most page caches treat as a separate URL.

## Shopify
- Titles and descriptions: each product, collection, page and blog post has a "Search engine listing" block; the homepage's is under Online Store, Preferences.
- Products appear at `/products/handle` and `/collections/x/products/handle`; Shopify canonicals the second to the first (leave as is). `/sitemap.xml` is generated and cannot be edited; hide a page by theme conditional noindex or by hiding the product from the Online Store channel.
- Redirects: Online Store, Navigation, View URL redirects (these are 301s). Changing a handle offers to create one; accept.
- Alt text: edit on the product media. Structured data comes from the theme (check `Product` JSON-LD validity; apps often add a duplicate).
- `robots.txt.liquid` can adjust robots rules (rarely needed).

## Next.js, Astro and other frameworks, and static HTML
- Next.js (App Router): per-route `metadata` or `generateMetadata` for `title`, `description`, `alternates.canonical`, `openGraph`; `app/sitemap.ts` and `app/robots.ts`; `next/image` with `alt`, width and height (priority only for the hero); `<html lang>` in the root layout; `redirects()` in `next.config.js` with `permanent: true` (308 is treated as permanent); call `notFound()` for missing data so the status is a real 404, not a 200 "not found" page; keep `trailingSlash` consistent.
- Static HTML: write `<title>`, `<meta name="description">`, `<link rel="canonical">`, `<html lang>`, viewport and Open Graph tags by hand; generate `sitemap.xml`; add redirects in the host's file (`_redirects`, `vercel.json` with `permanent: true`, `.htaccess`).
- Vercel, Netlify and similar: remember `www` to apex redirects and HTTPS are host settings.

## JavaScript-rendered sites
If the content is not in the initial HTML, Google must render it. Confirm what Google sees with URL Inspection, "View crawled page" and the rendered HTML. Prefer server-side or static rendering for pages you want indexed, give every view a real URL and link (`<a href>`, not click handlers), and return real status codes.
