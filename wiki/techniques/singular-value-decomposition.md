---
title: "Singular Value Decomposition (SVD)"
knowledge_type: technique
also_type: [result]
domain: [statistical-learning]
tags: [linear-algebra, dimensionality-reduction]
related_concepts: ["[[matrix-decompositions]]", "[[eigendecomposition]]", "[[principal-component-analysis]]"]
sources: ["[[deisenroth-mml]]", "[[benzi-hidden-structure-matrices]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

## Reading Path
- [[deisenroth-mml]] (unread) — full derivation: existence proof, thin vs. full SVD, connection to eigendecomposition and PCA
- [[benzi-hidden-structure-matrices-ch01]] (unread) — Van Loan: Tucker decomposition as multi-mode SVD; tensor train SVD; Kronecker product structure enabling FFT-accelerated computation

Factorization $A = U\Sigma V^T$ of any real matrix into orthogonal matrices $U, V$ and diagonal $\Sigma$ (singular values); the rank-$k$ truncation gives the best low-rank approximation in Frobenius norm, making SVD the computational backbone of PCA, latent semantic analysis, and matrix completion. Classification note: also functions as a result (the existence and uniqueness theorem for SVD).
