#!/usr/bin/env python3
"""Merge a fresh BeyondSEO checkout with the Ghulam Ali strategy layer into one skill folder.

  py -3 -I merge-beyondseo.py [--upstream DIR] [--out DIR]

* --upstream  a fresh clone of https://github.com/beyondtahir/beyondseo (default: newest folder under _upstream/)
* --out       where to build the merged skill (default: beyondseo-plus next to this script). Only a folder this script built
              (it contains NOTICE-MERGE.md) or a missing folder is replaced.

What it does: copies the upstream skill without repo-only folders (.git, .github, tests, media) and without its install receipt,
adds the playbook, workflow, triage script and notes template from the source folders next to this script, generalises client names,
patches SKILL.md (name, description, version, one added section) and checks every added relative link. It stops with a clear message
if an anchor in upstream SKILL.md has moved. Stdlib only. Never run code from the upstream folder.
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOP_EXCLUDE = {".github", "tests", "media"}
ANY_EXCLUDE = {".git", ".venv", "__pycache__", "beyondseo.egg-info"}
FILE_EXCLUDE = {".gitattributes", "beyondseo-install.json"}
NEW_PATHS = [
    "playbooks/ghulam-ali", "playbooks/core/combined-workflow.md", "references/search-console-triage.md",
    "references/field-lessons.md", "scripts/sc_triage.py", "assets/site-notes-template.md", "examples/sc-triage", "NOTICE-MERGE.md",
]


def die(msg):
    sys.exit("merge stopped: " + msg)


def read(p):
    return Path(p).read_text(encoding="utf-8")


def write(p, text):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")


def newest_upstream():
    cands = sorted((HERE / "_upstream").glob("beyondseo-*"))
    if not cands:
        die("no folder under _upstream/ (git clone --depth 1 https://github.com/beyondtahir/beyondseo.git _upstream/beyondseo-<date>)")
    return cands[-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--upstream")
    ap.add_argument("--out", default=str(HERE / "beyondseo-plus"))
    a = ap.parse_args()
    up = Path(a.upstream).resolve() if a.upstream else newest_upstream()
    out = Path(a.out).resolve()
    gh, cm, ov = HERE / "ghulamali-seo-master", HERE / "seo-combined-master", HERE / "beyondseo-plus-overlay"
    for need in (up / "SKILL.md", up / "pyproject.toml", gh / "SKILL.md", cm / "scripts" / "sc_triage.py", ov / "strategy-section.md"):
        if not need.exists():
            die("missing " + str(need))
    if out.exists():
        if not (out / "NOTICE-MERGE.md").exists():
            die("%s exists and was not built by this script; choose another --out" % out)
        shutil.rmtree(out)

    version = re.search(r'^version\s*=\s*"([^"]+)"', read(up / "pyproject.toml"), re.M).group(1)
    try:
        commit = subprocess.run(["git", "-C", str(up), "rev-parse", "--short", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        commit = "unknown"

    # 1. upstream copy
    def ignore(d, names):
        skip = []
        for n in names:
            if n in ANY_EXCLUDE or n in FILE_EXCLUDE or n.endswith(".pyc"):
                skip.append(n)
            elif Path(d) == up and n in TOP_EXCLUDE:
                skip.append(n)
        return skip
    shutil.copytree(up, out, ignore=ignore)

    for rel in NEW_PATHS:
        if (out / rel).exists():
            die("upstream already has %s; rename our addition before merging" % rel)

    # 2. Ghulam Ali playbook
    pb = out / "playbooks" / "ghulam-ali"
    pb.mkdir(parents=True)
    for f in sorted((gh / "references").glob("*.md")):
        shutil.copy2(f, pb / f.name)
    st = read(gh / "STATUS.md").replace("](references/", "](").replace("[references/", "[")
    st_lines = st.split("\n")
    st_note = ("\n> Maintainer notes. Folder paths and the `sources/` files named below belong to the original working folder and are not part of this skill; "
               "the video table and the notes on what each video added are the useful part.\n")
    write(pb / "STATUS.md", st_lines[0] + "\n" + st_note + "\n".join(st_lines[1:]))

    g = pb / "grow-existing-site-without-new-content.md"
    t = read(g)
    t, n1 = re.subn(r"such as marianholyart\.com:", "such as a WooCommerce or WordPress shop:", t)
    t, n2 = re.subn(r"This is what the 17 Nov 2026 pass on marianholyart\.com.*?changelog\.",
                    "A first pass on one client shop used exactly this order: paged archive titles, visible Quick answers blocks, and a descriptive title on a page whose query had impressions but almost no clicks.", t, flags=re.S)
    if n1 != 1 or n2 != 1:
        die("grow-existing-site-without-new-content.md changed shape (client-name replacements: %d, %d)" % (n1, n2))
    write(g, t)

    c = pb / "combining-with-beyondseo.md"
    t = read(c)
    lines = t.split("\n")
    note = ("\n> In this merged edition BeyondSEO and the playbook live in one skill folder. The commands named below are the ones in "
            "[SKILL.md](../../SKILL.md); the combined order of work is in [combined-workflow.md](../core/combined-workflow.md). "
            "The text below was written when they were two separate skills, so read paths such as `~/.claude/skills/beyondseo` as this folder.\n")
    write(c, lines[0] + "\n" + note + "\n".join(lines[1:]))

    body = read(gh / "SKILL.md")
    m = re.search(r"^## How to read this playbook honestly.*", body, re.M | re.S)
    if not m:
        die("ghulamali-seo-master/SKILL.md lost its 'How to read this playbook honestly' section")
    idx = m.group(0)
    idx = idx.replace("](references/", "](").replace("[references/", "[")
    idx, n3 = re.subn(r"\(for example marianholyart\.com, a WooCommerce store\)", "(for example a WooCommerce store)", idx)
    if n3 != 1:
        die("playbook index: client-name replacement did not match once")
    readme = ("# Ghulam Ali strategy playbook (index)\n\n"
              "Distilled from the most-watched 2026 videos of the YouTube channel @ghulamaliseo (GMS Digitals), read from the channel's own transcripts and "
              "rewritten as working notes. The video list and how each was read is in [STATUS.md](STATUS.md). This is the layer that decides what to do and in "
              "which order; BeyondSEO's crawl, audit and reports supply the evidence. The order of work is in [combined-workflow.md](../core/combined-workflow.md).\n\n"
              + idx)
    write(pb / "README.md", readme)

    # 3. workflow, triage script, notes
    shutil.copy2(ov / "combined-workflow.md", out / "playbooks" / "core" / "combined-workflow.md")
    for name in ("search-console-triage.md", "field-lessons.md"):
        t = read(cm / "references" / name).replace("`beyondseo/docs/operations.md`", "`docs/operations.md`")
        write(out / "references" / name, t)
    shutil.copy2(cm / "scripts" / "sc_triage.py", out / "scripts" / "sc_triage.py")
    shutil.copy2(cm / "assets" / "site-notes-template.md", out / "assets" / "site-notes-template.md")
    (out / "examples" / "sc-triage").mkdir(parents=True)
    for f in (cm / "examples").glob("*.txt"):
        shutil.copy2(f, out / "examples" / "sc-triage" / f.name)

    # 4. SKILL.md
    s = read(out / "SKILL.md")
    fm = re.match(r"---\n(.*?)\n---\n", s, re.S)
    if not fm:
        die("upstream SKILL.md has no front matter")
    head = fm.group(1)
    h2, n = re.subn(r"^name: beyondseo$", "name: beyondseo-plus", head, flags=re.M)
    if n != 1:
        die("front matter 'name: beyondseo' not found")
    extra = (" This merged edition adds a practitioner strategy layer from Ghulam Ali's most-watched 2026 SEO and GEO videos, covering untapped keywords, topical maps, "
             "semantic content, local SEO, growing an existing site, and getting cited by AI search, plus a combined workflow and a Search Console triage script. "
             "Use it for any website audit, SEO plan, Search Console review, title and content improvement or AI search visibility work, even if no skill is named.")
    h2, n = re.subn(r"^(description: .*)$", lambda mm: mm.group(1).rstrip() + extra, h2, count=1, flags=re.M)
    if n != 1:
        die("front matter description not found")
    h2, n = re.subn(r"^(\s+)version: " + re.escape(version) + r"$",
                    lambda mm: "%sversion: %s+plus.1\n%sbased-on: BeyondSEO %s commit %s by Muhammad Tahir Ashraf under MIT, with an added strategy layer" % (mm.group(1), version, mm.group(1), version, commit),
                    h2, count=1, flags=re.M)
    if n != 1:
        die("front matter version %s not found" % version)
    rest = s[fm.end():]
    anchor = "## Run in the available host"
    if rest.count(anchor) != 1:
        die("SKILL.md anchor '%s' not found exactly once" % anchor)
    rest = rest.replace(anchor, read(ov / "strategy-section.md").rstrip("\n") + "\n\n" + anchor)
    write(out / "SKILL.md", "---\n" + h2 + "\n---\n" + rest)
    try:
        import yaml
        d = yaml.safe_load(h2)
        assert d["name"] == "beyondseo-plus" and d["metadata"]["version"].endswith("+plus.1")
    except ImportError:
        pass

    write(out / "NOTICE-MERGE.md", read(ov / "NOTICE-MERGE.md").replace("{UPSTREAM_VERSION}", version).replace("{UPSTREAM_COMMIT}", commit))

    # 5. check relative links in everything we added or edited
    added = [out / "SKILL.md", out / "NOTICE-MERGE.md", out / "playbooks" / "core" / "combined-workflow.md",
             out / "references" / "search-console-triage.md", out / "references" / "field-lessons.md"] + sorted(pb.glob("*.md"))
    broken = []
    for f in added:
        for mm in re.finditer(r"\]\(([^)\s]+)\)", read(f)):
            target = mm.group(1)
            if re.match(r"(https?:|mailto:|#)", target):
                continue
            path = target.split("#")[0]
            if path and not (f.parent / path).resolve().exists():
                broken.append("%s -> %s" % (f.relative_to(out), target))
    n_files = sum(1 for p in out.rglob("*") if p.is_file())
    print("built %s from BeyondSEO %s (%s): %d files, %d ghulam-ali pages, %d broken links" % (out, version, commit, n_files, len(list(pb.glob('*.md'))), len(broken)))
    for b in broken:
        print("  BROKEN", b)
    if broken:
        sys.exit(1)


if __name__ == "__main__":
    main()
