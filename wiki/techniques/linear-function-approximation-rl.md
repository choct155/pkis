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
id: pkis:technique:linear-function-approximation-rl
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
tags:
- linear-methods
- feature-vector
- basis-functions
- convergence
title: Linear Function Approximation in RL
understanding: 0
---

## Definition
The case in which v̂(s,w) = wᵀ x(s) = Σ_i w_i x_i(s) is linear in the weights, where x(s) is a feature vector whose components x_i(s) are basis functions of the state. The gradient is simply ∇v̂(s,w) = x(s), so the SGD update reduces to w ← w + α [U_t − v̂(S_t,w)] x(S_t). The linear case is the most analytically tractable and underlies almost all convergence guarantees in RL: there is a single optimum, so any method converging to a local optimum reaches the global one. Gradient MC converges to the global VE optimum; semi-gradient TD(0) converges (by a separate theorem) to the TD fixed point near—but not at—the optimum. Tabular methods are a special case in which features are one-hot indicators of states. Linearity cannot represent interactions between features unless conjunctive features are explicitly added.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]