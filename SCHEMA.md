# PKIS Wiki Schema
Version: 2.0

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
```

### Node Type Descriptions

| Type | What it represents | Distinguishing question |
|---|---|---|
| **Source** | A document in the corpus | "What did this author write?" |
| **Concept** | An idea with a definition and boundary | "What IS this thing?" |
| **Technique** | A procedure that takes inputs and produces outputs | "How do I DO this?" |
| **Result** | A proven or established claim | "What do we KNOW for certain?" |
| **Framework** | A coherent system that organizes concepts, techniques, and results | "How does this field THINK about problems?" |
| **Problem** | A well-defined challenge that motivates methods | "What are we TRYING to solve?" |
| **Principle** | A guiding idea that constrains or evaluates other knowledge | "What SHOULD guide our choices?" |

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
must check existing tags across the wiki before coining a new one, and the Maintenance
agent flags near-duplicates.

**Tags vs. nodes:** Tags are navigational markers. If a tag keeps appearing on many
nodes and the corpus has something substantive to say about the tag itself (not just
about things it labels), that's a signal it may deserve its own concept node.

---

## Epistemic Status

Every knowledge node (not sources) carries three independent status dimensions:

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

---

## Relationship Predicates

Eight core predicates connect nodes across the graph. Each predicate has a general
meaning, but its specific interpretation depends on the types of the subject and
object nodes.

### Predicate Definitions

| Predicate | General meaning | Inverse |
|---|---|---|
| `specializes` | Subject is a more specific version of object | `generalizes` |
| `generalizes` | Subject is a more general version of object | `specializes` |
| `prerequisite-of` | Subject must be understood before object | — |
| `uses` | Subject employs or operates on object | `used-by` |
| `contrasts-with` | Subject and object are alternatives or in tension | (symmetric) |
| `extends` | Subject builds upon object, adding capability | — |
| `grounds` | Subject provides epistemic or theoretical foundation for object | — |
| `equivalent-in-context` | Subject and object are the same idea under different names in different domains | (symmetric) |
| `commonly-confused-with` | Subject and object appear similar but differ in important ways | (symmetric) |

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
title: ""
authors: ""
year:
type: paper | book | book-chapter | article | talk
domain: []
tags: []
source_url: ""          # arXiv URL, DOI, or similar; omit if not web-available
drive_id: ""            # Google Drive file ID — primary reference
drive_path: ""          # human-readable Drive path for orientation only
status: unread | reading | completed | paused
date_added: YYYY-MM-DD
concepts: []            # wikilinks to knowledge nodes this source covers
---
```

### Concept Node (`wiki/concepts/`)

```yaml
---
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
---
```

### Technique Node (`wiki/techniques/`)

```yaml
---
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
---
```

### Result Node (`wiki/results/`)

```yaml
---
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
---
```

### Framework Node (`wiki/frameworks/`)

```yaml
---
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
---
```

### Problem Node (`wiki/problems/`)

```yaml
---
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
---
```

### Principle Node (`wiki/principles/`)

```yaml
---
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
---
```

---

## Wikilink Convention

Use standard Obsidian wikilink format: `[[filename-without-extension]]`

Slugs are unique across ALL folders. Before creating a new slug, the Librarian
checks all 7 wiki subdirectories for collisions. Slugs are always lowercase-hyphenated:
`variational-inference`, not `VariationalInference`.

No folder prefix in wikilinks — `[[mcmc]]` not `[[techniques/mcmc]]`.

---

## Slug Conventions

| Source type | Pattern | Example |
|---|---|---|
| Paper | `author-shortitle-year` | `neal-mcmc-using-hamiltonian-2011` |
| Book | `author-shortitle` | `pearl-causality` |
| Book chapter | `author-book-chNN` | `bishop-prml-ch10` |
| Knowledge node | descriptive, lowercase-hyphenated | `variational-inference`, `credit-assignment-problem` |

---

## index.md Convention

Single file with 8 sections. Each entry on one line:

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
