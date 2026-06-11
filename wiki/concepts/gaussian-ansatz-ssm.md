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
contrasts-with:
- variational-inference
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- signal-processing
id: pkis:concept:gaussian-ansatz-ssm
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- kalman-filter
- extended-kalman-filter
related_concepts: []
sources:
- murphy-pml2-advanced-ch08
tags:
- Gaussian-approximation
- belief-propagation
- state-estimation
- approximate-inference
title: Gaussian Ansatz for State Estimation
understanding: 0
---

## Definition
The approximation of representing the belief state $p(\mathbf{z}_t|\mathbf{y}_{1:t})$ by a Gaussian $\mathcal{N}(\mu_{t|t}, \Sigma_{t|t})$ even when the true posterior is non-Gaussian (e.g., in nonlinear or non-Gaussian SSMs). The ansatz is exact for LG-SSMs (Kalman filter), but is applied approximately in the EKF, UKF, and assumed-density filters.

### Why it matters
The Gaussian ansatz makes filtering and smoothing tractable in continuous state spaces. It underpins a large family of algorithms — EKF, UKF, sigma-point filters, assumed-density filtering — and motivates the development of non-Gaussian alternatives (particle filters, variational filters) when the approximation is too crude.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[variational-inference]] — contrasts-with
- [[extended-kalman-filter]] — prerequisite-of
- [[kalman-filter]] — prerequisite-of
[To be populated during integration]