# PKIS Architecture Audit

**Phase 1 (Reconnaissance) artifact.** Read-only. No code was modified to produce
this document. Cites `file:line` against the tree as of branch `main`,
commit `04f8d685`.

Scope: the executable code surfaces — `app.py`, `tools/`, `scripts/`, and
`viewer/`. The wiki content tree (`wiki/**`, ~2800 markdown nodes) is data, not
code, and is out of scope except where the code's contract with it is a failure
surface.

---

## 0. Executive summary

PKIS is a single 6,467-line Flask module (`app.py`) serving **three distinct
surfaces** from one process, plus a React/Vite PWA (`viewer/`) and a loose
collection of operational/one-shot Python scripts (`tools/`, `scripts/`). It is
functional and in production at `pkis.dev`. There are no known active bugs.

The structural risks that matter most for the upcoming IKS build, in priority
order:

1. **No dependency manifest exists anywhere in the repo.** No `requirements.txt`,
   `pyproject.toml`, or lockfile. The runtime environment is reconstructable only
   from `/home/pkis/venv` on the live VPS. This blocks reproducible CI and is the
   single biggest obstacle to Phase 4.
2. **The MCP contract drifts from itself.** 28 tools are advertised via
   `tools/list`; 42 are actually dispatchable. 14 tools are reachable but
   invisible (§2).
3. **Two parallel write surfaces** (MCP `dispatch_tool` and REST `/pkis-api/*`)
   call the same `tool_*` functions through **different auth gates**, and neither
   is covered by a test (§7, Seam A/B).
4. **Git-persistence logic is copy-pasted** across at least three write paths
   with subtly different error handling (§7, Seam C).
5. **Zero automated tests** in the entire repo — Python or TypeScript — and no CI.

None of these is an emergency. All of them get more expensive to fix once IKS is
reading and writing against the same surfaces.

---

## 1. Component map

### 1.1 `app.py` — the monolith (6,467 lines)

One Flask app. It does **not** exceed one *deployment* responsibility, but it far
exceeds one *module* responsibility. Distinct concerns currently co-resident in
the single file:

| # | Concern | Representative lines | Should it be one module? |
|---|---------|----------------------|--------------------------|
| 1 | Config / env loading | 36–204 | yes (its own `config.py`) |
| 2 | Node load + IRI/slug/alias resolution | 235–383 | yes (`store.py`) |
| 3 | Graph build (NetworkX from frontmatter) | 384–441, 576–617 | yes (`graph.py`) |
| 4 | Search: BM25 + dense embeddings + RRF fusion | 442–702 | yes (`search.py`) |
| 5 | Auth: static key, OAuth JWT, WorkOS web session | 703–892 | yes (`auth.py`) |
| 6 | Tool implementations (`tool_*`, ~40 functions) | 893–4660 | yes — split by domain |
| 7 | External-API adapters (arXiv, CrossRef, S2, Readwise, podcast, YouTube) | 1928–2036, 3147–4357 | yes (`adapters/`) |
| 8 | Git persistence | 3348–3368 + inline copies | yes (`persistence.py`) |
| 9 | MCP JSON-RPC transport + dispatch | 4898–5693 | yes (`mcp.py`) |
| 10 | Viewer REST API (`/pkis-api/*`, ~35 routes) | 5731–6450 | yes (`rest.py`) |
| 11 | Docs/webhook/health/reader routes | 4664–4897, 5951–6068 | yes |

**Single biggest scope violation:** concerns 6, 7, and 8 are interleaved — a
`tool_*` function will parse input, call an external API, mutate a file, *and*
shell out to git inline, all in one body (e.g. `tool_edit_node` 2572–2662,
`tool_save_podcast_source` 4358–4577). This is what makes the file hard to test
in isolation.

The `tool_*` naming convention is consistent and is the file's saving grace: it
makes the MCP surface mechanically enumerable (used in §2).

### 1.2 `viewer/` — React/Vite/TypeScript PWA

Clean for its size. 9 views + 19 components, no store (prop-drilling from
`App.tsx` + per-view `useAsync`). Largest units: `DetailSheet.tsx` (444 lines),
`ReaderView.tsx` (328). Both are large-but-cohesive (one feature each). The
frontend's entire contract with the backend is `viewer/src/lib/api.ts` (273
lines, ~31 endpoint wrappers) — a clean, single choke point. Auth is a WorkOS
sealed-session cookie; the frontend never handles tokens (`credentials:
'same-origin'`). **No tests, no test tooling.**

### 1.3 `tools/` + `scripts/` — operational & one-shot scripts

Two populations mixed in one directory:

- **Operational dependencies** (invoked by `app.py` or cron):
  `reader_build.py` (via REST `pkis_api_reader_build`, app.py:6058, and shell
  wrappers), `scripts/build_source_graph.py` (via `tool_rebuild_source_graph`,
  app.py:1652), `discovery_openalex.py` (cron, Mondays),
  `mine_proposals.py` + `mackay_phasec_driver.py` (Phase-C ingest pipeline).
- **One-shot / migration**: `book_outline.py`, `book_setup.py`, `book_split.py`,
  `import_drive_books.py`, `reader_split_book.py`, `scripts/iri_backfill.py`,
  `build_reader_blei.py` (a hardcoded single-paper specimen).

There is no separation (e.g. `tools/oneshot/` vs `tools/ops/`) signalling which
scripts are load-bearing. See §4 and §5.

---

## 2. MCP surface inventory

This is the contract Phase 2 must pin down. The canonical source is
`_get_tools_list()` (app.py:5013–5376) for *advertised* tools and the three
dispatch dicts in `dispatch_tool()` (app.py:5506–5679) for *reachable* tools.

**They do not match: 28 advertised, 42 dispatchable.**

### 2.1 Advertised AND dispatchable (the intended public contract)

Read tier (no auth): `get_write_schema`, `search_wiki`, `get_node`,
`resolve_concept`, `detect_concepts`, `get_related`, `add_to_queue`,
`get_reading_queue`, `get_concept_frontier`, `get_health_metrics`,
`get_sourceless_stubs`, `get_reading_graph`, `get_staged_nodes`,
`get_transcript_queue`, `list_documents`.

Write tier (`PKIS_MCP_WRITE_KEY` / OAuth owner|writer / web session):
`create_bridge_note`, `log_idea`, `create_source_stub`, `create_node_stub`,
`create_hypothesis`, `edit_node`, `add_connections`, `commit_staged_node`,
`rebuild_source_graph`, `upload_document`, `save_url_source`,
`save_podcast_source`, `set_priority_config`.

### 2.2 Dispatchable but NOT advertised — "hidden" tools (14)

These are callable over `/mcp` but absent from `tools/list`, so no compliant MCP
client can discover them. Each is a latent contract with no published schema:

```
build_reader                    get_index
check_alias_collision           get_node_stub
get_assets                      get_operational_references
get_cluster_priorities          log_operation            (trusted tier)
get_clusters                    register_operational_reference (trusted tier)
get_concept_operational_load    resolve_or_detect
get_dependency_chain            search_wiki_index
```

Most are read-tier conveniences also exposed via REST (e.g. `get_clusters`,
`get_index`, `get_assets`). Two are the **only** members of the trusted tier
(`register_operational_reference`, `log_operation`, app.py:5573–5586) and exist
solely for an external "mnemon" system — they are dispatchable but undocumented
and untested.

**Finding F-1 (contract):** advertised ≠ dispatchable. A single test asserting
`set(advertised) ⊆ set(dispatchable)` and a deliberate allow-list for the
hidden-on-purpose tools would freeze this drift. This is the cheapest high-value
test in the whole plan.

### 2.3 Tier / gating note

- `set_priority_config` is **advertised with a read-flavored description** but
  lives in `write_tools` (app.py:5640) — it requires write auth. Minor
  description/placement mismatch worth noting in contract tests.
- Gating happens in `dispatch_tool` (app.py:5681–5692): read = open,
  trusted = `is_trusted`, write = `is_write_authorized`. Errors flow through
  `gate_error` → `OAuthChallenge` (401 + `WWW-Authenticate`) when OAuth is on and
  caller is anonymous, else `PermissionError` (403).

### 2.4 Transport surface

- `/mcp` and `/mcp/<path:session>` (app.py:5446–5447) — both route to the same
  handler; the session segment is accepted and ignored (stateless server).
- JSON-RPC 2.0 path (`handle_jsonrpc`, 5379) **and** a legacy `{"tool","params"}`
  path (5484–5491) coexist on the same endpoint. The legacy path skips the
  JSON-RPC error envelope. Two input contracts, one set of tools.
- Manifest at `/.well-known/mcp` (5699) re-serves `_get_tools_list()`, so it
  inherits the same 28-tool view.

---

## 3. Dependency graph

### 3.1 Internal Python imports

The codebase is **flat** — there is no package; every `.py` is a top-level
module. Internal import edges:

```
reader_build.py        ──imports──> app  (app.py:39, reuses anthropic_client, paths, graph)
reader_split_book.py   ──imports──> reader_build
fill_missing.py        ──imports──> mackay_phasec_driver
app.py                 ──subprocess──> reader_build.py        (tool_build_reader / _maybe_autobuild_reader)
app.py                 ──subprocess──> scripts/build_source_graph.py (tool_rebuild_source_graph, 1652)
```

**Finding F-2 (coupling cycle):** `reader_build.py` imports `app` at module load
(app.py:39 in the agent's reading), while `app.py` shells out to
`reader_build.py` as a subprocess. It is not a Python import cycle (the back-edge
is a subprocess), but it is a real bidirectional dependency: importing
`reader_build` executes `app.py`'s module body (Flask app construction, client
init). Any unit test that imports `reader_build` pays the full `app` import cost
and side effects. Flag for the test-fixture design in Phase 2.

No internal module imports more than one other internal module, so the "imports
>3 internal modules" complexity flag does not fire at the file level. **The
coupling is intra-file, inside `app.py`**, not inter-file.

### 3.2 Third-party dependencies (actually imported)

Collected from `import`/`from` across `app.py`, `tools/`, `scripts/`:

| Package | Used by | Notes |
|---------|---------|-------|
| `flask` | app.py | core |
| `pyyaml` (`yaml`) | app.py, build_source_graph | frontmatter + graph |
| `python-frontmatter` (`frontmatter`) | app.py | node parsing |
| `networkx` | app.py | graph |
| `numpy` | app.py, discovery_openalex | vector math |
| `rank_bm25` | app.py | keyword search |
| `anthropic` | app.py, reader_build, mine_proposals, discovery_openalex | LLM calls |
| `sentence-transformers` | app.py (lazy), discovery_openalex | dense search; **optional** (graceful degrade, app.py:63–67) |
| `beautifulsoup4` (`bs4`) | reader_build | HTML scrape |
| `pypdf` | book_*, reader_build, reader_split_book, section_pages | PDF |
| `lameenc` | reader_build | MP3 |
| `gdown` | import_drive_books | Drive import |
| `PyJWT[crypto]` (`jwt`) | app.py (lazy, 716/723) | OAuth — **optional** |
| `workos` | app.py (lazy, 779) | web session — **optional** |
| `cryptography` (`Fernet`) | app.py (194–200) | validates cookie key |

`piper` and `ffmpeg`/`ffprobe` are external binaries invoked via subprocess, not
pip deps. The "optional, lazily imported" packages (`sentence-transformers`,
`jwt`, `workos`) are a deliberate design so the app boots in a minimal env — this
is good and must be preserved when a manifest is finally written (they belong in
an `extras`/optional group, not the base requirements).

---

## 4. Dead-code candidates

Flagged for human review only — **not** for deletion. Some are intentionally
dormant.

| Candidate | Location | Evidence | Assessment |
|-----------|----------|----------|------------|
| `rebuildGraph()` | viewer api.ts:246 | no importer in `viewer/src` | exported, unused in UI |
| `saveUrl()` | viewer api.ts:237 | no importer in `viewer/src` | backend route exists; UI never calls it |
| `detectConcepts()` | viewer api.ts:251 | no importer in `viewer/src` | backend route exists; UI never calls it |
| `build_reader_blei.py` | tools/ | hardcoded single-paper specimen; superseded by generalized `reader_build.py` | likely obsolete; confirm Blei reader is rebuilt the general way |
| `book_split.py` | tools/ | overlaps `reader_split_book.py`; the "dumb map" variant | possibly superseded; complementary at best |
| trusted-tier tools | app.py:5573–5586 | `register_operational_reference`, `log_operation` serve an external "mnemon" system not present in repo | dormant by design — confirm mnemon still planned |
| `search_wiki_index` / `get_node_stub` | app.py dispatch | hidden tools, unclear callers | confirm any client depends on them |

No Python function-level dead-code sweep was run exhaustively (would require an
AST pass); the candidates above are the high-signal ones surfaced during the
read. A systematic `vulture`-style pass is a Phase-3 option.

---

## 5. Hardcoded configuration

`app.py` is generally **well-behaved**: nearly everything is `os.environ.get(...)`
with a default (config block 36–204). The hardcoding problem lives almost
entirely in `tools/` and `scripts/`.

### 5.1 In `app.py` (low severity — defaults, overridable)

- Production paths as *defaults*: `/home/pkis/pkis-wiki/...` (40–47, 101, 164).
  Overridable via env, so fine for prod; awkward for local/CI (no fixture root).
- `github.com/choct155/pkis` baked into returned URLs (e.g. edit_node 2661,
  and source-graph/return payloads). User-specific; would need templating for
  any fork/multi-tenant use.
- Model IDs as literals scattered in tools (below), not centralized.

### 5.2 In `tools/` + `scripts/` (higher severity — no env fallback)

| Value | File:line | Remediation |
|-------|-----------|-------------|
| `/home/pkis/...` absolute paths (wiki, docs, proposals, venv) | nearly every script | derive from a shared `PKIS_ROOT` env or a single `paths.py` |
| `choct155@gmail.com` (OpenAlex polite-pool mailto) | discovery_openalex.py:56 | env var |
| `http://127.0.0.1:5000` (localhost API/MCP) | discovery_openalex.py:54, mackay_phasec_driver.py:27 | env var |
| `claude-sonnet-4-6` / `claude-haiku-4-5` model IDs | reader_build.py:41–42, mine_proposals.py:30, discovery_openalex.py:39 | central `MODELS` config |
| `BAAI/bge-small-en-v1.5` | discovery_openalex.py:57 (and app.py:54 as env default) | share with app's `EMBED_MODEL_NAME` |
| Piper binary + voice paths | run_build.sh:10–11, book_extract_batch.sh:10–11 | env |
| Tuning constants (`N_FRONTIER`, `FROM_YEAR`, `LAMBDA`, `MIN_EDGE_WEIGHT`, …) | discovery_openalex.py:60–78, section_pages.py:54, build_source_graph.py:54–55 | acceptable as module constants; document them |

**Finding F-3:** the `/home/pkis/` assumption is repo-wide in the scripts and is
the reason none of them can run in CI or a fresh checkout without edits. A single
`PKIS_ROOT`-derived paths module would unblock testability for the operational
scripts.

---

## 6. Dependency audit

**Finding F-4 (blocking for CI):** there is **no declared dependency set**. The
only file matching `requirements*` is a false positive (`tools/book_setup.py`).
No `pyproject.toml`, no `requirements.txt`, no lockfile, no `Pipfile`. The
`.gitignore` is the stock GitHub Python template (lines 14–57 are all standard).

Consequences:
- The runtime is defined implicitly by whatever is installed in `/home/pkis/venv`.
- A fresh clone cannot be installed or tested without reverse-engineering imports
  (which §3.2 does).
- Phase 4 (CI) **cannot proceed** until a manifest exists. This should arguably
  be the first concrete artifact after this audit is approved, even though the
  plan slots it implicitly under Phase 4 — flagging it here so it isn't a
  surprise blocker.

Recommended shape (for later, not now): a `pyproject.toml` with a minimal base
(`flask`, `pyyaml`, `python-frontmatter`, `networkx`, `numpy`, `rank-bm25`,
`anthropic`) and optional extras: `[semantic]` (sentence-transformers),
`[oauth]` (PyJWT[crypto], workos, cryptography), `[reader]` (beautifulsoup4,
pypdf, lameenc), `[ingest]` (gdown). The lazy-import pattern in app.py already
maps cleanly onto these extras.

There are **no unused declared dependencies** to flag, because nothing is
declared. The inverse risk — undeclared-but-used — is total.

`viewer/` *does* have a manifest (`package.json` + `package-lock.json`); its only
gap is the absence of any test dependency.

---

## 7. Seam inventory (Phase 2 insertion points)

Each seam is a place where a component hands control to another and something can
fail silently. Ordered by test value.

### Seam A — MCP dispatch ↔ `tool_*` implementations  ★ highest value
- **Where:** `dispatch_tool` (app.py:5498–5692); the three lambda dicts map
  `params` dict → typed `tool_*(**kwargs)`.
- **Silent failure mode:** a `tool_*` signature changes (rename/required-arg) but
  the lambda and the `inputSchema` don't, or vice versa. A `KeyError` on
  `p["x"]` becomes a 500; a dropped optional silently changes behavior.
- **Test:** contract test per advertised tool — valid canonical input → assert
  response shape & required fields (the plan's Priority 1). Plus the
  advertised⊆dispatchable invariant from F-1.

### Seam B — REST `/pkis-api/*` ↔ the same `tool_*` functions  ★ highest value
- **Where:** ~35 routes (app.py:5731–6450). Write routes use `@require_write`
  (verified: reader-build 6057, staged/commit 6144, bridge-note 6164,
  source-stub 6182, queue/add 6211, discovery/act 6354, upload-document 6368,
  save-url 6394, rebuild-graph 6411, reader-annotate 6079). Reads are open.
- **Silent failure mode:** this is a **second, parallel copy of the call surface**
  with **different auth plumbing** (`@require_write` decorator vs. in-dispatch
  `is_write_authorized`). A tool can be write-gated on MCP but the REST twin can
  drift (added without the decorator), or the two can diverge in argument
  defaults. `detect-concepts` (6420) is intentionally ungated — confirm that's
  the only one.
- **Test:** parametrized check that every REST write route carries `require_write`,
  and that REST and MCP return the same shape for the same logical call.

### Seam C — `tool_*` ↔ git persistence  ★ high value
- **Where:** the canonical helper `_git_commit_files` (app.py:3348–3368)
  **swallows all exceptions and returns `''`** on any failure (including a failed
  push). But several write tools **don't use it** and inline their own
  add/commit/push with *different* handling — e.g. `tool_edit_node`
  (2634–2651) separates commit-failure from push-failure and *retains the local
  commit on push failure*, returning `git_pushed: False`.
- **Silent failure mode:** a push fails (divergence/network) and, depending on
  which path ran, the caller may get `git_commit: ''` (looks like nothing
  happened) or `git_pushed: False` (committed locally, invisible to other
  workers until reconciled). Three+ copies of this logic guarantee they'll
  diverge further.
- **Test:** round-trip integration test against a **local fixture git repo**
  (the plan's Priority 2): write a node → read it back → assert content integrity
  and a well-formed commit result. Inject a push failure → assert the contract
  reports it rather than reporting success.

### Seam D — write ↔ cache freshness
- **Where:** per-worker in-memory caches (`_node_cache`, `_graph`, `_bm25_*`,
  `_embed_*`, 210–223) invalidated via a git-HEAD content signature
  (`_content_signature` 235, `ensure_fresh` 258, `_cache_gen` 232). `dispatch_tool`
  calls `ensure_fresh()` first (5503).
- **Silent failure mode:** `tool_edit_node` manually zeroes `_node_cache`/`_graph`
  (2617–2619) but does **not** rebuild BM25/embeddings inline nor bump
  `_cache_gen`; it relies on the commit changing HEAD so other workers rebuild
  lazily. A staged-only create (no commit) deliberately doesn't trigger rebuild.
  The interplay (manual zeroing vs. signature-driven rebuild) is subtle and
  exactly the kind of thing that breaks when someone "optimizes" it.
- **Test:** write → `search_wiki` finds the new/edited node within the same worker
  without a restart.

### Seam E — auth gating
- **Where:** `is_write_authorized` (867), `is_trusted` (859), `require_write`
  (842), `gate_error` (879), `OAuthChallenge` (159). Three credential sources
  (static key, OAuth JWT, WorkOS web session) collapse into two tiers.
- **Silent failure mode:** a bad token should yield a *well-formed* 401/403, never
  a silent success or a hang. The OAuth/WorkOS paths are lazy-imported and
  DORMANT unless env is set — a misconfiguration could make `OAUTH_ENABLED` False
  and silently fall back to static-key-only.
- **Test:** the plan's auth-failure-path test — bad token → well-formed error;
  and the dormant-fallback behavior is exercised (no env → static key still gates).

### Seam F — node load / IRI resolution
- **Where:** `load_node` (317), `slug_from_path` (276), `iri_from_slug` (280),
  `parse_iri` (285), `find_node_path` / `_by_iri` (293/302), `build_alias_registry`
  (366).
- **Silent failure mode:** malformed frontmatter, a slug/IRI mismatch, or an alias
  collision returns the wrong node or silently `None`. These are **pure-ish
  functions over the file tree** — ideal unit-test targets (plan's Priority 3).
- **Test:** unit tests over a tiny fixture wiki: round-trip slug↔IRI, alias
  resolution, collision detection (`tool_check_alias_collision`, 1831).

### Seam G — graph build ↔ search
- **Where:** `build_graph` (384) reads typed edges from frontmatter;
  `hybrid_search` (622) fuses BM25 (`build_bm25_index` 442) and vector
  (`vector_search` 543) via RRF (`rrf_score` 618).
- **Silent failure mode:** an edge predicate not in `EDGE_WEIGHTS` (104–115) is
  silently dropped from ranking; an embedding cache keyed on a stale content hash
  returns vectors for the wrong text.
- **Test:** unit-test RRF fusion and edge-weight lookup with known inputs (pure
  logic — high value, the plan's Priority-3 sweet spot). Search relevance itself
  is not worth asserting exact ranks on.

### Seam H — external-API adapters
- **Where:** arXiv (1928), CrossRef (1961), Semantic Scholar (1997), Readwise
  (3255), URL metadata (3193), podcast index/Apple/YouTube/Listen/Podchaser
  (3844–4357), OpenAlex (in discovery script).
- **Silent failure mode:** network/format changes upstream. These should **not**
  be unit-tested against live services (the plan says so explicitly). Mark any
  test touching them `@pytest.mark.live`.
- **Test:** none by default; optionally a contract test with recorded fixtures.

### Seam I — staging → commit (two-phase write)
- **Where:** `create_*_stub` / `create_bridge_note` / `create_hypothesis` write to
  `wiki/staging/` (STAGING_DIR 101); `commit_staged_node` (2883) promotes to live
  + git. `get_staged_nodes` (3036) reads the queue.
- **Silent failure mode:** a staged node is promoted with unresolved fuzzy links,
  or `action:"discard"` leaves an orphan. The Phase-C recovery script
  `fill_missing.py` exists precisely because a mid-run restart once lost creates.
- **Test:** stage → list → commit round-trip on a fixture; assert the staged item
  appears, then lands live with edges intact.

### Seam J — `app.py` ↔ `reader_build.py` (subprocess + reverse import)
- **Where:** §3.1. `tool_build_reader` (6013) / `_maybe_autobuild_reader` (5989)
  shell out; `reader_build` imports `app` back.
- **Silent failure mode:** the subprocess env (Piper paths, `OUTDIR`, model env)
  is assembled by shell wrappers (`run_build.sh`); a missing var fails the build
  with output only in a log file. Reader build status is polled via
  `/pkis-api/reader/<slug>/status` (5973).
- **Test:** out of scope for the core suite (needs Piper/ffmpeg); document as a
  `@pytest.mark.live`/manual surface.

---

## 8. Things that are already good (preserve them)

- The `tool_*` naming convention — makes the surface enumerable and testable.
- Lazy/optional imports for heavy or env-gated deps (`sentence-transformers`,
  `jwt`, `workos`) with graceful degradation. Keep this when adding a manifest.
- The viewer's single `api.ts` choke point and token-free `same-origin` auth.
- The git-HEAD content-signature cache-invalidation idea (Seam D) is sound;
  it just needs to be the *only* invalidation path, not co-existing with manual
  cache zeroing.
- Config-via-env-with-defaults discipline in `app.py` proper.

---

## 9. Suggested Phase-2 priority (preview, not a commitment)

Mapping seams to the plan's tiers, highest value first:

1. **F-1 contract invariant** (advertised ⊆ dispatchable) — one test, freezes §2 drift.
2. **Seam A** MCP contract tests for the 15 advertised read + 13 write tools.
3. **Seam C** git round-trip integration test on a fixture repo.
4. **Seam B** REST/MCP parity + `require_write` coverage check.
5. **Seam E** auth-failure path.
6. **Seam F/G/I** selective unit tests (IRI resolution, RRF/edge-weights, staging round-trip).

Prerequisite for *all* of it: a `conftest.py` that builds a **fixture wiki +
fixture git repo** in a tmp dir and points `WIKI_DIR`/`REPO_DIR`/`STAGING_DIR` at
it — which the env-with-defaults design already permits, *if* the `/home/pkis`
script paths (§5.2) are not in the import path of what we test.

---

## 10. Decisions recorded (post-review)

Captured after the Phase-1 review so they live in the artifact, not just chat:

- **D-1 — `app.py` modular split lands BEFORE the IKS build.** The split (§7
  step 7) is a committed Phase-3 target, not a maybe. Consequence: the Phase-2
  scaffold must give *comprehensive* (not sampled) coverage of the seams the
  split moves code across — Seam A (MCP contract), Seam B (REST/MCP parity), and
  Seam C (git persistence) must be green before the restructure begins. They are
  the safety net the split depends on.
- **D-2 — the "mnemon" trusted tier is still planned; keep it.**
  `register_operational_reference` and `log_operation` (app.py:5573–5586) are
  *promoted*, not removed: they get advertised in `_get_tools_list()` with proper
  schemas and join the contract-test set. The F-1 invariant
  (advertised ⊆ dispatchable) therefore needs a *smaller* "hidden on purpose"
  allow-list — these two come off it.

---

*End of Phase 1 artifact (with post-review decisions). Phase 2 in progress.*
