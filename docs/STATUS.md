# PKIS Status

The single canonical snapshot of current build state. Changes frequently — update
after every build session. This is not a design doc (see [`ARCHITECTURE.md`](ARCHITECTURE.md))
or a decision record (see [`DECISIONS.md`](DECISIONS.md)).

_Last updated: 2026-06-25_

## Component status

| Component | Status | Notes |
|---|---|---|
| PKIS-MCP server (`app.py`) | **live** | MCP (41 tools) + `/pkis-api/*` + docs/webhook/health on `pkis.dev`; gunicorn `pkis-mcp.service`; corrupted `!=` in docs-drift anchor check repaired (broke import) |
| Knowledge graph (`pkis-wiki`) | **live** | ~2,944 nodes |
| Viewer PWA (`pkis.dev/app`) | **live** | mobile-first; **wide-desktop dashboard** (≥1280px: widened shell + right context rail = agenda + recently-viewed; 2-col browse); **retrieval lab view** (side-by-side search-regime comparison + unified retrieve/answer ask panel) |
| MCP write tools | **live** | stub/edge/hypothesis/bridge/source/edit; auto-commit+push, cache auto-refresh; `add_to_queue` correctly classified as READ tier (was mislabelled write in docs) |
| Auth (WorkOS AuthKit) | **live** | OAuth (claude.ai/MCP) + web sealed session; **identity keyed on email** (stable across login methods, fixed 2026-06-24); allowlist by email OR sub; single-use-refresh race coalesced |
| Ask (NL Q&A) | **live** | shared `ask.py` engine + `/pkis-api/ask` + viewer Ask tab; read-only Q&A+traversal, IP-throttled; **conversation persistence** (auto-save, signed-in), voice I/O, capability-link sharing |
| Inbox (owner review hub) | **live** | consolidated staged + discovery + agent lanes; owner-only; bridge-note review + inline link-resolution; **doc-drift lane** (accept/dismiss atomic edits to STATUS.md and other docs) |
| Semantic search | **live** | BM25 + bge-small dense fused via RRF; instrumented profile-driven pipeline + cross-encoder rerank; **graph rerank** (personalized PageRank); path/relationship queries; standing-eval loop (owner query capture + nightly runner); embed cache gitignored |
| Research clusters + frontier priority | **live** | all 12 clusters de-orphaned; frontier-driven priority; Priority = ranked reading queue w/ rationale |
| Read+listen reader | **live** | LLM semantic narration + section-synced chapter PDF; mp3 encoder streamed (long-narration OOM fixed); **resilient TTS** — Piper-unvoiceable segments skipped rather than aborting the build |
| Proactive discovery | **live** | frontier-gated OpenAlex cite-graph, cron'd Mondays; inbox + accept/dismiss feedback + learned-prior loop (prior still cold until feedback logged) |
| Documentation system (`docs/`) | **live** | 6 docs + `log_idea` + viewer Docs view |
| Explainers | **live** | HTML explainers as `asset` nodes; desktop live-edit loop (live-reload + git snapshot + in-app ⟳ preview); **Tier-2 dynamic-explainer Flask blueprint** scaffold (`/pkis-api/x/<name>/`) |
| Comptroller (cost) | **live** | `usage.py` SQLite at `/home/pkis/usage`; per-origin cost; narration logs as `pkis-reader` |

## Source / narration coverage

All 11 backlog books **split into per-chapter PDFs** (136 chapters) and 50 papers
downloaded — all viewable. **~373 chapters narrated**; the remaining backlog
narration is **in flight** (resumable `backlog_build.sh`: Haiku extract → Sonnet
voice → Piper TTS), guarded by a self-healing watchdog (`narration_watchdog.sh`,
cron */15) that auto-pauses on API-credit exhaustion and auto-resumes.

Books split: cassandras-des-intro, tanner, cimiano, gulli (29 ch, Springer-anchor
split), cunningham, carrell, allemang, kroese, nielsen, benzi, lange — plus the
earlier Phase-C set (MacKay, Hastie ESL, AIMA, Gelman, Sutton, Deisenroth, Pearl,
Resnick, Goodfellow, Murphy PML 1&2, Jaynes).

## Active workstream — calibration explainers

A 3-tab calibration explainer (`accuracy-calibration-tabs.html`, iframe-tab shell):
Tab 1 = pristine silver/gold explainer; Tab 2 = covariance/Dirichlet (flat joint
Dirichlet degenerates to independent Betas → correlated prior is the real lever);
Tab 3 = PPI (rectifier + PPI++ λ "never worse than gold"). PPI/PPI++ source nodes
ingested + narrated. Local-only until published.

## Known issues

- Discovery **learned prior is cold** — inbox + feedback loop live, but no
  accept/dismiss decisions logged yet, so the per-signal prior is neutral.
- Git can diverge across the laptop and server checkouts of the one repo — both
  commit to `origin/main`, server auto-commits on every MCP write. Reconcilable
  (commit / `git checkout --` / `pull` / push).
- An `app.py` restart drops the claude.ai connector (users must reconnect) —
  minimize restarts; content changes don't need one (cache auto-refresh).

## Most recent session (2026-06-25)

Hardened the TTS pipeline: the reader now skips any Piper-unvoiceable segment
rather than aborting the entire narration build, making backlog runs more
resilient to edge-case segments. Chapter count ticks up to 373; graph holds at
2,944 nodes.

## Next priorities

1. Let the backlog narration finish (multi-day; watchdog-guarded).
2. Publish the calibration tabs + register as a PKIS asset node.
3. Start exercising discovery feedback to warm the learned prior.
4. Log the first doc-drift accept/dismiss decisions to validate the new inbox lane.
5. Architect automation (daily cron + post-deploy hook) so this doc stops drifting further.
