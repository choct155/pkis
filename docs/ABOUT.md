# About PKIS

**PKIS** (Personal Knowledge Integration System) is a git-backed, agent-maintained
knowledge graph spanning six converging technical domains:

- Bayesian statistics
- Deep learning
- Reinforcement learning
- Causal analysis
- Knowledge representation
- Symbolic / sub-symbolic AI

## Why it exists

These fields are converging — and a single person studying across all of them
accumulates more than any pile of notes can keep navigable. The bottleneck isn't
capturing material; it's **integrating** it: seeing that a result in one domain is
the same structure as a technique in another, knowing what is genuinely understood
versus merely filed, and keeping all of it traversable as it grows past thousands
of nodes.

PKIS is that integration layer. Every concept, technique, result, framework,
problem, or principle is **one node**. Nodes are joined by **typed edges**
(`prerequisite-of`, `uses`, `specializes`, `analogous-to`, …). Every node is backed
by **sources**, and every change is **version-controlled markdown** in git.

## Principles

- **Integration over accumulation.** The value lives in the edges, not the node
  count. A new note that connects two existing clusters is worth more than ten
  isolated ones.
- **Capture everywhere, integrate deliberately.** Friction-free capture from any
  device (phone included) lands in an inbox; a deliberate integration pass promotes
  raw captures into structured, sourced, connected nodes.
- **Agent-maintained, human-directed.** Specialized agents (Librarian, Synthesizer,
  Maintenance, Hygienist) do the mechanical work — ingest, enrichment, link
  integrity, orphan detection. The human sets direction and makes the judgment calls.
- **Sourced by default.** A node created before its canonical source exists is
  flagged `needs_canonical_source`; the system actively suggests references.
- **Everything is git.** The knowledge base is plain markdown in a repo. No
  proprietary store, fully diffable, recoverable, and scriptable.

## What it is *not*

- **Not a notes app.** It is a typed graph with conventions (see `SCHEMA.md`), not a
  freeform notebook.
- **Not multi-user.** Single maintainer (`choct155@gmail.com`); colleagues may get
  read access or, via OAuth, scoped write access.

## Relation to ARS and IKS (future)

PKIS is intended as one of **three epistemic layers**. The other two — **ARS** and
**IKS** — are sibling projects, *not yet built*. The expectation:

- **PKIS ↔ ARS** — a **porous** boundary (knowledge flows relatively freely).
- **PKIS ↔ IKS** — a **harder** boundary (a deliberate, controlled interface).

These are recorded here only as named future interface points; nothing in PKIS
depends on them yet.

## The research program

Beyond the domain graph, PKIS hosts a **research-program layer** — research clusters
and hypotheses (e.g. *intensional grounding*) that organize open questions and drive
a frontier-based reading/priority agenda. See the `clusters/` and `hypotheses/` node
types in `SCHEMA.md`.

---

*Next: [`ARCHITECTURE.md`](ARCHITECTURE.md) for how it's built · [`USAGE.md`](USAGE.md)
for how to use it · [`STATUS.md`](STATUS.md) for where it stands now.*
