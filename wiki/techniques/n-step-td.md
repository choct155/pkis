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
id: pkis:technique:n-step-td
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch07
tags:
- reinforcement-learning
- prediction
- policy-evaluation
- bootstrapping
title: n-step TD
understanding: 0
---

## Definition
n-step TD is the prediction (policy-evaluation) algorithm that estimates the state-value function v_pi by moving each state's estimate toward the n-step return: V_{t+n}(S_t) <- V_{t+n-1}(S_t) + alpha[G_{t:t+n} - V_{t+n-1}(S_t)]. Because the n-step return depends on rewards and states up to time t+n, the update for state S_t is not made until time t+n; no updates occur during the first n-1 steps of an episode, and an equal number of catch-up updates are made after termination. With n=1 the algorithm is ordinary one-step TD; as n grows toward the episode length it approaches the Monte Carlo (constant-alpha MC) estimate. Empirically, on the 19-state random walk used as a running example in Chapter 7, intermediate values of n (combined with appropriate step size alpha) minimize the RMS prediction error, demonstrating that the n-step generalization can outperform both extremes. Convergence to v_pi follows from the error reduction property of the n-step return.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]