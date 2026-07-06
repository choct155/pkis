# PKIS Architecture

Structural reference and **index**. This file describes what components exist, how
they connect, and the non-obvious design choices — and links to the canonical doc
for each subsystem rather than restating it. When structure changes, update this
file; when build *status* changes, update [`STATUS.md`](STATUS.md).

## Components

| Component | What it is | Canonical doc |
|---|---|---|
| **PKIS-MCP server** | `app.py` — one Flask app serving three surfaces: the MCP tool API (`/mcp`), the viewer REST API (`/pkis-api/*`), and docs/webhook/health endpoints. Runs on `pkis.clowderpack.dev` (gunicorn). | [`MCP_ACCESS_GUIDE.md`](MCP_ACCESS_GUIDE.md), [`SCHEMA.md`](SCHEMA.md) |
| **pkis-wiki repo** | The knowledge graph itself — one markdown file per node under `wiki/`, plus `index.md`, `log.md`, `queue.md`. Git is the source of truth. | [`SCHEMA.md`](SCHEMA.md) |
| **Viewer PWA** | React/Vite app at `pkis.clowderpack.dev/app` — mobile-first browse / search / clusters / priority / graph / staged / explainers / discover / reader / **docs**. | — |
| **Agents** | Operating procedures for the agent roles. | [`LIBRARIAN.md`](LIBRARIAN.md), [`SYNTHESIZER.md`](SYNTHESIZER.md), [`AUDITOR.md`](AUDITOR.md), [`HYGIENIST.md`](HYGIENIST.md), [`ARCHITECT.md`](ARCHITECT.md) |
| **Auth** | Reads open; writes gated by a static key (Claude Code) or OAuth identity (claude.ai), WorkOS AuthKit. | [`MCP_ACCESS_GUIDE.md`](MCP_ACCESS_GUIDE.md), [`OAUTH_PLAN.md`](OAUTH_PLAN.md) |
| **Plan** | The original phased build-out. | [`PKIS_Wiki_Implementation_Plan.md`](PKIS_Wiki_Implementation_Plan.md) |

## Repo topology

It's **one** git repo — `github.com/choct155/pkis` — holding `app.py`, `viewer/`,
`tools/`, `docs/`, and the knowledge graph under `wiki/`. Two checkouts share it:

- **Local dev** — the working copy on the laptop.
- **Server (prod)** — checked out at `/home/pkis/pkis-wiki` (where `REPO_DIR` /
  `WIKI_DIR` point; `app.py` is symlinked from `/home/pkis/app.py`). Both checkouts
  push and pull `origin/main`, and the server also commits here directly — every MCP
  write tool (`create_node_stub`, `add_connections`, …) auto-commits and pushes.

Because the laptop and the server both commit to the same branch, the two can diverge
(see STATUS "known issues"); reconcile by committing, `git pull --no-rebase`, push.

`DOCS_REPO_DIR` (docs reads + the `log_idea` write) defaults to the repo root holding
`app.py` — the same checkout — resolving symlinks so the prod symlink lands correctly.
It's configurable so docs could split into their own repo later, but today it equals
`REPO_DIR`.

> Not to be confused with the server's `DOCS_DIR` (`/home/pkis/docs/`) — that's the
> uploaded-source document store (books/PDFs), unrelated to this `docs/` set.

## Data flows

**Capture → integrate → graph**
```
phone / web capture ──▶ SQLite inbox ──▶ raw/captures/ (weekend integration)
                                          └─▶ structured wiki nodes (Librarian)
```
Raw captures are friction-free and unstructured; promotion into sourced, connected
nodes is a deliberate pass, not automatic.

**MCP write → commit → visible**
```
write tool ─▶ stage/edit markdown ─▶ git commit + push (wiki repo)
                                      └─▶ cache auto-refresh (git-HEAD signature)
```
New content is searchable immediately — no service restart. A restart is needed only
for `app.py` code changes, and it **drops the claude.ai connector** (user reconnects).

**Viewer ↔ API**
```
Viewer PWA ──HTTP POST──▶ /pkis-api/*  (search, node, related, clusters,
                                        priority, staged, assets, docs, …)
```
The viewer never speaks MCP; it uses the parallel REST surface. Reads are open;
viewer writes use a WorkOS sealed-session cookie.

**Proactive discovery**
```
frontier gaps ─▶ OpenAlex citation-graph crawl ─▶ ranked candidates ─▶ discovery inbox
```
Wiki-as-filter; fit-dominant ranking. Surfaces in the viewer's `discover` view.

## Semantic search

Hybrid retrieval: BM25 keyword + bge-small dense vectors, fused via Reciprocal Rank
Fusion. The dense index (`.embed_cache.npz`) is **derived and gitignored** — the git
HEAD sha is its freshness signature, so it must never enter version control. Built
offline at deploy.

## External integrations

- **Readwise Reader** — source capture + webhook (`/readwise/webhook`).
- **Google Drive** — binary source PDFs under `PKIS/sources/`, never committed.
- **GitHub** — version control + backlog (Issues), referencing `IDEAS.md` by title.
- **Anthropic API** — extraction/narration pipelines (Librarian ingest, reader).

## Key design decisions

Recorded with rationale in [`DECISIONS.md`](DECISIONS.md) — see it for the "why"
behind OAuth-by-WorkOS, the gitignored embedding cache, two-phase staged writes, and
the docs-system repo split. This file links structure; that file keeps the history.
