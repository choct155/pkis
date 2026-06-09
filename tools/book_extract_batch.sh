#!/bin/bash
# Detached, idempotent Haiku TEXT extraction for the 6 Phase-C books.
# Reads chapter slugs from /home/pkis/proposals/*_map.json, runs reader_build
# `extract` (no narration/TTS), writes payload.json per chapter, skips done,
# continues past failures. Run: nohup bash book_extract_batch.sh &
set -u
cd /home/pkis
set -a; . /home/pkis/.env; set +a
export PYTHONPATH=/home/pkis/pkis-wiki
PY=/home/pkis/venv/bin/python
SCRIPT=/home/pkis/pkis-wiki/tools/reader_build.py
READER=/home/pkis/pkis-wiki/wiki/reader
LOG=/home/pkis/book_extract_batch.log

: > "$LOG"
echo "[BATCH START] $(date '+%F %T')" >> "$LOG"
slugs=$($PY -c "
import json,glob
ks=[]
for f in sorted(glob.glob('/home/pkis/proposals/'+'*_map.json')):
    ks += list(json.load(open(f)).keys())
print(' '.join(sorted(set(ks))))
")
n=0; ok=0; fail=0; skip=0
for s in $slugs; do
  n=$((n+1))
  out="$READER/$s"
  if [ -f "$out/payload.json" ]; then echo "[SKIP] $s (payload exists)" >> "$LOG"; skip=$((skip+1)); continue; fi
  mkdir -p "$out"
  echo "[START $n] $s $(date '+%T')" >> "$LOG"
  if OUTDIR="$out" $PY -u "$SCRIPT" "$s" extract >> "$LOG" 2>&1; then
    echo "[OK] $s" >> "$LOG"; ok=$((ok+1))
  else
    echo "[FAIL] $s" >> "$LOG"; fail=$((fail+1))
  fi
done
echo "[BATCH DONE] $(date '+%F %T') total=$n ok=$ok fail=$fail skip=$skip" >> "$LOG"
