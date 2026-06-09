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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
id: pkis:concept:bellman-error-vs-projected-bellman-error
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch11
tags:
- bellman-error
- projected-bellman-error
- objective-function
- td-fixed-point
- learnability
- value-function-geometry
title: Bellman Error vs. Projected Bellman Error
understanding: 0
---

## Definition
Two competing objective functions for value-function approximation, best understood geometrically in the space of value vectors with the mu-weighted norm ||v||_mu^2 = sum_s mu(s) v(s)^2. The Bellman operator B_pi maps a value function to (r + gamma v') in expectation; the Bellman error vector is delta_w = B_pi v_w - v_w, and its squared mu-norm is the mean square Bellman Error, BE(w) = ||delta_w||_mu^2. The BE is the expected TD error at each state. Applying the projection operator Pi (which maps any value function to the closest representable one in norm) to the Bellman error vector and taking its squared norm gives the mean square Projected Bellman Error, PBE(w) = ||Pi delta_w||_mu^2. Their minimizers differ in general: minimizing the VE gives Pi v_pi (the Monte Carlo solution); minimizing the BE gives a distinct 'min BE' point; minimizing the PBE gives the TD fixed point w_TD, at which the PBE is zero in the linear case. Sutton & Barto argue the BE is the wrong objective on two grounds: (a) on genuine function approximation it converges to undesirable values (A-presplit example), and (b) more fundamentally it is NOT learnable — two MRPs producing identical data distributions can have different BEs and different BE-minimizers, so the BE-minimizing parameter cannot be recovered from observable data. The PBE, by contrast, is learnable with O(d) complexity and is the target of Gradient-TD methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]