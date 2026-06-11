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
- signal-processing
- statistics
id: pkis:concept:kalman-gain
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch08
tags:
- kalman
- Bayesian-update
- signal-to-noise
- state-estimation
title: Kalman Gain Matrix
understanding: 0
---

## Definition
$$K_t = \Sigma_{t|t-1}H_t^T S_t^{-1} = \Sigma_{t|t-1}H_t^T(H_t\Sigma_{t|t-1}H_t^T + R_t)^{-1}$$

The $N_z \times N_y$ matrix that weights the **innovation** (observation residual) $e_t = y_t - \hat{y}_t$ when updating the filtered mean: $\mu_{t|t} = \mu_{t|t-1} + K_t e_t$. In the scalar case with $H=I$, $K_t = \Sigma_{t|t-1}/S_t$ is the ratio of prior variance to total observation variance — a form of inverse signal-to-noise ratio.

### Why it matters
The Kalman gain encodes the optimal trade-off between trusting the dynamics prediction and trusting the sensor measurement. Understanding $K_t$ reveals why the filter reduces to pure prediction when sensors are very noisy ($R_t \to \infty$, $K_t \to 0$) and to pure measurement when the prior is diffuse ($\Sigma_{t|t-1} \to \infty$, $K_t \to H_t^{-1}$).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]