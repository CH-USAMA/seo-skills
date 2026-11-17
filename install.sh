#!/bin/bash
# Installs the three standalone skills into ~/.claude/skills (or the folder given as the first argument).
# Existing copies are moved to <dest>/../skills-backups/ first. BeyondSEO is not installed by this script (see README).
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
DEST="${1:-$HOME/.claude/skills}"
BK_ROOT="$(dirname "$DEST")/skills-backups"
mkdir -p "$DEST"
for s in ghulamali-seo-master seo-combined-master seo-site-audit; do
  [ -f "$HERE/$s/SKILL.md" ] || { echo "missing $HERE/$s/SKILL.md" >&2; exit 1; }
  if [ -d "$DEST/$s" ]; then
    mkdir -p "$BK_ROOT"
    mv "$DEST/$s" "$BK_ROOT/$s-$(date +%Y%m%d-%H%M%S)"
    echo "previous $s saved to $BK_ROOT"
  fi
  mkdir -p "$DEST/$s"
  cp -r "$HERE/$s/." "$DEST/$s/"
  find "$DEST/$s" -name "__pycache__" -type d -prune -exec rm -rf {} + 2>/dev/null || true
  echo "installed $s -> $DEST/$s"
done
echo "Done. Start a new Claude Code conversation to load them."
