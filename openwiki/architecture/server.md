# Server Architecture (`app.py`)

`app.py` (~7,400 lines) is a Flask application that serves the wiki through
**three parallel surfaces backed by one shared tool layer**. It's deployed at
`https://pkis.dev`, reading wiki markdown from `WIKI_DIR` (`config.py`).

## Three API surfaces, one tool layer

1. **MCP (JSON-RPC 2.0, Streamable HTTP)** at `POST/GET /mcp` (and a
   session-suffixed `/mcp/<session>` accepted for claude.ai connector
   compatibility — see `app.py:5457-5480`). Handles `initialize`,
   `tools/list`, `tools/call`, `ping`, plus a legacy
   `{"tool": ..., "params": ...}` shorthand. Discovery metadata is served at
   `/.well-known/mcp` and `/.well-known/oauth-protected-resource` (`app.py:5759-5780`).
2. **REST** under `/pkis-api/*` (81 `@app.route` declarations total across the
   file) — backs the React viewer SPA (built assets expected at
   `config.VIEWER_DIST`; the `viewer/` source is **not included** in this
   repository subset).
3. **Direct `tool_*` functions** — ~55 functions (`tool_get_node`,
   `tool_search_wiki`, `tool_create_bridge_note`, `tool_commit_staged_node`,
   etc., `app.py:698-7231`) are the actual implementations. Both MCP dispatch
   and REST routes call the same functions, so behavior only needs to be
   correct once.

### Tool registry and dispatch gate

Tools are declared in three dicts — `READ_TOOLS`, `TRUSTED_TOOLS`,
`WRITE_TOOLS` (`app.py:~5517` onward) — each mapping a tool name to a lambda
that calls the matching `tool_*` function with unpacked params. This registry
is "the single source of truth for MCP dispatch... lifted out of
`dispatch_tool()` so the surface is introspectable" (comment at `app.py:5509`).
Tiers:

- **READ** — open to all callers.
- **TRUSTED** — requires `is_trusted(request)`.
- **WRITE** — requires `is_write_authorized(request)`.

`dispatch_tool()` looks up the tool across all three tables and gates by tier
before invoking it, which is what lets `tests/contract/test_mcp_tools.py`
"freeze" the advertised-vs-dispatchable tool set and catch tools that are
implemented but silently ungated or unreachable.

## Auth model

Four layered identity mechanisms compose to decide `is_trusted` /
`is_write_authorized` / ownership for any given request:

1. **Static bearer tokens** — `PKIS_TRUSTED_TOKEN` (read-tier) and
   `PKIS_MCP_WRITE_KEY` (write-tier), for machine-to-machine callers like
   Claude Code (`config.py` `TRUSTED_TOKEN`/`WRITE_KEY`).
2. **OAuth (JWT)** — dormant until `PKIS_OAUTH_ISSUER` is set
   (`config.OAUTH_ENABLED`). Validates via a JWKS endpoint (`PyJWT`, lazy
   import), resolving role from an allowlist file (`ROLES_PATH`).
   `oauth_identity(req)` (`app.py:273`) is the resolver used everywhere else.
3. **Web sign-in (WorkOS AuthKit)** — dormant until `WORKOS_API_KEY` +
   `WORKOS_CLIENT_ID` + `WORKOS_COOKIE_PASSWORD` are set
   (`config.WEB_AUTH_ENABLED`). Uses a sealed-session cookie
   (`WEB_SESSION_COOKIE = "wos_session"`), validated/refreshed in request
   handling, with **cross-process refresh coalescing via SQLite**
   (`PKIS_AUTH_REFRESH_DB`) so a single-use refresh token isn't burned twice
   by concurrent requests (`app.py:307-314`).
4. **Native app (Capacitor APK)** — dormant unless web auth is configured
   (`config.NATIVE_AUTH_ENABLED = WEB_AUTH_ENABLED`). After a WorkOS login,
   PKIS mints its **own** opaque bearer tokens (access + refresh) and hands
   them to the app via a PKCE-secured one-time-code deep link
   (`com.pkis.app://`), because the app's WebView is served from
   `https://localhost` and can't complete the cookie-based web flow. Tokens
   are stored server-side as SHA-256 hashes only (`config.py:127-142`,
   `app.py` `_native_issue_code` etc.).

`gate_error(tier)` (`app.py:685`) picks the right failure mode: a 401
`OAuthChallenge` (to trigger connector-driven OAuth) when OAuth is enabled and
the caller is anonymous, otherwise a plain 403 — this distinction is tested in
`tests/integration/test_auth.py` ("Seam E"), which asserts gating always
returns well-formed JSON-RPC errors, never a silent 200 or a 500.

Routes: `/pkis-api/auth/login`, `/callback`, `/me`, `/logout`, and the
`native/{start,token,refresh,logout}` family (`app.py:6447-6603`).

## Search subsystem

Hybrid search fuses **lexical (BM25, `rank_bm25`)** and **optional dense
embeddings (`sentence-transformers`, lazy import)** via **Reciprocal Rank
Fusion** (`store.rrf_score`, `k=60` by default). The app degrades gracefully
to BM25-only if `sentence-transformers` isn't installed — this is why it's an
optional dependency (`pyproject.toml`) rather than a base one. Named,
persistable **search profiles** (`DEFAULT_SEARCH_PROFILE` in `store.py`, plus
`tool_set_search_profile`) let the retrieval lab toggle transforms (HyDE,
alias expansion), retrievers, fusion method, rerankers, and filters
per-experiment without code changes. See
[Data & Storage](data-and-storage.md) for the `WikiStore` internals and
[Knowledge Workflows](../domain/knowledge-workflows.md) for how the retrieval
lab uses this.

## Git-backed write path {#git-backed-write-path}

Every write tool (create/edit node, bridge notes, source/resource/finding
stubs, staged-node commits) ultimately calls a consolidated
`_git_commit_and_push` helper that:

- commits the change locally, then attempts to push;
- **never silently swallows a push failure** — it raises `GitPushError` with
  diagnostics, leaving the local commit intact for manual reconciliation;
- is covered by `tests/integration/test_git_persistence.py` ("Seam C"), which
  asserts success, no-op-on-no-changes, and the loud-failure/retained-commit
  behavior.

`tools/reconcile_push.py` is the load-bearing remediation script for when a
push falls behind (diagnoses divergence, recommends an action, and only acts
with an explicit `--confirm` flag — see
[Operations](../operations/tools-and-cron.md)).

New content mostly enters through a **two-phase staging pattern** rather than
landing directly in canonical folders — see
[Curation & Lifecycle](../domain/curation-and-lifecycle.md) for that workflow
and `tests/integration/test_staging_commit.py` ("Seam I").

## Adjacent subsystems inside `app.py`

- **Document ingestion** — uploads, URL saves, podcast/YouTube transcript
  fetching via `adapters.py`, Readwise webhook integration, arXiv/DOI
  resolution, hash-based dedup (`app.py:3893-4424`).
- **Reading queue & reading graph** — `tool_get_reading_queue`,
  `tool_add_to_queue`, `tool_get_reading_graph`, prerequisite/dependency chain
  traversal (`app.py:1160-1329`, `1737-1903`).
- **Discovery / docs-drift / graph-gaps queues** — human-in-the-loop
  accept/reject queues backed by JSON files (`tool_get_discovery`,
  `tool_discovery_act`, `tool_docs_drift_*`, `tool_graph_gaps_*`,
  `app.py:7023-7231`).
- **Reader** — builds an audio/annotated reading experience per source
  (`tool_build_reader`, `app.py:6698`), driven by `tools/reader_build.py`.
- **Tier-2 dynamic explainers** — Flask Blueprint pattern for interactive
  explainers served at `/pkis-api/x/<name>/`, as opposed to static HTML
  (`app.py:7360`, `explainer_x.py`).

## Source map

- `app.py:1-130` — imports, B2-split provenance comments, Flask app + config setup.
- `app.py:260-700` — auth helpers (`oauth_identity`, native token issuance, `is_write_authorized`, `gate_error`).
- `app.py:698-4780` — `tool_*` implementations (read tools, write tools, ingestion).
- `app.py:4780-5760` — write-schema introspection, MCP transport, tool registry + `dispatch_tool`.
- `app.py:5760-7231` — well-known endpoints, viewer REST routes, auth routes, sharing, reader, discovery/drift/gap queues.
- `app.py:7360+` — Tier-2 explainer blueprint wiring.
