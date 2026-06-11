---
aliases: []
also_type: []
applies:
- hessian-matrix
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- linear-algebra
- optimization
id: pkis:concept:positive-definite-matrix
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- covariance-function
- gaussian-process
- gaussian-distribution
- condition-number
related_concepts: []
sources:
- goodfellow-deeplearning-ch02
- murphy-pml1-intro-ch07
specializes:
- linear-algebra
tags:
- positive definite
- positive semidefinite
- eigenvalues
- quadratic form
- covariance
title: Positive Definite and Positive Semidefinite Matrix
understanding: 0
uses:
- eigendecomposition
- cholesky-decomposition
- convex-set-and-function
---

## Definition
A real symmetric matrix $\mathbf{A}$ is **positive definite** (PD) if
$$\forall \mathbf{x} \neq \mathbf{0}: \mathbf{x}^T\mathbf{A}\mathbf{x} > 0$$
and **positive semidefinite** (PSD) if $\mathbf{x}^T\mathbf{A}\mathbf{x} \geq 0$ for all $\mathbf{x}$. Equivalently, $\mathbf{A}$ is PD iff all eigenvalues are strictly positive; PSD iff all eigenvalues are non-negative.

PSD matrices guarantee non-negative quadratic forms; PD matrices additionally guarantee non-singularity.

### Why it matters
Covariance matrices and kernel (Gram) matrices must be PSD. The Hessian of a loss function being PD at a critical point guarantees a local minimum. In optimization, ensuring a step-size update keeps a matrix PD is central to methods like natural gradient and Gauss-Newton.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[condition-number]] — prerequisite-of
- [[gaussian-distribution]] — prerequisite-of
- [[convex-set-and-function]] — uses
- [[cholesky-decomposition]] — uses
- [[linear-algebra]] — specializes
- [[gaussian-process]] — prerequisite-of
- [[covariance-function]] — prerequisite-of
- [[hessian-matrix]] — applies
- [[eigendecomposition]] — uses
[To be populated during integration]