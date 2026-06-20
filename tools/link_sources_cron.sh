#!/bin/bash
# Librarian Linking Mode — weekly backfill sweep (see LIBRARIAN.md § Linking Mode).
# Links any currently-unlinked sources (papers + book chapters) to the concepts they
# support, then refreshes the server — but ONLY if it actually added links, so weeks
# with no new ingests don't needlessly drop the claude.ai connector.
set -uo pipefail
REPO=/home/pkis/pkis-wiki
PY=/home/pkis/venv/bin/python
cd "$REPO" || exit 1

echo "=== $(date '+%F %T') link-sources sweep start ==="
git pull origin main >/dev/null 2>&1 || true

# Clear resume-state so the sweep re-evaluates ALL currently-unlinked sources
# (already-linked ones are excluded by the driver; this lets newly-created concepts
# pick up sources that previously matched nothing). Cheap — Haiku, only the residue.
rm -f "$REPO/tools/.link_sources_state.json"

BEFORE=$(git rev-parse HEAD)
$PY tools/link_sources_driver.py            || true   # standalone papers/books
$PY tools/link_sources_driver.py --chapters || true   # book chapters
AFTER=$(git rev-parse HEAD)

if [ "$BEFORE" != "$AFTER" ]; then
    sudo systemctl restart pkis-mcp
    echo "$(date '+%F %T') links added ($BEFORE..$AFTER) — service restarted"
else
    echo "$(date '+%F %T') no new links — no restart"
fi
echo "=== $(date '+%F %T') link-sources sweep done ==="
