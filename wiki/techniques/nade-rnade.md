---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- density-estimation
- generative-models
id: pkis:technique:nade-rnade
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch22
tags:
- NADE
- RNADE
- MADE
- autoregressive
- mixture-of-gaussians
- density-estimation
title: NADE / RNADE (Neural Autoregressive Density Estimator)
understanding: 0
---

## Definition
$$p(x_t \mid x_{1:t-1}) = \sum_{k=1}^{K} \pi_{t,k}\, \mathcal{N}(x_t \mid \mu_{t,k}, \sigma^2_{t,k}), \quad (\mu_t, \sigma_t, \pi_t) = f_t(x_{1:t-1};\theta_t)$$

NADE (Neural Autoregressive Density Estimator) parameterises each conditional $p(x_t|x_{1:t-1})$ with a neural network. RNADE (real-valued NADE) extends this to continuous data by outputting mixture-of-Gaussians parameters. Both models share parameters across conditionals via a single masked network (MADE) for efficiency.

### Why it matters
NADE/RNADE provided the first scalable, neural-network-based autoregressive density estimators, achieving competitive performance on image and tabular benchmarks. The parameter-sharing trick via masking (MADE) reduced the otherwise $O(T)$ separate networks to a single forward pass.

### Limitation
Assumes a fixed linear variable ordering, which is natural for sequential data but problematic for unordered domains like images or graphs (addressed by orderless extensions).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]