---
title: "Singular Value Decomposition (SVD)"
knowledge_type: technique
also_type: [result]
domain: [statistical-learning]
tags: [linear-algebra, dimensionality-reduction]
related_concepts: ["[[matrix-decompositions]]", "[[eigendecomposition]]", "[[principal-component-analysis]]"]
sources: ["[[deisenroth-mml]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Factorization $A = U\Sigma V^T$ of any real matrix into orthogonal matrices $U, V$ and diagonal $\Sigma$ (singular values); the rank-$k$ truncation gives the best low-rank approximation in Frobenius norm, making SVD the computational backbone of PCA, latent semantic analysis, and matrix completion. Classification note: also functions as a result (the existence and uniqueness theorem for SVD).
