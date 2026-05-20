# PKIS Wiki — Implementation Plan
**For:** Claude Code  
**Version:** 1.0 · May 2026  
**Owner:** Marvin  

---

## Context and Goals

This plan instantiates a personal knowledge base (the "wiki") for the Personal Knowledge Integration System (PKIS). The wiki sits between raw source materials and active learning — it is a persistent, compounding artifact maintained by LLM agents, not by the user directly.

The system must be:
- **Multi-device accessible** — workstation, laptop, and phone
- **Git-backed** — markdown as ground truth, version history preserved
- **Agent-maintainable** — three specialized agents handle ingestion, synthesis, and maintenance
- **Incrementally buildable** — Phase 1 is the Librarian only; Synthesizer and Maintenance follow

The wiki is a *complement* to the existing PKIS capture infrastructure (PWA → SQLite inbox), not a replacement. Raw captures from the phone continue to flow into the SQLite inbox. The wiki is where integrated, structured knowledge lives.

---

## Repository Structure

Create a new GitHub repository: `pkis-wiki`

```
pkis-wiki/
│
├── SCHEMA.md                  # Global conventions (read this first)
├── LIBRARIAN.md               # Librarian agent operating procedure
├── SYNTHESIZER.md             # Synthesizer agent operating procedure  
├── MAINTENANCE.md             # Maintenance agent operating procedure
│
├── raw/
│   ├── clippings/             # Markdown from Obsidian Web Clipper
│   ├── captures/              # Promoted fragments from SQLite inbox
│   └── assets/                # Images referenced by wiki pages
│
├── wiki/
│   ├── concepts/              # One .md per concept node
│   ├── sources/               # One .md per source (paper, book chapter)
│   ├── index.md               # Master catalog — updated on every ingest
│   ├── log.md                 # Append-only operation log
│   └── queue.md               # Reading queue — agent-populated, user-drained
│
└── .gitattributes             # Git LFS config (if needed later)
```

**Important separation:** This repo is the PKIS wiki — conceptual knowledge only. Work captures (the Org Graph) remain in a separate local-only repo and are never pushed to GitHub.

---

## Google Drive Integration

All PDFs and binary source materials live in Google Drive, not in the git repo. The agent has Drive access via MCP.

**Folder structure in Drive:**
```
PKIS/
  sources/
    papers/        # arxiv and other freely available papers (PDF)
    books/         # Textbooks and non-freely-available PDFs
    assets/        # Supporting images and figures
```

The wiki's source entries reference Drive locations via frontmatter. The agent can read from and write to Drive directly during ingestion. No PDFs are committed to git.

---

## SCHEMA.md — Global Conventions

This file governs all three agents. It must be read at the start of every agent session. Create it with the following content:

```markdown
# PKIS Wiki Schema
Version: 1.0

## Purpose
This is a personal knowledge integration wiki for six converging domains:
Bayesian statistics, deep learning, reinforcement learning, causal analysis,
knowledge representation, and symbolic/sub-symbolic AI.

The wiki is maintained entirely by LLM agents. The human's role is to source
materials, resolve synthesis proposals, and drain the reading queue.

## Domains
- `bayesian-stats`
- `deep-learning`
- `reinforcement-learning`
- `causal-analysis`
- `knowledge-representation`
- `symbolic-subsymbolic`

## Folder Conventions
- `raw/clippings/`  — web-clipped markdown sources, immutable
- `raw/captures/`   — promoted fragments from the capture inbox, immutable
- `raw/assets/`     — images referenced in wiki pages
- `wiki/concepts/`  — one file per concept, agent-maintained
- `wiki/sources/`   — one file per source document, agent-maintained

## Frontmatter: Source Entry
Every file in wiki/sources/ must have this frontmatter:

---
title: ""
authors: ""
year: 
type: paper | book-chapter | article | talk
domain: [list of domains from controlled vocabulary above]
source_url: ""        # arxiv URL or similar; null if not web-available
drive_path: ""        # Google Drive path; null if web-available
status: unread | reading | completed | paused
date_added: YYYY-MM-DD
concepts: []          # wikilinks to concept nodes this source covers
---

## Frontmatter: Concept Entry
Every file in wiki/concepts/ must have this frontmatter:

---
title: ""
domain: [list]
related_concepts: []  # wikilinks
sources: []           # wikilinks to source entries that cover this concept
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
confidence: 0-5       # 0=stub, 5=well-integrated
---

## Wikilink Convention
Use standard Obsidian wikilink format: [[filename-without-extension]]
All concept links point to files in wiki/concepts/
All source links point to files in wiki/sources/

## index.md Convention
index.md is a catalog. Format each entry as:
- [[filename]] — one-line summary (domain tag) (date added)
Organized into sections: ## Concepts | ## Sources | ## Reading Queue

## log.md Convention
Append-only. Each entry:
## [YYYY-MM-DD] operation-type | title
- Brief description of what was done
- Files created or modified

## queue.md Convention
Simple prioritized list. Format:
### High
- [ ] [[source-filename]] — reason for priority

### Normal  
- [ ] [[source-filename]] — reason for priority

Agent adds items. User checks them off when read.
```

---

## LIBRARIAN.md — Librarian Agent

```markdown
# Librarian Agent — Operating Procedure
Version: 1.0

## Role
The Librarian ingests new source materials into the wiki. It creates structured
entries, updates the index and log, and populates the reading queue with related
unread materials.

## Trigger
Invoked explicitly: "Librarian, ingest [source]"
Source may be: a URL, a Google Drive path, or a raw/ directory file.

## Tools Available
- Read/write access to entire pkis-wiki repo
- Google Drive MCP: read files, write to PKIS/sources/ folder
- Web fetch: retrieve content from URLs
- Anthropic API: content extraction and summarization

## Write Permissions
ALLOWED: wiki/sources/, wiki/concepts/ (stub creation only),
         wiki/index.md, wiki/log.md, wiki/queue.md, raw/
NOT ALLOWED: Modifying existing concept notes (that is the Synthesizer's job)

## Ingest Workflow

### Step 1: Retrieve the source
- If URL: fetch content, convert to markdown, save to raw/clippings/[slug].md
- If Drive path: confirm file exists and is readable
- If already in raw/: proceed to Step 2

### Step 2: Assess the source type
- Paper (≤50 pages): ingest as single source node
- Book chapter: ingest as single source node, note parent book
- Full book: create book index entry + stub entries for each chapter.
  DO NOT deep-ingest the full book. Stubs only.

### Step 3: Create the source entry
Create wiki/sources/[slug].md with:
- Complete frontmatter per SCHEMA.md
- ## Summary section (150-300 words): what this source argues/covers
- ## Key Concepts section: bulleted list of concepts this source introduces
  or substantially covers, each as a wikilink [[concept-slug]]
- ## Key Extractions section: 3-7 specific claims, methods, or findings
  worth preserving verbatim or near-verbatim
- ## Connection Candidates section: existing concept nodes or sources
  this might connect to (for Synthesizer to act on later)

### Step 4: Create or update concept stubs
For each concept in ## Key Concepts that does not yet have a
wiki/concepts/[slug].md file, create a stub:
- Complete frontmatter
- One-sentence description
- Source wikilink in frontmatter
DO NOT write full concept notes. Stubs only. Depth comes from the Synthesizer.

### Step 5: Update index.md
Add the new source to the ## Sources section.
Add any new concept stubs to the ## Concepts section.

### Step 6: Update reading queue
Scan existing concept nodes linked from this source.
If any linked concept nodes reference other sources that are unread
and relevant, add them to queue.md under appropriate priority.
Book chapters that are stubs and highly relevant to current
concept frontier: High priority.
Everything else: Normal priority.

### Step 7: Append to log.md
Record the operation with files created/modified.

## Quality Standards
- Never hallucinate citations or claims not present in the source
- If PDF extraction quality is poor, note it in the source entry
  and flag for manual review
- Concept slugs must be lowercase-hyphenated: variational-inference, not VariationalInference
- Every source entry must have at least one domain tag
```

---

## SYNTHESIZER.md — Synthesizer Agent

```markdown
# Synthesizer Agent — Operating Procedure
Version: 1.0

## Role
The Synthesizer deepens concept notes and draws connections across the wiki.
It proposes; the human resolves. It never commits changes without approval.

## Trigger
Invoked during weekend integration sessions:
"Synthesizer, work on [concept or domain or 'the inbox']"

Also triggered at the end of a domain block (assessment boundary).

## Tools Available
- Read access to entire pkis-wiki repo
- Read access to raw/captures/ (promoted inbox fragments)
- Write access ONLY after explicit human approval per change
- Anthropic API for synthesis work

## Write Permissions
ALLOWED (after approval): wiki/concepts/, wiki/sources/ (connection updates only)
NOT ALLOWED: raw/, index.md structural changes, log.md (Librarian writes log)

## Synthesis Workflow

### Mode 1: Concept deepening
Invoked for a specific concept: "Synthesizer, deepen [[variational-inference]]"

1. Read the concept stub and all linked sources
2. Read related concept nodes
3. Draft an updated concept note with:
   - ## Definition: precise, technically accurate
   - ## Intuition: one concrete analogy or worked example
   - ## Formal Statement (if applicable): key equations or algorithms
   - ## Connections: typed links to related concepts with explanation
     of the relationship (generalizes / specializes / contrasts /
     extends / applies / prerequisite-of)
   - ## Applications: where this concept is used in practice
   - ## Open Questions: what you don't yet understand about this concept
4. Present the draft to the human for review
5. On approval, write the file and update confidence score

### Mode 2: Connection discovery
Invoked broadly: "Synthesizer, find connections in [domain]"

1. Read all concept nodes in the specified domain
2. Identify non-obvious cross-domain connections
3. Present a ranked list of proposed connections with justification
4. Human selects which to develop
5. Synthesizer drafts the connection explanation for each selected pair
6. On approval, update both concept nodes with the new connection

### Mode 3: Inbox integration
Invoked after capture review: "Synthesizer, integrate these captures: [list]"

1. Read each capture fragment
2. Identify which existing concept node(s) it most relevantly extends
3. Propose either: (a) update to existing concept note, or
   (b) creation of new concept stub if no existing node fits
4. Present proposals grouped by concept
5. On human resolution, write approved updates

## Quality Standards
- Cross-domain connections are the highest-value output. Prefer them.
- Never invent connections not evidenced by source material
- Distinguish structural analogies from shared mechanisms — they are different
- Flag when a connection requires reading a queued source before it can be made
- Confidence scores increase only when multiple sources and the human confirm
```

---

## MAINTENANCE.md — Maintenance Agent

```markdown
# Maintenance Agent — Operating Procedure
Version: 1.0

## Role
The Maintenance agent performs periodic health checks on the wiki.
It produces a report; it does not make changes except for auto-fixable issues.

## Trigger
Run fortnightly or when wiki has grown significantly (>20 new sources since
last maintenance pass).
"Maintenance, run health check"

## Tools Available
- Read access to entire pkis-wiki repo
- Write access ONLY for auto-fixable issues (dead internal links, missing
  index entries)
- Produces maintenance_report.md for human review

## Health Check Workflow

Run these checks. Each may spawn a parallel sub-task.

### Check 1: Link integrity
- Scan all wikilinks across the wiki
- Identify dead links (target file does not exist)
- Auto-fix: if the target is a concept stub that should exist, create it
- Flag for human: links that cannot be auto-resolved

### Check 2: Orphan detection
- Identify concept nodes with no inbound links
- Identify source entries not referenced by any concept node
- Flag all orphans — human decides whether to connect or delete

### Check 3: Index completeness
- Verify every file in wiki/concepts/ and wiki/sources/ appears in index.md
- Auto-fix: add missing entries to index.md

### Check 4: Concept staleness
- For each concept note with confidence >= 3, check whether any source
  added since the concept was last updated contradicts or supersedes it
- Flag contradictions for human review with specific source citations

### Check 5: Queue hygiene
- Flag items that have been in queue.md for more than 30 days
- Propose reprioritization or removal for items no longer relevant

### Check 6: Connection gaps
- For each domain, identify concept nodes with fewer than 2 cross-domain
  connections
- Suggest which other domains likely contain relevant connection candidates

### Check 7: Stub graduation candidates
- List concept stubs (confidence 0-1) that have 3+ sources referencing them
- These are ready for Synthesizer deepening

## Report Format
Write to wiki/maintenance_report_[YYYY-MM-DD].md:

# Maintenance Report — [date]

## Auto-Fixed
[list of changes made automatically]

## Requires Human Action
### Critical (contradictions, dead links not auto-fixable)
### Normal (orphans, staleness, queue hygiene)
### Low (connection gaps, stub graduation candidates)

## Wiki Health Metrics
- Total concept nodes: N
- Total source entries: N  
- Average confidence score: X
- Cross-domain connections: N
- Items in reading queue: N
- Stubs awaiting deepening: N
```

---

## Phase 1 Implementation Steps

Execute these in order. Do not skip ahead.

### Step 1: Initialize the repository
```bash
git init pkis-wiki
cd pkis-wiki
mkdir -p raw/clippings raw/captures raw/assets
mkdir -p wiki/concepts wiki/sources
touch wiki/index.md wiki/log.md wiki/queue.md
```

Initialize index.md with sections:
```markdown
# PKIS Wiki Index

## Concepts

## Sources

## Reading Queue
```

Initialize log.md with:
```markdown
# PKIS Wiki Log
```

Initialize queue.md with:
```markdown
# Reading Queue

### High

### Normal
```

### Step 2: Create SCHEMA.md, LIBRARIAN.md, SYNTHESIZER.md, MAINTENANCE.md
Paste the content from this document into each file.

### Step 3: Connect Google Drive
Verify the Google Drive MCP connection is active and that the agent
can read from and write to `PKIS/sources/` in Drive.
Test with a single file read before proceeding.

### Step 4: First ingest
Choose a paper you know well — something already integrated in your
thinking — as the first test case. This lets you evaluate extraction
quality against your own knowledge.

Invoke: "Librarian, ingest [URL or Drive path]"

Review the output carefully:
- Is the summary accurate?
- Are the key extractions faithful to the source?
- Are the concept stubs named sensibly?
- Did index.md and log.md update correctly?

Adjust LIBRARIAN.md based on what you find.

### Step 5: Ingest 10-15 sources
Cover at least two domains. Mix papers and book chapters.
Include at least one book index pass (stubs only, no deep ingestion).

Do not invoke the Synthesizer yet. Build corpus first.

### Step 6: First Synthesizer session
Pick the concept with the most source references.
Invoke: "Synthesizer, deepen [[concept-name]]"

Review the draft. The quality of this output is your signal for
whether the Synthesizer prompt needs adjustment before you trust
it to run broadly.

### Step 7: First Maintenance pass
After 20+ sources are ingested.
Invoke: "Maintenance, run health check"
Review the report. Resolve critical items.

---

## Integration with Existing PKIS Infrastructure

The wiki is a new layer. Existing infrastructure continues unchanged.

**Capture flow (unchanged):**
PWA → SQLite inbox → awaits weekend integration

**New promotion flow:**
During weekend sessions, captures relevant to wiki concepts get promoted:
1. Export relevant captures from SQLite to raw/captures/ as markdown files
2. Invoke Synthesizer in inbox integration mode to wire them into concept notes

**Reading queue → capture loop:**
When you read a queued chapter or paper, capture key insights via the PWA
as normal. They will be promoted and integrated in the next weekend session.

**Assessment module (unchanged):**
Assessment nodes remain in the SQLite/NetworkX layer. The wiki and the
assessment module are separate systems. Cross-reference manually when needed.

---

## Multi-Device Access

| Device | Wiki access | Raw source access | Agent invocation |
|--------|-------------|-------------------|-----------------|
| Workstation | git clone, full read/write | Drive desktop app | Claude Code |
| Laptop | git clone, full read/write | Drive desktop app | Claude Code |
| Phone | GitHub web (read), PWA captures only | Drive mobile app | Not applicable |

Phone contribution to the wiki is always via capture → promotion pathway,
never direct wiki editing. This is by design.

Sync procedure:
- Before any session: `git pull`
- After any session: `git add -A && git commit -m "[agent] brief description" && git push`

The agent should handle commits as part of its workflow. Each agent session
ends with a commit.

---

## Decisions Deferred to Later Phases

These are explicitly out of scope for Phase 1:

- **Qdrant / vector search** — deferred until corpus scale makes
  in-context retrieval insufficient (rough threshold: 200+ concept nodes)
- **Audio brief integration** — wiki content feeds the brief generator
  once the Synthesizer is running well; wiring is straightforward then
- **Automated schedule triggers** — agents are invoked manually in Phase 1;
  automation is a Phase 2 consideration
- **Git LFS** — not needed while all binaries live in Drive; revisit
  only if offline access to PDFs becomes a hard requirement
- **Neo4j migration** — NetworkX remains the graph layer; wiki markdown
  is a separate surface, not a replacement

---

## What Success Looks Like at End of Phase 1

After approximately 4-6 focused weekend sessions:

1. 30-50 source entries covering all six domains
2. 20-40 concept nodes at varying depths (mix of stubs and deep notes)
3. Reading queue populated and actively draining
4. At least one substantive cross-domain connection identified by the Synthesizer
5. First maintenance report run and resolved
6. Agent behavior stable enough that you trust it without reviewing every edit

At that point, the Synthesizer moves from proposal mode toward higher autonomy,
and the system starts generating genuine integration value rather than
just organizing what you already know.
