---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:gram-schmidt
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch03
tags:
- mathematical-foundations
- linear-algebra
- analytic-geometry
title: Gram-Schmidt Orthogonalization
understanding: 0
---

## Definition
$$u_1 := b_1,\qquad u_k := b_k - \pi_{\mathrm{span}[u_1,\dots,u_{k-1}]}(b_k)$$

Gram-Schmidt constructively turns any basis into an orthogonal (and, after normalization, orthonormal) basis spanning the same subspace, using orthogonal projection at its core.

### The procedure
Given a basis $(b_1,\dots,b_n)$ of an $n$-dimensional space $V$, set $u_1 = b_1$, then for $k = 2,\dots,n$ subtract from $b_k$ its projection onto the span of the already-built vectors: $u_k = b_k - \pi_{\mathrm{span}[u_1,\dots,u_{k-1}]}(b_k)$. Each new $u_k$ is by construction orthogonal to all previous $u_i$, and $\mathrm{span}[b_1,\dots,b_n] = \mathrm{span}[u_1,\dots,u_n]$. Normalizing each $u_k$ to unit length yields an orthonormal basis (ONB).

### Worked intuition
For $b_1 = [2,0]^\top$, $b_2 = [1,1]^\top$ in $\mathbb{R}^2$: $u_1 = [2,0]^\top$, and $u_2 = b_2 - \frac{u_1 u_1^\top}{\|u_1\|^2}b_2 = [1,1]^\top - [1,0]^\top = [0,1]^\top$, which is orthogonal to $u_1$.

### Why it matters
Orthonormal bases dramatically simplify computation: projections become dot products and inner products decouple coordinate-by-coordinate. Gram-Schmidt underlies the QR decomposition, numerically stable solvers, and Krylov-subspace methods (conjugate gradients, GMRES) that minimize mutually orthogonal residuals. Naive Gram-Schmidt is numerically unstable; modified Gram-Schmidt or Householder reflections are preferred in practice.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]