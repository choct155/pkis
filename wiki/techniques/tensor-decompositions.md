---
id: "pkis:technique:tensor-decompositions"
aliases: []
title: "Tensor Decompositions"
knowledge_type: technique
also_type: []
domain: [optimization, statistical-learning]
tags: [linear-algebra, tensors, low-rank, tucker, cp-decomposition, tensor-train, kronecker-products, dimensionality-reduction]
related_concepts: ["[[structured-matrices]]", "[[singular-value-decomposition]]", "[[matrix-decompositions]]", "[[principal-component-analysis]]", "[[curse-of-dimensionality]]"]
sources: ["[[benzi-hidden-structure-matrices]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

Generalizations of matrix factorizations (especially SVD) to multi-dimensional arrays (tensors), enabling compact representations that scale with the number of modes d rather than exponentially with mode dimensions n.

The three principal families are: (1) Tucker decomposition — a multi-mode SVD where each mode has its own orthonormal factor matrix and a core tensor encodes the interactions; (2) CP (CANDECOMP/PARAFAC) decomposition — expresses the tensor as a sum of rank-1 tensors (outer products of vectors), analogous to a sum of rank-1 matrices; (3) Tensor Train (TT) decomposition — factorizes the tensor as a chain of three-dimensional cores, enabling O(d·n·r²) representation when all TT-ranks equal r. A key application is beating the curse of dimensionality: a d-dimensional tensor with n^d entries can be represented with O(d·n·r) parameters when intrinsic rank r is small.

## Reading Path
- [[benzi-hidden-structure-matrices]] (unread) — Ch. 1 (Van Loan): comprehensive treatment of Tucker, CP, tensor train, and Kronecker product structure; connections to matrix SVD; curse of dimensionality context
- [[benzi-hidden-structure-matrices-ch01]] (unread) — primary chapter
