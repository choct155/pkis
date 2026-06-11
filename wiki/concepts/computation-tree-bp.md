---
aliases: []
also_type: []
applies:
- loopy-belief-propagation
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probabilistic-graphical-models
id: pkis:concept:computation-tree-bp
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch09
tags:
- loopy-BP
- convergence-analysis
- belief-propagation
- Bethe-approximation
title: Computation Tree (Belief Propagation)
understanding: 0
uses:
- probabilistic-graphical-models
---

## Definition
The **computation tree** of a loopy graph $G$ is the infinite tree obtained by unrolling the message-passing computation: the root corresponds to a focal node at iteration $T$, its children correspond to the neighbours that sent it messages at iteration $T-1$, their children correspond to the neighbours that sent those messages at iteration $T-2$, and so on, allowing node labels to repeat.

$$\text{(T iterations of LBP on }G) \equiv \text{(exact BP on computation tree of depth }T+1\text{)}$$

Intuition: each LBP iteration adds one extra layer to an unrolled tree copy of the graph; convergence occurs when leaf influence decays.

### Why it matters
The computation tree provides the main theoretical lens for analysing loopy BP: (i) it explains why LBP is exact on trees (no repetition), (ii) it gives sufficient conditions for convergence (sufficiently weak edge potentials make leaf influence vanish), and (iii) it connects LBP to the Bethe free-energy approximation. Understanding the computation tree is essential for bounding LBP approximation error.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[probabilistic-graphical-models]] — uses
- [[loopy-belief-propagation]] — applies
[To be populated during integration]