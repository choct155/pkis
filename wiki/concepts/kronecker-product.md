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
- machine-learning
id: pkis:concept:kronecker-product
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch07
tags:
- tensor-product
- vec-operator
- K-FAC
- separable-covariance
- multi-linear
title: Kronecker Product
understanding: 0
---

## Definition
For matrices $\mathbf{A} \in \mathbb{R}^{m\times n}$ and $\mathbf{B} \in \mathbb{R}^{p\times q}$, the **Kronecker product** is the $mp \times nq$ block matrix
$$\mathbf{A} \otimes \mathbf{B} = \begin{pmatrix} a_{11}\mathbf{B} & \cdots & a_{1n}\mathbf{B} \\ \vdots & \ddots & \vdots \\ a_{m1}\mathbf{B} & \cdots & a_{mn}\mathbf{B}\end{pmatrix}.$$
Key identities: $(\mathbf{A}\otimes\mathbf{B})^{-1} = \mathbf{A}^{-1}\otimes\mathbf{B}^{-1}$ and $(\mathbf{A}\otimes\mathbf{B})\operatorname{vec}(\mathbf{C}) = \operatorname{vec}(\mathbf{B}\mathbf{C}\mathbf{A}^T)$.

### Why it matters
Kronecker products arise naturally in multi-linear models, separable covariance structures (Gaussian processes on grids, Kronecker-factored approximate curvature / K-FAC), and the vectorisation of matrix equations. The vec-permutation identity converts matrix equations $\mathbf{AXB}=\mathbf{C}$ into the linear system $(\mathbf{B}^T\otimes\mathbf{A})\operatorname{vec}(\mathbf{X})=\operatorname{vec}(\mathbf{C})$, enabling direct solution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]