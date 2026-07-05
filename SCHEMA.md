# PKIS Wiki Schema
Version: 3.0

## Purpose

This is a personal knowledge integration wiki for converging domains centered on
probabilistic reasoning, learning systems, causal inference, and knowledge representation.
The wiki also encompasses methodological connections from prior career work in applied
economics and policy analysis — including forecasting, state-space modeling,
microsimulation, and structural time series.

The wiki is maintained entirely by LLM agents. The human's role is to source
materials, resolve synthesis proposals, and drain the reading queue.

---

## Graph Structure

The wiki is a **multipartite knowledge graph** with 7 node types. Nodes live in
type-specific folders. Edges are typed wikilinks annotated with one of 8 core
relationship predicates. The predicate's interpretation depends on the types of
the nodes it connects — see the interpretation table below.

```
wiki/
  sources/        # documents: papers, books, articles, talks
  concepts/       # ideas with definitions: posterior distribution, d-separation
  techniques/     # procedures with inputs and outputs: MCMC, backpropagation
  results/        # proven or established claims: Bayes' theorem, universal approximation
  frameworks/     # coherent systems of concepts and methods: structural causal models, MDPs
  problems/       # motivating challenges: credit assignment, exploration-exploitation
  principles/     # guiding constraints: exchangeability, parsimony, falsifiability
  hypotheses/     # open questions requiring analytical resolution [infrastructure]
  clusters/       # research cluster nodes organizing hypothesis families [infrastructure]
  assets/         # durable learner-produced outputs: code, derivations, analyses [infrastructure]
  bridge-notes/   # ephemeral cross-domain connection captures [infrastructure]
  staging/        # two-phase write staging area — agent-written, human-reviewed [infrastructure]
```

### Node Type Descriptions

The wiki has two categories of node types.

**Knowledge nodes** — the seven original types, in production since launch:

| Type | What it represents | Distinguishing question |
|---|---|---|
| **Source** | A document in the corpus | "What did this author write?" |
| **Concept** | An idea with a definition and boundary | "What IS this thing?" |
| **Technique** | A procedure that takes inputs and produces outputs | "How do I DO this?" |
| **Result** | A proven or established claim | "What do we KNOW for certain?" |
| **Framework** | A coherent system that organizes concepts, techniques, and results | "How does this field THINK about problems?" |
| **Problem** | A well-defined challenge that motivates methods | "What are we TRYING to solve?" |
| **Principle** | A guiding idea that constrains or evaluates other knowledge | "What SHOULD guide our choices?" |

**Infrastructure nodes** — four types added in v3.0:

| Type | What it represents | Distinguishing question |
|---|---|---|
| **Hypothesis** | An open question or claim requiring analytical resolution | "What do I need to find out?" |
| **Research Cluster** | An organizing unit grouping related hypotheses into a research agenda | "What family of questions is this part of?" |
| **Asset** | A durable output produced by the learner evidencing understanding | "What have I built that demonstrates this?" |
| **Bridge Note** | An ephemeral cross-domain connection capture awaiting integration | "What connection did I just notice?" |

Infrastructure nodes carry `id` and follow IRI conventions but do not carry `component_scores`. Bridge notes are created only by the MCP `create_bridge_note` endpoint, never manually.

### Boundary Cases

Some knowledge objects straddle types. Handle this with canonical type + secondary typing:

```yaml
knowledge_type: technique       # canonical — determines folder and template
also_type: [framework]          # secondary — MCMC is also a framework for sub-techniques
```

The file lives in one folder (determined by `knowledge_type`). The `also_type` field
enables queries from other angles. The Librarian assigns its best guess at ingest;
the Synthesizer may propose reclassification during deepening.

### Disambiguation

When a term means different things in different domains (e.g., "identification" in
econometrics vs. causal inference vs. control theory), use a **single node** with a
`## Disambiguation` section at the top of the body, followed by domain-tagged
subsections. This forces explicit comparison of the meanings rather than isolating
them on separate islands.

---

## Domains

### Core Domains
- `bayesian-stats`
- `deep-learning`
- `reinforcement-learning`
- `causal-analysis`
- `knowledge-representation`
- `symbolic-subsymbolic`

### Extended Domains
- `state-space-models`
- `time-series`
- `forecasting`
- `microsimulation`
- `philosophy-of-science`
- `optimization`
- `information-theory`

Core and extended are not a hierarchy of importance — they are equally indexed and
cross-linked. New domain tags may be introduced by the Librarian when an ingested
source clearly falls outside all existing tags. Tag names are lowercase-hyphenated.

---

## Tags

Tags are a second classification axis, orthogonal to domains. They capture
cross-cutting mathematical substrates, methodological families, and epistemic themes:

```yaml
tags: [linear-algebra, probability-theory, measure-theory, graph-theory,
       dynamic-programming, variational-methods, epistemology, simulation]
```

Tags are **open vocabulary** — agents may introduce new tags freely. But the Librarian
must check existing tags across the wiki before coining a new one, and the Auditor
agent flags near-duplicates.

**Tags vs. nodes:** Tags are navigational markers. If a tag keeps appearing on many
nodes and the corpus has something substantive to say about the tag itself (not just
about things it labels), that's a signal it may deserve its own concept node.

---

## Epistemic Status

Every knowledge node carries three independent status dimensions plus component-level anatomy scores.

```yaml
coverage: 0          # 0=stub, 1=one source, 2=two sources, 3=several, 4=well-sourced, 5=exhaustive
understanding: 0     # 0=unfamiliar, 1=aware, 2=foggy, 3=working, 4=solid, 5=deeply integrated
maturity: settled    # settled | evolving | contested | historical
```

- **coverage** — agent-maintained. Tracks how many sources substantiate the node.
- **understanding** — human-maintained only. Updated during Synthesizer review sessions.
  Agents never modify this field.
- **maturity** — agent-proposed, human-confirmed. Reflects the state of the concept
  in the literature, not the user's grasp of it.

### Component Scores (v3.0)

All six non-source knowledge node types (concept, technique, result, framework, problem,
principle) additionally carry a `component_scores` dictionary. This replaces the single
undifferentiated confidence score with anatomy-specific dimensions per node type.

**Rules:**
- Human-maintained only — agents never write to `component_scores`
- Scoring rubric: `null` = unassessed; `1` = aware; `2` = partial; `3` = working; `4` = solid; `5` = deeply integrated
- Lazy population: existing nodes have all components set to `null` at migration; scores
  are populated as depth-creation sessions happen
- New nodes created after v3.0 carry the full `component_scores` block with all nulls

**Component names by node type:**

| Concept | Technique | Framework | Result | Problem | Principle |
|---|---|---|---|---|---|
| definition | operational_mechanism | structure | statement | formulation | statement |
| prerequisites | principled_mechanism | purpose | proof_sketch | why_hard | justification |
| boundary | conditions | primitives | conditions | solution_landscape | implications |
| scope | implementation | scope | implications | instances | violations |
| application | diagnostics | application | limitations | | |
| formal_statement | alternatives | limits | | | |
| dependents | failure_modes | | | | |
| transfer | | | | | |

Source nodes do not carry `component_scores` — sources are references, not subjects of mastery.

---

## Relationship Predicates

The graph supports **13 typed predicates** — the set in `config.EDGE_WEIGHTS`, which is
the runtime registry the graph builder reads and `add_connections` validates against.
Each has a general meaning whose specific interpretation depends on the subject and
object node types. (This table is the documented mirror of `config.EDGE_WEIGHTS`; keep
them in sync.)

### Predicate Definitions

| Predicate | General meaning | Inverse |
|---|---|---|
| `specializes` | Subject is a more specific version of object | `generalizes` |
| `generalizes` | Subject is a more general version of object | `specializes` |
| `prerequisite-of` | Subject must be understood before object | — |
| `uses` | Subject employs or operates on object | `used-by` |
| `applies` | Subject applies object to a domain or problem | — |
| `instantiates` | Subject is a concrete instance of object | — |
| `extends` | Subject builds upon object, adding capability | — |
| `contrasts-with` | Subject and object are alternatives or in tension | (symmetric) |
| `analogous-to` | Subject is structurally analogous to object (same structure, different mechanism/domain) | (symmetric) |
| `illustrated-by` | Subject is illustrated/explained by object (an interactive asset) | — |
| `evidence-for` | Subject (a Finding) is empirical evidence bearing on object (a Hypothesis) | — |
| `implemented-by` | Subject (a concept/technique) is concretely realized by object (a Resource) | — |
| `superseded-by` | Subject (a Resource) has been replaced or made obsolete by object (a Resource) | — |

**Proposed (not yet implemented).** These read well but are **not** in `config.EDGE_WEIGHTS`,
so the graph builder ignores them and `add_connections` rejects them — using them in
frontmatter today has no effect. Add them to `EDGE_WEIGHTS` (with a weight) before use:
`grounds` (epistemic/theoretical foundation for object), `equivalent-in-context` (same
idea under different names across domains, symmetric), `commonly-confused-with` (appear
similar but differ, symmetric).

### Interpretation Table

The table below encodes what each predicate means for common subject → object type
pairs. When creating a relationship, look up the pair to confirm the intended semantics.
Unlisted combinations use the obvious reading of the general meaning; if no obvious
reading exists, the combination is probably the wrong predicate.

#### `specializes` / `generalizes`

| Subject → Object | Interpretation | Example |
|---|---|---|
| concept → concept | X is a special case of Y | posterior distribution specializes probability distribution |
| technique → technique | X is a specialized form of Y | HMC specializes MCMC |
| result → result | X is a specific instance of Y | Bernstein-von Mises specializes asymptotic normality |
| framework → framework | X narrows the scope of Y | POMDPs specialize MDPs |
| problem → problem | X is a constrained version of Y | multi-armed bandits specialize explore-exploit |
| principle → principle | X is a domain-specific form of Y | exchangeability specializes symmetry |

#### `prerequisite-of`

| Subject → Object | Interpretation | Example |
|---|---|---|
| concept → concept | Understanding X is necessary for Y | probability theory prerequisite-of Bayesian inference |
| concept → technique | X must be understood to apply Y | matrix decomposition prerequisite-of PCA |
| concept → framework | X is foundational knowledge for Y | graph theory prerequisite-of structural causal models |
| concept → result | X must be understood to appreciate Y | convergence prerequisite-of CLT |
| technique → technique | X must be mastered before Y | gradient computation prerequisite-of backpropagation |
| result → technique | X must be known to justify use of Y | detailed balance prerequisite-of Metropolis-Hastings |
| result → result | X is used in the proof of Y | Markov inequality prerequisite-of Chebyshev inequality |

#### `uses`

| Subject → Object | Interpretation | Example |
|---|---|---|
| technique → concept | X operates on instances of Y | MCMC uses Markov chains |
| technique → technique | X calls Y as a subroutine | NUTS uses leapfrog integration |
| technique → result | X depends on Y for correctness | MCMC uses detailed balance |
| framework → concept | X incorporates Y as a building block | SCMs use d-separation |
| framework → technique | X employs Y as a computational method | Bayesian inference uses MCMC |
| framework → principle | X assumes Y as a foundational commitment | Bayesian statistics uses exchangeability |
| result → concept | Y appears in the statement or proof of X | CLT uses normal distribution |
| result → technique | X establishes properties of Y | convergence theorem characterizes MCMC |

#### `contrasts-with`

| Subject → Object | Interpretation | Example |
|---|---|---|
| concept → concept | X and Y are alternative formulations | frequentist probability contrasts Bayesian probability |
| technique → technique | X and Y are competing approaches to similar problems | MCMC contrasts variational inference |
| framework → framework | X and Y are rival paradigms | SCMs contrast potential outcomes framework |
| principle → principle | X and Y are in tension | parsimony contrasts expressiveness |

#### `extends`

| Subject → Object | Interpretation | Example |
|---|---|---|
| technique → technique | X adds capability to Y | HMC extends Metropolis-Hastings with gradient information |
| result → result | X strengthens or broadens Y | Bernstein-von Mises extends CLT to posterior distributions |
| framework → framework | X adds structure or generality to Y | POMDPs extend MDPs with partial observability |
| concept → concept | X refines Y with additional structure | conditional independence extends independence |

#### `grounds`

Use for epistemic, philosophical, or theoretical justification — not technical
prerequisites (use `prerequisite-of` for those). The distinction: you need
probability to do Bayesian statistics (`prerequisite-of`), but exchangeability
provides the philosophical justification for Bayesian statistics (`grounds`).

| Subject → Object | Interpretation | Example |
|---|---|---|
| principle → concept | X provides philosophical justification for Y | falsifiability grounds hypothesis testing |
| principle → technique | X provides normative justification for Y | exchangeability grounds Bayesian bootstrap |
| principle → framework | X provides foundational assumptions for Y | counterfactual reasoning grounds SCMs |
| result → technique | X provides theoretical guarantee for Y | convergence theorem grounds MCMC |
| result → framework | X provides theoretical foundation for Y | Cox's theorem grounds Bayesian probability |

#### `equivalent-in-context`

| Subject → Object | Interpretation | Example |
|---|---|---|
| concept → concept | X in domain A is the same as Y in domain B | identification (econometrics) ≡ identification (causal inference) |
| technique → technique | X in domain A is the same procedure as Y in domain B | Kalman filter ≡ recursive Bayesian estimation |

Mostly used between nodes of the same knowledge type. When used, the
`## Disambiguation` section in the relevant node should explain the contexts.

#### `commonly-confused-with`

| Subject → Object | Interpretation | Example |
|---|---|---|
| concept → concept | X appears similar to Y but they differ in important ways | correlation commonly-confused-with causation |
| technique → technique | X appears similar to Y but has different properties or assumptions | L1 regularization commonly-confused-with feature selection |

When used, both nodes should document the distinction in their bodies.

### Encoding Relationships in Markdown

In the `## Connections` section of a node, encode each relationship as:

```markdown
- [[target-slug]] — predicate: one sentence explaining this specific connection
```

Example:
```markdown
## Connections
- [[markov-chain]] — uses: MCMC constructs a Markov chain whose stationary distribution is the target posterior
- [[metropolis-hastings]] — generalizes: MCMC is the family; MH is the foundational specific algorithm
- [[variational-inference]] — contrasts-with: both approximate posteriors, but MCMC is asymptotically exact while VI trades accuracy for speed
- [[detailed-balance]] — uses: correctness of MCMC depends on the chain satisfying detailed balance
- [[exchangeability]] — grounds: the Bayesian framework that motivates MCMC rests on exchangeability
```

---

## IRI Identity

Every node in the PKIS wiki carries a stable, canonical IRI that makes it
addressable across systems — including the PKIS MCP server and the Mnemon
operational graph that holds references into this wiki.

**Format:** `pkis:{knowledge_type}:{slug}`

where `{health_type}` is the singular form of the node's canonical type:

| Folder | `knowledge_type` value | IRI prefix |
|---|---|---|
| `sources/` | `source` | `pkis:source:` |
| `concepts/` | `concept` | `pkis:concept:` |
| `techniques/` | `technique` | `pkis:technique:` |
| `results/` | `result` | `pkis:result:` |
| `frameworks/` | `framework` | `pkis:framework:` |
| `problems/` | `problem` | `pkis:problem:` |
| `principles/` | `principle` | `pkis:principle:` |
| `hypotheses/` | `hypothesis` | `pkis:hypothesis:` |
| `clusters/` | `research-cluster` | `pkis:research-cluster:` |
| `assets/` | `asset` | `pkis:asset:` |
| `bridge-notes/` | `bridge-note` | `pkis:bridge-note:` |
| `discovery/` | `discovery-stub` | `pkis:discovery-stub:` |
| `findings/` | `finding` | `pkis:finding:` |
| `resources/` | `resource` | `pkis:resource:` |

**Examples:**
- `pkis:concept:variational-inference`
- `pkis:technique:mcmc`
- `pkis:framework:structural-causal-models`
- `pkis:result:bayes-theorem`
- `pkis:source:hastie-esl-ch10`

**Properties:**
- Generated deterministically from node type and slug at creation time
- Stored in the `id` field of every node's YAML frontmatter
- Assigned once and never changed — even if the node is restructured
- If a node must be retired or merged, add a `deprecated_in_favor_of:` field
  pointing to the replacement IRI; do not reuse the old `id`

**Aliases registry:** Every node also carries an `aliases` list in its
frontmatter. This is the full set of known surface forms for the concept —
abbreviations, synonyms, alternative names across domains. The MCP server
builds a flat `alias → IRI` registry from all frontmatter at startup.
This registry enables string-based concept resolution without LLM involvement.

**Schema violation:** Any node missing an `id` field in frontmatter is a
schema violation. The Librarian must assign an IRI at node creation time.
The Auditor agent flags any node without `id`.

---

## Google Drive — Source of Truth for Binaries

No PDFs or binary files are committed to git. All binaries live in Google Drive under:

```
PKIS/
  sources/
    papers/     Drive ID: 1hTtbvU2TxWjGa0MX_bnnYUlOzQ9oAh3I
    books/      Drive ID: 1_hsD5_spfs_6B9iadd44GhSqvetF2CKZ
    assets/     (images and supporting figures)
```

Source entries reference Drive files by **file ID**, not by path. Paths change; IDs do not.

---

## Frontmatter Templates

### Source Entry (`wiki/sources/`)

```yaml
---
id: "pkis:source:{slug}"       # assigned at creation; never changed
aliases: []                    # known alternative titles or short names
title: ""
authors: ""
year:
type: paper | book | book-chapter | article | talk
domain: []
tags: []
source_url: ""          # arXiv URL, DOI, or similar; omit if not web-available
drive_id: ""            # Google Drive file ID — legacy pristine store
drive_path: ""          # human-readable Drive path — legacy
doc_path: ""            # path under DOCS_BASE_URL, e.g. sources/hastie-esl/hastie-esl.pdf
readwise_id: ""         # Readwise Reader document ID (set on upload; used for webhook routing)
isbn: ""                # books only; ISBN-13 preferred
toc_source: ""          # books only: "openlibrary" | "google-books" | "manual"
parent_book: ""         # book-chapter only; wikilink to parent book entry
chapter:                # book-chapter only; integer chapter number
status: unread          # unread | in-progress | read
date_added: YYYY-MM-DD
date_read: ""           # YYYY-MM-DD — set automatically by Readwise webhook on finish/archive
concepts: []            # wikilinks to knowledge nodes this source covers
---
```

### Discovery Stub (`wiki/discovery/`)

Lightweight placeholder for a source seen during discovery — potentially relevant,
not yet worth full ingest. **Max two concept links, no Reading Path, no Key
Extractions** (the `rationale` is the only substantive content). Promoted to a full
source node via Librarian ingest (a deliberate human decision); the stub is never
deleted — just marked `promoted: true`. Indexed under a `## Discovery` section in
`wiki/index.md`; the PWA discovery view reads `wiki/discovery/` filtered to
`promoted: false`. (Agent Roster v2.)

```yaml
---
id: "pkis:discovery-stub:{slug}"   # assigned at creation; never changed
aliases: []
title: ""
authors: ""
year:
type: paper | book | book-chapter | article | talk | unknown
domain: []
tags: []
source_url: ""          # URL if available; null otherwise
knowledge_type: discovery-stub
status: parked          # always parked until promoted (not unread/in-progress/read)
date_added: YYYY-MM-DD
rationale: ""           # why this source might be relevant — one to three sentences
primary_concepts: []    # max two wikilinks — the concepts that make this potentially relevant
promoted: false         # set true when promoted to a full source node; never delete the stub
promoted_to: ""         # wikilink to the full source node after promotion; null until promoted
---
```

### Concept Node (`wiki/concepts/`)

```yaml
---
id: "pkis:concept:{slug}"      # assigned at creation; never changed
aliases: []                    # abbreviations, synonyms, domain-specific alternative names
title: ""
knowledge_type: concept
also_type: []
domain: []
tags: []
related_concepts: []
sources: []
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
coverage: 0
understanding: 0
maturity: settled | evolving | contested | historical
component_scores:              # human-maintained only — agents never write this
  definition: null             # 1-5: precise statement of what the concept is
  prerequisites: null          # 1-5: demonstrated understanding of dependencies
  boundary: null               # 1-5: distinguishes from adjacent/confused concepts (the foil)
  scope: null                  # 1-5: knows applicability and where it breaks down
  application: null            # 1-5: can apply correctly in novel contexts
  formal_statement: null       # 1-5: can engage with mathematical/logical formulation
  dependents: null             # 1-5: understands what this concept unlocks downstream
  transfer: null               # 1-5: can apply outside original domain — expect null early
---
```

### Technique Node (`wiki/techniques/`)

```yaml
---
id: "pkis:technique:{slug}"    # assigned at creation; never changed
aliases: []                    # abbreviations, synonyms, domain-specific alternative names
title: ""
knowledge_type: technique
also_type: []
domain: []
tags: []
related_concepts: []
sources: []
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
coverage: 0
understanding: 0
maturity: settled | evolving | contested | historical
component_scores:              # human-maintained only — agents never write this
  operational_mechanism: null  # 1-5: can trace through what it does step by step
  principled_mechanism: null   # 1-5: understands why it works — objective, mathematical basis
  conditions: null             # 1-5: knows when to apply and when not to
  implementation: null         # 1-5: can instantiate in code or math from scratch
  diagnostics: null            # 1-5: can assess whether it's working on a given problem
  alternatives: null           # 1-5: knows competing approaches and when to prefer this one
  failure_modes: null          # 1-5: understands what goes wrong and why
---
```

### Result Node (`wiki/results/`)

```yaml
---
id: "pkis:result:{slug}"       # assigned at creation; never changed
aliases: []                    # abbreviations, synonyms, domain-specific alternative names
title: ""
knowledge_type: result
also_type: []
domain: []
tags: []
related_concepts: []
sources: []
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
coverage: 0
understanding: 0
maturity: settled | evolving | contested | historical
component_scores:              # human-maintained only — agents never write this
  statement: null              # 1-5: can state the result precisely
  proof_sketch: null           # 1-5: understands the core argument, not necessarily full proof
  conditions: null             # 1-5: knows the assumptions required for the result to hold
  implications: null           # 1-5: understands what follows from the result
  limitations: null            # 1-5: knows where the result does not apply
---
```

### Framework Node (`wiki/frameworks/`)

```yaml
---
id: "pkis:framework:{slug}"    # assigned at creation; never changed
aliases: []                    # abbreviations, synonyms, domain-specific alternative names
title: ""
knowledge_type: framework
also_type: []
domain: []
tags: []
related_concepts: []
sources: []
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
coverage: 0
understanding: 0
maturity: settled | evolving | contested | historical
component_scores:              # human-maintained only — agents never write this
  structure: null              # 1-5: can articulate components and how they relate
  purpose: null                # 1-5: understands what problem the framework was designed to solve
  primitives: null             # 1-5: knows foundational concepts the framework is built from
  scope: null                  # 1-5: knows what it applies to and what it does not
  application: null            # 1-5: can use it to organize and reason about a novel problem
  limits: null                 # 1-5: knows where it breaks down or misleads
---
```

### Problem Node (`wiki/problems/`)

```yaml
---
id: "pkis:problem:{slug}"      # assigned at creation; never changed
aliases: []                    # abbreviations, synonyms, domain-specific alternative names
title: ""
knowledge_type: problem
also_type: []
domain: []
tags: []
related_concepts: []
sources: []
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
coverage: 0
understanding: 0
maturity: settled | evolving | contested | historical
component_scores:              # human-maintained only — agents never write this
  formulation: null            # 1-5: can state the problem precisely
  why_hard: null               # 1-5: understands the structural source of difficulty
  solution_landscape: null     # 1-5: knows the space of approaches and their tradeoffs
  instances: null              # 1-5: can recognize this problem in novel contexts
---
```

### Principle Node (`wiki/principles/`)

```yaml
---
id: "pkis:principle:{slug}"    # assigned at creation; never changed
aliases: []                    # abbreviations, synonyms, domain-specific alternative names
title: ""
knowledge_type: principle
also_type: []
domain: []
tags: []
related_concepts: []
sources: []
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
coverage: 0
understanding: 0
maturity: settled | evolving | contested | historical
component_scores:              # human-maintained only — agents never write this
  statement: null              # 1-5: can articulate the principle precisely
  justification: null          # 1-5: understands why this principle should hold
  implications: null           # 1-5: knows what follows if the principle is accepted
  violations: null             # 1-5: can identify when and why the principle is violated
---
```

### Reading Path Convention

All knowledge nodes may include a `## Reading Path` body section listing the most
relevant sources (chapters or papers) ordered by recommended reading sequence:

```markdown
## Reading Path
- [[hastie-esl-ch10]] (unread) — primary treatment; covers loss functions and regularization paths
- [[deisenroth-mml-ch06]] (unread) — optimization geometry prerequisites
- [[zhang-graphrag-survey]] (unread) — application context in retrieval systems
```

**Format (v3.0):** each entry carries a read status, an edge type, and a rationale string:

```markdown
## Reading Path
- [[hastie-esl-ch10]] (unread) [integration] — primary treatment; must read before node can be considered well-sourced
- [[bishop-prml-ch09]] (unread) [orientation] — provides field-level context before deeper engagement
```

Edge types:
- **orientation** — source provides context, background, or framing; useful before deep engagement
- **integration** — source must be read deeply before the dependent concept can be considered mature

The Librarian populates this section when creating stubs or updating existing nodes.
The user updates status annotations as reading progresses. The Synthesizer checks this
section before deepening and flags unread primary sources rather than deepening from
zero confirmed evidence.

---

## Wikilink Convention

Use standard Obsidian wikilink format: `[[filename-without-extension]]`

Slugs are unique across ALL folders. Before creating a new slug, the Librarian
checks all 11 wiki subdirectories for collisions. Slugs are always lowercase-hyphenated:
`variational-inference`, not `VariationalInference`.

No folder prefix in wikilinks — `[[mcmc]]` not `[[techniques/mcmc]]`.

---

## Slug Conventions

| Node type | Pattern | Example |
|---|---|---|
| Paper | `author-shortitle-year` | `neal-mcmc-using-hamiltonian-2011` |
| Book | `author-shortitle` | `pearl-causality` |
| Book chapter | `author-book-chNN` | `bishop-prml-ch10` |
| Knowledge node | descriptive, lowercase-hyphenated | `variational-inference`, `credit-assignment-problem` |
| Hypothesis | descriptive, lowercase-hyphenated | `ontological-supervision-improves-embeddings` |
| Research cluster | descriptive, lowercase-hyphenated | `intensional-grounding`, `embedding-ontology-alignment` |
| Asset | descriptive with optional tool suffix | `em-algorithm-implementation-pymc`, `calibration-explainer` |
| Bridge note | `bn-YYYYMMDD-brief-descriptor` (auto-generated) | `bn-20260530-em-mcmc-vi-same-problem` |

---

## index.md Convention

Single file with sections per node type. Each entry on one line:

```markdown
# PKIS Wiki Index

## Sources
- [[source-slug]] — one-line description (domain-tag) (YYYY-MM-DD)

## Concepts
- [[concept-slug]] — one-line description (domain-tag) (YYYY-MM-DD)

## Techniques
- [[technique-slug]] — one-line description (domain-tag) (YYYY-MM-DD)

## Results
- [[result-slug]] — one-line description (domain-tag) (YYYY-MM-DD)

## Frameworks
- [[framework-slug]] — one-line description (domain-tag) (YYYY-MM-DD)

## Problems
- [[problem-slug]] — one-line description (domain-tag) (YYYY-MM-DD)

## Principles
- [[principle-slug]] — one-line description (domain-tag) (YYYY-MM-DD)

## Hypotheses
- [[hypothesis-slug]] — one-line description (cluster) (YYYY-MM-DD)

## Research Clusters
- [[cluster-slug]] — one-line thesis summary (YYYY-MM-DD)

## Assets
- [[asset-slug]] — one-line description (asset_type) (YYYY-MM-DD)

## Bridge Notes
Bridge notes count: N pending review
(Bridge notes are too ephemeral for full listing — check wiki/bridge-notes/ or use get_staged_nodes)

## Reading Queue
```

---

## log.md Convention

Append-only. Each entry:

```markdown
## [YYYY-MM-DD] operation-type | title
- Brief description of what was done
- Files created or modified
```

---

## queue.md Convention

Prioritized list. Agent adds items; user checks them off when read.

```markdown
### High
- [ ] [[source-slug]] — reason for priority

### Normal
- [ ] [[source-slug]] — reason for priority
```

---

## Infrastructure Node Templates

### Hypothesis Node (`wiki/hypotheses/`)

```yaml
---
id: "pkis:hypothesis:{slug}"   # assigned at creation; never changed
aliases: []
title: ""
knowledge_type: hypothesis
domain: []
tags: []
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
status: open | partially-addressed | resolved | superseded
origin: iks-fact-pattern | research-program | work-observation | operational-need | spontaneous
research_program_cluster: ""   # slug of parent Research Cluster node; null if independent
research_program_role: direct-test | boundary-condition | scaling-foil | enabling-hypothesis | independent
iks_link: ""                   # IKS fact pattern ID if origin is iks-fact-pattern; otherwise null
cluster_membership: []         # list of Research Cluster slugs — many-to-many
dependent_nodes: []            # PKIS knowledge node IRIs only; IKS operational deps go in body
evidence_nodes: []             # wikilinks to assets, sessions, or sources bearing on this
---
```

**dependent_nodes format** — each entry is an object with rationale:
```yaml
dependent_nodes:
  - node: "[[mcmc]]"
    node_type: technique
    rationale: "Requires understanding MCMC to evaluate it as alternative inference engine"
```

**Body sections:** `## Formal Statement`, `## Motivation`, `## Current Evidence`,
`## Open Questions`, `## Platform Requirements` (IKS deps only), `## Connections`

---

### Research Cluster Node (`wiki/clusters/`)

```yaml
---
id: "pkis:research-cluster:{slug}"  # assigned at creation; never changed
aliases: []
title: ""
knowledge_type: research-cluster
domain: []
tags: []
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
status: active | dormant | resolved | superseded
origin: research-program | organic | iks-derived
hypotheses: []              # list of hypothesis node slugs — many-to-many
cross_cluster_dependencies: []  # slugs of clusters this one depends on
frontier_hypotheses: []     # computed by Auditor agent — hypotheses addressable given current PKIS coverage
---
```

**Body sections:** `## Thesis`, `## Summary`, `## Research Program Context`,
`## Constituent Hypotheses`, `## Current Frontier`, `## Connections`

---

### Asset Node (`wiki/assets/`)

```yaml
---
id: "pkis:asset:{slug}"        # assigned at creation; never changed
aliases: []
title: ""
knowledge_type: asset
asset_type: code | derivation | interactive-artifact | synthesis-note | worked-analysis
generative_level: descriptive | constructive | generative
  # descriptive: summarizing existing knowledge
  # constructive: implementing or deriving from established procedures
  # generative: applying to novel problems or producing original analysis
domain: []
tags: []
date_created: YYYY-MM-DD
audience: self | team | external
hosted_url: ""          # URL if hosted; null otherwise
repo_path: ""           # path in a git repo if version-controlled; null otherwise
durable: true | false   # true if hosted or version-controlled and retrievable
ars_link: ""            # ARS concept ID or question ID if this seeds ARS content; null otherwise
nodes_evidenced: []     # see format below
---
```

**nodes_evidenced format:**
```yaml
nodes_evidenced:
  - node: "[[em-algorithm]]"
    node_type: technique
    components: [operational_mechanism, implementation, principled_mechanism]
    notes: "Full from-scratch implementation including E-step and M-step"
```

**Body sections:** `## Description`, `## What It Demonstrates`, `## Production Notes`,
`## ARS Potential`

---

### Bridge Note Node (`wiki/bridge-notes/`)

Bridge notes are created only by the MCP `create_bridge_note` endpoint — never manually.
They are explicitly temporary: intended to be integrated into proper node connections or
discarded. No `component_scores`.

```yaml
---
id: "pkis:bridge-note:{slug}"  # auto-assigned at creation
aliases: []
title: ""
knowledge_type: bridge-note
date_created: YYYY-MM-DD
status: unreviewed | reviewed | integrated | discarded
origin: voice-capture | conversation | reading | spontaneous
source_context: ""      # fuzzy reference to what prompted this
linked_nodes: []        # wikilinks to nodes this connection spans
proposed_edge_type: ""  # proposed relationship predicate; null if unknown
rationale: ""           # the connection or insight being captured
integration_target: ""  # wikilink to target node for promotion; null if unknown
---
```

**Body sections:** `## Connection`, `## Nodes Involved`, `## Integration Notes`

---

### Finding Node (`wiki/findings/`)

A Finding is a **scrubbed, aggregate empirical result** produced by an external
experimental system (initially OpGraph) and accepted into PKIS as evidence bearing on
a hypothesis. Findings are created only by the MCP `create_finding_stub` endpoint — a
narrow, content-restricted inbound gate — never manually. PKIS validates only the
schema and that `evidence-for` resolves to a live hypothesis; it never recomputes or
verifies the statistics, and never reaches back toward the producing system. The human
staging review is the content gate (it confirms the finding carries no identifying
content). No `component_scores`.

```yaml
---
id: "pkis:finding:{slug}"      # auto-assigned at creation; never changed
aliases: []
title: ""
knowledge_type: finding
domain: []                      # inherited from the target hypothesis
tags: []                        # e.g. [opgraph, structural_priors]
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
maturity: evolving
finding_id: ""                  # uuid from the producing system
generated_at: ""               # ISO 8601 — when the producing system computed it
summary: ""                     # plain-language, already scrubbed by the producer
statistics: {}                  # aggregate stats only (strategy, metric, value, n, CI, ...)
stratification: {}              # structural/methodological strata only (e.g. mention_type)
source_system: ""              # producing system, e.g. 'opgraph'
source_run_id: ""              # analysis-run reference in the producing system
source_log_date_range: []      # [start_date, end_date]
evidence-for: []               # [hypothesis-slug] — typed edge Finding -> Hypothesis
---
```

**Body sections:** `## Summary`, `## Statistics`, `## Provenance`, `## Connections`

The target hypothesis's `## Current Evidence` section is **not** auto-updated — that
synthesis stays human-curated (or a future, separately-staged Lab Assistant step).

---

### Resource Node (`wiki/resources/`)

A Resource is an **external tool, library, platform, dataset, documentation site, or
service** — anything with a development / maintenance / deprecation lifecycle. It is
epistemically distinct from a `source`: a resource backs *"this exists and does X"*,
not *"this claim is established"*. Its operational deployment is tracked in OpGraph,
**not** here — PKIS records what a resource *is*, not decisions about using it.
Created via the `create_resource_stub` endpoint (URL is taken as-is; no CrossRef /
arXiv / Semantic Scholar enrichment). No `component_scores`.

```yaml
---
id: "pkis:resource:{slug}"     # auto-assigned at creation; never changed
aliases: []
title: ""
knowledge_type: resource
domain: []
tags: []
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
maturity: evolving
resource_url: ""               # canonical URL — REQUIRED for resources
resource_type: ""              # library | tool | platform | dataset | documentation | service
status: active                 # active | unmaintained | deprecated | archived
last_evaluated: YYYY-MM-DD      # when you last assessed it (defaults to ingest date)
technological_scope: []        # free tags: language, framework, stack
understanding: 0
---
```

**Body sections:** `## Summary` (what it does, the problem it solves, dependencies,
caveats), `## Relationship Candidates` (which concepts/techniques it implements or
applies; resources it depends on or competes with). **No** `## Key Concepts` (that is
for academic sources).

**Edges:** a concept/technique → resource via `implemented-by`; resource → resource
dependency via `uses`; resource → resource replacement via `superseded-by`.

**Evidential weight (convention).** A resource is weaker evidence than a peer-reviewed
source. For maturity, treat it as roughly `0.4` of a source and `bridge-note` as `0.3`
— and as a hard convention, **resource citations alone must not push a concept to
`maturity: settled`**. (PKIS `maturity` is self-assessed, not computed, so this is a
discipline for the Synthesizer and human reviewers, not an automatic calculation.)

---

## Staging Area

The staging area (`wiki/staging/`) is the two-phase write buffer. All MCP write endpoint
outputs land here before promotion to the live graph. Staged nodes are standard markdown
files with additional staging frontmatter prepended:

```yaml
---
staged_at: YYYY-MM-DDTHH:MM:SSZ
staged_by: mcp-create-bridge-note | mcp-create-source-stub
staged_id: uuid4          # handle for commit_staged_node
review_status: pending | approved | rejected
proposed_edges: []        # edges proposed at staging time, written to live nodes at commit
---
```

**Rules:**
- The MCP server never writes directly to `wiki/<node_type>/` — only to `wiki/staging/`
- Only `commit_staged_node` promotes a staged file to the live graph
- The staging area is never indexed by the MCP's search or node-retrieval operations
- Staged files that are discarded are deleted; the discard event is logged to `log.md`

---

## Granularity Heuristics

**When does something earn a node?**

1. **Literary warrant:** it appears with distinct, non-trivial content in 2+ source
   entries. "Partial differentiation" probably fails. "Automatic differentiation" passes.

2. **Cognitive warrant:** the user has distinct thoughts about it that don't reduce to
   "this is a special case of X." If the Intuition section would just be the parent's
   intuition plus one qualifier, it doesn't need its own node.

3. **Bridge warrant:** it connects two otherwise-disconnected parts of the graph. Even
   with only one source, if it's the link between causal inference and reinforcement
   learning, it earns a node.

**When does something stay a tag?**

When it's a useful navigational marker but doesn't have its own "body of knowledge"
in the wiki. "Linear algebra" stays a tag until a source discusses it in a way that
illuminates its role across domains.

**When does a node deserve splitting?**

When it accumulates distinct domain-specific sections that don't cross-reference each
other. If a node's subsections are islands, they should be separate nodes linked by
`specializes`.
