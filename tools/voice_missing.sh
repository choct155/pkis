#!/bin/bash
# Batch-voice every reader chapter that has an extracted payload (paper_md) but no
# audio.mp3 yet: narrate (Claude Sonnet) + Piper TTS via reader_build.py's `voice`
# stage. TTS is local Piper ($0); only the narration LLM costs (logged by the
# Comptroller, origin=pkis-reader).
#
# Sequential by design — the org's input-tokens/minute limit makes parallelism
# pointless (reader_build backs off on 429). RESUMABLE: re-running skips chapters
# that already have audio.mp3, so a crash/kill loses at most one chapter.
#
#   nohup bash tools/voice_missing.sh > /home/pkis/voice_all.log 2>&1 &
set -u
ROOT=/home/pkis/pkis-wiki/wiki/reader
PY=/home/pkis/venv/bin/python

set -a; . /home/pkis/.env 2>/dev/null; set +a            # ANTHROPIC_API_KEY, etc.
export PIPER=/home/pkis/piper_dist/piper/piper
export PIPER_MODEL=/home/pkis/piper_dist/voices/en_GB-cori-high.onnx
export LD_LIBRARY_PATH=/home/pkis/piper_dist/piper
export PYTHONPATH=/home/pkis/pkis-wiki
cd /home/pkis

slugs=$(for d in "$ROOT"/*/; do s=$(basename "$d"); \
  [ -f "$d/payload.json" ] && [ ! -f "$d/audio.mp3" ] && echo "$s"; done | sort)
total=$(printf '%s\n' "$slugs" | grep -c .)
echo "$(date) — voicing $total missing-audio chapters (Piper=$PIPER_MODEL)"

done=0; fail=0; skip=0; i=0
for s in $slugs; do
  i=$((i+1)); d="$ROOT/$s"
  [ -f "$d/audio.mp3" ] && { skip=$((skip+1)); echo "[$i/$total] skip $s (already voiced)"; continue; }
  export OUTDIR="$d"
  echo "[$i/$total] $(date +%H:%M:%S) voicing $s …"
  echo '{"state":"building"}' > "$d/status.json"
  if $PY -u /home/pkis/pkis-wiki/tools/reader_build.py "$s" voice > "$d/voice.log" 2>&1; then
    echo '{"state":"ready"}' > "$d/status.json"; done=$((done+1)); echo "    ok"
  else
    echo '{"state":"error"}' > "$d/status.json"; fail=$((fail+1)); echo "    FAIL — tail $d/voice.log"
    tail -3 "$d/voice.log" | sed 's/^/      /'
  fi
done
echo "$(date) — voice batch complete: $done ok, $fail failed, $skip skipped"
