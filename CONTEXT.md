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
- `tools/` — operational scripts (discovery, reader, ingest, reconcile, comptroller)
- `tests/` — hermetic pytest suite (96 tests: unit / integration / contract), `-m "not live"` default

## Schema Summary
Node types (12): concept, technique, result, framework, problem, principle, source,
hypothesis, research-cluster, asset, bridge-note, discovery-stub.
Relationship predicates (10): prerequisite-of, uses, specializes, generalizes,
extends, applies, instantiates, contrasts-with, analogous-to, illustrated-by.
Epistemic status: coverage (agent-assessed), understanding (human-only), maturity
(agent-proposed). Two-phase write: `create_*_stub` → `staged_id` → `commit_staged_node`.
IRI form: `pkis:{type}:{slug}` as the first frontmatter field.

## Corpus Size (this generation)
~2,793 nodes: concepts 926, techniques 760, sources 561, frameworks 194, results
171, principles 82, problems 42, hypotheses 28, bridge-notes 14, clusters 12,
assets 3, discovery-stubs 0.

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
- bcbb094d docs(roster/phase4): COMPTROLLER.md LIVE; reconcile to deployed reality
- fefe5d6a feat(roster/phase4): wire log_usage into the MCP server + config
- a861a1d6 feat(roster/phase4): usage.py — Comptroller accounting module
- ea25ebe8 docs(roster/phase3): create COMPTROLLER.md
- 9ef1d4bf docs(roster/phase3): Architect v1.1 — merged spec (CONTEXT.md + consistency)
- 57edd8c6 docs(roster/phase2): Synthesizer v2.1 — Mode 5 proposal pass
- 4da86618 docs(roster/phase2): Auditor v2.1 — inbox append
- 1a6f36c4 docs(roster/phase2): Librarian v3.1 — park path + inbox integration
