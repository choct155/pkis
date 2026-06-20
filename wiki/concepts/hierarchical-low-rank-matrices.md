---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- optimization
id: pkis:concept:hierarchical-low-rank-matrices
knowledge_type: concept
maturity: settled
related_concepts:
- '[[structured-matrices]]'
- '[[matrix-decompositions]]'
- '[[singular-value-decomposition]]'
- '[[regularization]]'
sources:
- '[[benzi-hidden-structure-matrices]]'
- benzi-hidden-structure-matrices-ch03
- benzi-hidden-structure-matrices-ch04
tags:
- linear-algebra
- numerical-pde
- h-matrices
- low-rank
- boundary-element-methods
- structured-matrices
title: Hierarchical Low-Rank Matrices
understanding: 0
---

A class of structured matrices (H-matrices) in which off-diagonal blocks have low numerical rank due to the smoothness of the underlying integral kernel or Green's function, enabling O(n log² n) complexity for matrix-vector products and approximate LU factorizations instead of O(n²) and O(n³) respectively.

The key property: matrices arising from boundary element methods and integral equations over well-separated domains have the property that their off-diagonal blocks (corresponding to far-field interactions) can be well-approximated by low-rank matrices. The hierarchical structure comes from recursively partitioning the matrix into blocks of varying size; near-diagonal blocks are stored densely while off-diagonal blocks are stored in low-rank form. This structure is "hidden" in the sense that the full matrix appears dense but has far fewer degrees of freedom.

## Reading Path
- [[benzi-hidden-structure-matrices]] (unread) — Ch. 3 (Kressner/Ballani): primary treatment; applications to elliptic PDEs; complexity analysis; construction algorithms
- [[benzi-hidden-structure-matrices-ch03]] (unread) — primary chapter