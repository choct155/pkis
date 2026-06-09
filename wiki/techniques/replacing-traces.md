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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
id: pkis:technique:replacing-traces
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch12
tags:
- reinforcement-learning
- eligibility-traces
- credit-assignment
title: Replacing and Dutch Traces
understanding: 0
---

## Definition
The family of update rules for the eligibility-trace vector. An accumulating trace adds the value gradient on each step and decays by gamma*lambda: z_t = gamma*lambda*z_{t-1} + grad v-hat. A replacing trace (Singh and Sutton, 1996), for binary features, sets the trace of an active feature to 1 rather than incrementing it (z_i <- 1), which avoids the unbounded build-up that accumulating traces suffer under repeated visits. A dutch trace, z_t = gamma*lambda*z_{t-1} + (1 - alpha*gamma*lambda*z_{t-1}^T x_t) x_t, is the trace used by true online TD(lambda) and true online Sarsa(lambda); it arises naturally as the F-matrix (forgetting/fading matrix) recursion in the derivation that converts the linear Monte Carlo/LMS forward view into an exact O(d) backward-view implementation, demonstrating that traces are not specific to TD learning. The name honors van Seijen and van Hasselt.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]