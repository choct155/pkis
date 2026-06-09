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
- reinforcement-learning
- optimization
id: pkis:technique:gradient-monte-carlo
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
tags:
- stochastic-gradient-descent
- monte-carlo
- value-prediction
title: Gradient Monte Carlo for Value Prediction
understanding: 0
---

## Definition
Applying stochastic gradient descent to value prediction using the Monte Carlo return as target: w ← w + α [G_t − v̂(S_t,w)] ∇v̂(S_t,w). Because the true value is the expected return, the MC target G_t is an unbiased estimate of v_π(S_t); the update is therefore a genuine SGD step on the squared error, and under the usual decreasing-step-size (stochastic approximation) conditions it converges to a local optimum of VE—and, under linear function approximation, to the global optimum. The update target does not depend on the weight vector, which is the key property (the step from ∇[v_π − v̂]² to the gradient form) that distinguishes true gradient methods from semi-gradient ones. Updates are made at the end of each episode once returns are available.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]