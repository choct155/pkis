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
- statistics
id: pkis:concept:design-matrix
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch03
- goodfellow-deeplearning-ch05
- murphy-pml1-intro-ch01
tags:
- feature-matrix
- linear-regression
- basis-functions
- gram-matrix
title: Design Matrix
understanding: 0
---

## Definition
The **design matrix** $\boldsymbol{\Phi}$ is the $N \times M$ matrix of basis function evaluations at training inputs:

$$\Phi_{nj} = \phi_j(x_n), \quad n=1,\ldots,N,\; j=0,\ldots,M-1$$

Columns of $\boldsymbol{\Phi}$ are the basis vectors in $N$-dimensional data space; rows are the feature vectors $\boldsymbol{\phi}(x_n)^T$ in $M$-dimensional parameter space.

### Why it matters
Centralises all data-dependent computation: the normal equations, the Bayesian posterior precision $\mathbf{S}_N^{-1} = \alpha\mathbf{I}+\beta\boldsymbol{\Phi}^T\boldsymbol{\Phi}$, the log evidence, and the eigenvalue analysis of the evidence approximation all hinge on $\boldsymbol{\Phi}$. The Gram matrix $\boldsymbol{\Phi}^T\boldsymbol{\Phi}$ determines the ridge-regression solution; the hat matrix $\boldsymbol{\Phi}\boldsymbol{\Phi}^\dagger$ is the orthogonal projector onto the model subspace.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]