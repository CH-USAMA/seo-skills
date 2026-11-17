# Status

Last updated: 17 Nov 2026 (all 22 selected videos read)

Selection: the 22 most-watched 2026 videos on youtube.com/@ghulamaliseo (de-duplicated by topic), chosen in the earlier claude.ai chat "Youtube channel skills". The channel list (260 videos) is in `sources/channel_list_260_videos.txt`.

## Done: all 22 transcripts read and distilled into the references

| Video | Views | URL |
|---|---|---|
| How to start SEO+GEO from ZERO in 2026 | 14,000 | https://www.youtube.com/watch?v=Xf6zQcpmMQs |
| The Only Video You Need to Watch | 13,000 | https://www.youtube.com/watch?v=dSk6qvL05xQ |
| Stop Chasing Backlinks — This Google Traffic Method Works Faster | 13,000 | https://www.youtube.com/watch?v=EkrIz8exbzo |
| This Boring Website Makes $36K/Month | 12,000 | https://www.youtube.com/watch?v=AcMorluygXk |
| Give me 9min, and I'll improve your SEO skills by 176% | 12,000 | https://www.youtube.com/watch?v=Q0GgrWDzQOA |
| I Spent 2,000 Hours Learning GEO/AEO For This | 12,000 | https://www.youtube.com/watch?v=t_Y5kznd2rk |
| How I Built an Online Business - After Testing 6 Skills | 11,000 | https://www.youtube.com/watch?v=s8wYlYakCQg |
| How to Never Fail in SEO | 11,000 | https://www.youtube.com/watch?v=kKPez3ASelk |
| I'm in Love With This Instant Google Ranking Process | 10,000 | https://www.youtube.com/watch?v=AKGWhzYtSng |
| The 30-Day SEO+GEO Roadmap For New Websites | 8,900 | https://www.youtube.com/watch?v=6iux_lS8_PA |
| How to Do SEO For a New Website ( Step by Step ) | 28,000 | https://www.youtube.com/watch?v=bOsfkTAe_Hc |
| Auditing 500 Websites Taught Me These Technical SEO Secrets | 8,200 | https://www.youtube.com/watch?v=DK1XqGanZl4 |
| If I Started SEO in 2026, I'd Do This (same recording as the new-website video above) | 63,000 | https://www.youtube.com/watch?v=n78mdPdjKRA |
| How to Make Tools Website ( Live Process ) | 40,000 | https://www.youtube.com/watch?v=9EIM33S5BgM |
| How to Make a Tools Website For Adsense (same script as the one above) | 33,000 | https://www.youtube.com/watch?v=-OzCNzHGFE8 |
| How to Rank Tool Site ( Complete Process ) | 19,000 | https://www.youtube.com/watch?v=k8JLlo6KM3Y |
| 5 Easiest Ways to Increase Organic Traffic to Website | 19,000 | https://www.youtube.com/watch?v=pPNtnso2K9I |
| Why Your Website isn't Ranking in Google ( & How to Rank it ) | 18,000 | https://www.youtube.com/watch?v=sOYZPXq8dbI |
| My SEO Strategy to Rank a website Fast ( SAAS, eCommerce, Business ) | 7,300 | https://www.youtube.com/watch?v=ekTY9D2BT1o |
| Master SEO in 2026: Google + AI Search | 6,900 | https://www.youtube.com/watch?v=4vxmyDBAPzM |
| I've never shared before these Local SEO Keyword Research Methods | 6,900 | https://www.youtube.com/watch?v=JDTX33m8lgw |
| How to Rank on Google Without Backlinks? | 6,600 | https://www.youtube.com/watch?v=bBxHKLSQuug |

## How the last ten were obtained

`yt-dlp` caption downloads stayed blocked by YouTube (HTTP 429) on this laptop. On 17 Nov 2026 the same transcripts were read from the **transcript panel on the YouTube watch page** in the built-in browser instead: open the video, scroll down a little so the page finishes loading, click "Show transcript", then read the segments. The panel only offers the **original Urdu/Hindi** (Devanagari script, with many English words), so those ten were translated by hand while distilling. Their raw text is not stored in `sources/transcripts/`; the references carry the distilled content.

Two of the 22 turned out to be duplicates of other videos (see the notes in the table). Three tool-site videos share one script, so they are covered by one reference file.

## What each of the ten added

- tool sites and AdSense: [references/tool-sites-and-adsense.md](references/tool-sites-and-adsense.md)
- why a site is not ranking: [references/why-your-site-isnt-ranking.md](references/why-your-site-isnt-ranking.md)
- five ways to grow traffic without new content, thin content: [references/grow-existing-site-without-new-content.md](references/grow-existing-site-without-new-content.md)
- local SEO keyword methods: [references/local-seo-keywords.md](references/local-seo-keywords.md)
- beginner blueprint, intent, sweet spot, 30-day plan: [references/beginner-blueprint-2026.md](references/beginner-blueprint-2026.md)
- rank without backlinks: [references/rank-without-backlinks.md](references/rank-without-backlinks.md)

## If more videos are wanted later

`sources/channel_list_260_videos.txt` and `sources/ranked_2026_views_and_dates.tsv` hold the channel list with views and upload dates. Pick the next most-watched 2026 titles, read them with the transcript-panel method above, add or extend a reference file, update the routing table in `SKILL.md`, and re-run `D:\SEO Skills\install-ghulamali-skill.sh`.

Tooling: yt-dlp lives in `D:\SEO Skills\_tools\venv`. `_tools` and `_work` can be deleted when disk space matters.
