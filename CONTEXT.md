# PKIS Context
Curator-generated 2026-07-05 — regenerated from ground truth (not hand-edited, not copied from the prior Architect-era file).

**PKIS (Personal Knowledge Integration System)** is a personal research wiki modeled as a
multipartite knowledge graph of markdown notes (concepts, techniques, results, frameworks,
problems, principles, sources, hypotheses, and more), read and written by LLM agents over the
**Model Context Protocol (MCP)** and rendered to a human via a REST API + SPA viewer plus a
native Capacitor app. Domain focus: probabilistic reasoning, learning systems, causal
inference, knowledge representation, with carry-over from applied economics/policy modeling.

## For the codebase, see `openwiki/quickstart.md`
The mechanical map of the code (modules, MCP/REST surface, viewer, tools) is owned by the
**OpenWiki cartographer** under `openwiki/` and refreshed on a cron (every 3 days). This file
does NOT duplicate it — it captures only the non-code ground truth an agent can't infer from
source. `SCHEMA.md` is the canonical spec for the data model.

## Graph state (verified this pass, `store.get_graph()`)
**2,941 nodes / 9,563 edges.** By type: concepts 1009, techniques 764, sources 584,
frameworks 199, results 171, principles 82, problems 42, hypotheses 29, bridge-notes 24,
discovery-stubs 15, research-clusters 12, assets 9, resources 1, findings 0.
- **14 node-type dirs** under `wiki/<type>/` (`resource` and `finding` are the newest,
  see SCHEMA.md §Node-type table ~L340; `findings/` and `resources/` are freshly added and
  near-empty). **13 typed predicates** = `config.EDGE_WEIGHTS`: prerequisite-of, uses,
  specializes, generalizes, extends, applies, instantiates, contrasts-with, analogous-to,
  illustrated-by, evidence-for, implemented-by, superseded-by.
- MCP surface: **44 advertised tools** (`tools/list`). Two-phase write: `create_*_stub` →
  `staged_id` → `commit_staged_node`; `wiki/staging/` is the human-review content gate.
- IRI form `pkis:{type}:{slug}`, first frontmatter field.

## Deploy topology (changed substantially — verify before assuming)
PKIS is now **workstation-primary and public**.
- Served at **https://pkis.clowderpack.dev** via **Cloudflare Tunnel → gunicorn on
  127.0.0.1:5001** (`pkis.service`, systemd `--user`, currently active). gunicorn serves
  `/app/` itself; the `deploy/nginx-pkis.conf` front on :8080 is **optional/documented, not
  required**.
- **Workstation self-deploy loop**: `*/15` cron in `/home/pkis/pkis-wiki` does
  `git pull origin main` and restarts `pkis.service` on new HEAD.
- **Path aliasing**: `/home/pkis` → `/home/choct155/projects/pkis-home` (operational logs,
  usage db, venv); `/home/pkis/pkis-wiki` → `/home/choct155/projects/pkis` (this checkout).
  So all `/home/pkis/pkis-wiki/...` cron paths resolve here.
- **Hetzner VPS (pkis.dev) is now a READ-ONLY git mirror** — its service is disabled,
  pull-only sync. Note: `config.py` OAuth-audience / `PUBLIC_BASE` still *default* to
  `pkis.dev` (L108/L113/L123) — production overrides these via env; don't take the defaults
  as the live host.
- Single remote `git@github.com:choct155/pkis.git`; one repo holds app + docs + wiki nodes.
- **Single-writer git model: only the workstation checkout commits/pushes.** Usage/cost
  accounting SQLite at `/home/pkis/usage/usage.sqlite` (Comptroller).

## Agent roster (Architect RETIRED)
The **Architect is retired** (`ARCHITECT.md` deprecation header, 2026-07-05): its code-map
role → OpenWiki (Cartographer), its CONTEXT/consistency role → the global **Curator**. Active
PKIS agents and their real cadences (from the workstation crontab):

| Agent | Cadence (cron) | Role |
|---|---|---|
| Librarian | Mon 07:00 discovery, Mon 05:00 source-linking; else on-demand | Ingest sources; `park`→discovery-stub; inbox append |
| Synthesizer | on-demand / weekly (no cron) | Deepen nodes, propose connections |
| Auditor | 8th & 22nd 06:00 (fortnightly `graph_audit_cron.sh`) | Graph health + conformance gaps |
| Hygienist | weekly / on-demand (no cron) | Schema conformance, report-only |
| Comptroller | daily 06:30, weekly Mon 06:40, monthly 1st 06:50 | API cost accounting (live, non-LLM) |
| Lab Assistant | daily 04:30 + nightly_eval 03:00 | NED/NER eval + descriptive drift monitoring → inbox Lab lane |

Also cron'd: OpenWiki refresh every 3 days 03:00 (Cartographer), `narration_watchdog` every 15
min. All agents append to `wiki/inbox.md` swim-lanes; only the human removes items.

## Boundaries
PKIS↔IKS **strict** (no raw IKS data in the graph); PKIS↔ARS **porous** (PKIS is the ARS
knowledge substrate); ARS↔IKS strict. ARS and IKS are sibling projects **not yet built**
(`docs/ABOUT.md` L50-56; `AGENT_ROSTER_v2.md` L490-492).

## Recent structural changes (git log)
Native **Capacitor APK with WorkOS bearer auth + biometric unlock** (9ca472db) → Lab
Assistant **finding intake** (19cde717) → OpGraph instrumentation plan → **public serving +
`resource` node + share-target + workos dep** (96428d60) → OpenWiki + DREAM `resource`/`source`
nodes → **VPS→workstation migration + divergence reconcile** (826feaf2 merge) →
**OpenWiki cartographer adopted + Architect retired + predicate drift fixed** (fd7fb4ce).

## Read these first
1. `SCHEMA.md` — canonical data model (node types, 13 predicates, epistemic status, staging).
2. `openwiki/quickstart.md` — the code map (delegated; don't re-read code from scratch).
3. `AGENT_ROSTER_v2.md` — agent system of record (note the retirement caveats above).
4. `MCP_ACCESS_GUIDE.md` / `README.md` — MCP surface + operational entry.

## Watch out for
- **Single-writer git.** Never let another checkout (or the VPS mirror) push — the workstation
  is the only writer. The mirror is pull-only.
- **`.embed_cache.npz` is keyed to git HEAD.** `store.content_signature()` (store.py L626-645)
  uses the repo HEAD sha as the cache signature, so every committed write invalidates the
  semantic cache cross-worker. Uncommitted node edits won't refresh embeddings.
- **Two-phase staging.** A `create_*_stub` alone is not in the graph until `commit_staged_node`;
  `wiki/staging/` is the review gate.
- **`config.py` host defaults still say `pkis.dev`** — the live public host is
  `pkis.clowderpack.dev`; trust env/tunnel config, not the code defaults.
