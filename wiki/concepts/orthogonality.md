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
id: pkis:concept:orthogonality
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch03
tags:
- mathematical-foundations
- linear-algebra
- analytic-geometry
title: Orthogonality
understanding: 0
---

## Definition
$$x \perp y \iff \langle x, y\rangle = 0$$

Two vectors are orthogonal when their inner product vanishes; this generalizes perpendicularity to any inner product, capturing the idea of "no shared direction."

### Definition and unit vectors
Vectors $x, y$ are **orthogonal** ($x \perp y$) iff $\langle x,y\rangle = 0$. If additionally $\|x\| = \|y\| = 1$ they are **orthonormal**. Because angles are defined through the inner product, vectors orthogonal under one inner product need not be orthogonal under another, e.g. $[1,1]^\top$ and $[-1,1]^\top$ are orthogonal under the dot product but not under $\langle x,y\rangle = x^\top \mathrm{diag}(2,1)\, y$. The zero vector is orthogonal to every vector.

### Orthonormal bases and complements
A basis is **orthonormal (ONB)** if $\langle b_i, b_j\rangle = \delta_{ij}$; the standard basis of $\mathbb{R}^n$ is the canonical example. The **orthogonal complement** $U^\perp$ of an $M$-dimensional subspace $U \subseteq V$ (with $\dim V = D$) is the $(D-M)$-dimensional subspace of all vectors orthogonal to every vector of $U$; any $x$ decomposes uniquely into a $U$ part and a $U^\perp$ part. The unit normal vector $w$ of a plane spans its orthogonal complement.

### Orthogonal matrices
A square matrix is **orthogonal** if $A^\top A = AA^\top = I$, so $A^{-1} = A^\top$. Such matrices preserve lengths ($\|Ax\| = \|x\|$) and angles, and represent rotations and reflections.

### Why it matters
Orthogonality makes projection, decomposition, and dimensionality reduction tractable: orthonormal bases turn projections into simple dot products, orthogonal complements define hyperplanes for SVMs, and orthogonal directions underpin PCA, Fourier analysis, and numerically stable linear solvers.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]