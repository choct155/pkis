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
id: pkis:technique:sarsa-lambda
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch12
tags:
- reinforcement-learning
- control
- eligibility-traces
- action-values
title: Sarsa(λ)
understanding: 0
---

## Definition
The eligibility-trace extension of Sarsa to control with approximate action values q-hat(s, a, w). It uses the same weight update w_{t+1} = w_t + alpha*delta_t*z_t as TD(lambda) but with the action-value TD error delta_t = R_{t+1} + gamma*q-hat(S_{t+1}, A_{t+1}, w_t) - q-hat(S_t, A_t, w_t) and an action-value trace z_t = gamma*lambda*z_{t-1} + grad q-hat(S_t, A_t, w_t). It approximates the action-value forward view (the action-based lambda-return). Eligibility traces let a single rewarding event update all recently-taken action values, fading with recency, which markedly speeds credit assignment over one-step and n-step methods (illustrated on Gridworld and Mountain Car). Variants include accumulating vs. replacing traces (binary-feature pseudocode), true online Sarsa(lambda) (the exact dutch-trace implementation of the online lambda-return ideal), and forward Sarsa(lambda), a truncated version effective with neural networks. The expectation-based Expected Sarsa(lambda) generalizes it to off-policy data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]