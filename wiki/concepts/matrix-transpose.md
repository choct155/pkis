---
aliases: []
also_type: []
applies:
- tensor-multidimensional-array
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
date_updated: '2026-06-20'
domain:
- linear-algebra
id: pkis:concept:matrix-transpose
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch02
- carrell-groups-matrices-vectors-ch03
tags:
- transpose
- matrix
- symmetric
- orthogonal
title: Matrix Transpose
understanding: 0
uses:
- orthogonality
- linear-mapping
---

## Definition
$$(\mathbf{A}^T)_{i,j} = A_{j,i}$$

The transpose of a matrix is its mirror image across the main diagonal; rows become columns and columns become rows.

The transpose is foundational for expressing dot products, symmetry conditions, and the product rule $(\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T$, which appears constantly in gradient derivations.

### Why it matters
Symmetric matrices satisfy $\mathbf{A} = \mathbf{A}^T$ and admit real eigendecompositions. Orthogonal matrices satisfy $\mathbf{A}^{-1} = \mathbf{A}^T$, making inversion trivial. The relation $(\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T$ is used in backpropagation to compute Jacobian-vector products.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[linear-mapping]] — uses
- [[orthogonality]] — uses
- [[tensor-multidimensional-array]] — applies
[To be populated during integration]