#!/bin/bash
# Publish explainer HTML. Commits any pending viz edits, pushes the current
# branch, and syncs wiki/assets/viz/ into the live serving copy on this
# workstation, where it's served at
# https://pkis.clowderpack.dev/pkis-api/viz/<slug>.html. After this, hit the ⟳ in
# the PKIS explainer overlay to see the new version in context.
#
# PKIS now runs locally; the old VPS rsync target (pkis@pkis.dev) is retired —
# we publish into WIKI_DIR (the app's configured serving copy) instead.
#
#   bash tools/explainer_publish.sh
set -u
cd "$(git rev-parse --show-toplevel)"
git add wiki/assets/viz/
if ! git diff --cached --quiet; then
  git commit -q -m "explainer: publish viz edits"
fi
branch="$(git branch --show-current)"
git push -q origin "$branch" 2>&1 | tail -1 || echo "(push skipped/failed — continuing to sync)"

# Sync into the live serving copy. WIKI_DIR comes from the app's .env (falls back
# to the known local path). No-op when this repo is already the serving copy.
WIKI_DIR="$(grep -E '^WIKI_DIR=' /home/choct155/projects/pkis/.env 2>/dev/null | cut -d= -f2- | tr -d '"')"
WIKI_DIR="${WIKI_DIR:-/home/choct155/projects/pkis-home/pkis-wiki/wiki}"
serve_viz="$WIKI_DIR/assets/viz/"
src_viz="$(pwd)/wiki/assets/viz/"

if [ "$src_viz" = "$serve_viz" ]; then
  echo "this repo is the live serving copy — viz already in place (branch: $branch)"
elif [ -d "$WIKI_DIR/assets" ]; then
  rsync -a "$src_viz" "$serve_viz" \
    && echo "published wiki/assets/viz/ → $serve_viz (branch: $branch)"
else
  echo "WARN: serving viz dir not found ($serve_viz) — is WIKI_DIR correct? skipped" >&2
  exit 1
fi
