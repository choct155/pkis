#!/bin/bash
# Publish explainer HTML to production. Commits any pending viz edits, pushes the
# current branch, and rsyncs wiki/assets/viz/ to the server, where it's served
# live at https://pkis.dev/pkis-api/viz/<slug>.html. After this, hit the ⟳ in the
# PKIS explainer overlay to see the new version in context.
#
#   bash tools/explainer_publish.sh
set -u
cd "$(git rev-parse --show-toplevel)"
git add wiki/assets/viz/
if ! git diff --cached --quiet; then
  git commit -q -m "explainer: publish viz edits"
fi
branch="$(git branch --show-current)"
git push -q origin "$branch" 2>&1 | tail -1 || echo "(push skipped/failed — continuing to rsync)"
rsync -az wiki/assets/viz/ pkis@pkis.dev:/home/pkis/pkis-wiki/wiki/assets/viz/ \
  && echo "published wiki/assets/viz/ to pkis.dev (branch: $branch)"
