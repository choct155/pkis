---
aliases: []
also_type: []
analogous-to:
- trace
applies:
- eigendecomposition
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
id: pkis:concept:determinant
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- eigendecomposition
related_concepts: []
sources:
- deisenroth-mml-ch04
- carrell-groups-matrices-vectors-ch05
tags: []
title: Determinant
understanding: 0
---

## Definition
$$\det(A) = \sum_{k=1}^{n} (-1)^{k+j} a_{kj} \det(A_{k,j})$$

The determinant is a scalar-valued function on square matrices $A \in \mathbb{R}^{n\times n}$ that measures the signed $n$-dimensional volume of the parallelepiped spanned by the matrix columns, and equals zero exactly when the matrix is singular.

### How it is computed
Closed forms exist for small matrices: $\det(A)=a_{11}$ for $n=1$, $a_{11}a_{22}-a_{12}a_{21}$ for $n=2$, and Sarrus' rule for $n=3$. For general $n$, the **Laplace expansion** above recursively reduces an $n\times n$ determinant to $(n-1)\times(n-1)$ submatrices ($A_{k,j}$ deletes row $k$, column $j$). In practice one uses Gaussian elimination to reach triangular form, where $\det(T)=\prod_i T_{ii}$.

### Key properties
$\det(AB)=\det(A)\det(B)$, $\det(A^\top)=\det(A)$, $\det(A^{-1})=1/\det(A)$, and $\det(\lambda A)=\lambda^n\det(A)$. Row/column swaps flip the sign; adding a multiple of one row to another leaves it unchanged. Crucially, $\det(A)=\prod_i \lambda_i$, the product of eigenvalues, and the determinant is invariant under basis change (similar matrices share it).

### Why it matters
$A$ is invertible iff $\det(A)\neq 0$ iff $\mathrm{rk}(A)=n$. The determinant feeds the **characteristic polynomial** $p_A(\lambda)=\det(A-\lambda I)$, whose roots are the eigenvalues, making it the analytic gateway to eigentheory. The sign reports basis orientation. Modern numerical ML mostly supersedes explicit determinants with direct elimination, but the determinant remains an indispensable theoretical tool for invertibility, volume change, and eigenvalue derivation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[trace]] — analogous-to
- [[eigendecomposition]] — applies
- [[eigendecomposition]] — prerequisite-of
[To be populated during integration]