# Brief — Phase C (book knowledge extraction) + viewer full-body fix

Hand-off brief for a fresh Claude Code instance. Three tasks, in order. Keep your context
lean: extract/propose off-context (server-side or subagents), write nodes in batches.

## Environment / mechanics (read first)
- **Server:** `ssh pkis@pkis.dev`. Wiki repo: `/home/pkis/pkis-wiki` (`wiki/` holds nodes). App = gunicorn `app:app`, `EnvironmentFile=/home/pkis/.env` (has `ANTHROPIC_API_KEY`).
- **Manual python runs on server:** `cd /home/pkis; set -a; . /home/pkis/.env; set +a; export PYTHONPATH=/home/pkis/pkis-wiki`.
- **MCP write tools** (via `pkis-wiki` server) auto-commit **and push** each write; cache auto-refreshes on write (git-HEAD signature) so new nodes are searchable immediately — **no restart**. Restart only for app code changes, and a restart **drops the claude.ai connector** (user must reconnect).
- **Call `get_write_schema`** (MCP read tool) for valid knowledge types + edge predicates. Predicates: `prerequisite-of, uses, specializes, generalizes, extends, applies, instantiates, contrasts-with, analogous-to`. Knowledge types: `concept, technique, result, framework, problem, principle` (+ `hypothesis`, `source`, `bridge-note` via their own tools).
- **`create_node_stub` CAN set `slug`** (and `sources`, `definition`, `domain`, `tags`); it STAGES → `commit_staged_node` to go live → `add_connections` for edges (targets must be live). `create_source_stub` can NOT set slug (auto-derives).
- **Credits:** watch the Anthropic balance — the MacKay reader batch hit a credit wall mid-run once. A failed-credit error is a 400 that fails instantly.

## State of the books (coverage layer done; readers/text vary)
| Book | slug | chapter stubs | reader text (`paper_md`)? |
|---|---|---|---|
| MacKay ITILA | `mackay-itila` | 50 | ✅ all 50 built |
| Hastie ESL | `hastie-esl` | 18 | ✅ built |
| Russell & Norvig AIMA | `russell-norvig-aima` | 28 | ❌ stubs only |
| Gelman BDA3 | `gelman-bda3` | 23 | ❌ |
| Sutton & Barto RL | `sutton-reinforcement-2018` | 17 (Ch.13 = `sutton-policy-2018`) | ❌ |
| Deisenroth MML | `deisenroth-mml` | 12 | ❌ |
| Pearl Causality | `pearl-causality` | 11 | ❌ |
| Resnick Stochastic Processes | `resnick-stochastic-processes` | 7 | ❌ |

Chapter text lives at `/home/pkis/pkis-wiki/wiki/reader/<slug>-chNN/payload.json` → `sections[].paper_md` (faithful markdown w/ LaTeX). **MacKay has it; the other 6 don't** — they need the extract step first (Task 2).
Still **unacquired:** Bishop PRML, Murphy PML ×2 (ask user to drop in Drive `books/`), Goodfellow (HTML-only, `deeplearningbook.org`).

---

## TASK 1 — Phase C for MacKay (text already extracted; cheapest)
Mine each MacKay chapter's `paper_md` → create knowledge nodes + enrich existing + wire edges.

**Pilot already done = the quality/shape bar.** Part I produced: `pkis:concept:typical-set` (keystone, links the explainer + `hmc`), `shannon-information-content`, `source-coding-theorem`, `kraft-inequality`, `huffman-coding`, `arithmetic-coding` + 11 edges. Read those nodes (`get_node`) before starting — match that depth (formula + mechanism + "why it matters"), granularity (one node per concept), and edge style.

**Method (context-safe):** go chapter-by-chapter (or fan out subagents — one per chapter — each reads its `payload.json` and returns a structured proposal; you serialize the writes since git is a single lock). For each chapter:
1. Read `paper_md` (don't load all 50 into one context).
2. **Dedup first:** `search_wiki` / `ls wiki/concepts wiki/techniques wiki/results` — many chapters share concepts (entropy, mcmc…). Enrich existing via `edit_node`; create only genuinely new ones.
3. `create_node_stub` (with `slug`, `definition`, `domain`, `tags`, `sources:["pkis:source:mackay-itila-chNN"]`) → `commit_staged_node`.
4. `add_connections` to wire intra-cluster + into the existing graph.

**Pending enrichments (do these too):** `entropy` and `kl-divergence` exist — fold in MacKay ch2 framing (decomposability, Gibbs' & Jensen's inequalities). MacKay overlaps heavily with existing nodes (`mcmc`, `variational-methods`/`mean-field-approximation`, `gaussian-processes`, `monte-carlo`, `ising-models`, `laplace-approximation`, `hopfield`, `belief-propagation`) — prefer **enrich + connect** over duplicate.

**HEADINGS GOTCHA:** inside a node `definition`, use **`###` for subsections, never `##`** (see Task 3 — the viewer truncates the Definition at the first `##`). The 6 pilot nodes were retro-fixed with `/home/pkis/fix_headings.py <file>` (demotes stray `##`→`###`). Once Task 3 ships this matters less, but author with `###` regardless.

## TASK 2 — Phase C for the other 6 books (needs extraction first)
They have stubs but no `paper_md`. Per chapter, run the reader pipeline's **extract** stage to get text (Haiku, ~$0.12/ch, no audio):
```
cd /home/pkis; set -a; . /home/pkis/.env; set +a; export PYTHONPATH=/home/pkis/pkis-wiki
OUTDIR=/home/pkis/pkis-wiki/wiki/reader/<slug>-chNN \
  /home/pkis/venv/bin/python tools/reader_build.py <slug>-chNN extract
```
(or `full` if the user also wants audio — confirm first; audio adds ~$0.14/ch + hours). Then do Task-1-style extraction on the resulting text. Run as a **detached server batch** like `/home/pkis/mackay_reader_batch.sh` (idempotent, logs, continues past failures). Prioritize by relevance: Gelman/Deisenroth/Sutton are closest to the existing Bayesian/RL clusters.

---

## TASK 3 — Viewer: render the FULL node body
**Bug:** `viewer/src/components/DetailSheet.tsx` only surfaces the `## Definition` section (truncated at the next `## `, via `extractSection`) + `## Intuition`. All other body sections (anatomy, `## Why it matters`, MacKay/Gibbs/HMC mechanism sections, etc.) are in the markdown but **invisible in `pkis.dev/app`**.

**Fix (~10 lines, ~lines 222–284):** render the **full body** for all node types instead of just Definition+Intuition. `fullBody` already exists (line 228 = content minus the `## Connections` prose, which shows structurally). Replace the `hasDefinition ? definition : fullBody` conditional with: always render `fullBody` as the body block; drop the now-duplicative separate Definition + Intuition blocks; keep graph / sources / connections as-is. Render markdown links so the explainer URLs are clickable.

**Deploy (viewer builds LOCAL — server lacks vite):**
```
cd viewer && npm install && npm run build      # produces viewer/dist
# rsync dist/ to wherever nginx serves pkis.dev/app  (confirm target — check the
# existing deploy; viewer memory: "build LOCAL + rsync dist")
```
Find the rsync target by inspecting how `/app` is currently served (nginx config or ask the user). After this ships, all node content displays and the `##`→`###` demoting is no longer required.

---

## Reference / patterns
- **Explainer publishing:** drop standalone HTML in `wiki/assets/viz/` → live at `pkis.dev/pkis-api/viz/<file>.html` (no deploy/restart). `typical-sets.html` is there + linked from `typical-set`. Source dev copy: `explainers/typical-sets.html` (live-reload it with `npx live-server explainers/`).
- **Cost model:** arXiv papers extract free (ar5iv); PDFs pay Haiku vision extraction (~$0.12/ch) — the cost driver. Narration (Sonnet) ~$0.14/ch is the audio cost. MacKay Phase C node-authoring (text already paid) ≈ $3–8; the other 6 books add their extraction cost.
- **Reconcile git** if local/server/origin diverge: commit wanted changes, `git checkout -- <deployed code>` for files origin already has, `git pull --no-rebase`, push.
