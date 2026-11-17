# About this merged edition

**BeyondSEO Plus** is BeyondSEO with an extra strategy layer. It is a modified copy, not the original, and it is not made, reviewed or endorsed by the BeyondSEO author.

- **Base:** BeyondSEO {UPSTREAM_VERSION} by Muhammad Tahir Ashraf (Beyond Tahir), MIT licence, https://github.com/beyondtahir/beyondseo, commit {UPSTREAM_COMMIT}. The engine (`src/`, `scripts/` apart from the added file below), `docs/`, `playbooks/` (apart from the added folders) and the licence files are unchanged. The licence and third-party notices are kept as released.
- **Added:** `playbooks/ghulam-ali/` (a playbook distilled from Ghulam Ali's most-watched 2026 YouTube videos; his numbers are his claims), `playbooks/core/combined-workflow.md`, `references/search-console-triage.md`, `references/field-lessons.md`, `scripts/sc_triage.py`, `assets/site-notes-template.md`.
- **Changed:** `SKILL.md` (name, description, version, and one added section "Strategy layer"). `beyondseo-install.json`, the repo-only folders (`.github`, `tests`, `media`) and `.git` are left out.
- **Updating:** BeyondSEO's own updater refuses to update a copy whose tracked files were edited, so this edition is not updated that way. Pull a fresh BeyondSEO and run the merge script again (`merge-beyondseo.py`); it applies the same additions and stops with a clear message if an upstream anchor has moved.
- **Runtime:** this folder does not carry a Python environment. Run `py -3 scripts/setup.py` here once, or point at an existing BeyondSEO environment with `py -3 scripts/run.py --runtime <path to that .venv> <command>`.
