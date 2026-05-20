# Hygienist Skill

Normalize Drive filenames so every PDF in `PKIS/sources/papers/` and `PKIS/sources/books/` carries the paper's actual title as its filename. Run this skill after uploading new files — before running Librarian — so the Librarian can always trust the filename to match the document.

## When to invoke

- After uploading one or more new PDFs to Drive
- As a periodic audit across the full `papers/` or `books/` folder
- Before a Librarian ingestion session when you suspect filenames are stale

**Do NOT run this inside the Librarian skill.** It is a separate, upstream hygiene step.

## What it does

For each PDF in scope:
1. Download the raw PDF bytes via `download_file_content`
2. Extract the canonical title (see Title Extraction below)
3. Compute the canonical filename (see Filename Convention below)
4. If the current Drive filename already matches, skip (no action needed)
5. If they differ, **rename the file** (see Rename Procedure below) and log the change

Produce a HYGIENE REPORT at the end (see Report Format below).

## Title Extraction

Try sources in this priority order. Use the first one that yields a non-empty, non-garbage string.

### 1. DocInfo `/Title` via pypdf

```python
import base64, io
from pypdf import PdfReader

# bytes_b64 comes from download_file_content result
raw = base64.b64decode(bytes_b64)
reader = PdfReader(io.BytesIO(raw))
title = (reader.metadata or {}).get("/Title", "").strip()
```

Accept if `len(title) >= 8` and it does not look like a path or UUID.

### 2. XMP `dc:title` via pypdf

```python
xmp = reader.xmp_metadata
if xmp:
    dc = xmp.dc_title          # dict keyed by language
    title = (dc.get("x-default") or next(iter(dc.values()), "")).strip()
```

Accept under the same quality check.

### 3. First-page text extraction via `read_file_content`

Use the MCP `read_file_content` tool to get the plain-text content of the PDF. The title is typically the largest or first prominent text on page 1. Extract it with this heuristic:

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

### Fallback

If all three sources fail, log the file as UNRESOLVED in the HYGIENE REPORT. Do not rename it. The user must supply the correct title manually.

## Filename Convention

```
{Title} - {AuthorLastNames}.pdf
```

- **Title:** Extracted title, title-cased, with punctuation preserved as-is. Strip leading/trailing whitespace. Replace `/` and `:` with `-`.
- **AuthorLastNames:** Last names only, separated by commas, in author order. Limit to first 3 authors; append "et al" if more. If author extraction is unavailable, omit this segment entirely and just use `{Title}.pdf`.
- **Extension:** Always `.pdf` (lowercase).

Examples:
```
Attention Is All You Need - Vaswani, Shazeer, Parmar et al.pdf
Elements of Statistical Learning - Hastie, Tibshirani, Friedman.pdf
GraphSAGE Inductive Representation Learning on Large Graphs - Hamilton, Ying, Leskovec.pdf
```

For books already ingested under a known slug (e.g., `hastie-esl`), the filename should match the title on the book's cover page, not the slug. The slug is the Librarian's internal handle; the filename is the human-visible label.

## Rename Procedure

The Drive MCP provides no native rename endpoint. Use `copy_file` to create a correctly-named copy, then flag the original for deletion.

**Security constraint: always ask the user before deleting anything on Drive.** After creating the copy, present the list of originals to delete and wait for explicit approval before proceeding.

Step-by-step:

1. Call `copy_file` with:
   - `file_id`: the existing file's Drive ID
   - `new_title`: the canonical filename (without `.pdf` — Drive stores the extension separately, or include it; confirm from MCP schema)
   - `parent_folder_id`: same folder as the original (so it stays in `papers/` or `books/`)

2. Verify the copy exists and has the correct name.

3. **Present a deletion list to the user:**
   > The following originals can be deleted now that correctly-named copies exist. Approve?
   > - `gnn_neural_symbolic_survey.pdf` (ID: `1iLM1jpTf6yepeT2jeiTz8STKqS3iJ15r`)

4. On user approval, note that Drive MCP also has no `delete_file` endpoint. If deletion is not possible via MCP, instruct the user to delete the originals manually from the Drive UI, or trash them via the Google Drive web interface.

## Report Format

After processing all files in scope, emit a HYGIENE REPORT:

```
## HYGIENE REPORT

Scanned: 13 files
Renamed: 9
Already correct: 2
Unresolved: 2

### Renamed
| Original filename | Canonical filename | Title source |
|---|---|---|
| gnn_neural_symbolic_survey.pdf | Neural-Symbolic Integration A Compositional Perspective - Lamb et al.pdf | DocInfo /Title |
| ... | ... | ... |

### Already Correct
- Elements of Statistical Learning - Hastie, Tibshirani, Friedman.pdf

### Unresolved (manual action required)
- limits_of_simulation.pdf — no title found in DocInfo, XMP, or first-page text
- ...

### Pending Deletion (awaiting user approval)
Files below are the originals that have been copied under their canonical names.
Please delete them from Drive once you have confirmed the copies look correct.
- gnn_neural_symbolic_survey.pdf (ID: 1iLM1jpTf6yepeT2jeiTz8STKqS3iJ15r)
- ...
```

## Scope control

When invoked, Hygienist operates on one of:
- A **single file** (by Drive file ID): `run on file 1iLM1jpTf6yepeT2jeiTz8STKqS3iJ15r`
- A **named folder** (papers or books): `run on papers/`
- An **explicit list**: `run on [id1, id2, id3]`

Default (no argument): scan both `PKIS/sources/papers/` and `PKIS/sources/books/`.

## Implementation notes

- `pypdf` 6.11.0 is installed at the system level (`pip3 install pypdf` was run 2026-05-20).
- `download_file_content` returns base64-encoded bytes; decode before passing to `PdfReader`.
- `read_file_content` returns plain text; no decoding needed.
- For XMP, `reader.xmp_metadata` returns `None` if no XMP packet is present — guard accordingly.
- Title strings from DocInfo are sometimes ALL CAPS or all lowercase; apply `str.title()` as a normalization step before writing to the filename.
- Some PDFs embed the journal/conference name as the `/Title` field rather than the paper title. Sanity-check: if the extracted title is longer than 120 characters or contains a URL, treat it as garbage and fall through to the next source.
