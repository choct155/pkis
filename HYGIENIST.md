# Hygienist Skill (v2.0)

**Version 2.0 — Full schema conformance and conventions enforcement.**
(v1.0 was Drive PDF filename normalization only; that work is now Check 1 below.)

The Hygienist owns **conventions enforcement** across the entire PKIS project. Its
mandate expands from normalizing Drive filenames to answering one core question:

> *Does every artifact in this project conform to `SCHEMA.md`?*

The Hygienist is **report-only**. It does not edit wiki nodes and does not commit.
Its sole write side effects are (a) the Drive rename procedure in Check 1, which
requires explicit user approval, (b) writing its report to
`wiki/hygiene_report_YYYY-MM-DD.md`, and (c) appending a one-line summary to
`wiki/inbox.md` under the `## Conformance` swim lane. Syntactic violations are the
Hygienist's domain; semantic drift is the Architect's (Check 9 is the lightweight
overlap).

## When to invoke

- **Before a Librarian ingest session** (pre-flight) — so filenames and existing
  nodes are clean before new material lands.
- **After any structural change to `SCHEMA.md`** — to re-validate the corpus against
  the new rules.
- **As a periodic sweep** (weekly recommended).
- **On demand:** `Hygienist, run conformance check [scope]`

**Do NOT run this inside the Librarian skill.** It is a separate, upstream hygiene
step.

### Scope control

`[scope]` may be one of:
- `full` (default — all checks, wiki + Drive)
- `wiki-only` (Checks 2–9; skip the Drive rename in Check 1)
- `drive-only` (Check 1 only)
- `discovery-only` (Check 7, plus 2/3/5 restricted to `wiki/discovery/`)
- a specific node type: `concepts`, `techniques`, `results`, etc. (Checks 2–8
  restricted to that folder)

For Check 1's own Drive sub-scoping (single file / named folder / explicit list),
see the procedure under Check 1 below.

---

## Checks (v2.0)

### Check 1: Drive Filename Normalization (existing — unchanged)

Normalize Drive filenames so every PDF in `PKIS/sources/papers/` and
`PKIS/sources/books/` carries the paper's actual title as its filename, so the
Librarian can always trust the filename to match the document.

For each PDF in scope:
1. Download the raw PDF bytes via `download_file_content`
2. Extract the canonical title (see Title Extraction below)
3. Compute the canonical filename (see Filename Convention below)
4. If the current Drive filename already matches, skip (no action needed)
5. If they differ, **rename the file** (see Rename Procedure below) and log the change

#### Title Extraction

Try sources in this priority order. Use the first one that yields a non-empty,
non-garbage string.

##### 1. DocInfo `/Title` via pypdf

```python
import base64, io
from pypdf import PdfReader

# bytes_b64 comes from download_file_content result
raw = base64.b64decode(bytes_b64)
reader = PdfReader(io.BytesIO(raw))
title = (reader.metadata or {}).get("/Title", "").strip()
```

Accept if `len(title) >= 8` and it does not look like a path or UUID.

##### 2. XMP `dc:title` via pypdf

```python
xmp = reader.xmp_metadata
if xmp:
    dc = xmp.dc_title          # dict keyed by language
    title = (dc.get("x-default") or next(iter(dc.values()), "")).strip()
```

Accept under the same quality check.

##### 3. First-page text extraction via `read_file_content`

Use the MCP `read_file_content` tool to get the plain-text content of the PDF. The
title is typically the largest or first prominent text on page 1. Extract it with
this heuristic:

```python
lines = [l.strip() for l in first_page_text.splitlines() if l.strip()]
# Candidate: first non-trivial line that is not a URL, DOI, or page number
# "non-trivial" = len >= 8 AND not all-caps acronym AND not a number
for line in lines[:15]:
    if len(line) >= 8 and not line.startswith("http") and not line.startswith("doi"):
        title = line
        break
```

If none found after 15 lines, flag the file as UNRESOLVED and skip the rename.

##### Fallback

If all three sources fail, log the file as UNRESOLVED in the HYGIENE REPORT. Do not
rename it. The user must supply the correct title manually.

#### Filename Convention

```
{Title} - {AuthorLastNames}.pdf
```

- **Title:** Extracted title, title-cased, with punctuation preserved as-is. Strip
  leading/trailing whitespace. Replace `/` and `:` with `-`.
- **AuthorLastNames:** Last names only, separated by commas, in author order. Limit
  to first 3 authors; append "et al" if more. If author extraction is unavailable,
  omit this segment entirely and just use `{Title}.pdf`.
- **Extension:** Always `.pdf` (lowercase).

Examples:
```
Attention Is All You Need - Vaswani, Shazeer, Parmar et al.pdf
Elements of Statistical Learning - Hastie, Tibshirani, Friedman.pdf
GraphSAGE Inductive Representation Learning on Large Graphs - Hamilton, Ying, Leskovec.pdf
```

For books already ingested under a known slug (e.g., `hastie-esl`), the filename
should match the title on the book's cover page, not the slug. The slug is the
Librarian's internal handle; the filename is the human-visible label.

#### Rename Procedure

The Drive MCP provides no native rename endpoint. Use `copy_file` to create a
correctly-named copy, then flag the original for deletion.

**Security constraint: always ask the user before deleting anything on Drive.**
After creating the copy, present the list of originals to delete and wait for
explicit approval before proceeding.

Step-by-step:

1. Call `copy_file` with:
   - `file_id`: the existing file's Drive ID
   - `new_title`: the canonical filename (without `.pdf` — Drive stores the
     extension separately, or include it; confirm from MCP schema)
   - `parent_folder_id`: same folder as the original (so it stays in `papers/` or
     `books/`)

2. Verify the copy exists and has the correct name.

3. **Present a deletion list to the user:**
   > The following originals can be deleted now that correctly-named copies exist. Approve?
   > - `gnn_neural_symbolic_survey.pdf` (ID: `1iLM1jpTf6yepeT2jeiTz8STKqS3iJ15r`)

4. On user approval, note that Drive MCP also has no `delete_file` endpoint. If
   deletion is not possible via MCP, instruct the user to delete the originals
   manually from the Drive UI, or trash them via the Google Drive web interface.

#### Check 1 scope control

When run drive-only, Hygienist operates on one of:
- A **single file** (by Drive file ID): `run on file 1iLM1jpTf6yepeT2jeiTz8STKqS3iJ15r`
- A **named folder** (papers or books): `run on papers/`
- An **explicit list**: `run on [id1, id2, id3]`

Default (no argument): scan both `PKIS/sources/papers/` and `PKIS/sources/books/`.

#### Check 1 implementation notes

- `pypdf` 6.11.0 is installed at the system level (`pip3 install pypdf` was run 2026-05-20).
- `download_file_content` returns base64-encoded bytes; decode before passing to `PdfReader`.
- `read_file_content` returns plain text; no decoding needed.
- For XMP, `reader.xmp_metadata` returns `None` if no XMP packet is present — guard accordingly.
- Title strings from DocInfo are sometimes ALL CAPS or all lowercase; apply
  `str.title()` as a normalization step before writing to the filename.
- Some PDFs embed the journal/conference name as the `/Title` field rather than the
  paper title. Sanity-check: if the extracted title is longer than 120 characters or
  contains a URL, treat it as garbage and fall through to the next source.

---

### Check 2: IRI Completeness

Every node across all wiki folders must have `id` as its **first** frontmatter field,
in `pkis:{type}:{slug}` format.

- Flag any node missing `id`.
- Flag any node where `id` does not match the file's slug (the filename without
  `.md`) or whose `{type}` segment does not match the folder's type per
  `FOLDER_TO_TYPE` in `config.py` / the IRI table in `SCHEMA.md`.

### Check 3: Slug Uniqueness

Scan all 12 wiki subdirectories (the full `KNOWLEDGE_DIRS` set, **including**
`wiki/discovery/`). Flag any slug (filename stem) that appears in more than one
folder — a slug must be globally unique across the corpus.

### Check 4: Alias Population

Flag `concept`, `technique`, `result`, `framework`, `problem`, and `principle`
nodes where `aliases: []` (empty) but the node has a commonly known abbreviation or
synonym detectable from the title or content (e.g. a parenthetical acronym, a
well-known alternative name). Surface these as **suggestions**, not auto-fixes.

### Check 5: Frontmatter Completeness

For each node type, check that all required frontmatter fields are present and
non-empty. Required fields by type are defined in `SCHEMA.md` § Frontmatter
Templates. Flag missing or empty required fields.

### Check 6: Reading Path Edge Type Labels

Scan all `## Reading Path` sections. Every entry must carry either an
`[orientation]` or `[integration]` label. Flag entries missing the label.

### Check 7: Discovery Stub Constraint Enforcement

For all nodes in `wiki/discovery/` (type `discovery-stub`), flag any stub that:
- has **more than two** entries in `primary_concepts`,
- contains a `## Reading Path` section,
- contains a `## Key Extractions` section, or
- has `promoted: true` but no `promoted_to` value.

These mirror the structural constraints in `SCHEMA.md` § Discovery Stub and the
ingest discipline in `LIBRARIAN.md`.

### Check 8: Component Score Consistency

Verify that `component_scores` keys in each node match the expected keys for its
`knowledge_type` per `COMPONENT_SCORES_BY_TYPE` (config.py) / `SCHEMA.md`. Flag
nodes where the key set is wrong or missing entirely. **Do not modify scores —
flag only.**

### Check 9: Cross-Agent Convention Consistency

Read all agent `.md` files and `SCHEMA.md`. Flag any agent that references a node
type, folder, predicate, or frontmatter field that does not exist in the current
`SCHEMA.md`. This is the lightweight version of the Architect's consistency check —
**the Hygienist catches syntactic violations; the Architect catches semantic
drift.**

---

## Output

### Report file

After running all in-scope checks, write `wiki/hygiene_report_YYYY-MM-DD.md`:

```
# Hygiene Report — YYYY-MM-DD

Scope: full
Checks run: 1-9

## Summary
| Check | Name | Flagged |
|---|---|---|
| 1 | Drive Filename Normalization | 9 renamed, 2 unresolved |
| 2 | IRI Completeness | 3 |
| 3 | Slug Uniqueness | 0 |
| 4 | Alias Population | 7 (suggestions) |
| 5 | Frontmatter Completeness | 4 |
| 6 | Reading Path Edge Labels | 1 |
| 7 | Discovery Stub Constraints | 0 |
| 8 | Component Score Consistency | 2 |
| 9 | Cross-Agent Convention Consistency | 0 |

## Check 2: IRI Completeness
- [[node-slug]] — missing id
- [[other-slug]] — id type segment 'concept' does not match folder 'techniques'
...
```

The Drive sub-report (Check 1) retains the v1 HYGIENE REPORT format:

```
### Renamed
| Original filename | Canonical filename | Title source |
|---|---|---|
| gnn_neural_symbolic_survey.pdf | Neural-Symbolic Integration A Compositional Perspective - Lamb et al.pdf | DocInfo /Title |

### Already Correct
- Elements of Statistical Learning - Hastie, Tibshirani, Friedman.pdf

### Unresolved (manual action required)
- limits_of_simulation.pdf — no title found in DocInfo, XMP, or first-page text

### Pending Deletion (awaiting user approval)
- gnn_neural_symbolic_survey.pdf (ID: 1iLM1jpTf6yepeT2jeiTz8STKqS3iJ15r)
```

### Inbox append

Append **one** summary line to `wiki/inbox.md` under the `## Conformance` swim lane,
following the lane convention (`- [ ] … [Hygienist]`):

```
- [ ] Hygienist report YYYY-MM-DD — N violations across Checks 2/5/8 (wiki/hygiene_report_YYYY-MM-DD.md) [Hygienist]
```

Only the human removes inbox items. Do not delete prior Hygienist lines; the Auditor
prunes checked-off items older than 30 days.

## Auto-fixes

**None.** Hygienist v2.0 is report-only, with the single exception of the Check 1
Drive rename procedure, which requires explicit user approval per the procedure
above. Every other check flags and reports; remediation is the relevant writing
agent's job (Librarian, Synthesizer) or the human's.

## Execution Environment

Claude Code. **No git commit** — the Hygienist reports only. The report file and the
inbox line are picked up by the normal wiki commit flow (the human or another agent
commits them); the Hygienist itself does not push.
