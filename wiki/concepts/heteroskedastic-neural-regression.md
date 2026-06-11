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
- deep-learning
id: pkis:concept:heteroskedastic-neural-regression
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch13
tags:
- regression
- uncertainty
- heteroskedasticity
- multi-head
- calibration
title: Heteroskedastic Regression with Neural Networks
understanding: 0
---

## Definition
A neural network can parameterize both the conditional mean and input-dependent variance of a regression target:
$$p(y|x,\theta) = \mathcal{N}\!\left(y\,\big|\,w_\mu^T f(x;w_{\text{shared}}),\; \sigma_+\!\left(w_\sigma^T f(x;w_{\text{shared}})\right)\right)$$
where $\sigma_+(a) = \log(1 + e^a)$ (softplus) ensures positivity of the variance, and $f(x;w_{\text{shared}})$ is a shared backbone followed by two output heads: a linear head for $\mu$ and a softplus head for $\sigma$.

### Why it matters
Models with a fixed (input-independent) output variance are miscalibrated when the true noise level varies across input space. The multi-head architecture simultaneously learns mean and uncertainty, enabling well-calibrated prediction intervals without extra computational cost.

### Connection to stochastic volatility
The model can represent data-generating processes in which both mean and variance evolve (e.g., financial returns, climate measurements), providing a lightweight alternative to full stochastic-volatility models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]