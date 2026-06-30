#!/bin/bash
# Daily PKIS Lab Assistant descriptive monitoring. Sources the service env, runs the
# monitor (writes a dated JSONL snapshot under PKIS_LAB_DIR, appends any drift flags to
# the wiki/inbox.md Lab lane), then commits + pushes the inbox ONLY if it changed.
# Descriptive only — never touches live wiki content, never restarts the service.
set -u
cd /home/pkis/pkis-wiki
set -a; . /home/pkis/.env 2>/dev/null; set +a
export PYTHONPATH=/home/pkis/pkis-wiki
export PKIS_LAB_DIR="${PKIS_LAB_DIR:-/home/pkis/lab}"
LOG=/home/pkis/lab_assistant.log

echo "=== lab monitor $(date '+%F %T') ===" >> "$LOG"
/home/pkis/venv/bin/python /home/pkis/pkis-wiki/tools/lab_monitor.py >> "$LOG" 2>&1

# Surface drift flags only if the monitor actually appended to the inbox.
if ! git diff --quiet -- wiki/inbox.md; then
  git add wiki/inbox.md
  git commit -q -m "[lab-assistant] drift flags $(date '+%F')" >> "$LOG" 2>&1
  git push -q >> "$LOG" 2>&1 && echo "pushed inbox update" >> "$LOG"
fi
