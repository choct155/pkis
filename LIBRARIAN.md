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
| Book chapter | Single source node, note parent book in summary |
| Full book | Book-level index entry + stub entries for each chapter. NO deep ingest. |
| Article / talk | Single source node, full ingest |

For full books: create `wiki/sources/[book-slug].md` with chapter stubs listed in a
`## Chapters` section. Do not create separate source files for each chapter — wait
until a chapter is specifically requested for ingestion.

### Step 3: Create the source entry

Create `wiki/sources/[slug].md` with:

```markdown
---
title: ""
authors: ""
year:
type: paper | book | book-chapter | article | talk
domain: []
tags: []
source_url: ""
drive_id: ""
drive_path: ""
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
```

### Step 4: Classify and create knowledge node stubs

For each knowledge object identified in **Key Knowledge Objects**:

1. **Determine the type.** Ask: Is this an idea with a definition (concept)? A procedure
   (technique)? A proven claim (result)? A coherent system (framework)? A motivating
   challenge (problem)? A guiding constraint (principle)?

2. **Check for existing nodes.** Search ALL 6 knowledge folders for an existing slug
   that matches or nearly matches. Also check existing tags for near-duplicates.
   If a node exists, add this source to its `sources:` frontmatter list and update
   `date_updated`. Do not modify the body.

3. **Create the stub** in the appropriate folder with the correct frontmatter template
   (see SCHEMA.md § Frontmatter Templates). The body is one sentence: what is this
   knowledge object?

4. **If unsure about type,** default to `concept` and add your best alternate guess
   to `also_type`. The Synthesizer will reclassify during deepening if needed.

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
- Created stubs: [[x]] (technique), [[y]] (concept), [[z]] (result)
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
- **Type accuracy matters but isn't precious.** Get it right when it's clear. Default
  to `concept` with `also_type` when it's ambiguous. The Synthesizer will fix it.
- **Domain coverage.** Every node must have at least one domain tag.
- **Drive ID is mandatory.** If the source came from Drive, `drive_id` must be populated.
- **No invention.** If you cannot locate a Drive file, say so rather than guessing an ID.

## Session End

After completing an ingest (or batch), commit with message:
```
[librarian] ingest: [short title or count]
```
