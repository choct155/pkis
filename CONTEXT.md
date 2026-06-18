# PKIS Context
Generated: 2026-06-18 by Architect v1.1
Do not edit — regenerated automatically (see ARCHITECT.md § CONTEXT.md Generation Workflow)

PKIS (Personal Knowledge Integration System) is a markdown/NetworkX knowledge graph
served over an MCP + REST API, with a PWA viewer. This file is the session primer:
read it before engaging with PKIS. It is generated from ground truth, never
hand-edited.

## Infrastructure
- Graph backend: markdown nodes + NetworkX (frontmatter files under `wiki/<type>/`)
- MCP server: https://pkis.dev/mcp (OAuth via WorkOS AuthKit) — Flask app, gunicorn
  `pkis-mcp.service`, 40 advertised tools
- REST + viewer: https://pkis.dev/app (React/Vite PWA), `/pkis-api/*`
- VPS: Hetzner; deploy = 15-min cron `git pull origin main` + restart on new HEAD
- Repo: github.com/choct155/pkis (public) — one repo holds app, docs, and wiki nodes
- Usage accounting: SQLite at `/home/pkis/usage/usage.sqlite` (Comptroller)

## Repo Structure (code)
- `app.py` — Flask monolith: MCP JSON-RPC, REST routes, all `tool_*` handlers
- `config.py` — env constants + static lookup tables (the B2 split)
- `store.py` — `WikiStore`, the dependency-injected cache/graph/search container
- `adapters.py` — external-API fetchers (arXiv, Crossref, Readwise, podcasts)
- `usage.py` — Comptroller cost model + best-effort `log_usage`
- `paths.py` — single source of truth for repo + operational filesystem paths (B4)
- `tools/` — operational scripts (discovery, reader, ingest, reconcile, comptroller)
- `tests/` — hermetic pytest suite (113 tests: unit / integration / contract), `-m "not live"` default; viewer has vitest (`api.ts` contract)

## Schema Summary
Node types (12): concept, technique, result, framework, problem, principle, source,
hypothesis, research-cluster, asset, bridge-note, discovery-stub.
Relationship predicates (10): prerequisite-of, uses, specializes, generalizes,
extends, applies, instantiates, contrasts-with, analogous-to, illustrated-by.
Epistemic status: coverage (agent-assessed), understanding (human-only), maturity
(agent-proposed). Two-phase write: `create_*_stub` → `staged_id` → `commit_staged_node`.
IRI form: `pkis:{type}:{slug}` as the first frontmatter field.

## Corpus Size (this generation)
~2,807 nodes: concepts 926, techniques 760, sources 561, frameworks 194, results
171, principles 82, problems 42, hypotheses 28, discovery-stubs 15, bridge-notes 14,
clusters 12, assets 3.

## Active Research Context
Hypothesis clusters (12): composite-credibility, compositional-query-grounding,
embedding-ontology-alignment, evaluation-infrastructure, intensional-grounding,
learned-symbol-grounding, model-evolution, ontological-coverage-planning,
parsed-intent-calibration, research-instrumentation, retrieval-inference-tradeoff,
structured-validation-truth-discovery.
Reading priority: frontier-driven (fit²-dominant), browse the live Priority view at
pkis.dev/app — not statically tracked here.

## Agent Roster
| Agent | Version | Schedulable | Role |
|---|---|---|---|
| Librarian | 3.1 | on-demand | Ingest sources; `park` → discovery-stub; inbox append |
| Synthesizer | 2.1 | weekly | Deepen nodes, find connections; Mode 5 async proposal pass |
| Auditor | 2.1 | fortnightly | Graph health checks; inbox gaps + conformance |
| Hygienist | 2.0 | weekly | Schema conformance (Checks 1–9), report-only |
| Architect | 1.1 | weekly | System self-knowledge; CONTEXT.md + cross-agent consistency |
| Comptroller | 1.1 | daily/weekly/monthly | API cost accounting (LIVE; non-LLM script) |

All agents append to `wiki/inbox.md` (swim lanes: Discovery, Proposals, Staged,
Structural Gaps, Awaiting Classification, Conformance, Budget); only the human
removes items. The Auditor's `## Structural Gaps` lane is the Synthesizer's
proposal-pass work queue.

## Boundary Constraints
- PKIS↔IKS: strict — no raw IKS data in the PKIS graph.
- PKIS↔ARS: porous — PKIS is the ARS knowledge substrate.
- ARS↔IKS: strict.

## Recent Structural Changes (last 8)
- 26563298 docs(structural): reconsider B3 (intent-met) + C-3 (deferred)
- a0531e1b feat(comptroller): scheduled budget alert via queue file + Auditor fold-in
- 3ca54352 feat(roster/phase1c): 15 discovery-stub nodes from discovery_inbox.json
- 3219907b feat(comptroller): Claude Code transcript ingest (dedup by requestId)
- f617b394 feat(B4): paths.py SSOT + instrument tools/ scripts for cost tracking
- ddaf985e feat(roster/phase5): generate CONTEXT.md
- bcbb094d docs(roster/phase4): COMPTROLLER.md LIVE
- fefe5d6a feat(roster/phase4): wire log_usage into the MCP server + config
