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
- signal-processing
- robotics
id: pkis:technique:extended-kalman-filter
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch08
tags:
- nonlinear-filtering
- kalman
- linearization
- jacobian
- state-estimation
title: Extended Kalman Filter (EKF)
understanding: 0
---

## Definition
For the nonlinear additive-noise SSM $\mathbf{z}_t = \mathbf{f}(\mathbf{z}_{t-1},\mathbf{u}_t)+\mathbf{q}_t$, $\mathbf{y}_t = \mathbf{h}(\mathbf{z}_t,\mathbf{u}_t)+\mathbf{r}_t$, the EKF replaces the nonlinear functions with their first-order Taylor expansions:
$$F_t \equiv \mathrm{Jac}(\mathbf{f}(\cdot,u_t))(\mu_{t-1|t-1}), \quad H_t \equiv \mathrm{Jac}(\mathbf{h}(\cdot,u_t))(\mu_{t|t-1})$$
and then runs standard Kalman filter equations with these Jacobian matrices in place of the linear system matrices.

The **iterated EKF (IEKF)** iteratively re-linearizes the measurement model at the current posterior mean $\mu_{t|t}$, which is equivalent to a Gauss–Newton method minimizing
$$L(z_t) = \tfrac{1}{2}(y_t-h(z_t))^TR_t^{-1}(y_t-h(z_t)) + \tfrac{1}{2}(z_t-\mu_{t|t-1})^T\Sigma_{t|t-1}^{-1}(z_t-\mu_{t|t-1})$$

### Why it matters
The EKF is the workhorse of nonlinear state estimation in robotics, navigation (GPS/INS), and sensor fusion. Its weaknesses — poor accuracy when nonlinearity is large or prior covariance is wide — motivate the UKF and other sigma-point filters.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]