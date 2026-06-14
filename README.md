# PKIS — Personal Knowledge Integration System

A git-backed, agent-maintained knowledge wiki for six converging domains:
Bayesian statistics, deep learning, reinforcement learning, causal analysis,
knowledge representation, and symbolic/sub-symbolic AI.

## Repository Structure

```
pkis/
├── SCHEMA.md          # Global conventions (read this first)
├── LIBRARIAN.md       # Librarian agent operating procedure
├── SYNTHESIZER.md     # Synthesizer agent operating procedure
├── AUDITOR.md         # Auditor agent operating procedure (graph-integrity audits)
├── ARCHITECT.md       # Architect agent operating procedure (system architecture docs)
│
├── raw/
│   ├── clippings/     # Markdown from Obsidian Web Clipper
│   ├── captures/      # Promoted fragments from SQLite inbox
│   └── assets/        # Images referenced by wiki pages
│
└── wiki/
    ├── concepts/      # One .md per concept node
    ├── sources/       # One .md per source (paper, book chapter)
    ├── index.md       # Master catalog — updated on every ingest
    ├── log.md         # Append-only operation log
    └── queue.md       # Reading queue — agent-populated, user-drained
```

## Agents

| Agent | Role | Trigger |
|-------|------|---------|
| Librarian | Ingests source materials, creates structured entries | `Librarian, ingest [source]` |
| Synthesizer | Deepens concept notes, draws cross-domain connections | `Synthesizer, work on [concept/domain]` |
| Auditor | Periodic graph-integrity audits: link integrity, orphan detection, structural gaps | `Auditor, run health check` |
| Architect | Keeps system-architecture docs + product overview true to the code | `Architect, refresh the overview` |

## Domains

- `bayesian-stats`
- `deep-learning`
- `reinforcement-learning`
- `causal-analysis`
- `knowledge-representation`
- `symbolic-subsymbolic`

## Device Access

| Device | Wiki access | Agent invocation |
|--------|-------------|-----------------|
| Workstation / Laptop | git clone, full read/write | Claude Code |
| Phone | GitHub web (read), PWA captures only | Not applicable |

Phone contributions flow through the capture → promotion pathway only.

## Related Infrastructure

Binary source materials (PDFs) live in Google Drive under `PKIS/sources/` — never committed to git.
Raw captures flow from the PWA into a local SQLite inbox and are promoted to `raw/captures/` during weekend integration sessions.
Assessment nodes remain in the SQLite/NetworkX layer and are cross-referenced manually.

## Implementation Plan

See [PKIS_Wiki_Implementation_Plan.md](PKIS_Wiki_Implementation_Plan.md) for the full phased build-out.
