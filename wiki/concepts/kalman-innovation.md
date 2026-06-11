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
- signal-processing
- statistics
- machine-learning
id: pkis:concept:kalman-innovation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- kalman-filter
related_concepts: []
sources:
- murphy-pml2-advanced-ch08
tags:
- kalman
- residual
- one-step-ahead
- model-checking
title: Innovation (Measurement Residual)
understanding: 0
---

## Definition
$$e_t = y_t - \hat{y}_t = y_t - H_t\mu_{t|t-1}, \quad S_t = H_t\Sigma_{t|t-1}H_t^T + R_t$$

The difference between the actual observation $y_t$ and the model's one-step-ahead predicted observation $\hat{y}_t$; $S_t$ is its covariance. Under a correctly specified model, innovations form a zero-mean white-noise sequence, providing a diagnostic tool for model validation.

### Why it matters
Innovations are the signal that drives all updates in the Kalman filter (and its extensions). The log-likelihood of the observation sequence decomposes as $\log p(y_{1:T}) = \sum_t \log \mathcal{N}(y_t|\hat{y}_t, S_t)$, making innovations central to parameter estimation and anomaly detection.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kalman-filter]] — prerequisite-of
[To be populated during integration]