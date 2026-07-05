#!/usr/bin/env bash
# OpenWiki refresh driver (the "Cartographer" half of the docs cast).
#
# OpenWiki has NO in-place ignore mechanism (no --ignore flag, no config, no .gitignore
# respect) — it will read the whole tree, including large content dirs (e.g. PKIS's
# 2,900-node wiki/). So we scope PHYSICALLY: rsync a CODE-ONLY copy into a throwaway
# staging dir, run OpenWiki there, then copy the generated openwiki/ back into the live
# repo and commit+push just the docs.
#
# Model: Sonnet. Haiku hallucinated tool names in testing — unsafe for unattended docs.
# Key: read inline from the repo's gitignored .env; never persisted to a plaintext config.
#
# Usage: openwiki_refresh.sh <repo-dir>
#   Expects <repo-dir>/.openwiki-exclude (rsync --exclude-from list of non-code paths).
set -euo pipefail

REPO="${1:?usage: openwiki_refresh.sh <repo-dir>}"
REPO="$(cd "$REPO" && pwd)"
STAGE="${OPENWIKI_STAGE_ROOT:-/home/pkis/openwiki-stage}/$(basename "$REPO")"
MODEL="${OPENWIKI_MODEL_ID:-claude-sonnet-4-6}"
OWBIN="${OPENWIKI_BIN:-/home/choct155/.pixi/envs/nodejs/bin/openwiki}"

KEY="$(grep -E '^ANTHROPIC_API_KEY=' "$REPO/.env" 2>/dev/null | cut -d= -f2- || true)"
[ -n "$KEY" ] || { echo "openwiki_refresh: no ANTHROPIC_API_KEY in $REPO/.env" >&2; exit 1; }
[ -f "$REPO/.openwiki-exclude" ] || { echo "openwiki_refresh: missing $REPO/.openwiki-exclude" >&2; exit 1; }

# 1. code-only staging copy (throwaway git repo — OpenWiki leans on git log/blame)
mkdir -p "$STAGE"
rsync -a --delete --exclude-from="$REPO/.openwiki-exclude" "$REPO/" "$STAGE/"
cd "$STAGE"
git rev-parse --git-dir >/dev/null 2>&1 || git init -q
git add -A -q
git -c user.email=openwiki@local -c user.name=openwiki commit -q -m "stage $(date -u +%FT%TZ)" || true

# 2. run OpenWiki — init the first time, update thereafter
CMD=--update; [ -d "$STAGE/openwiki" ] || CMD=--init
OPENWIKI_PROVIDER=anthropic OPENWIKI_MODEL_ID="$MODEL" ANTHROPIC_API_KEY="$KEY" LANGSMITH_API_KEY= \
  "$OWBIN" "$CMD" -p

# 3. copy the generated code map back into the live repo
rsync -a --delete "$STAGE/openwiki/" "$REPO/openwiki/"
[ -f "$STAGE/AGENTS.md" ] && cp "$STAGE/AGENTS.md" "$REPO/AGENTS.md"

# 4. commit + push ONLY the docs (never sweeps other working-tree changes)
cd "$REPO"
git add openwiki AGENTS.md
if git diff --cached --quiet; then
  echo "openwiki_refresh: no doc changes for $REPO"
else
  git commit -q -m "docs(openwiki): refresh code map $(date -u +%F)"
  # The workstation has several processes pushing to the same branch; retry with rebase
  # so a concurrent push (non-fast-forward) doesn't strand the docs commit locally.
  BR="$(git rev-parse --abbrev-ref HEAD)"
  for attempt in 1 2 3; do
    if git push -q origin HEAD 2>/dev/null; then break; fi
    git pull --rebase -q origin "$BR" 2>/dev/null || { echo "openwiki_refresh: rebase failed (commit retained)" >&2; break; }
  done
fi
