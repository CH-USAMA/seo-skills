# SEO skills for Claude Code

Skills for auditing and growing websites, built around one idea: **get evidence first, choose priorities second, change things safely third, measure last.**

| Folder | What it is |
|---|---|
| `ghulamali-seo-master/` | A practitioner playbook (strategy layer) distilled from the most-watched 2026 SEO and GEO videos of the YouTube channel @ghulamaliseo: untapped keywords, topical maps, semantic content, local SEO, growing an existing site, getting cited by AI search, new sites and tool sites. His numbers are his claims, and the notes say so. |
| `seo-combined-master/` | A conductor skill: one workflow (preflight, evidence, prioritise, propose, apply safely, measure, keep site notes), a Search Console triage script and field lessons from real client work. |
| `seo-site-audit/` | Google's SEO Starter Guide and Search Essentials turned into an audit-and-fix skill with a site audit script (WordPress, WooCommerce, Shopify, static sites). |
| `beyondseo-plus-overlay/` + `merge-beyondseo.py` | Recipe that merges a **fresh copy of BeyondSEO** with the playbook above into one skill, `beyondseo-plus`. |

BeyondSEO itself is **not** in this repository. It is MIT-licensed work by Muhammad Tahir Ashraf (Beyond Tahir): https://github.com/beyondtahir/beyondseo . The merge script pulls it from its author so you always start from the current release.

## Install the three standalone skills

Claude Code reads user-level skills from `~/.claude/skills`. This works the same in the terminal, the desktop app and the VS Code extension. Start a new conversation afterwards.

```bash
bash install.sh            # macOS, Linux, Git Bash
```
```powershell
powershell -ExecutionPolicy Bypass -File install.ps1
```

Each script copies the three folders into `~/.claude/skills` and moves any older copy to `~/.claude/skills-backups/` first.

## Build the merged skill (BeyondSEO fresh, plus the playbook)

```bash
git clone --depth 1 https://github.com/beyondtahir/beyondseo.git _upstream/beyondseo-$(date +%Y%m%d)
py -3 -I merge-beyondseo.py            # Windows;  python3 -I merge-beyondseo.py elsewhere
```

That writes `beyondseo-plus/` (BeyondSEO unchanged except `SKILL.md`, plus `playbooks/ghulam-ali/`, `playbooks/core/combined-workflow.md`, `references/`, `scripts/sc_triage.py`, `assets/` and a `NOTICE-MERGE.md`). Copy the folder to `~/.claude/skills/beyondseo-plus`, then give it a runtime once with `py -3 scripts/setup.py` inside it, or point it at an existing BeyondSEO environment: `py -3 scripts/run.py --runtime <path to that .venv> doctor`.

The script refuses to run if an anchor in BeyondSEO's `SKILL.md` has moved, so a future upstream change cannot silently break the merge. BeyondSEO's own updater will not update a merged copy (it refuses edited files); re-run the merge on a new clone instead.

## Using it

In Claude Code type `/` and choose a skill, or just say what you want ("audit this site", "look at my Search Console data"). For Search Console data, `seo-combined-master/scripts/sc_triage.py` (also inside the merged skill) sorts a Pages/Queries export into snippet fixes, ranking help, probable zero-click questions and seasonal pages:

```bash
python -I seo-combined-master/scripts/sc_triage.py --pages Pages.csv --queries Queries.csv
```

## Honesty rules the skills follow

- Say what was and was not checked; label partial results as partial.
- No promises of rankings, traffic or AI citations.
- Any change to a live site waits for an approved list, starts with a backup and ends with a check of the live page.
- No shared credentials, no bypassing sign-in or CAPTCHAs.

## Licences and credits

- BeyondSEO: MIT, Muhammad Tahir Ashraf. Not included here; the merged build keeps its licence and notices.
- The playbook is a set of working notes about public videos, not a copy of them; the claims in it belong to the video's author.
- `seo-site-audit` follows Google's public documentation.
- No licence has been chosen yet for the original material in this repository.
