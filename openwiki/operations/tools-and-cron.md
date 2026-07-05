# Tools & Cron

`tools/` holds ~30 standalone operational scripts that run outside the
request/response cycle of `app.py` — cron-scheduled agents, one-shot ingest
pipelines, and audits. `tools/README.md` is the load-bearing manifest for
this directory; treat it as the primary source and this page as a guided
tour plus the cron schedule it doesn't fully spell out.

**Convention**: scripts resolve filesystem paths and model IDs through
`paths.py` / `config.py` rather than hardcoding `/home/pkis/...` — do this in
any new script. Cost-incurring scripts log through `usage.log_usage()`
(best-effort, never raises). A recurring safety pattern is a `--dry`/
`--dry-run` flag that computes and prints without writing (see
`architect_audit.py`, `lab_monitor.py`, `reconcile_push.py`).

## 🔴 Load-bearing (cron/app-wired — change with care)

| Script | Wired to | What it does |
|---|---|---|
| `comptroller.py` | VPS crontab (daily/weekly/monthly) | Reads the `usage.py` SQLite store, writes cost reports by origin/model/project, appends a budget alert to `wiki/inbox.md` on threshold crossing. No LLM call itself. |
| `discovery_openalex.py` | `discovery_cron.sh` (Monday 07:00) | Frontier-gated OpenAlex citation-graph discovery — see [Curation & Lifecycle](../domain/curation-and-lifecycle.md#discovery-how-new-sources-enter-the-funnel). |
| `reader_build.py` | `app.py`'s reader pipeline (`tool_build_reader`), `run_build.sh` | LLM narration build for the audio/annotated reader experience; imports `app`. |
| `reconcile_push.py` | `app.py`'s `GitPushError` remediation path, tests | Diagnoses git divergence after a failed push; reports only by default, executes `pull --rebase` + push only with `--confirm`. Exit codes: 0 in-sync, 1 reconcile failed, 2 remote unreachable. |
| `architect_reconcile.py` | `architect_cron.sh` (daily) | Reconciles `docs/STATUS.md` drift; commits + pushes if changed. |
| `lab_monitor.py` | `lab_assistant_cron.sh` (daily) | Descriptive-only research-health snapshot; see [Curation & Lifecycle](../domain/curation-and-lifecycle.md#health-drift-and-audit-monitoring). |

## 🟡 Supporting (actively run, not cron'd)

| Script | Role |
|---|---|
| `mine_proposals.py` | Synthesizer-style proposal mining, run manually (`nohup`). |
| `discovery_stubs_from_inbox.py` | Converts `discovery_inbox.json` entries into `wiki/discovery/` stub nodes; idempotent, re-runnable. |
| `link_sources_driver.py` | "Librarian Linking Mode" — links unlinked sources to concepts via a cheap (Haiku) model pass; wired to `link_sources_cron.sh` (weekly), which resets resume-state before each sweep so newly-created concepts can re-match previously-orphaned sources. |
| `architect_audit.py` | Fortnightly LLM-driven doc-drift audit (reads `app.py`, `config.py`, `store.py`, `adapters.py`, `usage.py`, `paths.py`, `ask.py`, `conversations.py` against `docs/ARCHITECTURE.md`/`ABOUT.md`/`USAGE.md`); emits atomic accept/dismiss items to `architect_drift.json`. Wired to `architect_audit_cron.sh`. |
| `graph_audit.py` / `audit_asset_kinds.py` | Structural graph audits (missing IRIs, malformed edges, asset-kind consistency). Wired to `graph_audit_cron.sh`. |
| `nightly_eval.py` | Standing-eval loop — replays the deliberate query log (`experiments.py`'s `query_log` table) through the retrieval-lab profile suite nightly. |
| `search_harness.py` | Manual harness for exercising search profiles outside the live server. |

## ⚪ One-shot / historical (safe to change or archive)

Book ingestion pipeline — all "book waves complete": `book_setup.py`,
`book_outline.py`, `book_extract_batch.sh`, `reader_split_book.py`,
`import_drive_books.py`, `section_pages.py`, `mackay_phasec_driver.py`
(all 8 books mined). Plus `fill_missing.py` (as-needed backfill),
`relabel_books.py`, `split_by_nodes.py`, `voice_missing.sh`,
`explainer_autosnapshot.sh` / `explainer_publish.sh` / `explainer_serve.sh`
(static explainer asset lifecycle).

## Cron schedule summary

Based on the `*_cron.sh` wrappers (all `cd /home/pkis/pkis-wiki`, source
`/home/pkis/.env`, log to a dedicated `.log` file):

- **Daily**: `architect_cron.sh` (STATUS.md reconciliation),
  `lab_assistant_cron.sh` (Lab Assistant snapshot + drift flags — pushes
  `wiki/inbox.md` only if it changed, and hard-resets to `origin/main` on any
  rebase/push failure so the VPS never carries an unpushed local commit).
- **Weekly (Monday 07:00)**: `discovery_cron.sh` → `discovery_openalex.py`.
- **Weekly**: `link_sources_cron.sh` → `link_sources_driver.py`.
- **Fortnightly**: `architect_audit_cron.sh` → `architect_audit.py`.
- **Periodic (audit cadence)**: `graph_audit_cron.sh` → `graph_audit.py`.
- **Daily/weekly/monthly**: `comptroller.py` cost reports (invoked with a
  `report {daily|weekly|monthly|ytd}` subcommand).

## What to check when changing a script here

- If a script is 🔴 load-bearing, check `tools/README.md` for what it's wired
  to before changing its CLI surface, output paths, or exit codes — the
  corresponding `.sh` wrapper and/or `app.py` may depend on them.
- If a script calls an LLM, confirm it still calls `log_usage()` and that a
  logging failure can't abort the main task (mirror the try/except-and-degrade
  pattern in `discovery_openalex.py`'s usage import).
- If a script writes to the wiki git repo, confirm it follows the
  "loud failure over silent desync" pattern used by `lab_assistant_cron.sh`
  and `reconcile_push.py` — reconcile via rebase, and hard-reset/abort rather
  than leaving an unpushed local commit.
- Relevant tests: `tests/integration/test_reconcile_push.py`,
  `tests/integration/test_lab_assistant.py`,
  `tests/unit/test_discovery_stubs.py`, `tests/unit/test_comptroller.py`,
  `tests/unit/test_paths.py`.

## Source map

- `tools/README.md` — authoritative load-bearing/supporting/one-shot manifest.
- `tools/reconcile_push.py:1-18` — Layer-2 loud-push reconciliation policy.
- `tools/comptroller.py:1-19` — cost report CLI usage.
- `tools/lab_assistant_cron.sh`, `architect_cron.sh`, `link_sources_cron.sh` — cron wiring and cadence.
