---
aliases: []
also_type: []
analogous-to:
- linear-discriminant-analysis
applies:
- gaussian-distribution
- multivariate-normal-model
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
- statistics
- geometry
- machine-learning
id: pkis:concept:mahalanobis-distance
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- linear-discriminant-analysis
related_concepts: []
sources:
- bishop-prml-ch02
- murphy-pml1-intro-ch03
- murphy-pml1-intro-ch16
tags:
- gaussian-distribution
- distance-metric
- covariance
- discriminant-analysis
title: Mahalanobis Distance
understanding: 0
uses:
- gaussian-distribution
- students-t-distribution
- covariance-and-correlation
- eigendecomposition
- gaussian-mixture-model
- inner-product
---

## Definition
$$\Delta^2 = (\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})$$

The Mahalanobis distance measures how many standard deviations $\mathbf{x}$ lies from the mean $\boldsymbol{\mu}$ of a Gaussian with covariance $\boldsymbol{\Sigma}$; it reduces to Euclidean distance when $\boldsymbol{\Sigma}=I$. Surfaces of constant Mahalanobis distance are ellipsoids aligned with the eigenvectors of $\boldsymbol{\Sigma}$, with radii proportional to $\lambda_i^{1/2}$.

### Why it matters
The Mahalanobis distance appears in the exponent of any multivariate Gaussian and hence in discriminant analysis, Gaussian-kernel SVMs, anomaly detection, and robust statistics. It automatically accounts for variable scales and correlations, unlike Euclidean distance. The multivariate t-distribution is also parameterised through $\Delta^2$, and the squared distance follows a chi-squared distribution under the true Gaussian.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[linear-discriminant-analysis]] — analogous-to: LDA implicitly uses a Mahalanobis-like metric via pooled covariance
- [[inner-product]] — uses: Mahalanobis distance is an inner product in the M-weighted space
- [[gaussian-mixture-model]] — uses
- [[eigendecomposition]] — uses
- [[covariance-and-correlation]] — uses
- [[multivariate-normal-model]] — applies
- [[gaussian-distribution]] — applies
- [[students-t-distribution]] — uses: Multivariate t parameterised via squared Mahalanobis distance
- [[linear-discriminant-analysis]] — prerequisite-of
- [[gaussian-distribution]] — uses
[To be populated during integration]