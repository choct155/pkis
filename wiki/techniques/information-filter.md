---
aliases: []
also_type: []
analogous-to:
- kalman-filter
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
- signal-processing
- statistics
- machine-learning
id: pkis:technique:information-filter
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch08
tags:
- kalman
- natural-parameters
- information-form
- precision-matrix
title: Information Form Kalman Filter
understanding: 0
uses:
- exponential-family
---

## Definition
Parameterize the Gaussian belief state by its natural parameters: information vector $\eta_{t|t} = \Sigma_{t|t}^{-1}\mu_{t|t}$ and information matrix $\Lambda_{t|t} = \Sigma_{t|t}^{-1}$. The update step then takes the additive form
$$\Lambda_{t|t} = \Lambda_{t|t-1} + H_t^T R_t^{-1} H_t, \quad \eta_{t|t} = \eta_{t|t-1} + H_t^T R_t^{-1}(y_t - D_tu_t - d_t)$$
while the predict step requires a matrix inversion (dual to the moment-form update).

### Why it matters
The information filter is preferable when (i) the observation dimension $N_y \gg N_z$ (update is cheap, $O(N_z^2 N_y)$ vs $O(N_y^3)$), (ii) $R_t^{-1}$ is precomputed or sparse, or (iii) numerical precision is critical. It is the dual of the standard Kalman filter: easy updates, hard predictions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[exponential-family]] — uses: uses natural parameters of the Gaussian
- [[kalman-filter]] — analogous-to
[To be populated during integration]