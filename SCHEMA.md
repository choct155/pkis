# PKIS Wiki Schema
Version: 1.1

## Purpose
This is a personal knowledge integration wiki for converging domains centered on
probabilistic reasoning, learning systems, causal inference, and knowledge representation.
The wiki also encompasses methodological connections from prior career work in applied
economics and policy analysis — including forecasting, state-space modeling,
microsimulation, and structural time series.

The wiki is maintained entirely by LLM agents. The human's role is to source
materials, resolve synthesis proposals, and drain the reading queue.

## Core Domains
- `bayesian-stats`
- `deep-learning`
- `reinforcement-learning`
- `causal-analysis`
- `knowledge-representation`
- `symbolic-subsymbolic`

## Extended Domains
These are not second-class — they are fully indexed and cross-linked. The boundary
between core and extended is fuzzy by design; connections across it are high-value.

- `state-space-models`
- `time-series`
- `forecasting`
- `microsimulation`
- `philosophy-of-science`
- `optimization`
- `information-theory`

New domain tags may be introduced by the Librarian when an ingested source clearly
falls outside all existing tags. Tag names must be lowercase-hyphenated.

## Google Drive — Source of Truth for Binaries
No PDFs or binary files are committed to git. All binaries live in Google Drive under:

```
PKIS/
  sources/
    papers/     Drive ID: 1hTtbvU2TxWjGa0MX_bnnYUlOzQ9oAh3I
    books/      Drive ID: 1_hsD5_spfs_6B9iadd44GhSqvetF2CKZ
    assets/     (images and supporting figures)
```

Source entries reference Drive files by **file ID**, not by path. Paths change;
IDs do not.

## Folder Conventions
- `raw/clippings/`  — web-clipped markdown sources, immutable once written
- `raw/captures/`   — promoted fragments from the capture inbox, immutable
- `raw/assets/`     — images referenced in wiki pages
- `wiki/concepts/`  — one file per concept, agent-maintained
- `wiki/sources/`   — one file per source document, agent-maintained

## Frontmatter: Source Entry
Every file in `wiki/sources/` must have this frontmatter:

```yaml
---
title: ""
authors: ""
year:
type: paper | book | book-chapter | article | talk
domain: []          # one or more tags from the domain vocabulary above
source_url: ""      # arXiv URL, DOI, or similar; omit field if not web-available
drive_id: ""        # Google Drive file ID — primary reference
drive_path: ""      # Human-readable Drive path for orientation only
status: unread | reading | completed | paused
date_added: YYYY-MM-DD
concepts: []        # wikilinks to concept nodes this source covers
---
```

## Frontmatter: Concept Entry
Every file in `wiki/concepts/` must have this frontmatter:

```yaml
---
title: ""
domain: []           # one or more domain tags
related_concepts: [] # wikilinks to other concept nodes
sources: []          # wikilinks to source entries that cover this concept
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
confidence: 0        # 0=stub, 1=skeleton, 2=draft, 3=solid, 4=deep, 5=well-integrated
---
```

## Wikilink Convention
Use standard Obsidian wikilink format: `[[filename-without-extension]]`
- Concept links → files in `wiki/concepts/`
- Source links → files in `wiki/sources/`
- Slugs are always lowercase-hyphenated: `variational-inference`, not `VariationalInference`

## index.md Convention
Catalog format. Each entry:
```
- [[filename]] — one-line summary (domain tag) (date added)
```
Organized into sections: `## Concepts` | `## Sources` | `## Reading Queue`

## log.md Convention
Append-only. Each entry:
```
## [YYYY-MM-DD] operation-type | title
- Brief description of what was done
- Files created or modified
```

## queue.md Convention
Prioritized list. Format:
```
### High
- [ ] [[source-filename]] — reason for priority

### Normal
- [ ] [[source-filename]] — reason for priority
```
Agent adds items. User checks them off when read.
