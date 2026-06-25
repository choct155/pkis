#!/bin/bash
# Fortnightly Architect doc-drift audit. Reads the backend + living docs and writes
# atomic, individually-acceptable drift items to /home/pkis/architect_drift.json,
# which surface in the owner inbox (Docs drift lane) with accept/dismiss.
set -u
cd /home/pkis/pkis-wiki
set -a; . /home/pkis/.env 2>/dev/null; set +a
export PYTHONPATH=/home/pkis/pkis-wiki
echo "=== architect audit $(date '+%F %T') ===" >> /home/pkis/architect_audit.log
/home/pkis/venv/bin/python /home/pkis/pkis-wiki/tools/architect_audit.py >> /home/pkis/architect_audit.log 2>&1
