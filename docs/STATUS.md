# PKIS Status

The single canonical snapshot of current build state. Changes frequently — update
after every build session. This is not a design doc (see [`ARCHITECTURE.md`](ARCHITECTURE.md))
or a decision record (see [`DECISIONS.md`](DECISIONS.md)).

_Last updated: 2026-06-25_

## Component status

| Component | Status | Notes |
|---|---|---|
| PKIS-MCP server (`app.py`) | **live** | MCP (41 tools) + `/pkis-api/*` + docs/webhook/health on `pkis.dev`; gunicorn `pkis-mcp.service` |
| Knowledge graph (`pkis-wiki`) | **live** | ~2,940 nodes |
| Viewer PWA (`pkis.dev/app`) | **live** | mobile-first; **wide-desktop dashboard** (≥1280px: widened shell + right context rail = agenda + recently-viewed; 2-col browse); **retrieval lab view** (side-by-side search-regime comparison) |
| MCP write tools | **live** | stub/edge/hypothesis/bridge/source/edit; auto-commit+push, cache auto-refresh |
| Auth (WorkOS AuthKit) | **live** | OAuth (claude.ai/MCP) + web sealed session; **identity keyed on email** (stable across login methods, fixed 2026-06-24); allowlist by email OR sub; single-use-refresh race coalesced |
| Ask (NL Q&A) | **live** | shared `ask.py` engine + `/pkis-api/ask` + viewer Ask tab; read-only Q&A+traversal, IP-throttled; **conversation persistence** (auto-save, signed-in), voice I/O, capability-link sharing |
| Inbox (owner review hub) | **live** | consolidated staged + discovery + agent lanes; owner-only; bridge-note review + inline link-resolution |
| Semantic search | **live** | BM25 + bge-small dense fused via RRF; instrumented profile-driven pipeline + cross-encoder rerank; standing-eval loop (owner query capture + nightly runner); embed cache gitignored |
| Research clusters + frontier priority | **live** | all 12 clusters de-orphaned; frontier-driven priority; Priority = ranked reading queue w/ rationale |
| Read+listen reader | **live** | LLM semantic narration + section-synced chapter PDF; mp3 encoder streamed (long-narration OOM fixed) |
| Proactive discovery | **live** | frontier-gated OpenAlex cite-graph, cron'd Mondays; inbox + accept/dismiss feedback + learned-prior loop (prior still cold until feedback logged) |
| Documentation system (`docs/`) | **live** | 6 docs + `log_idea` + viewer Docs view |
| Explainers | **live** | HTML explainers as `asset` nodes; desktop live-edit loop (live-reload + git snapshot + in-app ⟳ preview); **Tier-2 dynamic-explainer Flask blueprint** scaffold (`/pkis-api/x/<name>/`) |
| Comptroller (cost) | **live** | `usage.py` SQLite at `/home/pkis/usage`; per-origin cost; narration logs as `pkis-reader` |

## Source / narration coverage

All 11 backlog books **split into per-chapter PDFs** (136 chapters) and 50 papers
downloaded — all viewable. **~371 chapters narrated**; the remaining backlog
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

Added a **retrieval lab view** to the viewer: side-by-side comparison of search
regimes (BM25, dense, fused RRF, reranked), making it easy to inspect and
contrast result sets for any query without leaving the app.

## Next priorities

1. Let the backlog narration finish (multi-day; watchdog-guarded).
2. Publish the calibration tabs + register as a PKIS asset node.
3. Start exercising discovery feedback to warm the learned prior.
4. Architect automation (daily cron + post-deploy hook) so this doc stops
   drifting.
