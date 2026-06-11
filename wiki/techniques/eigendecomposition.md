---
aliases: []
also_type:
- result
coverage: 2
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
id: pkis:technique:eigendecomposition
knowledge_type: technique
maturity: settled
related_concepts:
- '[[matrix-decompositions]]'
- '[[singular-value-decomposition]]'
- '[[principal-component-analysis]]'
sources:
- '[[deisenroth-mml]]'
- '[[carrell-groups-matrices-vectors]]'
specializes:
- matrix-decompositions
tags:
- linear-algebra
title: Eigendecomposition
understanding: 0
uses:
- positive-definite-matrix
- orthogonal-matrix
---

Factorization $A = PDP^{-1}$ of a diagonalizable square matrix into eigenvectors (columns of $P$) and eigenvalues (diagonal of $D$); restricted to symmetric positive definite matrices, becomes the spectral decomposition $A = PDP^T$ with orthonormal eigenvectors — the form underlying PCA's covariance decomposition.

## Reading Path
- [[deisenroth-mml]] (unread) — eigenvalue/eigenvector definition, characteristic polynomial, spectral decomposition for SPD matrices
- [[carrell-groups-matrices-vectors-ch08]] (unread) — characteristic polynomial, diagonalizability, Cayley–Hamilton, Principal Axis Theorem
- [[carrell-groups-matrices-vectors-ch09]] (unread) — Schur triangularization, normal matrix theorem, quadratic forms, polar decomposition

## Connections
- [[orthogonal-matrix]] — uses
- [[positive-definite-matrix]] — uses
- [[matrix-decompositions]] — specializes