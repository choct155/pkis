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
id: pkis:technique:td-lambda
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch12
tags:
- reinforcement-learning
- temporal-difference
- prediction
- eligibility-traces
title: TD(λ)
understanding: 0
---

## Definition
The classic backward-view, eligibility-trace algorithm for state-value prediction, and one of the oldest and most widely used RL algorithms. It maintains an accumulating eligibility trace z_t = gamma*lambda*z_{t-1} + grad v-hat(S_t, w_t) and updates the weights each step by w_{t+1} = w_t + alpha * delta_t * z_t, where delta_t is the one-step TD error. Oriented backward in time, it assigns the current TD error to recently visited states in proportion to their current trace. It improves over the off-line lambda-return algorithm by updating on every step (rather than only at episode end), distributing computation uniformly in time, and applying to continuing problems. TD(0) (lambda=0) recovers one-step semi-gradient TD; TD(1) (lambda=1) implements Monte Carlo online and incrementally. Linear TD(lambda) converges on-policy (under standard step-size conditions) to a solution whose value error is bounded by (1 - gamma*lambda)/(1 - gamma) times the minimum error. It only approximates the (ideal) online lambda-return algorithm, and can be unstable at large step sizes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]