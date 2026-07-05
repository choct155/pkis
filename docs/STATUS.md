# PKIS Status

The single canonical snapshot of current build state. Changes frequently — update
after every build session. This is not a design doc (see [`ARCHITECTURE.md`](ARCHITECTURE.md))
or a decision record (see [`DECISIONS.md`](DECISIONS.md)).

_Last updated: 2026-07-05_

## Component status

| Component | Status | Notes |
|---|---|---|
| PKIS-MCP server (`app.py`) | **live** | MCP (41 tools) + `/pkis-api/*` + docs/webhook/health on `pkis.dev`; gunicorn `pkis-mcp.service`; pinned deps in `requirements.txt` added for fresh-clone setup; architect/graph/link tools marked executable |
| Knowledge graph (`pkis-wiki`) | **live** | 2,943 nodes (+5 since 2026-06-28); new source: DREAM (Dense Retrieval Embeddings via Autoregressive Modeling); new framework: Musical Preference Ontology; new resource: OpenWiki; music-preference-profile doc auto-created |
| Viewer PWA (`pkis.dev/app`) | **live** | mobile-first; wide-desktop dashboard (≥1280px); retrieval lab view (side-by-side regimes + unified retrieve/answer panel); path-mode UI; **native Capacitor APK** with WorkOS bearer auth + biometric unlock |
| MCP write tools | **live** | stub/edge/hypothesis/bridge/source/edit; auto-commit+push, cache auto-refresh |
| Auth (WorkOS AuthKit) | **live** | OAuth (claude.ai/MCP) + web sealed session; identity keyed on email; allowlist by email OR sub; single-use-refresh race coalesced; WorkOS dep added to resource node + public serving layer |
| Ask (NL Q&A) | **live** | shared `ask.py` engine + `/pkis-api/ask` + viewer Ask tab; conversation persistence, voice I/O, capability-link sharing |
| Inbox (owner review hub) | **live** | consolidated staged + discovery + agent lanes; **finding intake** added (Parts A+B); **lab-assistant cron inbox push** made divergence-safe; doc-drift lane; Graph gaps lane |
| Lab Assistant | **live** | **finding intake + descriptive Lab Assistant (Parts A+B)** shipped; cron inbox push divergence-safe |
| Semantic search | **live** | BM25 + bge-small dense fused via RRF; graph rerank (personalized PageRank); path/relationship queries; standing-eval loop; **OpGraph designated as live NED/NER experimental platform** with six resolution strategies operationalizing the intensional-grounding-ned-accuracy hypothesis |
| Retrieval lab deep metrics | **live** | P4 metrics (C(q) coverage, concision, relevance) per search regime; lab view + path-mode UI |
| Research clusters + frontier priority | **live** | all 12 clusters de-orphaned; frontier-driven priority queue |
| Read+listen reader | **live** | LLM semantic narration + section-synced chapter PDF; resilient TTS (Piper-unvoiceable segments skipped); mp3 encoder streamed |
| Proactive discovery | **live** | frontier-gated OpenAlex cite-graph, cron'd Mondays; inbox + accept/dismiss feedback + learned-prior loop (prior still cold) |
| Documentation system (`docs/`) | **live** | 6 docs + `log_idea` + viewer Docs view; music-preference-profile doc auto-added via doc-store |
| Explainers | **live** | HTML explainers as `asset` nodes; desktop live-edit loop; Tier-2 dynamic-explainer Flask blueprint scaffold (`/pkis-api/x/<name>/`) |
| Comptroller (cost) | **live** | `usage.py` SQLite at `/home/pkis/usage`; per-origin cost; narration logs as `pkis-reader` |
| Ideas log | **live** | `log_idea` tool; new entry: OpGraph Strategist — multi-agent strategic council |

## Source / narration coverage

All 11 backlog books **split into per-chapter PDFs** (136 chapters) and 50 papers
downloaded — all viewable. **0 chapters narrated** (count reset/unconfirmed since
last update — watchdog-guarded backlog build in flight); the remaining backlog
narration is **in flight** (resumable `backlog_build.sh`: Haiku extract → Sonnet
voice → Piper TTS), guarded by a self-healing watchdog (`narration_watchdog.sh`,
cron */15) that auto-pauses on API-credit exhaustion and auto-resumes.

Books split: cassandras-des-intro, tanner, cimiano, gulli (29 ch, Springer-anchor
split), cunningham, carrell, allemang, kroese, nielsen, benzi, lange — plus the
earlier Phase-C set (MacKay, Hastie ESL, AIMA, Gelman, Sutton, Deisenroth, Pearl,
Resnick, Goodfellow, Murphy PML 1&2, Jaynes).

## Active workstream — OpGraph as NED/NER experimental platform

Instrumentation plan filed: OpGraph operationalizes the intensional-grounding-ned-accuracy
hypothesis via six named entity resolution strategies. This makes the live graph a
controlled experimental surface for measuring NED/NER accuracy improvements from
grounded intensional representations.

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
- Narrated chapter count unconfirmed in live counts (showing 0); watchdog status
  should be verified.

## Most recent session (2026-07-05)

Node count advanced to 2,943 (+5). Key additions: DREAM source node, Musical
Preference Ontology framework (multiple commits consolidated), OpenWiki resource,
music-preference-profile doc (auto-created via doc-store). Native Capacitor APK
shipped with WorkOS bearer auth and biometric unlock. Lab Assistant finding intake
(Parts A+B) landed; cron inbox push made divergence-safe. OpGraph designated as
live NED/NER experimental platform with a six-strategy instrumentation plan
operationalizing the intensional-grounding-ned-accuracy hypothesis. Ideas log
received OpGraph Strategist (multi-agent strategic council). Housekeeping: pinned
`requirements.txt` added, tool scripts marked executable.

## Next priorities

1. Verify narration watchdog status and confirm actual narrated chapter count.
2. Review and resolve remaining orphan nodes in the Graph gaps inbox lane.
3. Publish the calibration tabs + register as a PKIS asset node.
4. Start exercising discovery feedback to warm the learned prior.
5. Begin OpGraph NED/NER instrumentation — baseline measurements for the six resolution strategies.
6. Log the first doc-drift accept/dismiss decisions to validate that inbox lane.
7. Architect automation (daily cron + post-deploy hook) so this doc stops drifting further.
