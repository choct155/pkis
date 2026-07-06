# Explainer authoring & editing workflow

Explainers are interactive HTML pages registered as `asset` nodes. This is the
desktop workflow for building/extending them with a live preview, a Claude Code
dialogue, and git-versioned rollback — plus the path from a static page to a
server-backed one.

## Where things live

- **HTML** — self-contained files in `wiki/assets/viz/<slug>.html` (git-tracked).
- **Node** — `wiki/assets/<slug>.md`, `kind: explainer`, `viz: <slug>` (→ static
  HTML) **or** `viz_url: /pkis-api/x/<name>/` (→ Tier-2 dynamic, see below).
- **Served** — `/pkis-api/viz/<slug>.html` (static) straight from the server's
  checkout; the viewer shows it full-screen in `ExplainerOverlay`.

## The desktop editing loop

```
                ┌──────────── git (versioning / rollback) ────────────┐
                │                                                      │
  Claude Code ──┴─ edits ─▶ wiki/assets/viz/<slug>.html ─ live-reload ─▶ browser tab
                                       │
                          explainer_publish.sh ──▶ pkis.dev  ──▶  ⟳ in PKIS overlay
```

1. **Live preview** — `bash tools/explainer_serve.sh [port]` serves the viz dir
   with auto-refresh on save. Open `http://localhost:5500/<slug>.html`; every save
   refreshes instantly. (Local only; nothing deployed.)
2. **Edit** — in this Claude Code session (the agentic dialogue). Optionally work
   on a throwaway branch: `git switch -c edit/<slug>`.
3. **Fine-grained rollback** — `bash tools/explainer_autosnapshot.sh` commits every
   save to the current branch. Roll back to any save with
   `git checkout <sha> -- wiki/assets/viz/<slug>.html`; squash-merge to `main` when
   done so history stays clean.
4. **Publish** — `bash tools/explainer_publish.sh` commits, pushes, and rsyncs the
   viz dir to pkis.dev. Then hit **⟳** in the PKIS explainer overlay to re-pull the
   live version in context (no close/reopen).

## Static → server-side: the graduated model

Climb only as high as a given explainer forces you to.

| Tier | What | When |
|------|------|------|
| **0** standalone HTML | self-contained page | explanatory + light interactive viz |
| **1** HTML + rich client JS | sliders, simulations, in-browser recompute, small bundled data | **most "interactive" needs** |
| **2** HTML + Flask blueprint | `explainer_x.py`, served at `/pkis-api/x/<name>/` | genuine server-side: persistence, heavy compute, secret keys, auth-gated writes |
| **3** separate proxied service | own runtime/DB | when it becomes its own product |

**Promote to Tier 2** without a rewrite: add routes for `<name>` in `explainer_x.py`
(copy the `/sample/` pair), then point the asset node at it with
`viz_url: /pkis-api/x/<name>/` instead of `viz: <slug>`. It rides the existing
`/pkis-api/*` proxy (no nginx change) and reuses the app's WorkOS auth + Comptroller
logging via the hooks passed to `explainer_x.register(...)`. Verify the scaffold:
`curl https://pkis.clowderpack.dev/pkis-api/x/sample/`.

## Deploy notes

- Static explainers: `explainer_publish.sh` (rsync). No service restart.
- `explainer_x.py` / app.py changes: deploy app.py (git pull + preflight `import app`
  + `systemctl restart pkis-mcp.service`); the blueprint mounts at import time.
