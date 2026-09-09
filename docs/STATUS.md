# PKIS Status

The single canonical snapshot of current build state. Changes frequently — update
after every build session. This is not a design doc (see [`ARCHITECTURE.md`](ARCHITECTURE.md))
or a decision record (see [`DECISIONS.md`](DECISIONS.md)).

_Last updated: 2026-09-09_

## Component status

| Component | Status | Notes |
|---|---|---|
| PKIS-MCP server (`app.py`) | **live** | MCP (42 tools) + `/pkis-api/*` + docs/webhook/health on `pkis.clowderpack.dev`; gunicorn `pkis-mcp.service`; pinned deps in `requirements.txt`; architect/graph/link tools marked executable; `get_openwiki` read-only tool exposing openwiki/ code map; `index.html` served `no-store` to eliminate stale-shell fetches; ask caps tightened to reduce latency tail |
| Knowledge graph (`pkis-wiki`) | **live** | **2,978 nodes**; MCP-committed sources: A Mathematical Introduction to Diffusion Models, Language Models Can Control Their Own Attention; doc-store added terminalist-bloombergs-last-stand + terminalist-bloombergx27s; 40+ librarian link-ops across diffusion, Bayesian inference, amortized VI, autoregressive, Kalman/state-estimation, autodiff, and deep-learning nodes |
| Viewer PWA (`pkis.clowderpack.dev/app`) | **live** | mobile-first; wide-desktop dashboard (≥1280px); retrieval lab view; path-mode UI; native Capacitor APK with WorkOS bearer auth + biometric unlock; **edit-node action added**; **explainers now render, download, and share correctly on mobile**; **native app now loads UI from live server URL — per-frontend APK rebuilds eliminated** |
| MCP write tools | **live** | stub/edge/hypothesis/bridge/source/edit; auto-commit+push, cache auto-refresh; `save_url_source` and `save_podcast_source` documented in authoring tools; `edit_node content=` parameter clarified; **cross-worker cache staleness fixed; reload + download added to writing assets** |
| Auth (WorkOS AuthKit) | **live** | OAuth (claude.ai/MCP) + web sealed session; identity keyed on email; allowlist by email OR sub; single-use-refresh race coalesced; opaque-token fallback via OIDC userinfo for MCP writes |
| Ask (NL Q&A) | **live** | shared `ask.py` engine + `/pkis-api/ask` + viewer Ask tab; two-model split: fast retrieval model + strong synthesis model (~2× faster); conversation persistence, voice I/O, capability-link sharing; clearer progress indicators + graceful recovery on interrupted queries; serial round-trips parallelised (~24s→~15s); ask caps tightened; answer now rendered even when trailing 'done' frame is lost |
| Inbox (owner review hub) | **live** | consolidated staged + discovery + agent lanes; finding intake (Parts A+B); lab-assistant cron inbox push divergence-safe; doc-drift lane; Graph gaps lane; staged-file removal now committed on promote/discard |
| Lab Assistant | **live** | finding intake + descriptive Lab Assistant (Parts A+B) shipped; cron inbox push divergence-safe; drift-flag runs 2026-07-18 and 2026-08-01 processed |
| Semantic search | **live** | BM25 + bge-small dense fused via RRF; `sentence-transformers` + CPU torch in `requirements.txt`; graph rerank (personalized PageRank); path/relationship queries; standing-eval loop; OpGraph designated as live NED/NER experimental platform with six resolution strategies operationalizing the intensional-grounding-ned-accuracy hypothesis |
| Retrieval lab deep metrics | **live** | P4 metrics (C(q) coverage, concision, relevance) per search regime; lab view + path-mode UI |
| Research clusters + frontier priority | **live** | all 12 clusters de-orphaned; frontier-driven priority queue |
| Read+listen reader | **live** | LLM semantic narration + section-synced chapter PDF; resilient TTS (Piper-unvoiceable segments skipped); mp3 encoder streamed; **494 chapters narrated**; narration audio/PDF URLs absolutized for native app; real narration-build failure reason surfaced; content-filtered PDF chunks and failing sections no longer abort extraction or narration builds |
| Proactive discovery | **live** | frontier-gated OpenAlex cite-graph, cron'd Mondays; inbox + accept/dismiss feedback + learned-prior loop (prior still cold) |
| Ingest pipeline | **live** | enriches non-arXiv web sources (blogs, distill.pub, docs pages) in addition to arXiv/PDF paths |
| Documentation system (`docs/`) | **live** | 6 docs + `log_idea` + viewer Docs view; OpenWiki cartographer adopted; predicate drift fixed; CONTEXT.md regenerated from ground truth; Google Drive integration removed; MCP write auto-refresh mechanism clarified; **position paper updated: related explainers + cited nodes + external sources linked; org-change framing removed; §7.3 retitled for mixed audience** |
| OpenWiki refresh driver | **live** | rebase-retry push logic; concurrent-writer safe; `git add` staging fix; binaries/images/HTML/.env excluded from code-map staging |
| Explainers | **live** | HTML explainers as `asset` nodes; desktop live-edit loop; Tier-2 dynamic-explainer Flask blueprint scaffold (`/pkis-api/x/<name>/`); viz published to local serving copy; render/download/share fixed esp. on mobile |
| Deploy | **live** | one-command deploy script: build + embeddings + graceful reload |
| Comptroller (cost) | **live** | `usage.py` SQLite at `/home/pkis/usage`; per-origin cost; narration logs as `pkis-reader` |
| Ideas log | **live** | `log_idea` tool; entry: OpGraph Strategist — multi-agent strategic council |

## Source / narration coverage

All 11 backlog books **split into per-chapter PDFs** (136 chapters) and 50 papers
downloaded — all viewable. **494 chapters narrated**; resumable `backlog_build.sh`
(Haiku extract → Sonnet voice → Piper TTS), guarded by a self-healing watchdog
(`narration_watchdog.sh`, cron */15) that auto-pauses on API-credit exhaustion and
auto-resumes.

Books split: cassandras-des-intro, tanner, cimiano, gulli (29 ch, Springer-anchor
split), cunningham, carrell, allemang, kroese, nielsen, benzi, lange — plus the
earlier Phase-C set (MacKay, Hastie ESL, AIMA, Gelman, Sutton, Deisenroth, Pearl,
Resnick, Goodfellow, Murphy PML 1&2, Jaynes).

Doc-store additions this cycle: terminalist-bloombergs-last-stand, terminalist-bloombergx27s.
MCP-committed sources: A Mathematical Introduction to Diffusion Models; Language Models
Can Control Their Own Attention. Librarian linked 40+ sources across diffusion model
nodes (DDPM, DDIM, stochastic encoder-decoder), Bayesian inference nodes (intractable
posterior, prior/likelihood/posterior, approximate Bayesian computation, Bayesian
decision analysis, causal-statistical distinction, turning-the-Bayesian-crank),
amortized inference nodes (amortized VI, learned approximate inference, amortized
inference), autoregressive nodes (ARM framework, autoregressive technique), state
estimation nodes (Kalman filter, filtering/prediction/smoothing, robot perception),
autodiff nodes (automatic differentiation, chain rule multivariate, JVP/VJP, vector
calculus, linear algebra), and deep learning nodes (feed-forward NN, deep learning,
deep NN computation graph, universal approximation theorems ×3), plus meta-learning,
semi-supervised learning, hierarchical Bayesian models, multilevel regression, and
recurrent neural networks.

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
  (commit / `git checkout --` / `pull` / push). OpenWiki refresh driver now uses
  rebase-retry to mitigate concurrent-writer conflicts.
- An `app.py` restart drops the claude.ai connector (users must reconnect) —
  minimize restarts; content changes don't need one (cache auto-refresh).

## Most recent session (2026-09-09)

Infrastructure and graph-coverage sprint. **Native app**: UI now loads from the live
server URL, eliminating per-frontend APK rebuilds on content changes. **MCP cache**:
cross-worker cache staleness fixed; reload + download added to writing assets.
**Position paper**: linked to related explainers, cited nodes, and external sources;
org-change framing removed; §7.3 retitled for a mixed audience. **Graph sources**:
two new MCP-committed sources (diffusion models, LLM attention control); two URL
sources doc-stored (terminalist Bloomberg pieces); 40+ librarian link-ops wiring
existing sources into diffusion, Bayesian, amortized inference, autoregressive,
state-estimation, autodiff, and deep-learning nodes. Node count moved 2,974 → 2,978.

## Next priorities

1. Publish the calibration tabs + register as a PKIS asset node.
2. Start exercising discovery feedback to warm the learned prior.
3. Begin OpGraph NED/NER instrumentation — baseline measurements for the six resolution strategies.
4. Log the first doc-drift accept/dismiss decisions to validate that inbox lane.
5. Continue narration build to push chapter count beyond 494.
6. Automate STATUS.md updates (daily cron + post-deploy hook) so this doc stops drifting.
