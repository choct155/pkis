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
- statistics
- signal-processing
id: pkis:technique:kalman-rts-smoother
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch08
tags:
- kalman
- smoothing
- FFBS
- RTS
- state-estimation
- offline-inference
title: Kalman (RTS) Smoother
understanding: 0
---

## Definition
$$J_t = \Sigma_{t|t}F_t^T\Sigma_{t+1|t}^{-1}$$
$$\mu_{t|T} = \mu_{t|t} + J_t(\mu_{t+1|T}-\mu_{t+1|t})$$
$$\Sigma_{t|T} = \Sigma_{t|t} + J_t(\Sigma_{t+1|T}-\Sigma_{t+1|t})J_t^T$$

A two-pass algorithm (forwards filtering, then backwards smoothing) that computes the fixed-interval smoothed posterior $p(\mathbf{z}_t|\mathbf{y}_{1:T}) = \mathcal{N}(\mu_{t|T}, \Sigma_{t|T})$ for a linear-Gaussian SSM. The backwards pass uses the backwards Kalman gain $J_t$ to propagate information from future observations back to earlier time steps.

### Why it matters
Smoothing yields strictly smaller posterior covariances than filtering and is essential for offline trajectory estimation, parameter learning via EM (E-step), and drawing posterior samples via forwards-filtering backwards-sampling. The RTS smoother is preferred over two-filter smoothing due to numerical stability.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]