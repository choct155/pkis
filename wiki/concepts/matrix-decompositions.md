---
id: "pkis:concept:matrix-decompositions"
aliases: []
title: "Matrix Decompositions"
knowledge_type: concept
also_type: [framework]
domain: [statistical-learning]
tags: [linear-algebra, mathematical-foundations]
related_concepts: ["[[linear-algebra]]", "[[singular-value-decomposition]]", "[[eigendecomposition]]", "[[principal-component-analysis]]"]
sources: ["[[deisenroth-mml]]", "[[benzi-hidden-structure-matrices]]", "[[carrell-groups-matrices-vectors]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

## Reading Path
- [[deisenroth-mml]] (unread) — foundational family: eigendecomposition, SVD, Cholesky; matrix phylogeny relating when each applies
- [[benzi-hidden-structure-matrices]] (unread) — structured variants exploiting hidden regularity: Toeplitz (displacement rank), hierarchical low-rank, group-equivariant; Tucker/CP/tensor-train as multi-mode generalizations
- [[carrell-groups-matrices-vectors-ch04]] (unread) — LPDU factorization: LU generalized with permutation matrix group element

The family of factorizations that reveal structure in matrices — eigendecomposition (for square symmetric matrices), SVD (for any matrix), Cholesky (for positive definite matrices) — organized by MML's "matrix phylogeny" showing how each relates to the others and when each applies.
