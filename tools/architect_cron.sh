#!/bin/bash
# Daily + post-deploy Architect reconciliation of docs/STATUS.md. Sources the API
# key, runs the reconciler (commits + pushes STATUS.md if it drifted), logs.
set -u
cd /home/pkis/pkis-wiki
set -a; . /home/pkis/.env 2>/dev/null; set +a
export PYTHONPATH=/home/pkis/pkis-wiki
echo "=== architect reconcile $(date '+%F %T') ===" >> /home/pkis/architect_cron.log
/home/pkis/venv/bin/python /home/pkis/pkis-wiki/tools/architect_reconcile.py >> /home/pkis/architect_cron.log 2>&1
