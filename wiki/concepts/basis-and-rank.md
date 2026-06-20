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
date_updated: '2026-06-20'
domain:
- statistical-learning
id: pkis:concept:basis-and-rank
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- linear-mapping
related_concepts: []
sources:
- deisenroth-mml-ch02
- carrell-groups-matrices-vectors-ch03
- carrell-groups-matrices-vectors-ch06
- carrell-groups-matrices-vectors-ch07
tags:
- mathematical-foundations
- linear-algebra
title: Basis, Dimension, and Rank
understanding: 0
---

## Definition
$$V = \mathrm{span}[b_1,\ldots,b_n],\quad \{b_i\}\text{ linearly independent}\;\Rightarrow\; \dim(V)=n$$

A basis is a minimal set of vectors that generates the whole space; its size is the dimension, and the rank of a matrix is the dimension of the space its columns span.

### Generating set and span
The **span** of a set $A$ is the set of all its linear combinations. $A$ is a **generating set** of $V$ if $\mathrm{span}[A]=V$.

### Basis
A **basis** is a linearly independent generating set — equivalently, a minimal generating set, or a maximal independent set. Every vector then has a *unique* representation as a combination of basis vectors. Bases are not unique, but all bases of a given space have the same cardinality, the **dimension** $\dim(V)$ (the number of independent directions, not the number of entries per vector).

### Rank
The **rank** $\mathrm{rk}(A)$ of a matrix is the number of linearly independent columns, which equals the number of independent rows ($\mathrm{rk}(A)=\mathrm{rk}(A^\top)$). It equals the dimension of the column space (image). $A\in\mathbb{R}^{n\times n}$ is invertible iff $\mathrm{rk}(A)=n$; full rank means $\mathrm{rk}(A)=\min(m,n)$.

### Why it matters
Dimension and rank quantify the effective degrees of freedom in data and models: rank deficiency signals collinearity, governs solvability of $A x = b$ (via $\mathrm{rk}(A)=\mathrm{rk}([A|b])$), and is the lever behind low-rank approximation and dimensionality reduction.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[linear-mapping]] — prerequisite-of: Transformation matrices and coordinates are defined with respect to ordered bases; rank = dim of the image.
[To be populated during integration]