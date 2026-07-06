# Testing

The suite is `pytest`, organized by **architecture seam** rather than by
source file — each test module targets a specific interface boundary the
project has decided is worth freezing behavior against. The seam taxonomy is
defined in `ARCHITECTURE_AUDIT.md` (referenced throughout the tests but not
included in this repository subset); test docstrings cite the seam letter
(e.g. "Seam C") so you can cross-reference even without that file.

Run with: `pytest` (from the repo root, after `pip install -e .[dev]` or
equivalent). Config lives in `pyproject.toml`'s `[tool.pytest.ini_options]`.

## Markers

Four markers, defined in `pyproject.toml`:

- `unit` — pure-function logic over fixtures (IRI resolution, RRF fusion math).
- `contract` — asserts the *observable* MCP/REST tool contract (shape +
  required fields), not internal behavior.
- `integration` — exercises a real seam (git round-trip, auth path, staging
  queue) against the fixture environment.
- `live` — hits a live server or external API (pkis.clowderpack.dev, arXiv, OpenAlex,
  etc.); **skipped by default**, run explicitly with `pytest -m live`.

Default `pytest` runs are fully hermetic (fixture wiki + fixture git repo
only) — no network, no `/home/pkis`, no live server.

## The fixture harness (`tests/conftest.py`)

This file is the prerequisite that makes hermetic testing possible against a
codebase that reads config from environment variables at import time. Before
`app.py` is imported, it:

1. Strips any `*_PROXY`/`*_SOCKS` environment variables (the Anthropic SDK's
   httpx client honors proxy env vars at construction time and can fail
   import in CI sandboxes/corp networks otherwise).
2. Builds a throwaway git repo + wiki tree under a session tmp dir and points
   `WIKI_DIR` / `REPO_DIR` / `DOCS_REPO_DIR` / `STAGING_DIR` env vars at it —
   **before** `import app`, since `app.py` binds these to module-level
   constants at import time (`WIKI_DIR = Path(os.environ.get(...))`), not
   read lazily per-call.
3. Sets a dummy `ANTHROPIC_API_KEY`, forces `PKIS_SEMANTIC_SEARCH=0` (BM25-only:
   deterministic, and avoids pulling `torch` into the test environment), and
   points the usage DB at the tmp dir.
4. Clears OAuth/WorkOS/static-token env vars so auth subsystems are dormant by
   default — `tests/integration/test_auth.py` opts specific tests back in via
   monkeypatch.

Key fixtures exposed: `appmod` (the imported `app` module), `client` (a Flask
test client), and `isolated_wiki` (a fresh per-test repo+wiki, for tests that
write). `write_node()` is the helper for seeding fixture nodes with
frontmatter matching `app.py`'s on-disk format.

**If you change how `app.py`/`config.py` read paths or construct the
Anthropic client at import time, re-check this file first** — it is tightly
coupled to those import-time side effects.

## Test inventory by seam / area

| File | Seam / focus |
|---|---|
| `tests/contract/test_mcp_tools.py` | Seam A — MCP dispatch vs. `tool_*` implementations; freezes the advertised-vs-dispatchable tool set (tool count, tiering) so a tool silently becoming unreachable or ungated fails loudly. |
| `tests/contract/test_rest_parity.py` | Seam B — REST `/pkis-api/*` vs. the same tools; parses `app.py` decorators to assert every write route carries the write-auth guard and no read route is wrongly gated. |
| `tests/integration/test_git_persistence.py` | Seam C — `_git_commit_and_push` contract: success, no-op-on-no-changes, loud `GitPushError` with retained local commit on push failure. |
| `tests/integration/test_cache_freshness.py` | Seam D — write → `WikiStore` cache invalidation/freshness. |
| `tests/integration/test_auth.py` | Seam E — auth gating matrix (static key, bad bearer, OAuth-dormant, native tokens); always well-formed JSON-RPC errors, never silent success or a 500. |
| `tests/unit/test_iri_resolution.py` | Seam F — slug/IRI parsing round-trips. |
| `tests/unit/test_search_fusion.py` | Seam G — RRF fusion math + `EDGE_WEIGHTS` completeness. |
| `tests/integration/test_staging_commit.py` | Seam I — the two-phase staging → commit write. |
| `tests/integration/test_finding_intake.py` | Finding-stub creation, incl. domain inheritance from parent hypothesis. |
| `tests/integration/test_resource_intake.py` | Resource-stub creation/intake. |
| `tests/integration/test_reading_queue.py` | Reading queue add/list/priority behavior. |
| `tests/integration/test_reconcile_push.py` | `tools/reconcile_push.py` end-to-end against a fixture repo (subprocess). |
| `tests/integration/test_lab_assistant.py` | `lab_monitor.py` / `lab_transform.py` snapshot + drift-flagging behavior. |
| `tests/integration/test_usage_instrumentation.py` | `usage.log_usage()` called correctly around real tool calls. |
| `tests/unit/test_comptroller.py` | Cost model, cache-token pricing, model-family rate routing (`tools/comptroller.py` + `usage.py`). |
| `tests/unit/test_usage.py` | `usage.py` store/schema unit coverage. |
| `tests/unit/test_discovery_stubs.py` | `discovery_stubs_from_inbox.py` idempotency + schema conformance. |
| `tests/unit/test_paths.py` | Cross-module path consistency (`paths.py` vs. `config.py`). |
| `tests/unit/test_store.py` | `store.py` unit coverage (node/graph helpers). |
| `tests/unit/test_retrieval_lab.py` | `experiments.py`/`metrics.py` retrieval-lab logic. |

## Notable engineering pattern: frozen inventories

Several contract tests deliberately **freeze an inventory** — the hidden-tool
set, the write-gated route set, an advertised-tool count — as an explicit
constant. This is a low-noise regression net around a large, single-file
Flask app: unintentional drift in the tool/route surface fails immediately,
while an intentional addition/removal requires updating the test's expected
constant in the same change. If a contract test fails after you add or
re-tier a tool, **update the frozen constant deliberately** rather than
treating the test as flaky.

## What to run when changing each area

- Changed a `tool_*` function or its tier → `tests/contract/test_mcp_tools.py`,
  `tests/contract/test_rest_parity.py`.
- Changed git write/push behavior → `tests/integration/test_git_persistence.py`,
  `tests/integration/test_reconcile_push.py`.
- Changed auth (any of the four mechanisms) → `tests/integration/test_auth.py`.
- Changed `WikiStore`, search, or `EDGE_WEIGHTS` →
  `tests/unit/test_search_fusion.py`, `tests/unit/test_store.py`,
  `tests/integration/test_cache_freshness.py`.
- Changed staging/promotion logic → `tests/integration/test_staging_commit.py`,
  `test_finding_intake.py`, `test_resource_intake.py`.
- Changed `usage.py`/`comptroller.py` pricing or schema →
  `tests/unit/test_usage.py`, `tests/unit/test_comptroller.py`,
  `tests/integration/test_usage_instrumentation.py`.
- Changed `lab_monitor.py`/`lab_transform.py` → `tests/integration/test_lab_assistant.py`.
- Changed `paths.py`/`config.py` path resolution → `tests/unit/test_paths.py`,
  and re-check `tests/conftest.py` (see above).
