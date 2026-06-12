# PKIS Decisions

Append-only decision log. A decision made is permanent history — even if reversed,
the reversal is a **new** entry (and the original gets `Status: superseded-by`).
This is the "why did we do it this way" record that prevents re-litigating settled
questions. Newest entries at the top.

Format:
```
## [YYYY-MM-DD] <short title>
**Decision:** what was decided
**Alternatives considered:** what was rejected and why
**Rationale:** why this choice
**Consequences:** what this forecloses or enables
**Status:** active | superseded-by: [date + title]
```

---

## [2026-06-12] Documentation system: four-doc taxonomy + viewer Docs surface

**Decision:** Establish `docs/` with ABOUT, ARCHITECTURE (an index, not a restatement),
USAGE, STATUS, DECISIONS (this file), IDEAS; surface them — plus existing canonical
docs — through a mobile-first **Docs** view in the viewer, driven by `docs/manifest.json`.
Add a `log_idea` MCP write tool that appends to IDEAS.md.
**Alternatives considered:** Markdown files in the repo with no consumption surface
(rejected: unreadable on phone, which is a required use case); a wiki node type for
docs (rejected: docs are infrastructure, not knowledge content — wrong layer).
**Rationale:** Clear separation by update-cadence (structure / history / now /
pre-decision) keeps docs alive; the viewer already renders markdown and is mobile-first,
so consumption is nearly free.
**Consequences:** STATUS.md becomes the single canonical state surface (absorbs
`PHASE_C_BRIEF.md`, which is removed). Adding a doc = adding a manifest entry.
**Status:** active

## [2026-06-12] Docs + `log_idea` live in the single project repo; `DOCS_REPO_DIR` configurable

**Decision:** Keep `docs/` (and the `log_idea` write target) in the one project repo
(`choct155/pkis`) that also holds `app.py` and the `wiki/` nodes. `log_idea` commits via
`DOCS_REPO_DIR`, which defaults to the symlink-resolved directory of `app.py` (the repo
root) and is overridable by env.
**Alternatives considered:** A separate docs repo (rejected: docs are infrastructure
that ships with the code — one checkout, one history). Hardcoding `REPO_DIR` (rejected:
a dedicated, symlink-resolving, overridable var documents intent and survives a future
split).
**Rationale:** On the server `app.py` is symlinked into the checkout at
`/home/pkis/pkis-wiki`; `.resolve()` makes the default land on the real repo root, so
today `DOCS_REPO_DIR == REPO_DIR`. A separate commit helper keeps docs commits
(`[ideas] log: …`) distinct from wiki-node commits.
**Consequences:** Degrades gracefully (`git_pushed: false`, local commit retained) if
the repo has no reachable remote.
**Status:** active

## [2026-06-09] Authenticated writes via WorkOS AuthKit OAuth

**Decision:** Gate claude.ai (mobile/web) writes behind OAuth using WorkOS AuthKit;
keep the static `PKIS_MCP_WRITE_KEY` as the desktop Claude Code machine-to-machine path.
**Alternatives considered:** URL-embedded credentials in the connector (`?wk=` and
`/mcp/<key>`) — both tested and rejected; claude.ai refuses to carry ad-hoc creds.
**Rationale:** Per-identity, revocable write access; reads stay open. ~$0/mo.
**Consequences:** Write access is granted by adding a WorkOS `sub` to the allowlist;
the static key is demoted to a documented service credential. See `OAUTH_PLAN.md`.
**Status:** active

## [2026-06-09] Semantic search = BM25 + dense, fused by RRF; embed cache gitignored

**Decision:** Hybrid retrieval (BM25 keyword + bge-small dense vectors) fused via
Reciprocal Rank Fusion. The dense index (`.embed_cache.npz`) is gitignored and rebuilt
offline at deploy.
**Alternatives considered:** Keyword-only (weaker recall on paraphrase); committing
the index (rejected — the git HEAD sha is the cache-freshness signature, so the cache
must never enter HEAD).
**Rationale:** Dense recall + keyword precision; derived artifact stays out of git.
**Consequences:** Deploy must run an offline `build-embeddings` step.
**Status:** active
