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
id: pkis:concept:vector-space
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch02
tags:
- mathematical-foundations
- linear-algebra
title: Vector Space
understanding: 0
---

## Definition
$$V = (V, +, \cdot),\quad +: V\times V\to V,\quad \cdot:\mathbb{R}\times V\to V$$

A vector space is a set whose elements (vectors) can be added together and scaled by scalars without ever leaving the set — the algebraic formalization of "closure" under addition and scaling.

### Definition
A real vector space is a set $V$ with an inner operation $+$ (vector addition) and an outer operation $\cdot$ (scalar multiplication) such that $(V,+)$ is an Abelian group (closure, associativity, a neutral zero vector $\mathbf{0}$, and additive inverses), scalar multiplication distributes over both vector and scalar addition, is associative ($\lambda(\psi x)=(\lambda\psi)x$), and has $1\cdot x = x$. The elements are called vectors regardless of their concrete form.

### Examples
The canonical example is $\mathbb{R}^n$ with componentwise operations, but geometric arrows, polynomials, audio signals, $m\times n$ matrices ($\mathbb{R}^{m\times n}\cong\mathbb{R}^{mn}$), and $\mathbb{C}$ are all vector spaces — the abstraction is what makes one theory cover all of them.

### Subspaces
A non-empty subset $U\subseteq V$ is a vector subspace if it contains $\mathbf{0}$ and is closed under both operations; every such $U$ is itself the solution set of some homogeneous system $A x = \mathbf{0}$.

### Why it matters
Vector spaces are the substrate on which essentially all of machine learning lives: data points, parameters, gradients, and feature representations are vectors, and subspaces underpin dimensionality reduction (e.g., PCA). Finite-dimensional real vector spaces are all isomorphic to some $\mathbb{R}^n$, so reasoning in $\mathbb{R}^n$ loses no generality.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]