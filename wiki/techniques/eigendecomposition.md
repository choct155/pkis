---
title: "Eigendecomposition"
knowledge_type: technique
also_type: [result]
domain: [statistical-learning]
tags: [linear-algebra]
related_concepts: ["[[matrix-decompositions]]", "[[singular-value-decomposition]]", "[[principal-component-analysis]]"]
sources: ["[[deisenroth-mml]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Factorization $A = PDP^{-1}$ of a diagonalizable square matrix into eigenvectors (columns of $P$) and eigenvalues (diagonal of $D$); restricted to symmetric positive definite matrices, becomes the spectral decomposition $A = PDP^T$ with orthonormal eigenvectors — the form underlying PCA's covariance decomposition.
