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
- machine-learning
- linear-algebra
- kernel-methods
id: pkis:concept:gram-matrix
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch06
- murphy-pml1-intro-ch07
- murphy-pml1-intro-ch17
tags:
- gram-matrix
- kernel
- positive-semidefinite
- dual-representation
title: Gram Matrix
understanding: 0
---

## Definition
$$K_{nm} = k(\mathbf{x}_n, \mathbf{x}_m) = \varphi(\mathbf{x}_n)^T\varphi(\mathbf{x}_m), \quad \mathbf{K} = \boldsymbol{\Phi}\boldsymbol{\Phi}^T \in \mathbb{R}^{N \times N}$$

The Gram matrix collects all pairwise kernel evaluations between training points; it is symmetric and positive semi-definite by construction, encoding the geometry of the data in feature space.

### Why it matters
The Gram matrix is the central object of kernel methods: the dual formulation of regularised least squares yields the predictor $y(\mathbf{x}) = \mathbf{k}(\mathbf{x})^T(\mathbf{K}+\lambda I)^{-1}\mathbf{t}$, expressed entirely through $K$. Being PSD is a necessary and sufficient condition for a function to be a valid kernel, so checking the Gram matrix directly gives the canonical validity test without requiring an explicit feature map.

### Connections
For Gaussian process regression the Gram matrix becomes the prior covariance over training function values, and adding $\beta^{-1}I$ gives the noise-augmented covariance $C_N$ used in prediction.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]