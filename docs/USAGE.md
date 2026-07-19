# Using PKIS

How to read, search, capture, and extend the knowledge base — from your laptop and
from your phone.

## The two main surfaces

| Surface | Best for | Where |
|---|---|---|
| **Viewer PWA** | Browsing, searching, reading, capturing — especially on mobile | `https://pkis.clowderpack.dev/app` |
| **MCP (via Claude)** | Asking questions in chat, and authoring/editing nodes | `https://pkis.clowderpack.dev/mcp` |

## Reading & browsing (viewer)

Open `pkis.clowderpack.dev/app` (installable as a PWA — "Add to Home Screen" on phone). Nav:

- **browse** — all nodes, filterable by type / domain / cluster.
- **search** — hybrid keyword + semantic search (top bar).
- **clusters** — research clusters and their agendas.
- **priority** — the frontier-driven reading priority list.
- **graph** — the typed-edge graph, focusable on a node.
- **staged** — nodes awaiting review/promotion.
- **explainers** — interactive explainers + visualizations.
- **reader** — read+listen reader (semantic narration of a source; available per slug).
- **discover** — proactively surfaced candidate sources.
- **docs** — this documentation set (what you're reading).

Tap a node for its full body, sources, connections, and graph neighborhood. Some
nodes have a **read+listen** reader (semantic narration of the source).

## Capturing (phone or web)

Use the capture button (＋) in the viewer to drop a fragment, URL, or idea. Captures
land in an inbox and are **promoted during integration sessions** — they are not
auto-merged into the graph. This keeps capture friction-free without polluting the
structured graph.

## Asking questions in chat (MCP)

Connect Claude to the wiki, then ask domain questions and Claude will search the
graph first. See [`MCP_ACCESS_GUIDE.md`](MCP_ACCESS_GUIDE.md) for full connection
steps. In short:

- **Claude Code (desktop):** configured in `~/.claude.json` with a Bearer key —
  reads *and* writes.
- **claude.ai (mobile/web):** add a custom connector to `https://pkis.clowderpack.dev/mcp` —
  reads anonymously; writes after OAuth sign-in (if you're on the allowlist).

## Authoring & editing (MCP write tools)

Writing requires authorization (see the access guide). Always call
**`get_write_schema`** first — it returns valid knowledge types, edge predicates, and
each tool's parameters, so writes are correct by construction.

Typical flow:

1. **`search_wiki`** — check the concept doesn't already exist (enrich over duplicate).
2. **`create_node_stub`** (concept/technique/result/framework/problem/principle) or
   `create_source_stub` / `create_hypothesis` / `create_bridge_note`. These **stage** a node.
3. **`commit_staged_node`** — promote the staged node to live.
4. **`add_connections`** — wire typed edges to existing live nodes.
5. **`edit_node`** — enrich a live node's frontmatter or named body sections (`section_updates`), or replace the entire body (`content`). Also used by the viewer's edit sheet.

Each write auto-commits, pushes, and refreshes the search cache — new content is
findable immediately, no restart.

> **Authoring note:** inside a node's body, use `###` for subsections (never a bare
> `##` inside the Definition). See `SCHEMA.md`.

## Logging ideas from any session (`log_idea`)

While working in any Claude chat or Claude Code session, capture a not-yet-decided
idea straight into [`IDEAS.md`](IDEAS.md) with the **`log_idea`** MCP tool:

- Required: `title`, `idea`.
- Optional: `source` (defaults to `Claude Code: <branch>`), `relation_to_system`,
  `open_questions`.

It prepends a dated, `status: open` entry and commits to the **main repo**. It does
**not** promote anything to `DECISIONS.md` — graduating an idea to a decision stays a
deliberate human action.

## The agents

Invoke an agent in a Claude Code session by name:

| Agent | Invoke with | Does |
|---|---|---|
| **Librarian** | `Librarian, ingest [source]` | Ingests sources → structured, sourced nodes |
| **Synthesizer** | `Synthesizer, work on [concept/domain]` | Deepens nodes, draws cross-domain edges |
| **Auditor** | `Auditor, run health check` | Link integrity, orphan detection, structural gaps |
| **Hygienist** | (see `HYGIENIST.md`) | Convention/cleanliness passes |
| **Architect** | `Architect, refresh the overview` | Keeps architecture docs + product overview true to the code |

## The weekend-integration loop

The recurring rhythm that keeps the graph healthy:

1. **Drain the inbox** — promote raw captures to `raw/captures/`.
2. **Ingest** queued sources (Librarian).
3. **Synthesize** — turn promoted material into nodes and edges; enrich existing.
4. **Maintain** — health check, fix orphans/broken links.
5. **Review priority** — let the frontier agenda set next reading.

---

*See [`ABOUT.md`](ABOUT.md) for the why, [`ARCHITECTURE.md`](ARCHITECTURE.md) for the
how, and [`STATUS.md`](STATUS.md) for current state.*
