---
aliases: []
also_type:
- framework
coverage: 3
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
extends:
- linear-mapping
id: pkis:concept:matrix-decompositions
knowledge_type: concept
maturity: settled
prerequisite-of:
- principal-component-analysis
related_concepts:
- '[[linear-algebra]]'
- '[[singular-value-decomposition]]'
- '[[eigendecomposition]]'
- '[[principal-component-analysis]]'
sources:
- '[[deisenroth-mml]]'
- '[[benzi-hidden-structure-matrices]]'
- '[[carrell-groups-matrices-vectors]]'
tags:
- linear-algebra
- mathematical-foundations
title: Matrix Decompositions
understanding: 0
---

## Reading Path
- [[deisenroth-mml]] (unread) — foundational family: eigendecomposition, SVD, Cholesky; matrix phylogeny relating when each applies
- [[benzi-hidden-structure-matrices]] (unread) — structured variants exploiting hidden regularity: Toeplitz (displacement rank), hierarchical low-rank, group-equivariant; Tucker/CP/tensor-train as multi-mode generalizations
- [[carrell-groups-matrices-vectors-ch04]] (unread) — LPDU factorization: LU generalized with permutation matrix group element

The family of factorizations that reveal structure in matrices — eigendecomposition (for square symmetric matrices), SVD (for any matrix), Cholesky (for positive definite matrices) — organized by MML's "matrix phylogeny" showing how each relates to the others and when each applies.

## Connections
- [[linear-mapping]] — extends: Eigendecomposition/SVD seek a basis change making a linear map's matrix diagonal (Ch. 4/Ch. 10), foreshadowed by the basis-change theorem.
- [[principal-component-analysis]] — prerequisite-of: MML Ch.1: matrix decompositions (Ch.4) give efficient, interpretable operations on data matrices; PCA (Ch.10) is built directly on eigendecomposition/SVD of the covariance matrix.