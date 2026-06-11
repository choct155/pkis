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
contrasts-with:
- gram-matrix
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- linear-algebra
- statistics
- machine-learning
id: pkis:concept:scatter-matrix
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- principal-component-analysis
- linear-discriminant-analysis
related_concepts: []
sources:
- murphy-pml1-intro-ch07
specializes:
- linear-algebra
tags:
- covariance
- PCA
- LDA
- sample-covariance
- centering-matrix
title: Scatter Matrix and Sum-of-Squares Matrix
understanding: 0
uses:
- covariance-and-correlation
---

## Definition
For a data matrix $\mathbf{X} \in \mathbb{R}^{N\times D}$ with sample mean $\bar{\mathbf{x}}$, the **sum-of-squares matrix** is
$$S_0 \triangleq \mathbf{X}^T\mathbf{X} = \sum_{n=1}^N \mathbf{x}_n \mathbf{x}_n^T \in \mathbb{R}^{D\times D},$$
and the **scatter matrix** (or unnormalised sample covariance) is
$$S_x \triangleq \sum_{n=1}^N (\mathbf{x}_n - \bar{\mathbf{x}})(\mathbf{x}_n - \bar{\mathbf{x}})^T = \mathbf{X}^T\mathbf{C}_N\mathbf{X},$$
where $\mathbf{C}_N = \mathbf{I}_N - \frac{1}{N}\mathbf{1}\mathbf{1}^T$ is the centering matrix. The sample covariance is $\hat{\boldsymbol{\Sigma}} = S_x / (N-1)$.

### Why it matters
Scatter matrices appear in linear discriminant analysis, PCA, canonical correlation analysis, and multivariate regression. Computing them via $\mathbf{X}^T\mathbf{X}$ is an $O(ND^2)$ operation amenable to BLAS level-3 routines, making it far faster than iterating over data points.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gram-matrix]] — contrasts-with
- [[covariance-and-correlation]] — uses
- [[linear-discriminant-analysis]] — prerequisite-of
- [[principal-component-analysis]] — prerequisite-of
- [[linear-algebra]] — specializes
[To be populated during integration]