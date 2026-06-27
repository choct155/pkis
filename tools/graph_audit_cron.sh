#!/bin/bash
# Fortnightly graph-gaps audit. Finds orphaned concept-side nodes and writes editable
# suggested typed edges to /home/pkis/graph_gaps.json, surfaced in the owner inbox
# "Graph gaps" lane (approve/edit/dismiss).
set -u
cd /home/pkis/pkis-wiki
set -a; . /home/pkis/.env 2>/dev/null; set +a
export PYTHONPATH=/home/pkis/pkis-wiki
echo "=== graph audit $(date '+%F %T') ===" >> /home/pkis/graph_audit.log
/home/pkis/venv/bin/python /home/pkis/pkis-wiki/tools/graph_audit.py >> /home/pkis/graph_audit.log 2>&1
