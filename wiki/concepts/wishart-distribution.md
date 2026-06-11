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
- probability
- statistics
- bayesian-inference
id: pkis:concept:wishart-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch02
- murphy-pml2-advanced-ch02
tags:
- matrix-distribution
- conjugate-prior
- precision-matrix
- multivariate-gaussian
title: Wishart Distribution
understanding: 0
---

## Definition
$$\mathcal{W}(\boldsymbol{\Lambda}|\mathbf{W},\nu) = B|\boldsymbol{\Lambda}|^{(\nu-D-1)/2}\exp\left\{-\tfrac{1}{2}\text{Tr}(\mathbf{W}^{-1}\boldsymbol{\Lambda})\right\}$$

where $\nu>D-1$ is the degrees of freedom, $\mathbf{W}$ is a $D\times D$ positive-definite scale matrix, and $B$ is the normalisation constant. It is the conjugate prior for the precision matrix $\boldsymbol{\Lambda}$ of a multivariate Gaussian.

### Why it matters
The Wishart is the matrix generalisation of the Gamma distribution: if $\nu$ vectors $\mathbf{y}_i\sim\mathcal{N}(\mathbf{0},\mathbf{W})$ are drawn independently, then $\sum_i\mathbf{y}_i\mathbf{y}_i^T\sim\mathcal{W}(\mathbf{W},\nu)$. In Bayesian multivariate analysis, the Normal-Wishart distribution $\mathcal{N}(\boldsymbol{\mu}|\boldsymbol{\mu}_0,(\beta\boldsymbol{\Lambda})^{-1})\mathcal{W}(\boldsymbol{\Lambda}|\mathbf{W},\nu)$ is the conjugate prior for the mean and precision of a multivariate Gaussian, enabling closed-form posterior updates.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]