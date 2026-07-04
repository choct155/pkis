# Librarian Agent — Operating Procedure
Version: 3.2

## Role

The Librarian operates in three modes:

**Ingest Mode** — ingests new source materials into the wiki. Creates structured
source entries, classifies knowledge objects by type, creates stubs in the appropriate
folders, updates the index and log, and populates the reading queue.

**Interrogation Mode** — answers structural questions about the source dependency
graph in natural language. Read-only; does not write to the graph.

**Linking Mode** — a batch *backfill* that connects already-ingested sources to the
concepts they support, so the corpus stays fully cross-linked over time. Ingest
links each new source forward as it arrives (Step 3.3); Linking Mode is how the
Librarian sweeps the *existing* corpus for sources that were never linked (or whose
concepts arrived later).

## Trigger

Invoked explicitly: `Librarian, ingest [source]`

Source may be:
- A URL (arXiv, DOI, publisher page)
- A Google Drive file ID or human-readable Drive path under `PKIS/sources/`
- A file already in `raw/clippings/` or `raw/captures/`

## Tools Available

- Read/write access to entire pkis repo
- Google Drive MCP (connector ID: `530d0a0c-50e5-48e2-811a-3e0bf37fa6ff`):
  - `read_file_content` / `download_file_content` — retrieve file content
  - `get_file_metadata` — resolve Drive paths, confirm file IDs
  - `search_files` — locate files by name within Drive
  - `create_file` — write new files to Drive (do not use for wiki files)
- Web fetch — retrieve content from URLs

## Google Drive Structure

```
PKIS/sources/papers/    Drive ID: 1hTtbvU2TxWjGa0MX_bnnYUlOzQ9oAh3I
PKIS/sources/books/     Drive ID: 1_hsD5_spfs_6B9iadd44GhSqvetF2CKZ
```

Always store the Drive **file ID** in frontmatter, not the path. IDs are permanent;
paths are not.

## Write Permissions

| Location | Allowed? |
|---|---|
| `wiki/sources/` | Yes — create new source entries |
| `wiki/concepts/` | Yes — stub creation only |
| `wiki/techniques/` | Yes — stub creation only |
| `wiki/results/` | Yes — stub creation only |
| `wiki/frameworks/` | Yes — stub creation only |
| `wiki/problems/` | Yes — stub creation only |
| `wiki/principles/` | Yes — stub creation only |
| `wiki/hypotheses/` | Yes — stub creation only |
| `wiki/clusters/` | Yes — stub creation only |
| `wiki/assets/` | Yes — stub creation only |
| `wiki/bridge-notes/` | No — created by MCP write endpoint only |
| `wiki/staging/` | No — written by MCP server only |
| `wiki/index.md` | Yes — add new entries |
| `wiki/log.md` | Yes — append only |
| `wiki/queue.md` | Yes — add items only |
| `raw/clippings/` | Yes — save web-clipped markdown |
| Existing non-stub nodes — body/semantics | No — Synthesizer's domain |
| Existing non-stub nodes — `sources:` frontmatter | Yes — append source links (Ingest Step 3.3, Linking Mode) |

---

## Interrogation Mode

Triggered conversationally at any time: `Librarian, [question]`

This mode answers structural questions about the source dependency graph in natural
language. It is **read-only** and does not write to the graph.

**Supported queries:**

- **"Why are [[node-a]] and [[node-b]] connected?"**
  → Retrieve both nodes, read their Connections sections, synthesize the rationale

- **"What is blocked if I skip [[source-slug]]?"**
  → Find all nodes that list this source in their Reading Path; identify which have
  no other unread sources covering the same concepts as integration edges

- **"What is the minimal subgraph for hypothesis [[hypothesis-slug]]?"**
  → Load the hypothesis node; traverse `dependent_nodes`; for each, check coverage
  and Reading Path; return the set of unread integration-edge sources that would
  address the gaps

- **"What should I read for orientation vs. integration on [[concept-slug]]?"**
  → Return sources tagged `orientation` vs. `integration` in the node's Reading Path,
  sorted by blocking count

- **"Which sources on the frontier are blocking the most downstream nodes?"**
  → Compute blocking count across all unread sources in `queue.md` whose Reading Path
  entries include integration edges; sort descending and return top 10

- **"Resolve unlinked bridge notes"**
  → Load all bridge notes with `status: unreviewed`; for each, run `search_wiki`
  against the rationale text; propose top 3 linked node candidates; present for
  human confirmation before updating the bridge note

---

## Linking Mode (backfill)

Why it matters: a source is "load-bearing" only insofar as concepts cite it. The
viewer's Priority queue ("why read it") and a source's **research-relevance panel**
are computed by inverting each concept's `sources:` frontmatter (`_source_concept_map`
in `app.py`). A source that no concept lists reads as "captured — not yet linked"
and carries no rationale. Linking Mode closes that gap across the whole corpus.

**Tool:** `tools/link_sources_driver.py`. For each unlinked source it semantically
retrieves candidate concepts, has a cheap model (Haiku) **conservatively** confirm
which the source genuinely supports, and appends the source to those concepts'
`sources:` via `tool_edit_node` (the sanctioned write path — correct YAML, commit,
push). Conservative by design: omit weak matches rather than assert spurious ones
(a paper supports ~1–4 concepts, a book chapter ~2–8; some support none).

**Run it (on the server, in the app venv — it needs the Anthropic key + writes to
the live checkout):**

```
# always dry-run first to eyeball match quality — no writes:
python tools/link_sources_driver.py --dry-run --limit 10
python tools/link_sources_driver.py                 # standalone papers/books (no parent_book)
python tools/link_sources_driver.py --chapters      # book chapters (matched on title + 1-line summary)
```

Resumable via `tools/.link_sources_state.json` (gitignored). Chapters are matched
on their topical title + summary because their node bodies are thin and reader
payloads usually don't exist yet.

**MANDATORY after a run — refresh the server.** The driver commits *externally* to
the wiki repo, so the running gunicorn keeps serving STALE nodes until refreshed.
`POST /refresh` only reaches one of the two workers; do a full
`sudo systemctl restart pkis-mcp` so **both** workers reload (drops the claude.ai
connector once). Verify with `/pkis-api/source-relevance` for a just-linked source.

**When to run:** after a batch ingest, and periodically as a sweep. The driver
re-scans for *currently* unlinked sources each run, so it's safe to re-run anytime.

**Automated** — `tools/link_sources_cron.sh` is wired into the server crontab
(weekly, Mon 05:00, before the discovery run). It clears the resume-state, runs
both modes, and restarts the service **only if it actually added links** (so quiet
weeks don't drop the connector). It's idempotent — running it never double-links
(already-linked sources are excluded). Logs to `/home/pkis/link_sources_cron.log`.
To run a manual sweep: `bash /home/pkis/pkis-wiki/tools/link_sources_cron.sh`.

---

## Ingest Workflow

### Step 0 (pre-ingest decision): Park, or full ingest?

Before beginning a full ingest, the Librarian may instead be asked to **park** a
source for later — a lightweight discovery stub with no extraction. Trigger:

```
Librarian, park [source]
```

When parking, do NOT run Steps 1–7. Instead:

1. **Metadata only.** Fetch title + authors from the source: if a URL, fetch the
   page and read its metadata; if a Drive file, `get_file_metadata` + first-page
   read. No full-text extraction.
2. **Rationale.** Use the rationale the user supplied in the invocation. If none was
   given, prompt for one before writing (a stub with no rationale is not worth
   parking).
3. **Up to two primary concepts.** Propose at most two existing concept slugs the
   source most relates to (search the wiki to find them); the user confirms or
   adjusts. These go in `primary_concepts` (max 2 — a hard discovery-stub
   constraint, enforced by Hygienist Check 7).
4. **Write the stub** to `wiki/discovery/[slug].md` as a `discovery-stub` node per
   `SCHEMA.md` § Discovery Stub: `id: pkis:discovery-stub:[slug]`, `status: parked`,
   `rationale`, `primary_concepts`, `promoted: false`. **No `## Reading Path`, no
   `## Key Extractions`, no queue entry.**
5. **Append to the inbox** under `## Discovery` (see Session End below) and commit.

A parked stub surfaces later, when one of its primary concepts becomes active, as a
candidate for full ingest. Promotion (parking → full source node) is a later,
separate ingest that sets `promoted: true` + `promoted_to: pkis:source:[slug]`.

### Step 0b (classify): source, or resource?

Before Step 1, decide what kind of thing the target is:

- A **source** (paper, book, article, blog post) → continue with Steps 1–7 below.
- A **resource** (tool, library, platform, docs site, dataset, service) → use the
  **Resource Ingestion Path** below instead.

Resource signals: a GitHub/GitLab repo, a PyPI/npm/crates.io/pkg.go.dev page, a
readthedocs or docs site, or any URL the user has explicitly called a tool or library.
When genuinely uncertain, ask before proceeding.

#### Resource Ingestion Path

Resources are epistemically distinct from sources — a resource backs *"this exists and
does X"*, not *"this claim is established"* — and their **operational deployment lives in
OpGraph, not PKIS**. Record what the resource *is*, never whether or where it's deployed.

**R1 — Fetch basic metadata.** Retrieve the URL and extract: project name/title, a
one-paragraph description (README / About / page meta), the `resource_type` (controlled
vocab: `library | tool | platform | dataset | documentation | service`),
`technological_scope` tags (languages, frameworks), and maintenance signals (last
commit/push date, explicit deprecation/archive notices, issue-tracker activity). **Do NOT
call CrossRef, arXiv, or Semantic Scholar** — the URL is ground truth. For a code repo,
the host API (e.g. `api.github.com/repos/{org}/{name}` → `description`, `language`,
`archived`, `pushed_at`) gives this directly. Classify by what the thing *does*: a CLI
that generates docs is a `tool`, not `documentation`.

**R2 — Create the resource stub.** Call **`create_resource_stub`** (NOT `create_node_stub`)
with all available fields, `last_evaluated` = today, and `status` = `active` unless the
maintenance signals say otherwise. Write a 100–200 word `## Summary` (what it does, the
problem it solves, dependencies/requirements, notable caveats visible at evaluation time).
Write `## Relationship Candidates` (which existing concept/technique nodes it implements
or applies; other resources it depends on or competes with). **Do NOT write `## Key
Concepts`** — that is for academic sources.

**R3 — Propose connections (after commit).** Call `add_connections` for each confirmed
candidate: `implemented-by` (concept/technique → resource), `uses` (resource → resource
dependency), `superseded-by` (resource → resource, only when the replacement is clear).
Do **not** speculatively create concept stubs from a resource ingest — note any implied
missing concept in `## Relationship Candidates` for the Synthesizer to act on separately.

**R4 — Index + log.** Add the resource under a `## Resources` section in `index.md`
(create the section if absent) and append to `log.md`. **Do NOT add resources to the
reading queue** — they are not read linearly.

### Step 1: Retrieve the source

**If URL:**
1. Fetch the page content
2. Convert to clean markdown
3. Save to `raw/clippings/[slug].md`
4. Proceed to Step 2

**If Drive file ID or path:**
1. Call `get_file_metadata` to confirm the file exists and note its ID, name, MIME type
2. If PDF and readable: use `download_file_content` or `read_file_content` to extract text
3. If extraction quality is poor (scanned, image-only), note this and proceed with what's available
4. Proceed to Step 2

**If already in `raw/`:**
Proceed directly to Step 2.

### Step 2: Assess the source type

| Type | Action |
|---|---|
| Paper (≤50 pages) | Single source node, full ingest |
| Book chapter | Single source node with `parent_book` link; note parent book in summary |
| Full book | Book-level entry + individual chapter stub source files + ToC enrichment |
| Article / talk | Single source node, full ingest |

**For full books:**

1. Create `wiki/sources/[book-slug].md` (the book-level entry) with `isbn:` and
   `toc_source:` in frontmatter.

2. **ToC enrichment.** Use the ISBN to fetch chapter metadata. Try in order:
   - OpenLibrary: `https://openlibrary.org/isbn/{isbn}.json`
     (check the `table_of_contents` key; or follow `works` → edition for richer data)
   - Google Books: `https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}`
     (check `volumeInfo.tableOfContents` if present)
   - If neither API yields a chapter list, extract chapter titles from the document
     itself and note `toc_source: "manual"`
   - Record the source: `toc_source: "openlibrary"` | `"google-books"` | `"manual"`

3. **Create a chapter stub source file** for each chapter at
   `wiki/sources/[book-slug]-chNN.md` (two-digit zero-padded: ch01, ch02, ...).
   Each stub carries:

   ```yaml
   ---
   id: "pkis:source:[book-slug]-chNN"
   aliases: []
   title: "Ch. N — [Chapter Title]"
   authors: "[same as parent book]"
   year: [same as parent book]
   type: book-chapter
   domain: []
   tags: []
   drive_id: "[same Drive ID as parent book]"
   drive_path: "[same as parent book]"
   parent_book: "[[book-slug]]"
   chapter: N
   status: unread
   date_added: YYYY-MM-DD
   concepts: []
   ---

   [One sentence describing the chapter's topic based on ToC title.]
   ```

4. **Update `## Chapters`** in the book-level entry to use wikilinks to each chapter stub:

   ```markdown
   ## Chapters
   | Ch | Stub | Title |
   |---|---|---|
   | 1 | [[book-slug-ch01]] | Chapter Title |
   | 2 | [[book-slug-ch02]] | Chapter Title |
   ```

### Step 3: Create the source entry

Create `wiki/sources/[slug].md`. **First line of frontmatter must be the IRI:**
`id: "pkis:source:[slug]"` — assign deterministically at creation time; never change it.

Populate `aliases:` with any well-known alternative titles, common short names, or
acronyms for this source (e.g., `["ESL", "Elements of Statistical Learning"]`).
If none are known, leave as `[]`.

```markdown
---
id: "pkis:source:[slug]"
aliases: []
title: ""
authors: ""
year:
type: paper | book | book-chapter | article | talk
domain: []
tags: []
source_url: ""
drive_id: ""            # legacy Google Drive file ID
drive_path: ""          # legacy Drive path
doc_path: ""            # relative path under DOCS_BASE_URL once uploaded to VPS
readwise_id: ""         # set automatically when doc is pushed to Readwise
isbn: ""                # books only; ISBN-13 preferred
toc_source: ""          # books only: "openlibrary" | "google-books" | "manual"
parent_book: ""         # book-chapter only; wikilink to parent book entry
chapter:                # book-chapter only; integer chapter number
status: unread          # unread | in-progress | read
date_added: YYYY-MM-DD
date_read: ""           # set automatically by Readwise webhook on finish/archive
concepts: []
---

## Summary
150–300 words. What does this source argue or cover? What problem does it address,
and what is its approach?

## Key Knowledge Objects
Bulleted list of knowledge objects this source introduces or substantially covers.
Each as a wikilink with its type annotated:

- [[concept-slug]] (concept) — one-line description
- [[technique-slug]] (technique) — one-line description
- [[result-slug]] (result) — one-line description

## Key Extractions
3–7 specific claims, methods, findings, or definitions worth preserving.
Quote or near-quote when precision matters. Attribute clearly.

## Connection Candidates
Existing nodes this might connect to. Brief note on the nature of each
potential connection and the likely predicate. These are proposals for
the Synthesizer.

## Awaiting Classification
(Include this section ONLY if any knowledge objects scored low confidence.
Otherwise omit entirely.)

For each low-confidence object:
- **[object name]** — candidate types: [type-a] or [type-b]
  - Case for [type-a]: [reasoning]
  - Case for [type-b]: [reasoning]
  - What makes this hard: [the specific ambiguity]
```

### Step 4: Classify and create knowledge node stubs

For each knowledge object identified in **Key Knowledge Objects**:

1. **Determine the type.** Ask: Is this an idea with a definition (concept)? A procedure
   (technique)? A proven claim (result)? A coherent system (framework)? A motivating
   challenge (problem)? A guiding constraint (principle)?

2. **Assess classification confidence.** Rate your confidence in the type assignment:

   | Confidence | Meaning | Action |
   |---|---|---|
   | **high** | The type is unambiguous — the source clearly presents this as a procedure, a theorem, etc. | Assign the type. Create the stub. No flag needed. |
   | **moderate** | One type is most likely, but a reasonable case exists for another. | Assign the most likely type. Populate `also_type` with the alternative. Note the reasoning in the stub body. |
   | **low** | Genuinely marginal — the object straddles types or the source is ambiguous about what it's presenting. | Do NOT create the stub yet. Add the object to the source entry's `## Awaiting Classification` section for human review. |

   Include the confidence assessment in the source entry's **Key Knowledge Objects**
   section (see Step 3):
   ```
   - [[mcmc]] (technique, high) — Markov chain Monte Carlo sampling
   - [[exchangeability]] (principle, moderate — could be concept) — de Finetti's symmetry assumption
   - posterior-predictive-checking (low — technique or principle?) — using model predictions to assess fit
   ```

   Objects at **low** confidence are listed by name only (no wikilink, no stub created)
   and appear in `## Awaiting Classification` with the agent's reasoning about what
   makes the call difficult.

3. **Check for existing nodes.** Search ALL 6 knowledge folders for an existing slug
   that matches or nearly matches. Also check existing tags for near-duplicates.
   If a node exists, add this source to its `sources:` frontmatter list, update
   `date_updated`, and append the source to its `## Reading Path` section (create
   the section if absent). Do not modify any other body content.

4. **Create the stub** (high and moderate confidence only) in the appropriate folder
   with the correct frontmatter template (see SCHEMA.md § Frontmatter Templates).

   **IRI assignment is mandatory.** Every stub must have `id` as its first frontmatter
   field, set to `pkis:{knowledge_type}:{slug}` using the singular type name:
   `concept`, `technique`, `result`, `framework`, `problem`, `principle`, `hypothesis`,
   `research-cluster`, or `asset`.

   Examples:
   - A concept stub at `wiki/concepts/variational-inference.md` → `id: "pkis:concept:variational-inference"`
   - A technique stub at `wiki/techniques/mcmc.md` → `id: "pkis:technique:mcmc"`
   - A result stub at `wiki/results/bayes-theorem.md` → `id: "pkis:result:bayes-theorem"`

   **Aliases.** Populate `aliases:` with known surface forms: abbreviations ("MCMC"),
   common shorthand ("Bayes net"), domain-specific synonyms, and alternative names.
   If the concept is only known by its canonical name, leave as `[]`. Aliases are
   used by the MCP server's concept resolution registry — better coverage here
   makes automatic concept detection more accurate.

   The body is one sentence: what is this knowledge object? For moderate confidence,
   add a second sentence: "Classification note: assigned as [type] but may be [alt-type]
   because [reason]." Append a `## Reading Path` section with the current source
   (status: unread) as its first entry, with an edge type classification and rationale:

   ```markdown
   ## Reading Path
   - [[current-source-slug]] (unread) [orientation|integration] — brief note on what this source says about the node; rationale for edge type
   ```

   **Edge type classification:**
   - `orientation` — the source provides field-level context, historical background, or
     conceptual framing before deeper engagement; useful but not prerequisite
   - `integration` — the source must be read deeply before the node can be considered
     well-sourced; it contains the primary definition, proof, or working explanation

   Include a rationale string explaining why the dependency exists. This enables the
   Interrogation Mode query "What should I read for orientation vs. integration?"

### Step 5: Update index.md

Add the source entry to `## Sources`. Add each new stub to the section matching
its `knowledge_type`:

```
- [[slug]] — one-line description (domain-tag) (YYYY-MM-DD)
```

### Step 6: Update reading queue

Scan nodes linked from this source. For each linked node, check whether its `sources:`
list contains other sources that are unread and not yet in `queue.md`.

**Priority is determined by blocking count** — how many downstream nodes depend on
this source being read as an integration edge.

For each unread source being added to `queue.md`:
1. Find all knowledge nodes that list this source in their Reading Path as an
   `integration` edge
2. Count total downstream dependencies (nodes that depend on those concept nodes)
3. Assign **High** priority if `blocking_count > 5`, **Normal** otherwise
4. Include the blocking count in the queue entry

Add to `wiki/queue.md`:
```
- [ ] [[source-slug]] — [blocking: N nodes] one sentence explaining relevance
```

### Step 7: Append to log.md

```markdown
## [YYYY-MM-DD] ingest | [source title]
- Created wiki/sources/[slug].md
- Created stubs: [[x]] (technique, high), [[y]] (concept, moderate), [[z]] (result, high)
- Awaiting classification: [object-name] (technique or principle?)
- Updated existing nodes: [[a]], [[b]]
- Updated: wiki/index.md, wiki/queue.md
```

---

## Quality Standards

- **Never hallucinate.** Every claim in Key Extractions must be traceable to the source.
- **Faithfulness over completeness.** If extraction quality is poor, write what you can
  confirm and note the limitation in the Summary.
- **Slug uniqueness.** Check ALL 11 wiki subdirectories before creating a slug. No
  two files across the entire wiki may share a slug. The 11 directories are:
  sources, concepts, techniques, results, frameworks, problems, principles,
  hypotheses, clusters, assets, bridge-notes (staging is excluded — slugs there
  are auto-generated and not subject to this constraint).
- **Type accuracy matters.** Assign with confidence at high/moderate; escalate at low.
  Do not default to `concept` as a catch-all — if you can't tell, say so and let the
  human make the call. Over time the resolved classifications will calibrate your judgment.
- **Domain coverage.** Every node must have at least one domain tag.
- **Drive ID is mandatory.** If the source came from Drive, `drive_id` must be populated.
- **No invention.** If you cannot locate a Drive file, say so rather than guessing an ID.
- **IRI is mandatory.** Every node — source entry and every knowledge stub — must have
  `id: "pkis:{type}:{slug}"` as its first frontmatter field. A node without `id` is
  a schema violation. Use the singular type names: `source`, `concept`, `technique`,
  `result`, `framework`, `problem`, `principle`, `hypothesis`, `research-cluster`,
  `asset`, `bridge-note`. Assign at creation; never modify.
- **Aliases add value.** Populate `aliases:` thoughtfully — abbreviations, alternative
  names, and synonyms improve the MCP server's concept resolution accuracy. Do not
  leave `aliases: []` for well-known concepts that have common abbreviations or
  synonyms (e.g., MCMC should list `["Markov chain Monte Carlo", "MCMC sampling"]`).

## Session End

### Inbox append (before committing)

At the end of every Librarian session — ingest or park — append the relevant lines
to `wiki/inbox.md` under the matching swim lane, following each lane's convention
(`- [ ] … [Librarian]`). Only the human removes inbox items.

- Any source whose knowledge-object classification was **low confidence** →
  `## Awaiting Classification`
  (e.g. `- [ ] [[source-slug]] § object-name — candidate types: technique or principle (YYYY-MM-DD) [Librarian]`)
- Any **discovery stub** created this session → `## Discovery`
  (e.g. `- [ ] [[discovery-slug]] — rationale (primary: [[concept-slug]]) (YYYY-MM-DD) [Librarian]`)
- Any source whose **Drive ID could not be confirmed** → `## Conformance`
  (e.g. `- [ ] [[source-slug]] — Drive ID unconfirmed (YYYY-MM-DD) [Librarian]`)

This is consistent with the `## Awaiting Classification` section the source entry
already records (Step 3) — the inbox line is the project-wide surface; the section
in the source node is the local record.

### Commit

After completing an ingest (or batch), commit with message:
```
[librarian] ingest: [short title or count]
```

For a park-only session, use:
```
[librarian] park: [short title]
```
