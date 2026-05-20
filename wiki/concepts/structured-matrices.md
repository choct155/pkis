---
title: "Structured Matrices"
knowledge_type: concept
also_type: []
domain: [optimization, statistical-learning]
tags: [linear-algebra, numerical-methods, toeplitz, low-rank, hierarchical-matrices, displacement-rank, tensors]
related_concepts: ["[[matrix-decompositions]]", "[[singular-value-decomposition]]", "[[linear-algebra]]", "[[toeplitz-matrices]]", "[[hierarchical-low-rank-matrices]]", "[[tensor-decompositions]]"]
sources: ["[[benzi-hidden-structure-matrices]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Matrices possessing non-obvious structural properties — such as constant diagonals (Toeplitz), low-rank off-diagonal blocks (hierarchical/H-matrices), displacement-rank characterizations (Cauchy-like), decay patterns, or group symmetries — that enable sub-quadratic algorithms for matrix-vector products, factorizations, and function evaluations compared to generic O(n²) or O(n³) methods.

Hidden structure is "hidden" in the sense that it may not be apparent from the matrix entries themselves but is revealed through algebraic analysis (e.g., the DFT matrix is dense but has O(n log n) structure via Kronecker factorization). The detection and exploitation of such structure is a central theme in modern numerical linear algebra, with applications ranging from PDE solvers to signal processing to quantum physics.

## Reading Path
- [[benzi-hidden-structure-matrices]] (unread) — book-length treatment of multiple structure types: Toeplitz/displacement-rank (Ch. 2), hierarchical low-rank (Ch. 3), off-diagonal decay/localization (Ch. 4), group-equivariant structure (Ch. 5), tensor-derived structure (Ch. 1)
