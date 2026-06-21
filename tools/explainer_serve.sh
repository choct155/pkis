#!/bin/bash
# Live-reload preview server for the HTML explainers (wiki/assets/viz/*.html).
# Serves the directory with auto-refresh on save, so editing an explainer — in
# this Claude Code session or any editor — updates the browser instantly. Local
# only; nothing is deployed. Pair with explainer_autosnapshot.sh for rollback.
#
#   bash tools/explainer_serve.sh [port]      # default 5500
#   then open  http://localhost:5500/accuracy-calibration-explainer.html
set -u
PORT="${1:-5500}"
cd "$(git rev-parse --show-toplevel)"
echo "live-reload serving wiki/assets/viz/ at http://localhost:$PORT/"
echo "open e.g.  http://localhost:$PORT/accuracy-calibration-explainer.html"
echo "(Ctrl-C to stop)"
exec npx --yes live-server "wiki/assets/viz/" --port="$PORT" --no-browser --quiet
