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
- deep-learning
- probabilistic-modeling
id: pkis:concept:heteroscedastic-neural-network
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch06
tags:
- uncertainty-quantification
- output-unit
- conditional-gaussian
- precision-parametrization
title: Heteroscedastic Neural Network Model
understanding: 0
---

## Definition
A heteroscedastic neural network outputs both the mean and the variance (or precision) of a conditional Gaussian distribution, allowing the predicted uncertainty to vary with input: $$p(y\mid\mathbf{x}) = \mathcal{N}\!\left(y;\,\mu(\mathbf{x};\theta),\,\sigma^2(\mathbf{x};\theta)\right).$$ The precision $\beta(\mathbf{x}) = \sigma^{-2}(\mathbf{x})$ is typically obtained by passing a raw network output through a softplus: $\beta = \zeta(a)$, ensuring positivity. The diagonal multivariate case uses $\text{diag}(\beta)$.

Parametrizing via precision rather than variance or standard deviation yields a numerically better-conditioned objective because the log-likelihood involves only multiplication and $\log\beta$, avoiding unstable divisions near zero.

### Why it matters
Homoscedastic regression assumes constant noise, which is incorrect for many real-world problems (e.g., image regions vary in predictability). Heteroscedastic models learn input-dependent uncertainty, which is critical for downstream decision-making and is a building block of mixture density networks and Bayesian deep learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]