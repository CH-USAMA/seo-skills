#!/usr/bin/env python3
"""Triage a Google Search Console Pages report (and optionally Queries) into actionable buckets.

Inputs (either format, auto-detected):
  * the CSV export: header `Top pages,Clicks,Impressions,CTR,Position` (queries: `Top queries,...`)
  * text copied from the Performance table: one row per line, `<url or query> <clicks> <impressions> <ctr>% <position>`

Usage (run with -I so a stray file in the current folder cannot shadow a module):
  python -I sc_triage.py --pages Pages.csv [--queries Queries.csv] [--min-impr 50] [--host example.com]

The CTR floors are a rough screen, not Google data. Tune them with --floors "3:8,7:2.5,10:1" (position:minimum CTR in percent).
Stdlib only. Prints Markdown.
"""
import argparse
import csv
import io
import re
import sys
from urllib.parse import urlparse

ROW_RE = re.compile(r"^(?P<label>.+?)\s+(?P<clicks>[\d,]+)\s+(?P<impr>[\d,]+)\s+(?P<ctr>[\d.]+)%\s+(?P<pos>[\d.]+)\s*$")
MONTHS = "january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec"
SEASONAL_RE = re.compile(r"(?<![a-z0-9])(20\d\d|%s)(?![a-z])" % MONTHS, re.I)
SKIP_RE = re.compile(r"/(cart|checkout|my-account[^/]*|account|login|wp-login[^/]*|tag|author|feed|wp-json|search)(/|$)|#|\?", re.I)
ANSWER_RE = re.compile(r"\b(when is|when does|when do|when was|what day|what date|which day|which date|what time|date of|date for|how many|who is|who was)\b|\bdate\b", re.I)


def num(s):
    return float(str(s).replace(",", "").replace("%", "").strip() or 0)


def read_rows(path):
    raw = open(path, encoding="utf-8-sig", errors="replace").read()
    rows = []
    first = raw.lstrip().splitlines()[0] if raw.strip() else ""
    if "," in first and re.search(r"clicks", first, re.I) and re.search(r"impressions", first, re.I):
        for r in csv.DictReader(io.StringIO(raw)):
            keys = list(r.keys())
            label = r[keys[0]]
            def pick(name):
                for k in keys:
                    if k.strip().lower() == name:
                        return r[k]
                return "0"
            rows.append(dict(label=label.strip(), clicks=num(pick("clicks")), impr=num(pick("impressions")),
                             ctr=num(pick("ctr")), pos=num(pick("position"))))
    else:
        for line in raw.splitlines():
            m = ROW_RE.match(line.strip())
            if m:
                rows.append(dict(label=m["label"].strip(), clicks=num(m["clicks"]), impr=num(m["impr"]),
                                 ctr=num(m["ctr"]), pos=num(m["pos"])))
    return rows


def short(url, host):
    if not url.startswith("http"):
        return url
    p = urlparse(url)
    path = p.path or "/"
    return path if (not host or host in p.netloc) else url


def floor_for(pos, floors):
    for p, f in floors:
        if pos <= p:
            return f
    return None


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pages", required=True)
    ap.add_argument("--queries")
    ap.add_argument("--min-impr", type=float, default=50, help="ignore rows below this many impressions in the action lists (default 50)")
    ap.add_argument("--host", default="", help="host name to strip from URLs in the output")
    ap.add_argument("--floors", default="3:8,7:2.5,10:1", help="position:min CTR percent pairs, ascending")
    ap.add_argument("--top", type=int, default=15, help="max rows per list")
    a = ap.parse_args()

    floors = sorted((float(x.split(":")[0]), float(x.split(":")[1])) for x in a.floors.split(","))
    pages = read_rows(a.pages)
    if not pages:
        sys.exit("no rows read from --pages (expected the CSV export or text copied from the table)")
    queries = read_rows(a.queries) if a.queries else []

    tot_clicks = sum(p["clicks"] for p in pages)
    tot_impr = sum(p["impr"] for p in pages)
    pages.sort(key=lambda p: -p["impr"])
    print("# Search Console triage\n")
    print("Rough screen, not a verdict. CTR floors (position <= p needs about this CTR): "
          + ", ".join("%g -> %g%%" % (p, f) for p, f in floors) + ". Minimum impressions in action lists: %g.\n" % a.min_impr)
    print("**Pages:** %d rows, %d clicks, %d impressions, overall CTR %.2f%%." % (
        len(pages), tot_clicks, tot_impr, 100.0 * tot_clicks / tot_impr if tot_impr else 0))
    top = pages[0]
    print("**Concentration:** the top page (`%s`) holds %.0f%% of all impressions; the top 3 hold %.0f%%.\n" % (
        short(top["label"], a.host), 100.0 * top["impr"] / tot_impr if tot_impr else 0,
        100.0 * sum(p["impr"] for p in pages[:3]) / tot_impr if tot_impr else 0))

    content = [p for p in pages if not SKIP_RE.search(p["label"]) and p["impr"] >= a.min_impr]

    # 1. Fix the snippet
    snip = []
    for p in content:
        f = floor_for(p["pos"], floors)
        if f is not None and p["ctr"] < f:
            snip.append((p, f))
    print("## 1. Fix the snippet? (position within the floors, CTR under the floor)\n")
    print("Check the title and description against the real queries first. Seasonal or date-question pages: see lists 3 and 4 before rewriting anything.\n")
    if snip:
        print(table(["Page", "Impr", "Clicks", "CTR %", "Pos", "Floor %", "Note"],
                    [(short(p["label"], a.host), int(p["impr"]), int(p["clicks"]), "%.1f" % p["ctr"], "%.1f" % p["pos"], "%g" % f,
                      "seasonal URL, see list 3" if SEASONAL_RE.search(urlparse(p["label"]).path) else "")
                     for p, f in snip[:a.top]]))
    else:
        print("None.")
    print()

    # 2. Strike zone
    strike = [p for p in content if 8 <= p["pos"] <= 20]
    strike.sort(key=lambda p: -p["impr"])
    print("## 2. Needs ranking help, not a new title (position 8 to 20)\n")
    print("Cover the query wording in the text, answer first, add internal links from stronger pages, consider visible Q&A with FAQ schema.\n")
    if strike:
        print(table(["Page", "Impr", "Clicks", "Pos"],
                    [(short(p["label"], a.host), int(p["impr"]), int(p["clicks"]), "%.1f" % p["pos"]) for p in strike[:a.top]]))
    else:
        print("None.")
    print()

    # 3. Seasonal
    seas = [p for p in pages if SEASONAL_RE.search(urlparse(p["label"]).path) and not SKIP_RE.search(p["label"]) and p["impr"] >= a.min_impr]
    print("## 3. Seasonal or dated URLs\n")
    print("Traffic ends with the event. Plan the refresh or a redirect for after the date, and link to the next season's page.\n")
    if seas:
        print(table(["Page", "Impr", "Clicks", "Pos"],
                    [(short(p["label"], a.host), int(p["impr"]), int(p["clicks"]), "%.1f" % p["pos"]) for p in seas[:a.top]]))
    else:
        print("None.")
    print()

    # 4. Queries
    if queries:
        queries.sort(key=lambda q: -q["impr"])
        ans = [q for q in queries if ANSWER_RE.search(q["label"]) and q["clicks"] == 0 and q["impr"] >= max(10, a.min_impr / 5)]
        ans_impr = sum(q["impr"] for q in ans)
        q_impr = sum(q["impr"] for q in queries)
        print("## 4. Probably zero-click (date or one-fact questions with no clicks)\n")
        print("Google often answers these on the results page. Leave the title alone and do not read the low CTR as a failure. "
              "These %d queries hold %.0f%% of query impressions.\n" % (len(ans), 100.0 * ans_impr / q_impr if q_impr else 0))
        if ans:
            print(table(["Query", "Impr", "Pos"], [(q["label"], int(q["impr"]), "%.1f" % q["pos"]) for q in ans[:a.top]]))
        else:
            print("None.")
        print()
        ans_set = {q["label"] for q in ans}
        near = [q for q in queries if q["label"] not in ans_set and q["clicks"] == 0 and q["impr"] >= max(10, a.min_impr / 5) and q["pos"] <= 20]
        print("## 5. Queries with impressions, no clicks, position 20 or better (not answer-box suspects)\n")
        print("The wording to cover on the matching pages. Match query to page by topic and say so; the reports do not pair them.\n")
        if near:
            print(table(["Query", "Impr", "Pos"], [(q["label"], int(q["impr"]), "%.1f" % q["pos"]) for q in near[:a.top * 2]]))
        else:
            print("None.")
        print()

    skipped = [p for p in pages if SKIP_RE.search(p["label"]) and p["impr"] > 0]
    print("## 6. Skip (not content): %d rows" % len(skipped))
    print("Check these are noindexed or redirected instead of optimising them: "
          + (", ".join(short(p["label"], a.host) for p in skipped[:8]) or "none") + ("..." if len(skipped) > 8 else "") + "\n")


if __name__ == "__main__":
    main()
