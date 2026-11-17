# Search Console: getting the data and reading it

## Three ways to get the Pages and Queries reports

1. **Claude in Chrome** (the user's own signed-in Chrome). Works when Chrome is in front and not minimised; a hidden window freezes the tab and screenshots time out. Open a **new tab** and go to:
   `https://search.google.com/search-console/performance/search-analytics?resource_id=<url-encoded property>&num_of_days=90&breakdown=page&metrics=CLICKS%2CIMPRESSIONS%2CCTR%2CPOSITION`
   (use `breakdown=query` for queries; a domain property uses `sc-domain%3Aexample.com`). Wait a few seconds, scroll to the table, open "Rows per page", choose 500, then read the page text. Each row reads `url clicks impressions ctr% position`. Close the tab when done.
2. **The user exports it.** Performance, Export, Download CSV gives `Pages.csv` and `Queries.csv` with the headers `Top pages,Clicks,Impressions,CTR,Position`. Downloading is the user's action; ask them to drop the files in the project folder.
3. **The built-in browser pane** only works if the user has signed in to Google there themselves. Never type their password.

BeyondSEO also imports a Search Console CSV privately (`beyondseo/docs/operations.md`, "review Search Console exports"). Use it when the user supplies a CSV and wants the saved-page matching it provides.

Save what you pulled (date range, totals, the rows you used) in the site's project folder so the next pull can be compared like for like.

## Reading it

Run `python -I scripts/sc_triage.py --pages Pages.csv --queries Queries.csv` (or give it the copied text). Then read the real pages before deciding anything. The buckets:

| Bucket | Meaning | What to do |
|---|---|---|
| Fix the snippet | Position 10 or better, impressions high enough, CTR under a rough floor | Check the title and description against the exact queries; rewrite only if the keyword or the benefit is missing |
| Needs ranking help | Position 8 to 20 | A title will not fix this. Cover the query wording in the text, answer first, add internal links, consider Q&A with FAQ schema |
| Probably zero-click | Queries asking for a date, time or one fact | Google answers on the results page. Leave the title alone, do not read low CTR as a failure |
| Seasonal | Year, month or feast in the URL | Plan the update or redirect for after the date; the traffic ends with the event |
| Skip | cart, account, checkout, tag, author, feed, fragments | Not content; check they are noindexed or redirected instead |

The CTR floors are a **rough screen**, not Google data: about 8% at positions 1 to 3, 2.5% at 4 to 7, 1% at 8 to 10. Tune them with the site's own homepage and brand pages, which show what a "normal" CTR looks like there.

## Caveats that change the conclusion

- **Averages hide the shape.** One page or one season can hold most of the impressions (on one shop, 85% came from a single seasonal page). Look at the share before celebrating or panicking.
- **Position is an average** across queries and days. A page at 11.3 may sit at 7 for one phrase and 40 for another. Check the query list.
- **Low volume is noise.** Under about 50 impressions, one click moves CTR by 2 points. Use a minimum (the script has `--min-impr`).
- **Dates.** A chart flat for weeks and then rising means new pages are still being discovered; compare equal periods only.
- **Query to page pairs** are not in these two reports. Do not invent which page a query belongs to; open the page's own query view in Search Console, or match by obvious topic and say it is a match by topic.
- **The playbook's "high impressions, low CTR" test is a starting point.** On a young or small site it often returns false alarms (zero-click questions, positions where low CTR is normal). Confirm with the checks above before spending the client's money or trust.
