# `tools/` — operational + one-shot scripts

This manifest is the B7 deliverable: a single place that signals **which scripts are
load-bearing (wired to cron, the app, or the live pipeline) versus historical
one-shots safe to change or delete.** Files are intentionally *not* split into
`ops/` and `oneshot/` subdirectories — too many of them are referenced by path
(`app.py`, the VPS crontab, `discovery_cron.sh`, the build shell scripts, and several
tests), so a physical move would be high-churn for an organizational gain. The
classification lives here instead.

Legend: **🔴 load-bearing** = wired to cron/app/live pipeline; changing it can affect
production. **🟡 supporting** = imported/invoked by a load-bearing script. **⚪ one-shot**
= historical ingest/backfill; completed, safe to change or archive.

## 🔴 Load-bearing (wired — change with care)

| Script | Wired to | Notes |
|---|---|---|
| `comptroller.py` | VPS crontab (daily/weekly/monthly) | Usage cost reports → `/home/pkis/usage`; weekly `--alert-queue`. Imports `usage.py`. |
| `discovery_openalex.py` | `discovery_cron.sh` (Mon 07:00) | Frontier-gated OpenAlex discovery; writes `discovery_inbox.json`. Logs usage (`pkis-discovery`). |
| `reader_build.py` | `app.py` (reader pipeline), `run_build.sh` | LLM narration build; imports `app`. Logs usage (`pkis-reader`). |
| `reconcile_push.py` | `app.py` (GitPushError remediation), tests | Layer-2 push reconciliation; referenced in loud-push diagnostics. |

## 🟡 Supporting / actively-run (not cron'd, but load-bearing when run)

| Script | Role |
|---|---|
| `mine_proposals.py` | Synthesizer-style proposal mining (run manually via `nohup`). Logs usage (`pkis-mine-proposals`). |
| `discovery_stubs_from_inbox.py` | Phase-1c: recast `discovery_inbox.json` → `wiki/discovery/` stubs. Re-runnable, idempotent. |

## ⚪ One-shot ingest / backfill (historical — safe to change or archive)

| Script | Purpose | Status |
|---|---|---|
| `run_build.sh` | Orchestrates the book reader-build pipeline | book waves complete |
| `book_extract_batch.sh` | Batch chapter extraction wrapper | book waves complete |
| `book_setup.py` | Build per-book chapter maps | book waves complete |
| `book_outline.py` | Derive book outlines | book waves complete |
| `reader_split_book.py` | Split a book PDF into per-chapter PDFs | book waves complete |
| `import_drive_books.py` | Server-side Drive PDF import | as-needed |
| `section_pages.py` | Generate reader section payloads | as-needed |
| `mackay_phasec_driver.py` | Phase-C book mining driver | **complete** (all 8 books mined) |
| `fill_missing.py` | Backfill missing nodes for a wave | as-needed backfill |

## Paths & config

All scripts resolve filesystem paths and model IDs through `paths.py` / `config.py`
(B4 + B6) where they've been updated; the historical one-shots may still carry inline
`/home/pkis/...` literals (harmless — they only run on the VPS). New scripts should
`from paths import …` / `from config import …` rather than hardcode.
