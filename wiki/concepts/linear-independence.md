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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:concept:linear-independence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch02
tags:
- mathematical-foundations
- linear-algebra
title: Linear Independence
understanding: 0
---

## Definition
$$\sum_{i=1}^{k}\lambda_i x_i = \mathbf{0} \;\Rightarrow\; \lambda_1=\cdots=\lambda_k=0$$

Vectors are linearly independent when the only way to combine them into the zero vector is the trivial way — i.e., none of them is redundant.

### Definition
Given $x_1,\ldots,x_k$ in a vector space $V$, a **linear combination** is $\sum_i \lambda_i x_i$ with $\lambda_i\in\mathbb{R}$. The vectors are **linearly dependent** if some non-trivial combination (at least one $\lambda_i\neq 0$) equals $\mathbf{0}$; otherwise they are **linearly independent**. Equivalently, a set is dependent iff at least one vector is a linear combination of the others.

### Intuition
Independence means no redundancy: removing any vector strictly shrinks the set of points reachable by combinations. The book's geographic example — "506 km NW" and "374 km SW" are independent, but "751 km W" is their combination — captures this exactly.

### Testing
Stack the vectors as columns of a matrix and run Gaussian elimination to row-echelon form: pivot columns are independent of those to their left; any non-pivot column is a combination of earlier pivots. All columns are independent iff every column is a pivot column.

### Why it matters
Linear independence is the gatekeeper for the notions of basis, dimension, and rank, and it determines when a system $A x = b$ has a unique solution — making it foundational to identifiability and conditioning throughout statistics and ML.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]