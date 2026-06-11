---
aliases: []
also_type: []
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
generalizes:
- rotation-matrix
id: pkis:concept:orthogonal-matrix
instantiates:
- orthogonality
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch02
specializes:
- matrix-inverse
tags:
- orthogonal matrix
- isometry
- rotation
- eigendecomposition
- SVD
title: Orthogonal Matrix
understanding: 0
uses:
- matrix-transpose
---

## Definition
$$\mathbf{A}^T\mathbf{A} = \mathbf{A}\mathbf{A}^T = \mathbf{I} \implies \mathbf{A}^{-1} = \mathbf{A}^T$$

An orthogonal matrix is a square real matrix whose rows and columns are each mutually orthonormal unit vectors; equivalently, multiplication by an orthogonal matrix preserves Euclidean norms and angles (it is an isometry).

### Why it matters
Orthogonal matrices appear as the $Q$ factor in eigendecomposition of symmetric matrices and as the $U,V$ factors in SVD. Their inversion is $O(n^2)$ instead of $O(n^3)$, which matters for computational efficiency. Rotation and reflection matrices are orthogonal, connecting linear algebra to geometric transformations used in robotics and computer vision.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[rotation-matrix]] — generalizes
- [[orthogonality]] — instantiates
- [[matrix-inverse]] — specializes
- [[matrix-transpose]] — uses
[To be populated during integration]