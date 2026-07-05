# PKIS Quickstart

## What this repository is

**PKIS** (Personal Knowledge Integration System) is the backend for a personal
research wiki: a **multipartite knowledge graph** of markdown notes (concepts,
techniques, results, frameworks, problems, principles, sources, hypotheses, and
more) that is read and written by LLM agents over the **Model Context Protocol
(MCP)**, and rendered to a human through a REST API + SPA viewer.

The project description in its own words (`pyproject.toml`):

> Personal Knowledge Integration System — MCP wiki server (`app.py`) + viewer.

Domain focus: probabilistic reasoning, learning systems, causal inference, and
knowledge representation, plus methodological carry-over from applied
economics/policy work (forecasting, state-space modeling, microsimulation).
See [`/SCHEMA.md`](../SCHEMA.md) for the full node/edge/tagging schema — it is
the canonical spec for the data model and is treated as source-of-truth
documentation rather than duplicated here.

The wiki is **maintained by LLM agents**; the human's role is to source
material, resolve synthesis proposals, and drain the reading queue
(`SCHEMA.md` "Purpose"). Almost every code path in this repo exists to support
that agent-driven maintenance loop safely (see
[Curation & Lifecycle](domain/curation-and-lifecycle.md)).

## Repository shape

This is a **flat single-module Python codebase** — there is no package tree.
`app.py` is exposed as a top-level `py-module` (`pyproject.toml`) so
`pip install -e .` makes `import app` work for the test suite and for
gunicorn's `app:app` entrypoint.

```
/app.py            Flask monolith: MCP server + REST API + tool implementations (~7,400 lines)
/config.py         All environment-derived constants (paths, feature flags, edge weights)
/paths.py          Filesystem paths for standalone tools/ scripts (re-exports config.py)
/store.py          WikiStore: node loading, graph build, BM25 + dense hybrid search
/adapters.py       External API fetchers (arXiv, CrossRef, Semantic Scholar, Readwise, podcasts)
/ask.py            The "ask brain" — retrieve → traverse → cite agent loop (Anthropic tool use)
/conversations.py  SQLite-backed persistence for saved ask conversations
/shares.py         Capability-link sharing (token → owned item, public read-only)
/experiments.py    Append-only log of search/ask runs for the "retrieval lab"
/metrics.py        Reference-free retrieval-quality metrics
/usage.py          Cost/usage accounting ("Comptroller") for every Claude API call
/explainer_x.py    Flask Blueprint pattern for dynamic interactive explainers
/SCHEMA.md         Canonical knowledge-graph schema (node types, IRIs, predicates)
/tools/            ~30 operational scripts (cron jobs, one-shot ingestion, audits)
/tests/            pytest suite: contract/, integration/, unit/
```

This subset of the repository was captured as a single git snapshot commit
("sandbox: pkis code subset for openwiki test"); deep commit history and the
`viewer/` SPA frontend are **not present** in this checkout. Where source code
references files that aren't here (e.g. `ARCHITECTURE_AUDIT.md`,
`COMPTROLLER.md`, the `viewer/app/dist` build), this wiki notes that
explicitly rather than inventing their contents.

## Where to go next

| Section | What it covers |
|---|---|
| [Architecture → Server](architecture/server.md) | `app.py`'s three API surfaces (MCP JSON-RPC, REST, direct tool functions), the tool registry/dispatch gate, the auth model (static tokens, OAuth, WorkOS web sign-in, native app), and the git-backed write path |
| [Architecture → Data & Storage](architecture/data-and-storage.md) | The knowledge graph data model, `WikiStore` (node cache, graph, hybrid search), `adapters.py` external fetchers, and the two-phase staging→commit write pattern |
| [Domain → Knowledge Workflows](domain/knowledge-workflows.md) | The "ask" agent loop, saved conversations, the retrieval lab (experiments + metrics), and dynamic explainers — i.e. how a human/agent *asks* the wiki things |
| [Domain → Curation & Lifecycle](domain/curation-and-lifecycle.md) | Domains/tags taxonomy, discovery pipeline, staging lifecycle for new nodes, health/drift monitoring, sharing, and usage/cost accounting |
| [Operations → Tools & Cron](operations/tools-and-cron.md) | The `tools/` script inventory (load-bearing vs. one-shot), what runs on cron, and operational conventions |
| [Testing](testing.md) | Test suite structure, fixtures, markers, and what to check when changing each area |

## First things to read as a new agent

1. `SCHEMA.md` — the data model everything else is built around.
2. `app.py:1-130` — module docstring, imports, and the B2-split comments that
   explain which code moved to which sibling module and why (this matters:
   `app.py` does `from config import *`, `from store import ...`,
   `from adapters import *`, etc., so functions/constants you see used in
   `app.py` may actually be defined in a sibling file).
3. `tools/README.md` — the load-bearing/supporting/one-shot classification for
   every script in `tools/`.
4. `tests/conftest.py` — how the hermetic test fixture wiki+git-repo is built;
   essential context before touching anything that reads/writes wiki content.

## Key things to watch out for when changing this codebase

- **`app.py` is a monolith mid-refactor.** Several modules (`store.py`,
  `adapters.py`, `config.py`, `paths.py`, `ask.py`, `conversations.py`,
  `shares.py`, `experiments.py`, `metrics.py`, `usage.py`, `explainer_x.py`)
  were incrementally carved out of it. They are re-imported with
  `from X import *` or explicit names specifically so **existing call sites in
  `app.py` keep working unchanged** and gunicorn's `app:app` entrypoint stays
  valid. When adding new shared logic, prefer extending a sibling module over
  growing `app.py` further, and preserve the re-export shim if you do.
- **Tests monkeypatch module-level globals** (`app.WIKI_DIR`, `app.REPO_DIR`,
  `app.STAGING_DIR`, etc.) at call time — because of the `import *` pattern,
  these resolve as `app`-module globals even though they're defined in
  `config.py`. Don't refactor them into function-local reads without checking
  `tests/conftest.py` and the contract tests first.
- **Every git write must go through `_git_commit_and_push`** (see
  [Architecture → Server](architecture/server.md#git-backed-write-path)). It
  fails loudly (`GitPushError`) rather than silently dropping content — never
  swallow or "fix" that exception without understanding the reconciliation
  workflow (`tools/reconcile_push.py`).
- **`usage.log_usage()` must never raise.** It's called after every Claude API
  call and is explicitly documented as best-effort so a logging bug can never
  break a real tool call.
- **Contract tests freeze the tool/route surface on purpose**
  (`tests/contract/test_mcp_tools.py`, `test_rest_parity.py`). If you add,
  remove, or re-tier a tool/route, expect (and update) an assertion that
  encodes the previous count/set — that's intentional drift protection, not a
  stale test.
- **Do not read or commit secrets.** Live credentials live in environment
  variables / a `.env` on the VPS (`paths.ENV_FILE`), never in this repo.
