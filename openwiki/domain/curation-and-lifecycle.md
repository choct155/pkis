# Curation & Lifecycle

The wiki's stated purpose is that it's "maintained entirely by LLM agents;
the human's role is to source materials, resolve synthesis proposals, and
drain the reading queue" (`SCHEMA.md`). This page covers the machinery that
makes that safe: how new content enters the graph, how it's classified, and
how drift/health is monitored without an agent ever being trusted to silently
rewrite live content.

## Domains and tags: classification axes

- **`domain`** — an open, curated list per node (`SCHEMA.md` "Domains"): six
  *Core* domains (`bayesian-stats`, `deep-learning`, `reinforcement-learning`,
  `causal-analysis`, `knowledge-representation`, `symbolic-subsymbolic`) and
  seven *Extended* domains (`state-space-models`, `time-series`,
  `forecasting`, `microsimulation`, `philosophy-of-science`, `optimization`,
  `information-theory`) — not a hierarchy, just two equally-indexed buckets.
- **`tags`** — a fully open vocabulary for cross-cutting mathematical/
  methodological/epistemic themes (`linear-algebra`, `dynamic-programming`,
  `epistemology`, ...), orthogonal to `domain`.
- In code, `domain` is a first-class filter/facet, not just descriptive
  metadata: `WikiStore.search` accepts a `domains` filter (hybrid search
  scoped to specific domains), `tool_get_index(domain=...)` browses the
  catalog by domain, `tool_get_domains()` aggregates domain→count for the
  viewer's domain facet UI, `tool_get_source_graph(focus_domain=...)`
  restricts the source dependency graph, and the graph-health report computes
  `cross_domain_connections` (edges linking nodes with disjoint domain sets)
  as a structural health signal.
- **Domain values are rarely hand-typed twice.** They're gated in once from
  external metadata (OpenAlex `field`/`subfield` in discovery, see below) or
  **inherited down the provenance chain** — e.g. a staged Finding inherits
  `domain` from its parent Hypothesis (`tool_create_finding_stub`, verified by
  `tests/integration/test_finding_intake.py`), and the same inheritance
  pattern is reused for bridge-note staging. This keeps the taxonomy
  consistent without a central enforcement pass, at the cost of depending on
  the *first* classification (discovery gate or Librarian judgment) being
  correct.

## Discovery: how new sources enter the funnel

`tools/discovery_openalex.py` (🔴 load-bearing, cron'd weekly — see
[Operations](../operations/tools-and-cron.md)) is a **frontier-gated**
proactive discovery pipeline designed for high signal-to-noise by "letting
the wiki BE the filter":

1. **Frontier** — pull the top under-covered, high-inbound concepts (what
   you're trying to learn next) and embed them with the same `bge-small`
   model the server uses.
2. **Seeds** — find existing sources most relevant to that frontier by cosine
   similarity, so expansion starts from material already chosen for ingest.
3. **Expand** — for each seed, query OpenAlex for recent works that *cite* it
   (forward citation expansion — newer work building on existing sources).
4. **Gate** — every candidate must clear relevance (cosine similarity to the
   nearest frontier concept ≥ `tau`), novelty (not already a source or in the
   inbox), and have a real abstract.
5. **Rank** — relevance × citation-authority × recency × frontier-priority.

Survivors are written to `discovery_inbox.json` with a graph-grounded reason.
`tools/discovery_stubs_from_inbox.py` (🟡 supporting, idempotent) then recasts
inbox entries into lightweight `wiki/discovery/` **discovery-stub** nodes
(max two concept links, no reading path — see `SCHEMA.md` "Discovery Stub"),
which a human reviews and either promotes (via Librarian ingest into a full
source node, `promoted: true`) or leaves parked. The discovery view in the
viewer reads `wiki/discovery/` filtered to `promoted: false`.

## Staging lifecycle {#staging-lifecycle}

New knowledge (bridge notes, hypotheses, findings, resource stubs) almost
never lands directly in its canonical folder. Instead it follows a
**two-phase staging pattern**:

1. A write tool (`tool_create_bridge_note`, `tool_create_hypothesis`,
   `tool_create_finding_stub`, `tool_create_resource_stub`, discovery
   promotion, etc.) writes the node into `wiki/staging/` with
   `review_status: pending`, provenance fields (`staged_by`, `staged_id`,
   `staged_at`), and any inherited/derived facets (domain, tags, edges).
2. A human — or `tool_commit_staged_node` — promotes the staged file into its
   canonical folder (`wiki/findings/`, `wiki/hypotheses/`, etc.), at which
   point it becomes visible to search, the index, and graph traversal tools.
3. Downstream monitoring (Lab Assistant, audits — below) only ever inspects
   the *promoted* graph; it never touches the staging gate logic itself.

This is the business-process reason the git write path
(see [Server Architecture](../architecture/server.md#git-backed-write-path))
is built the way it is: every promotion is a real, individually-reviewable
git commit. Test coverage: `tests/integration/test_staging_commit.py`
("Seam I"), `tests/integration/test_finding_intake.py`,
`tests/integration/test_resource_intake.py`.

## Health, drift, and audit monitoring

Three independent, **read-only** monitoring tools watch the promoted graph
without ever asserting truth or editing live content:

- **`tools/lab_monitor.py` (+ `lab_transform.py`)** — the "Lab Assistant."
  Computes a dated, descriptive snapshot (node counts, coverage, hypothesis
  status distribution, cluster health, staged-node throughput), appends it to
  an append-only JSONL store kept *outside* the wiki, and flags drift (idle
  clusters past `LAB_STALE_CLUSTER_DAYS`, staged nodes stuck past
  `LAB_STALE_STAGED_HOURS`, status swings) into `wiki/inbox.md`'s Lab lane for
  a human to drain. Its own spec is explicit and non-negotiable: **descriptive
  only** — it never decides a hypothesis is confirmed/refuted, never writes
  live wiki content, never asserts causality. It's decoupled by design
  (imports only `config`, no Anthropic client, no graph build), so it's cheap
  to schedule and fully testable against any wiki directory. Tested by
  `tests/integration/test_lab_assistant.py`.
- **`tools/architect_audit.py` (+ `architect_reconcile.py`)** — a fortnightly
  LLM-driven documentation-drift auditor. It reads backend code
  (`app.py`, `config.py`, `store.py`, `adapters.py`, `usage.py`, `paths.py`,
  `ask.py`, `conversations.py`) and living docs
  (`docs/ARCHITECTURE.md`, `docs/ABOUT.md`, `docs/USAGE.md` — not present in
  this repo subset) and emits **atomic, individually-acceptable** drift items
  — never one monolithic rewrite — each a single anchor→replacement edit,
  surfaced in the owner inbox's Docs-drift lane for accept/dismiss.
- **`tools/graph_audit.py`** — structural graph audits (e.g. missing IRIs,
  malformed edges) — the Auditor role described in `SCHEMA.md` ("flags
  near-duplicates," "flags any node without `id`").

## Sharing and cost accounting

- **Sharing** (`shares.py`) is covered in
  [Knowledge Workflows](knowledge-workflows.md) since it's primarily a
  read-access product feature.
- **Usage/cost accounting** (`usage.py`, the "Comptroller," Roster Phase 4) is
  the cost-governance layer underneath *every* LLM-calling workflow above
  (discovery, ask, lab monitoring is LLM-free, audits, reader build). It's a
  small, dependency-free (stdlib-only) module with two callers:
  `app.py` (`log_usage()` after every Claude API call — explicitly
  **best-effort**, since "a logging failure must NEVER break a tool call")
  and `tools/comptroller.py` (reads the same SQLite store to produce cost
  reports on a cron cadence — see
  [Operations](../operations/tools-and-cron.md)). The SQLite schema
  (`usage_events`, `budget_periods`, `config`) tracks input/output/cache
  tokens per call, computes cost **at emission time** (no retro-pricing if
  rates change later), and seeds default per-model-family pricing
  (`_DEFAULT_CONFIG`, e.g. Sonnet/Opus/Haiku input/output/cache rates) plus a
  monthly plan budget (`max_plan_monthly_usd`) and billing-cycle anchor.
  Tested by `tests/unit/test_usage.py`, `tests/unit/test_comptroller.py`,
  `tests/integration/test_usage_instrumentation.py`.

## Source map

- `SCHEMA.md` "Domains", "Tags", "Discovery Stub" — canonical taxonomy spec.
- `tools/discovery_openalex.py:1-24` — discovery pipeline design rationale.
- `tools/discovery_stubs_from_inbox.py` — inbox → discovery-stub conversion.
- `tools/lab_monitor.py:1-19` — Lab Assistant posture and scheduling.
- `tools/architect_audit.py:1-24` — doc-drift audit design.
- `usage.py:1-84` — Comptroller schema and pricing model.
- `tests/integration/test_finding_intake.py`, `test_staging_commit.py`, `test_lab_assistant.py` — lifecycle test coverage.
