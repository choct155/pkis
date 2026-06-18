# PKIS Structural Recommendations

**Phase 3 artifact.** A ranked, bounded list of structural changes worth making —
derived from `ARCHITECTURE_AUDIT.md`, filtered by the review plan's inclusion
criteria (reduces coupling, removes a 3×-repeated pattern, removes deploy/extend
friction, or unblocks the IKS build). Not a rewrite proposal.

Owned by the **Architect** agent (`ARCHITECT.md`); kept current as items land.

**Status legend:** ✅ done · 🔄 in progress · ⬜ pending · ❓ needs your decision
**Effort:** S (hours) · M (≤1 day) · L (multi-day)
**IKS timing:** per decision D-1, the `app.py` split lands **before** IKS, so
anything the split depends on is "before IKS" too.

---

## A. Already shipped this engagement (recorded, not pending)

| # | Change | Audit ref | Status |
|---|--------|-----------|--------|
| A1 | **Dependency manifest** — `pyproject.toml` with base + optional extras | F-4 | ✅ |
| A2 | **Tool registry** — dispatch tables lifted to module scope (`READ/TRUSTED/WRITE_TOOLS`, `DISPATCHABLE_TOOLS`, `TOOL_TIERS`); introspectable, split-ready | §2, F-1 | ✅ |
| A3 | **Loud push-failure consolidation** — 5 copy-pasted git sites → one `_git_commit_and_push`; failures raise `GitPushError` with diagnostics; `tools/reconcile_push.py` | §7 Seam C, F-3 | ✅ |
| A4 | **Dead-code removal** — 3 unused viewer `api.ts` fns; `build_reader_blei.py`, `book_split.py` | §4 | ✅ |
| A5 | **Test scaffold** — hermetic fixture + 34 passing guards | Phase 2 | ✅ (fill pending → B1) |
| A6 | **CI** — non-blocking, code/test-path + weekly | Phase 4 | 🔄 |

---

## B. Ranked pending recommendations

### B1 — Finish the Phase-2 contract-test fill  ✅  ·  M  ·  before IKS
**What:** flesh out the 39 documented stubs (23 per-tool contracts, REST/MCP
parity, auth/cache/staging seams, 2 units); mock-at-boundary for the 3 network
write tools.
**Why it matters:** these are the **safety net the split depends on** — they pin
the observable MCP/REST surface so B2 can move code across module boundaries
without silently changing behavior. **This is the gate for B2.**

### B2 — Split `app.py` into modules  ✅  ·  L  ·  before IKS  *(the headline)*
**Done:** `config.py`, `store.py` (DI'd `WikiStore` caches), `adapters.py`,
`usage.py`, `paths.py` extracted; `app.py` ~6,467→~5,660 lines; suite hermetic.
Flat-modules-with-shim form (D-③); package promotion (C-3) deferred — see below.
**What:** decompose the 6,467-line monolith into
`config / store / graph / search / auth / persistence / mcp / rest / adapters`,
**incrementally** — one module at a time, each extraction behind the green
contract tests, `import app` preserved at every step (a thin shim re-exports).
**Why:** the single biggest coupling reduction; IKS will reuse these surfaces, so
clean seams now save compounding integration cost later. Depends on B1.

### B3 — Unify the two write surfaces  ✅ (intent met)  ·  M  ·  before IKS (with B2)
**What:** route REST `/pkis-api/*` writes and MCP writes through **one** gated
dispatch path instead of two parallel copies with different auth plumbing
(`@require_write` vs in-dispatch `is_write_authorized`).
**Why:** removes a whole class of drift (a write route added to one surface but
not the other). Natural to do as the `mcp`/`rest` modules are carved out in B2.
Audit §7 Seam B.
**Verdict (2026-06-18, reconsidered):** the *valuable* unification is already in
place and contract-locked — not worth a literal dispatch merge:
- **Auth: one predicate.** Both `require_write` (REST decorator) and the MCP
  dispatch (`app.py` ~4578) delegate to the single `is_write_authorized(req)`. No
  parallel auth plumbing remains.
- **Logic: one implementation.** The 10 REST write routes are thin wrappers that
  call the same `tool_*` functions the MCP path dispatches (e.g. `tool_build_reader`,
  `tool_commit_staged_node`, `tool_discovery_act`) — not a second copy.
- **Drift: test-locked.** `tests/contract/test_rest_parity.py` freezes the
  write-gate inventory (`test_write_gate_inventory_is_frozen`), asserts every write
  route is gated, no read route is, and REST/MCP return the same shape.
Routing REST literally through `dispatch_tool` would add JSON-RPC-envelope
indirection to REST handlers for zero benefit. Closed as intent-met.

### B4 — `paths.py` / `PKIS_ROOT` for `tools/` + `scripts/`  ✅  ·  M  ·  before IKS
**Done (2026-06-18):** `paths.py` is the SSOT (repo + operational paths,
env-overridable, `bootstrap()`); adopted by touched scripts. Model-ID centralization
(`claude-sonnet-4-6` etc.) NOT yet done — folded into B6.
**What:** derive the `/home/pkis/...` absolute paths from one env-rooted module;
centralize the scattered model IDs (`claude-sonnet-4-6`, `claude-haiku-4-5`) and
the embed-model name.
**Why:** today no operational script runs in CI or a fresh clone without edits
(audit F-3, §5.2). Unblocks testing the scripts and is a prerequisite for ever
running them in CI.

### B5 — Resolve the 14 hidden tools  ✅ (mostly)  ·  S  ·  before IKS
**Done:** 12 advertised (now 40 live); mnemon tier advertised. **Left per your
call:** `search_wiki_index` + `get_node_stub` stay dispatchable-but-hidden (possible
external callers; you said leave them).
**What:** for each dispatchable-but-unadvertised tool, **advertise** it (add to
`_get_tools_list`) or **remove** it from dispatch. Mnemon tier
(`register_operational_reference`, `log_operation`) → advertise, per D-2 (the
`xfail` guard flips to pass).
**Why:** freezes the surface the split moves. **Needs your input** — see Decision
D-2 below (two tools can't be confirmed dead from the repo alone).

### B6 — Centralize repo-specific hardcoding  ⬜  ·  S  ·  after IKS ok
**What:** the `github.com/choct155/pkis` URLs baked into write-tool return
payloads → one config value.
**Why:** low urgency, but any fork/multi-tenant or repo move breaks the returned
`url` fields today (audit §5.1).

### B7 — Separate operational vs. one-shot scripts  ✅ (as manifest)  ·  S  ·  anytime
**Done (2026-06-18):** delivered as `tools/README.md` — a classification manifest
(🔴 load-bearing / 🟡 supporting / ⚪ one-shot) rather than an `ops/`+`oneshot/`
physical split. Rationale: too many scripts are referenced by path (`app.py`, VPS
crontab, `discovery_cron.sh`, build shell scripts, tests), so relocating is high-churn
for an organizational gain — the manifest gives the "safe to change?" signal at zero
breakage risk. Physical split remains available if ever wanted.
**What:** split `tools/` into `tools/ops/` (load-bearing: `reader_build`,
`discovery_openalex`, `mine_proposals`, `mackay_phasec_driver`, `fill_missing`)
vs. `tools/oneshot/` (book ingest, backfills); document which are wired to
`app.py`/cron.
**Why:** today nothing signals which scripts are safe to change vs. live
dependencies (audit §1.3).

### B8 — Viewer test tooling  ✅  ·  S  ·  after IKS ok
**Done (2026-06-18):** added `vitest@^2` (Node-18.11/vite-5 compatible) + `npm test`
(`vitest run`) + `viewer/src/lib/api.test.ts` — 6 smoke tests pinning the `api.ts` ↔
`/pkis-api/*` contract (base path, POST body shapes, a GET endpoint, ApiError on
non-ok). Frontend-only; no server deploy.
**What:** add `vitest` + a few smoke tests pinning the `api.ts` ↔ backend
contract (the frontend's single coupling point).
**Why:** the viewer has zero tests; `api.ts` is the one file whose drift breaks
the whole app. Low effort, real protection.

### B9 — Fix `set_priority_config` tier/description mismatch  ⬜  ·  S  ·  anytime
**What:** it's advertised with a read-flavored description but lives in
`WRITE_TOOLS`. Align the description (and confirm the tier).
**Why:** minor surface-hygiene; cheap to fix while B5 touches the same area.

### B10 — Dedupe reading priority: queue captures, frontier prioritizes  ❓⬜  ·  M  ·  after IKS ok
**What:** the flat reading queue's coarse `high/normal` tag duplicates the
continuous priority the concept frontier already computes. Keep the queue as a
pre-ingestion **capture inbox** (the frontier can't see un-ingested sources), but
demote the manual tag to a capture-time hint and derive queued-item ordering from
the frontier + reading graph once a source is ingested.
**Why:** two parallel priority signals that can disagree — the same de-dup smell
as the dual write surfaces. **Product decision** — logged to `docs/IDEAS.md`
(2026-06-14); needs your call before implementing.

### B11 — Close the loud-push race window (operational)  ⬜  ·  S  ·  soon
**What:** the server pulls `origin/main` every 15 min (cron) + restarts on change.
After an external push to `main` (me, CI) there's a ≤15-min window where a
production write commits on the server's stale HEAD, fails to push, and now —
post loud-push — **raises** instead of silently diverging. Mitigate by making the
write path `pull --rebase` before push (auto-reconcile the happy path), and/or
shortening the sync cron.
**Why:** the loud-raise design (correctly) stopped hiding divergence, but exposed
this narrow availability edge. Audit §7 Seam C / Seam D.

---

## C. Decisions needed from you

These are the items I can't resolve from the code or sensible defaults:

- **D-① Execution scope.** I recommend executing **B1–B5 before IKS** (they're the
  split + its prerequisites + the surface-freeze) and recording **B6–B9** for
  later. Confirm, or move items between buckets.
- **D-② Hidden-tool resolution (B5).** Mnemon tier → advertise (settled). But
  `search_wiki_index` and `get_node_stub` are dispatchable with no in-repo callers
  and **possible external callers I can't see** — advertise them, or remove them?
  (I will *not* remove a reachable tool without your word.) The other 12 are
  read-convenience tools also exposed via REST → I'll advertise them unless you'd
  rather prune.
- **D-③ Split packaging (B2).** Target a real Python package (`pkis/` with
  submodules) or keep flat top-level modules with a thin `app.py` that imports
  them? The server imports `app` and runs gunicorn from its checkout, so either
  works if `import app` stays valid — but the package form is cleaner long-term.
  I lean **flat-modules-with-shim first** (smaller deploy risk), package later.
  **Verdict (2026-06-18, C-3 reconsidered): keep flat; do NOT promote to a `pkis/`
  package now.** B2 already delivered the value that mattered — `config.py`,
  `store.py` (DI'd caches), `adapters.py`, `usage.py`, `paths.py` are clean modules;
  the cache-coupling and untestability that made `app.py` unwieldy are resolved, and
  the suite is hermetic. A `pkis/` package would only add namespacing while putting
  the proven server entrypoint at risk (`app:app` under gunicorn from
  `/home/pkis` with a symlinked `app.py`; `tools/reader_build.py` does `import app`
  + 7 internals; the realpath bootstrap already broke prod once). Risk > value with
  B2 done. Revisit only if a second top-level app/package ever shares this checkout.

---

*Prerequisite reminder: B2 (the split) does not start until B1 (contract fill) is
green. Everything in §A is already merged.*
