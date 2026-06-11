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
- linear-algebra
id: pkis:concept:precision-matrix
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch02
- goodfellow-deeplearning-ch03
tags:
- gaussian-distribution
- covariance
- conditional-distribution
- graphical-models
title: Precision Matrix
understanding: 0
---

## Definition
$$\boldsymbol{\Lambda} \equiv \boldsymbol{\Sigma}^{-1}$$

The precision matrix is the inverse of the covariance matrix of a multivariate Gaussian. In the partitioned form $\boldsymbol{\Lambda}=\begin{pmatrix}\Lambda_{aa}&\Lambda_{ab}\\\Lambda_{ba}&\Lambda_{bb}\end{pmatrix}$, the conditional distribution $p(\mathbf{x}_a|\mathbf{x}_b)$ has covariance $\Lambda_{aa}^{-1}$ and mean $\mu_a - \Lambda_{aa}^{-1}\Lambda_{ab}(\mathbf{x}_b-\mu_b)$, expressions that are simpler in precision-matrix form than in covariance form.

### Why it matters
Precision matrices arise naturally whenever conditioning on observations: the conditional precision is additive in the linear-Gaussian model. Sparse precision matrices define Gaussian Markov random fields (undirected graphical models). The Wishart distribution is the conjugate prior for the precision matrix of a multivariate Gaussian, enabling Bayesian covariance estimation.

### Relation to Schur complement
The Schur complement $(\Sigma_{aa}-\Sigma_{ab}\Sigma_{bb}^{-1}\Sigma_{ba})$ equals $\Lambda_{aa}^{-1}$, linking conditional Gaussian parameters to block-matrix inversion.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]