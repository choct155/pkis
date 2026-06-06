#!/bin/bash
# Slug-driven reader build launcher. Routes internally (arxiv | doc-store pdf | web html).
# Usage: run_build.sh <slug>   (back-compat: run_build.sh <arxiv_id> <slug> still works)
if [[ "$1" =~ ^[0-9]+\.[0-9]+$ ]] && [ -n "$2" ]; then
  slug="$2"; extra="$1 $2"   # back-compat positional form
else
  slug="$1"; extra="$1"
fi
d="/home/pkis/pkis-wiki/wiki/reader/$slug"
export PIPER=/home/pkis/piper_dist/piper/piper
export PIPER_MODEL=/home/pkis/piper_dist/voices/en_GB-cori-high.onnx
export LD_LIBRARY_PATH=/home/pkis/piper_dist/piper
export OUTDIR="$d"
mkdir -p "$d"
echo "{\"state\":\"building\"}" > "$d/status.json"
cd /home/pkis
export PYTHONPATH=/home/pkis/pkis-wiki
if /home/pkis/venv/bin/python -u /home/pkis/pkis-wiki/tools/reader_build.py $extra full > "$d/build.log" 2>&1; then
  echo "{\"state\":\"ready\"}" > "$d/status.json"
else
  echo "{\"state\":\"error\"}" > "$d/status.json"
fi
