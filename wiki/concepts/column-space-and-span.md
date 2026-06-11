---
aliases: []
also_type: []
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
- linear-algebra
id: pkis:concept:column-space-and-span
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch02
tags:
- column space
- span
- range
- linear combination
- solvability
title: Column Space and Span
understanding: 0
---

## Definition
$$\text{col}(\mathbf{A}) = \left\{\mathbf{A}\mathbf{x} \mid \mathbf{x} \in \mathbb{R}^n\right\} = \operatorname{span}\{\mathbf{A}_{:,1},\ldots,\mathbf{A}_{:,n}\}$$

The **span** of a set of vectors is the set of all their linear combinations; the **column space** (range) of a matrix is the span of its columns. The system $\mathbf{A}\mathbf{x}=\mathbf{b}$ has a solution iff $\mathbf{b}\in\text{col}(\mathbf{A})$.

### Why it matters
Understanding column space is essential for determining when a linear system is solvable, motivating the need for the Moore-Penrose pseudoinverse when $\mathbf{b}$ is outside the column space, and grounding the geometry of PCA (the optimal subspace is the column space of the top-$l$ eigenvectors).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]