---
aliases: []
also_type: []
applies:
- solving-linear-systems
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
id: pkis:concept:matrix-inverse
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- linear-independence
related_concepts: []
sources:
- goodfellow-deeplearning-ch02
tags:
- matrix inverse
- singular matrix
- identity matrix
- linear system
title: Matrix Inverse and Singular Matrix
understanding: 0
uses:
- matrix-transpose
- determinant
---

## Definition
$$\mathbf{A}^{-1}\mathbf{A} = \mathbf{A}\mathbf{A}^{-1} = \mathbf{I}_n$$

The matrix inverse $\mathbf{A}^{-1}$ is defined for square matrices with linearly independent columns (non-singular matrices); it is the unique matrix that, when multiplied by $\mathbf{A}$, yields the identity. A square matrix with at least one zero eigenvalue—and hence linearly dependent columns—is called **singular** and has no inverse.

### Why it matters
Matrix inversion provides the closed-form solution $\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$ to linear systems, which underlies ordinary least squares, Gaussian conditioning, and Kalman filtering. Singularity is directly linked to eigenvalues: $\mathbf{A}$ is singular iff $\det(\mathbf{A})=0$ iff at least one eigenvalue is zero.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[linear-independence]] — prerequisite-of
- [[determinant]] — uses
- [[solving-linear-systems]] — applies
- [[matrix-transpose]] — uses
[To be populated during integration]