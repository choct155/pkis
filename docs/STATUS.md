# PKIS Status

The single canonical snapshot of current build state. Changes frequently — update
after every build session. This is not a design doc (see [`ARCHITECTURE.md`](ARCHITECTURE.md))
or a decision record (see [`DECISIONS.md`](DECISIONS.md)).

_Last updated: 2026-06-12_

## Component status

| Component | Status | Notes |
|---|---|---|
| PKIS-MCP server (`app.py`) | **live** | MCP + `/pkis-api/*` + docs/webhook/health on `pkis.dev` |
| Knowledge graph (`pkis-wiki`) | **live** | ~1,675 nodes / ~4,372 edges |
| Viewer PWA (`pkis.dev/app`) | **live** | browse/clusters/priority/graph/staged/explainers/discover/reader; full node body renders |
| MCP write tools | **live** | stub/edge/hypothesis/bridge/source/edit; auto-commit+push, cache auto-refresh |
| OAuth (WorkOS AuthKit) | **live** | authenticated claude.ai writes; allowlist by WorkOS `sub` |
| claude.ai connector reads | **live** | 404 root-cause fixed; users reconnect once after the fix |
| Semantic search | **live** | BM25 + bge-small dense, fused via RRF; embed cache gitignored |
| Research clusters + frontier priority | **live** | all 12 clusters de-orphaned; frontier-driven priority |
| Read+listen reader | **live** | LLM semantic narration of sources |
| Proactive discovery | **live** | frontier-gated OpenAlex cite-graph, cron'd Mondays; inbox + accept/dismiss feedback + learned-prior loop all live (prior empty until first feedback) |
| Documentation system (`docs/`) | **live** | 6 docs + `log_idea` + mobile-first viewer Docs view; deployed |

## Book knowledge coverage (Phase C)

All eight acquired books mined into the graph (coverage layer done; reader text
varies). Reader `paper_md` built for MacKay (all 50 ch) and Hastie ESL; the other six
have chapter stubs/nodes but may lack extracted reader text.

| Book | slug |
|---|---|
| MacKay ITILA | `mackay-itila` |
| Hastie ESL | `hastie-esl` |
| Russell & Norvig AIMA | `russell-norvig-aima` |
| Gelman BDA3 | `gelman-bda3` |
| Sutton & Barto RL | `sutton-reinforcement-2018` |
| Deisenroth MML | `deisenroth-mml` |
| Pearl Causality | `pearl-causality` |
| Resnick Stochastic Processes | `resnick-stochastic-processes` |

**In acquisition:** Goodfellow (Deep Learning, HTML-only), Murphy PML vol. 1 & 2
(ingest configs staged). **Still unacquired:** Bishop PRML.

## Known issues

- Discovery **learned prior is cold** — the inbox + feedback loop are live, but no
  accept/dismiss decisions have been logged yet, so the per-signal prior is still
  neutral. Warms up once feedback starts. (Acting is write-gated — sign in to use it.)
- Git can diverge across the laptop and server checkouts of the one repo — both
  commit to `origin/main`, and the server auto-commits on every MCP write.
  Reconcilable: commit wanted changes, `git checkout --` for files origin already has,
  `git pull --no-rebase`, push.
- An `app.py` restart drops the claude.ai connector (users must reconnect) —
  minimize restarts; content changes don't need one (cache auto-refresh).

## Most recent session

Documentation system built **and deployed**: `docs/` (ABOUT, ARCHITECTURE, USAGE,
STATUS, DECISIONS, IDEAS) + manifest, the `log_idea` MCP write tool, docs read
endpoints, and a mobile-first **Docs** view; `PHASE_C_BRIEF.md` absorbed and removed.
Then folded the mobile bottom-nav into a primary bar + "more" menu (acting on a logged
idea). Corrected the discovery status below — its inbox/feedback/prior loop is live.

## Next priorities

1. Start exercising discovery feedback (accept/dismiss) to warm the learned prior.
2. Extract reader text for the six books lacking `paper_md` (prioritize Gelman /
   Deisenroth / Sutton — closest to existing clusters).
3. Finish acquiring Goodfellow + Murphy PML; acquire Bishop PRML.
