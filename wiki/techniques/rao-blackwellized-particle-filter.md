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
- robotics
- statistics
id: pkis:technique:rao-blackwellized-particle-filter
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch13
tags:
- particle-filter
- rao-blackwellization
- kalman-filter
- slam
- switching-dynamical-system
title: Rao-Blackwellized Particle Filter (RBPF)
understanding: 0
---

## Definition
RBPF partitions the latent state $z_t = (m_t, c_t)$ into a discrete (or otherwise tractable) component $m_t$ sampled by particles, and a continuous component $c_t$ integrated out analytically (e.g., via a Kalman filter conditioned on $m_{1:t}$). The resulting belief state is a mixture:
$$p(z_t, m_t|y_{1:t}) \approx \sum_{n=1}^N W_t^n \, \delta(m_t - m_t^n) \, \mathcal{N}(c_t|\mu_t^n, \Sigma_t^n)$$

### Why it matters
By marginalising the continuous variables analytically, RBPF reduces the effective sampling dimension, lowering Monte Carlo variance for a fixed particle budget. Key applications include (a) **switching linear dynamical systems** (mixture-of-Kalman-filters view) and (b) **FastSLAM**, where conditioning on the robot path makes landmark locations independent, reducing cost from $O(K^3)$ to $O(NK)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]