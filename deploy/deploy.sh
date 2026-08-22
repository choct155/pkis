#!/usr/bin/env bash
#
# deploy.sh — one-command PKIS deploy.
#
# Folds together every "activation" step so a redeploy is a single command:
#   1. pull latest code (fast-forward only — never auto-merges a divergence)
#   2. load the server env from the gitignored .env (app.py reads os.environ; it
#      does NOT load .env itself, so we export it here — same file the launcher uses)
#   3. build the viewer SPA into viewer/app/dist (served by serve_app / nginx alias)
#   4. warm the embedding cache out-of-band, so the first search after reload is
#      instant instead of paying a cold full-corpus encode inside a request
#   5. gracefully reload gunicorn (SIGHUP re-imports the app with zero bind drop);
#      starts it (daemonized, with a pidfile) if it isn't running
#   6. health-check the running server
#
# Usage:  deploy/deploy.sh                # full deploy
#         deploy/deploy.sh --skip-build   # backend-only (skip npm build)
#         deploy/deploy.sh --skip-embeddings
#
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$REPO/.env"
PY="$REPO/.venv/bin/python"
GUNICORN="$REPO/.venv/bin/gunicorn"
BIND="127.0.0.1:5001"
PIDFILE="$REPO/../pkis-home/gunicorn.pid"
ACCESS_LOG="$REPO/../pkis-home/access.log"
ERROR_LOG="$REPO/../pkis-home/error.log"

SKIP_BUILD=0; SKIP_EMBED=0
for a in "$@"; do
  case "$a" in
    --skip-build) SKIP_BUILD=1 ;;
    --skip-embeddings) SKIP_EMBED=1 ;;
    *) echo "unknown flag: $a" >&2; exit 2 ;;
  esac
done

say() { printf '\n\033[1;36m▶ %s\033[0m\n' "$*"; }

cd "$REPO"

say "1/6  Pulling latest code (fast-forward only)"
git pull --ff-only

say "2/6  Loading server env from $ENV_FILE"
[ -f "$ENV_FILE" ] || { echo "missing $ENV_FILE — cannot deploy without the server env" >&2; exit 1; }
set -a; # shellcheck disable=SC1090
source "$ENV_FILE"; set +a
echo "    WIKI_DIR=$WIKI_DIR"

if [ "$SKIP_BUILD" -eq 0 ]; then
  say "3/6  Building the viewer SPA"
  ( cd viewer && npm install --no-audit --no-fund --silent && npm run build )
else
  say "3/6  Skipping viewer build (--skip-build)"
fi

if [ "$SKIP_EMBED" -eq 0 ]; then
  say "4/6  Warming the embedding cache (out-of-band)"
  # Non-fatal: a disabled/absent semantic backend must not block a deploy — the app
  # degrades to BM25 and warms the cache lazily in the background anyway.
  "$PY" app.py build-embeddings || echo "    (embeddings build skipped/failed — continuing; search degrades to BM25)"
else
  say "4/6  Skipping embeddings (--skip-embeddings)"
fi

say "5/6  Reloading gunicorn"
find_master() {
  # Prefer the pidfile; fall back to the master heuristic (a gunicorn 'app:app'
  # process whose parent is NOT itself gunicorn — i.e. the master, not a worker).
  if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
    cat "$PIDFILE"; return 0
  fi
  local p ppid pcomm
  for p in $(pgrep -f "gunicorn.*app:app" || true); do
    ppid="$(ps -o ppid= -p "$p" | tr -d ' ')"
    pcomm="$(ps -o comm= -p "$ppid" 2>/dev/null || true)"
    case "$pcomm" in *gunicorn*) : ;; *) echo "$p"; return 0 ;; esac
  done
  return 1
}

if MASTER="$(find_master)"; then
  kill -HUP "$MASTER"
  echo "    SIGHUP → gunicorn master $MASTER (graceful worker reload)"
else
  echo "    gunicorn not running — starting it (daemonized)"
  "$GUNICORN" --workers 2 --bind "$BIND" --timeout 120 \
    --pid "$PIDFILE" \
    --access-logfile "$ACCESS_LOG" --error-logfile "$ERROR_LOG" \
    --daemon app:app
  echo "    started; pidfile=$PIDFILE"
fi

say "6/6  Health check"
# gunicorn needs a moment to finish re-importing before the first request lands.
ok=0
for _ in 1 2 3 4 5 6 7 8; do
  sleep 2
  if curl -fsS -m 5 -X POST "http://$BIND/pkis-api/health" \
       -H 'Content-Type: application/json' -d '{}' >/dev/null 2>&1; then
    ok=1; break
  fi
done
if [ "$ok" -eq 1 ]; then
  printf '\n\033[1;32m✓ deploy complete — server healthy on %s\033[0m\n' "$BIND"
else
  printf '\n\033[1;31m✗ server did not answer health check on %s — check %s\033[0m\n' "$BIND" "$ERROR_LOG" >&2
  exit 1
fi
