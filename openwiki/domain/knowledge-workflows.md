# Knowledge Workflows: Asking the Wiki Things

This page covers the product surface a human (or agent) uses to *interrogate*
the knowledge graph — as opposed to writing to it, which is covered in
[Curation & Lifecycle](curation-and-lifecycle.md). It's the "read side" of the
personal-knowledge-wiki product.

## The "ask brain" (`ask.py`)

`ask.py` implements one agentic **retrieve → traverse → cite** loop, shared by:

- the viewer's Ask view — `POST /pkis-api/ask`;
- the MCP `ask_pkis` tool (planned/later phase per the module docstring).

Design points worth knowing before touching this file:

- **Stateless engine.** The caller passes the full multi-turn message history
  on every call; the viewer holds conversation state client-side (persistence
  across sessions is a separate concern — see Conversations below).
- **Read tier only, by design.** The loop gives the model four tools:
  `search_wiki`, `get_node`, `get_related`, `get_dependency_chain`. Owner
  agentic writes from within `ask` are an explicit later phase, not yet built.
- **Answers must be grounded strictly in retrieved nodes**, cited as
  `[[slug]]` wikilinks that the viewer renders as live links — the system
  prompt (`ask.py:45+`) explicitly forbids answering from the model's own
  prior knowledge.
- **Eager preload (`PRELOAD_K = 8`)**: before the first model call, the loop
  runs the same hybrid search the model could call itself and injects the
  top-K nodes into the prompt. On a small graph this collapses most questions
  from ~3 serial model calls to one, since serial call count dominates
  wall-clock latency — a deliberate cost/latency optimization, not just a
  convenience.
- **Bounded loop**: `MAX_TOOL_TURNS = 8` is a backstop against a model that
  keeps searching without answering; `_NODE_CONTENT_CAP = 8000` caps how much
  of a single node's body is fed back per `get_node` call so a few fat nodes
  can't blow context/cost.
- **Default model**: `claude-sonnet-4-6` (`DEFAULT_MODEL`) — "fast and cheap
  enough for an interactive loop... matches the discovery/reader pipelines."
- `app` is imported **lazily inside functions** to avoid a circular import
  (`app.py` imports `ask` at module load to wire the route).

## Saved conversations (`conversations.py`)

SQLite-backed, per-user persistence (keyed by WorkOS `sub`) for the ask
transcripts the viewer renders — role/content/citations/metadata per turn.
Auto-saved, soft-deletable, and **append-only** (chat turns don't need version
history, unlike documents a conversation might be authoring in a future
"studio" companion — `artifact`/`anchor_*` columns are reserved for that
without needing a migration later). Pure stdlib, no Flask/Anthropic import, so
it's independently unit-testable and mirrors `usage.py`'s store style.

## Sharing (`shares.py`)

Capability-link sharing: an unguessable token (`secrets.token_urlsafe`) grants
**read-only public access** to one owned item (currently conversations; nodes
and studio docs planned to reuse the same mechanism). Possession of the token
*is* the authorization — no account needed to view. Owners can revoke, and
links may carry an optional expiry. `shares.py` deliberately knows nothing
about the shared item's content: it only maps `token → (kind, ref, owner)`;
the REST endpoint resolves the token, then fetches content through the item's
own store, scoped to `owner_sub`.

## The retrieval lab: `experiments.py` + `metrics.py`

Together these implement an internal **A/B evaluation harness** for search and
ask quality:

- **`experiments.py`** — an append-only SQLite log, one row per
  `(query, profile)` execution. Rows sharing a `comparison_id` render as
  columns side-by-side in the lab UI. Each row captures the query, the
  resolved search profile, `corpus_head` (git HEAD at run time, for
  reproducibility), computed metrics, a per-stage trace, retrieval/eval cost
  split out, and a compact result payload. A `query_log` table underlies a
  **standing-eval loop**: every deliberate owner query becomes a persisted
  test case that a nightly runner (`tools/nightly_eval.py`) replays through
  the full profile suite, so retrieval regressions/improvements are tracked
  over time rather than eyeballed once.
- **`metrics.py`** — the cheap, **reference-free** subset of what its
  docstring calls the "Multidimensional Retrieval Quality Framework"
  (presumably documented as a `framework:` node in the wiki itself — not
  present in this code subset): `structural_coherence` (does the retrieved
  set form a connected subgraph over typed edges?), redundancy/diversity (a
  proxy for concision), and groundedness (embedding-alignment proxy for
  whether generated text is supported by retrieved node text). These need no
  human-labeled relevance judgments (`C(q)`) and no LLM call, unlike the
  deeper metrics gated behind the `deep_metrics` search-profile toggle
  (see `store.DEFAULT_SEARCH_PROFILE` in
  [Data & Storage](../architecture/data-and-storage.md)). Pure functions
  (numpy + networkx in, plain dicts out) — callers own embedding/graph
  construction so this module stays dependency-light and unit-testable.

Related tools: `tools/lab_monitor.py`/`tools/lab_transform.py` (descriptive
health snapshots over hypotheses/clusters, not retrieval quality — see
[Curation & Lifecycle](curation-and-lifecycle.md)), `tools/search_harness.py`,
`tools/nightly_eval.py`. Tests:
`tests/unit/test_retrieval_lab.py`, `tests/unit/test_search_fusion.py`.

## Dynamic explainers (`explainer_x.py`)

A graduated model for interactive visual explainers attached to `asset` nodes,
per the (not-included) `EXPLAINER_WORKFLOW.md`:

| Tier | What it is |
|---|---|
| 0/1 | Static self-contained HTML under `wiki/assets/viz/<slug>.html` — the default |
| 2 | **This module** — a Flask Blueprint mounted at `/pkis-api/x/<name>/` (registered under the existing reverse-proxied `/pkis-api` prefix, so no nginx change is needed) for explainers that need server-side action: persistence, heavier compute, secrets, or auth-gated writes |
| 3 | A separate proxied service — only once an explainer outgrows the monolith |

Promoting an explainer from static to dynamic is a **metadata change, not a
rewrite**: give its asset node a `viz_url: /pkis-api/x/<name>/` frontmatter
field instead of `viz: <static-slug>`; `tool_get_assets` honors an explicit
`viz_url` and the viewer hosts it identically via iframe either way.
`register(app, is_write_authorized=..., log_usage=...)` injects the main app's
auth/usage hooks so dynamic explainers reuse Comptroller logging and WorkOS
auth rather than reimplementing them.

## Source map

- `ask.py:1-60` — module docstring, system prompt, tuning constants (`MAX_TOOL_TURNS`, `PRELOAD_K`, `_NODE_CONTENT_CAP`).
- `conversations.py:1-30` — schema and design rationale for chat persistence.
- `shares.py:1-50` — token model and schema.
- `experiments.py:1-50` — experiments/query_log schema.
- `metrics.py:1-40` — reference-free metric functions.
- `explainer_x.py` — Blueprint registration pattern.
- `tests/unit/test_retrieval_lab.py`, `test_search_fusion.py` — lab/search coverage.
