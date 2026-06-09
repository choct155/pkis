---
aliases:
- SVD
also_type:
- result
coverage: 3
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
generalizes:
- eigendecomposition
id: pkis:technique:singular-value-decomposition
knowledge_type: technique
maturity: settled
related_concepts:
- '[[matrix-decompositions]]'
- '[[eigendecomposition]]'
- '[[principal-component-analysis]]'
sources:
- '[[deisenroth-mml]]'
- '[[benzi-hidden-structure-matrices]]'
- '[[carrell-groups-matrices-vectors]]'
specializes:
- matrix-decompositions
tags:
- linear-algebra
- dimensionality-reduction
title: Singular Value Decomposition (SVD)
understanding: 0
uses:
- eigendecomposition
---

## Reading Path
- [[deisenroth-mml]] (unread) — full derivation: existence proof, thin vs. full SVD, connection to eigendecomposition and PCA
- [[benzi-hidden-structure-matrices-ch01]] (unread) — Van Loan: Tucker decomposition as multi-mode SVD; tensor train SVD; Kronecker product structure enabling FFT-accelerated computation
- [[carrell-groups-matrices-vectors-ch09]] (unread) — polar decomposition closely related to SVD; positive definite matrix structure

Factorization $A = U\Sigma V^T$ of any real matrix into orthogonal matrices $U, V$ and diagonal $\Sigma$ (singular values); the rank-$k$ truncation gives the best low-rank approximation in Frobenius norm, making SVD the computational backbone of PCA, latent semantic analysis, and matrix completion. Classification note: also functions as a result (the existence and uniqueness theorem for SVD).

## Connections
- [[eigendecomposition]] — uses
- [[eigendecomposition]] — generalizes
- [[matrix-decompositions]] — specializes