---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- time-series
id: pkis:framework:state-space-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch29
tags:
- sequential-models
- latent-variables
- time-series
- graphical-models
title: State-Space Model (SSM)
understanding: 0
---

## Definition
A partially observed Markov model defined by a transition function and observation function:

$$z_t = f(z_{t-1}, u_t, q_t), \quad y_t = h(z_t, u_t, y_{1:t-1}, r_t)$$

with joint distribution

$$p(y_{1:T}, z_{1:T} \mid u_{1:T}) = \left[p(z_1|u_1)\prod_{t=2}^T p(z_t|z_{t-1},u_t)\right]\left[\prod_{t=1}^T p(y_t|z_t,u_t)\right]$$

where $z_t$ are hidden states, $y_t$ are observations, $u_t$ are optional inputs, $q_t$ is process noise, and $r_t$ is observation noise. The key structural assumption is that hidden states evolve as a Markov process and observations are conditionally independent given the hidden states.

### Why it matters
SSMs unify a broad family of sequential models — HMMs, Kalman filters, particle filters, and deep sequential models — under a common probabilistic graphical framework, enabling principled inference (filtering, smoothing, prediction) and parameter learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]