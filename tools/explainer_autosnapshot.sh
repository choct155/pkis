#!/bin/bash
# Auto-commit every save of an explainer HTML, for fine-grained rollback during an
# editing session. Commits to the CURRENT branch — work on a throwaway edit/ branch
# and squash-merge to main when happy, so main history stays clean.
#
# Portable mtime poller (no fswatch dependency). Seeds current mtimes first, so it
# only commits saves made AFTER it starts.
#
#   git switch -c edit/<name>          # optional: keep main clean
#   bash tools/explainer_autosnapshot.sh
#   ... edit; each save -> one commit ...
#   git switch main && git merge --squash edit/<name> && git commit
set -u
cd "$(git rev-parse --show-toplevel)"
DIR="wiki/assets/viz"
_mtime() { stat -f %m "$1" 2>/dev/null || stat -c %Y "$1"; }

echo "auto-snapshot $DIR/*.html on save -> branch '$(git branch --show-current)' (Ctrl-C to stop)"
declare -A seen
for f in "$DIR"/*.html; do [ -e "$f" ] && seen["$f"]=$(_mtime "$f"); done

while true; do
  for f in "$DIR"/*.html; do
    [ -e "$f" ] || continue
    m=$(_mtime "$f")
    if [ "${seen[$f]:-}" != "$m" ]; then
      seen["$f"]=$m
      if ! git diff --quiet -- "$f"; then
        git add "$f" && git commit -q -m "snapshot($(basename "$f" .html)): $(date +%H:%M:%S)" \
          && echo "  snapshot $(basename "$f")  $(git rev-parse --short HEAD)"
      fi
    fi
  done
  sleep 2
done
