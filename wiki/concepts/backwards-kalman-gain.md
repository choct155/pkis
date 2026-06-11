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
id: pkis:concept:backwards-kalman-gain
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch08
tags:
- kalman
- RTS-smoother
- backwards-pass
- smoothing
title: Backwards Kalman Gain (Smoother Gain)
understanding: 0
---

## Definition
$$J_t = \Sigma_{t|t}F_t^T\Sigma_{t+1|t}^{-1}$$

The $N_z \times N_z$ matrix used in the RTS backward pass to propagate smoothed information from step $t+1$ back to step $t$. Analogous to the forward Kalman gain $K_t$, it weights the correction $(\mu_{t+1|T}-\mu_{t+1|t})$ applied to the filtered mean.

### Why it matters
Understanding $J_t$ clarifies the backward information flow in the RTS smoother and enables the derivation of the smoothed two-slice joint $p(z_t, z_{t+1}|y_{1:T})$, which is required for the EM M-step during parameter learning in LG-SSMs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]