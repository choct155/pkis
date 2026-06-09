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
id: pkis:technique:true-online-td-lambda
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch12
tags:
- reinforcement-learning
- temporal-difference
- eligibility-traces
- dutch-trace
title: True Online TD(λ)
understanding: 0
---

## Definition
An exact, computationally congenial backward-view implementation of the online lambda-return algorithm for the case of linear function approximation (van Seijen et al., 2016). Whereas the online lambda-return algorithm conceptually redoes all updates from the start of the episode on every step (filling a triangle of weight vectors w_t^h), true online TD(lambda) computes only the diagonal w_t^t directly via w_{t+1} = w_t + alpha*delta_t*z_t + alpha*(w_t^T x_t - w_{t-1}^T x_t)(z_t - x_t), using a dutch trace z_t = gamma*lambda*z_{t-1} + (1 - alpha*gamma*lambda*z_{t-1}^T x_t) x_t. It provably produces exactly the same weight sequence as the online lambda-return algorithm, while requiring the same O(d) memory as conventional TD(lambda) and only about 50% more per-step computation. It is 'truer' to the online lambda-return ideal than TD(lambda) is.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]