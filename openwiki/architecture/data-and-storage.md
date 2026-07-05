# Data Model & Storage

## The knowledge graph data model

The canonical spec is [`/SCHEMA.md`](../../SCHEMA.md) — read it directly for
full frontmatter templates and predicate-interpretation tables. Summary of
what matters for changing code:

- **Nodes are markdown files with YAML frontmatter**, organized into
  type-specific folders under `WIKI_DIR` (`config.KNOWLEDGE_DIRS`):
  `concepts/`, `techniques/`, `results/`, `frameworks/`, `problems/`,
  `principles/`, `sources/`, plus infrastructure folders `hypotheses/`,
  `clusters/`, `assets/`, `bridge-notes/`, `discovery/`, `findings/`,
  `resources/`. `config.FOLDER_TO_TYPE` / `TYPE_TO_FOLDER` map folder name ↔
  `knowledge_type` value.
- **Knowledge nodes** (concept, technique, result, framework, problem,
  principle) answer a distinct question each ("what IS this" vs. "how do I DO
  this" vs. "what do we KNOW", etc. — see the table in `SCHEMA.md`) and carry a
  `component_scores` dict of **human-maintained-only** mastery dimensions
  (e.g. a technique tracks `operational_mechanism`, `principled_mechanism`,
  `conditions`, `implementation`, `diagnostics`, `alternatives`,
  `failure_modes`, each 1-5 or `null`). Agents must never write
  `component_scores` or `understanding` — only `coverage` and `maturity` are
  agent-writable epistemic fields.
- **Infrastructure nodes** (hypothesis, research-cluster, asset, bridge-note)
  plus `discovery-stub`, `finding`, `resource` support the operational
  lifecycle (see [Curation & Lifecycle](../domain/curation-and-lifecycle.md))
  and do not carry `component_scores`.
- **Identity**: every node has a stable IRI `pkis:{knowledge_type}:{slug}`,
  assigned once at creation and never reused (`SCHEMA.md` "IRI Identity"). An
  `aliases` list on each node feeds a flat `alias → IRI` registry built at
  server startup for string-based concept resolution (`tool_resolve_concept`,
  `tool_detect_concepts`).
- **Edges** are typed wikilinks in a node's `## Connections` section, using
  one of 8 core predicates (`specializes`/`generalizes`, `prerequisite-of`,
  `uses`, `contrasts-with`, `extends`, `grounds`, `equivalent-in-context`,
  `commonly-confused-with`) plus a few operational predicates
  (`evidence-for`, `implemented-by`, `superseded-by`). Predicate meaning
  depends on the (subject-type, object-type) pair — see `SCHEMA.md`'s
  interpretation tables before adding a new edge type.
- **Domains and tags** are two orthogonal, open-vocabulary classification
  axes — see [Curation & Lifecycle](../domain/curation-and-lifecycle.md) for
  how `domain` is operationalized in code.

## `WikiStore` (`store.py`)

`store.py` is the in-progress extraction target for the data layer (the "B2
split" — see the module docstring). It currently owns:

- **Pure IRI/slug helpers**: `slug_from_path`, `iri_from_slug`, `parse_iri`
  (moved first because they have no dependency on mutable `WIKI_DIR` state —
  covered by `tests/unit/test_iri_resolution.py`, "Seam F").
- **`rrf_score(rank, k=60)`** — the Reciprocal Rank Fusion weight function
  used to combine lexical and dense retrieval rankings.
- **`DEFAULT_SEARCH_PROFILE`** — the baseline hybrid-search configuration
  (lexical + dense retrievers, RRF fusion `k=60`, 3x candidate pool per
  retriever, no rerankers/transforms) that "reproduces the pre-pipeline
  `hybrid_search` behavior exactly." Named profiles created via
  `tool_set_search_profile` shallow-merge over this default
  (`merge_search_profile`).
- **`WikiStore` class** — loads and parses nodes (via `python-frontmatter`)
  keyed by IRI; builds a `networkx.DiGraph` from frontmatter edges (weighted
  per `config.EDGE_WEIGHTS`, e.g. `prerequisite-of` = 1.0, `contrasts-with` =
  0.2) plus inline `[[wikilinks]]`; maintains a BM25 index (`rank_bm25`) and
  an optional disk-cached dense embedding index
  (`config.EMBED_MODEL_NAME`, default `BAAI/bge-small-en-v1.5`, cached at
  `config.EMBED_CACHE_PATH`). Caches are invalidated selectively
  (`invalidate_nodes/_graph/_search`) after writes, and a freshness check
  (content-signature comparison) picks up changes made by other worker
  processes without requiring a restart — this is what
  `tests/integration/test_cache_freshness.py` ("Seam D") verifies.
- Node loading/alias resolution that depend on the mutable `WIKI_DIR` are
  slated to move into `store.py` in a later increment per the module
  docstring — check the docstring's dated notes before assuming this file is
  "done."

`EDGE_WEIGHTS` (`config.py`) is the structural-ranking table used when
traversing the graph (e.g. `tool_get_related`, `tool_get_dependency_chain`,
`tool_path_between`); `tests/unit/test_search_fusion.py` asserts it stays
complete relative to the predicates in use.

## `adapters.py` — external API fetchers

Pure fetch functions for enrichment/ingestion, imported into `app.py` via
`from adapters import *` (their `__all__` controls what becomes an app-module
global — this matters because contract tests monkeypatch these names on
`app.<fetcher>`, not on `adapters.<fetcher>`). Covers:

- Academic metadata: arXiv, CrossRef, Semantic Scholar.
- Readwise Reader integration (source status sync, webhook payloads).
- Podcast/video transcript sources: YouTube (oEmbed + captions), PodcastIndex,
  Listen Notes, Podchaser.

These back the document-ingestion routes in `app.py`
(`tool_save_url_source`, `tool_save_podcast_source`, the Readwise webhook
handler) — see [Server Architecture](server.md) for where ingestion sits in
the route map.

## Two-phase write pattern

Writes that create new knowledge (bridge notes, hypotheses, findings,
resource stubs, discovery promotions) are staged into `wiki/staging/` or
`wiki/discovery/` with `review_status: pending` and provenance metadata before
being promoted into their canonical folder. This is documented in full in
[Curation & Lifecycle](../domain/curation-and-lifecycle.md#staging-lifecycle)
since it's a business-process concern as much as a storage concern; the git
mechanics underneath it are covered in
[Server Architecture → Git-backed write path](server.md#git-backed-write-path).

## Source map

- `SCHEMA.md` — canonical schema reference (read directly, not duplicated here).
- `store.py:1-60` — module docstring (extraction status), `rrf_score`, `DEFAULT_SEARCH_PROFILE`, `merge_search_profile`.
- `config.py:43-96` — `KNOWLEDGE_DIRS`, `FOLDER_TO_TYPE`/`TYPE_TO_FOLDER`, `COMPONENT_SCORES_BY_TYPE`, `EDGE_WEIGHTS`.
- `adapters.py` — external fetchers (arXiv/CrossRef/Semantic Scholar/Readwise/podcast APIs), exported via `__all__`.
- `tests/unit/test_store.py`, `test_iri_resolution.py`, `test_search_fusion.py` — data-layer unit coverage.
