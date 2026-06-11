---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- linear-algebra
- statistics
- machine-learning
id: pkis:technique:schur-complement
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch07
tags:
- block-matrix
- matrix-inversion
- Gaussian-conditioning
- Kalman-filter
title: Schur Complement and Partitioned Matrix Inversion
understanding: 0
---

## Definition
For a block matrix $\mathbf{M} = \begin{pmatrix}\mathbf{E} & \mathbf{F}\\ \mathbf{G} & \mathbf{H}\end{pmatrix}$, the **Schur complement** of $\mathbf{M}$ with respect to $\mathbf{H}$ is
$$\mathbf{M}/\mathbf{H} \triangleq \mathbf{E} - \mathbf{F}\mathbf{H}^{-1}\mathbf{G}.$$
The **partitioned inverse formula** then gives
$$\mathbf{M}^{-1} = \begin{pmatrix}(\mathbf{M}/\mathbf{H})^{-1} & -(\mathbf{M}/\mathbf{H})^{-1}\mathbf{F}\mathbf{H}^{-1}\\ -\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1} & \mathbf{H}^{-1}+\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1}\mathbf{F}\mathbf{H}^{-1}\end{pmatrix}.$$
The proof proceeds by block-diagonalising $\mathbf{M}$ with triangular factors and then inverting.

### Why it matters
Schur complements are fundamental in Gaussian conditioning (marginal and conditional covariances), Kalman filtering, and efficient computation of joint inverses. They also underlie the matrix inversion lemma (Sherman–Morrison–Woodbury), enabling $O(D^3)$ computations in place of $O(N^3)$ when $D \ll N$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]