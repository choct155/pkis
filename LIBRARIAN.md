# Librarian Agent — Operating Procedure
Version: 2.0

## Role

The Librarian ingests new source materials into the wiki. It creates structured
source entries, classifies knowledge objects by type, creates stubs in the appropriate
folders, updates the index and log, and populates the reading queue.

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
| `wiki/index.md` | Yes — add new entries |
| `wiki/log.md` | Yes — append only |
| `wiki/queue.md` | Yes — add items only |
| `raw/clippings/` | Yes — save web-clipped markdown |
| Existing non-stub nodes | No — Synthesizer's domain |

---

## Ingest Workflow

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
drive_id: ""
drive_path: ""
isbn: ""                # books only; ISBN-13 preferred
toc_source: ""          # books only: "openlibrary" | "google-books" | "manual"
parent_book: ""         # book-chapter only; wikilink to parent book entry
chapter:                # book-chapter only; integer chapter number
status: unread
date_added: YYYY-MM-DD
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
   `concept`, `technique`, `result`, `framework`, `problem`, or `principle`.

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
   (status: unread) as its first entry:
   ```markdown
   ## Reading Path
   - [[current-source-slug]] (unread) — brief note on what this source says about the node
   ```

### Step 5: Update index.md

Add the source entry to `## Sources`. Add each new stub to the section matching
its `knowledge_type`:

```
- [[slug]] — one-line description (domain-tag) (YYYY-MM-DD)
```

### Step 6: Update reading queue

Scan nodes linked from this source. For each linked node, check whether its `sources:`
list contains other sources that are unread and not yet in `queue.md`.

Priority rules:
- **High**: sources that are referenced by 3+ existing nodes (high connectivity value)
- **High**: book chapters that are stubs and directly relevant to nodes appearing in
  multiple source entries
- **Normal**: everything else that's unread and plausibly relevant

Add to `wiki/queue.md`:
```
- [ ] [[source-slug]] — one sentence explaining relevance
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
- **Slug uniqueness.** Check ALL 7 wiki subdirectories before creating a slug. No
  two files across the entire wiki may share a slug.
- **Type accuracy matters.** Assign with confidence at high/moderate; escalate at low.
  Do not default to `concept` as a catch-all — if you can't tell, say so and let the
  human make the call. Over time the resolved classifications will calibrate your judgment.
- **Domain coverage.** Every node must have at least one domain tag.
- **Drive ID is mandatory.** If the source came from Drive, `drive_id` must be populated.
- **No invention.** If you cannot locate a Drive file, say so rather than guessing an ID.
- **IRI is mandatory.** Every node — source entry and every knowledge stub — must have
  `id: "pkis:{type}:{slug}"` as its first frontmatter field. A node without `id` is
  a schema violation. Use the singular type names: `source`, `concept`, `technique`,
  `result`, `framework`, `problem`, `principle`. Assign at creation; never modify.
- **Aliases add value.** Populate `aliases:` thoughtfully — abbreviations, alternative
  names, and synonyms improve the MCP server's concept resolution accuracy. Do not
  leave `aliases: []` for well-known concepts that have common abbreviations or
  synonyms (e.g., MCMC should list `["Markov chain Monte Carlo", "MCMC sampling"]`).

## Session End

After completing an ingest (or batch), commit with message:
```
[librarian] ingest: [short title or count]
```
