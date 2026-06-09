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
id: pkis:concept:orthogonal-projection
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- principal-component-analysis
related_concepts: []
sources:
- deisenroth-mml-ch03
tags:
- mathematical-foundations
- linear-algebra
- analytic-geometry
title: Orthogonal Projection
understanding: 0
uses:
- orthogonality
- inner-product
- linear-algebra
---

## Definition
$$\pi_U(x) = B(B^\top B)^{-1} B^\top x$$

The orthogonal projection of $x$ onto a subspace $U$ is the unique point in $U$ closest to $x$; the residual $x - \pi_U(x)$ is orthogonal to $U$.

### Defining property
A **projection** is a linear map $\pi : V \to U$ that is idempotent, $\pi^2 = \pi$; correspondingly its matrix satisfies $P_\pi^2 = P_\pi$. It is **orthogonal** when the error $x - \pi_U(x)$ is orthogonal to every basis vector of $U$, which is exactly the condition that minimizes $\|x - \pi_U(x)\|$.

### Onto a line vs. a subspace
For a line spanned by $b$, $\pi_U(x) = \frac{bb^\top}{\|b\|^2}x$ with coordinate $\lambda = \frac{b^\top x}{\|b\|^2}$. For an $m$-dimensional subspace with basis matrix $B = [b_1,\dots,b_m]$, the orthogonality conditions give the **normal equation** $B^\top B\,\lambda = B^\top x$, hence $\lambda = (B^\top B)^{-1}B^\top x$ and the projection matrix $P_\pi = B(B^\top B)^{-1}B^\top$. The factor $(B^\top B)^{-1}B^\top$ is the **pseudo-inverse**. If $B$ is an ONB, $B^\top B = I$ and everything collapses to $\pi_U(x) = BB^\top x$, $\lambda = B^\top x$.

### Affine case
Projection onto an affine subspace $L = x_0 + U$ is $\pi_L(x) = x_0 + \pi_U(x - x_0)$.

### Why it matters
Orthogonal projection is the geometry behind least-squares regression (projecting $b$ onto the column space of $A$ minimizes residual error), the reconstruction-error view of PCA, and Gram-Schmidt orthogonalization; in ML it is the canonical way to find the best low-dimensional approximation of high-dimensional data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[principal-component-analysis]] — prerequisite-of
- [[linear-algebra]] — uses
- [[inner-product]] — uses
- [[orthogonality]] — uses
[To be populated during integration]