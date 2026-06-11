---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability
- statistics
- machine-learning
id: pkis:result:linear-gaussian-model
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch02
tags:
- gaussian-distribution
- bayesian-inference
- kalman-filter
- conjugate-prior
title: 'Linear-Gaussian Model: Marginal and Posterior'
understanding: 0
---

## Definition
Given a Gaussian marginal $p(\mathbf{x})=\mathcal{N}(\mathbf{x}|\boldsymbol{\mu},\boldsymbol{\Lambda}^{-1})$ and Gaussian conditional $p(\mathbf{y}|\mathbf{x})=\mathcal{N}(\mathbf{y}|A\mathbf{x}+\mathbf{b},L^{-1})$:

$$p(\mathbf{y}) = \mathcal{N}(\mathbf{y}|A\boldsymbol{\mu}+\mathbf{b},\; L^{-1}+A\boldsymbol{\Lambda}^{-1}A^T)$$
$$p(\mathbf{x}|\mathbf{y}) = \mathcal{N}(\mathbf{x}|\boldsymbol{\Sigma}\{A^TL(\mathbf{y}-\mathbf{b})+\boldsymbol{\Lambda}\boldsymbol{\mu}\},\; \boldsymbol{\Sigma})$$
$$\boldsymbol{\Sigma} = (\boldsymbol{\Lambda}+A^TLA)^{-1}$$

The posterior precision equals the prior precision plus the precision contribution from each observation through the linear map $A$.

### Why it matters
This result is a cornerstone of Bayesian signal processing: it recovers the Kalman filter update (with $A=I$), forms the basis of Gaussian process regression, factor analysis, probabilistic PCA, and linear regression with Gaussian noise. The posterior mean is a precision-weighted interpolation between prior and data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]