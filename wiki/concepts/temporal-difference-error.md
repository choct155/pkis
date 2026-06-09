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
- optimization
- deep-learning
id: pkis:concept:temporal-difference-error
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- reward-prediction-error-hypothesis
related_concepts: []
sources:
- sutton-reinforcement-2018-ch15
tags:
- td-error
- reinforcement-learning
- reinforcement-signal
- bootstrapping
- value-function
title: Temporal-Difference Error (delta)
understanding: 0
uses:
- eligibility-trace
- sutton-reinforcement-2018-ch06
---

## Definition
The temporal-difference error delta_{t-1} = R_t + gamma*V(S_t) - V(S_{t-1}) is the discrepancy between an earlier value estimate and a bootstrapped one-step-later estimate of expected return. It is a special kind of reward prediction error (RPE) — distinct from a simpler Rescorla-Wagner error — that compares successive long-term predictions rather than just expected vs. received reward. delta serves as the reinforcement signal in TD methods: it drives value-function updates (critic) toward smaller |delta|, and policy updates (actor) toward larger delta. delta is zero when reward is fully predicted by antecedent states, positive for better-than-expected outcomes, and negative for worse-than-expected ones (e.g. an omitted, previously-predicted reward). It separates the reward signal R_t (a component of delta) from the higher-order reinforcement term gamma*V(S_t) - V(S_{t-1}). Action-dependent variants underlie Sarsa and Q-learning. delta is the quantity that the phasic activity of dopamine neurons is hypothesized to convey (see reward-prediction-error-hypothesis).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sutton-reinforcement-2018-ch06]] — uses: TD error is defined and developed in Ch. 6 (Temporal-Difference Learning).
- [[reward-prediction-error-hypothesis]] — prerequisite-of: Understanding the TD error is required to grasp the reward-prediction-error hypothesis of dopamine activity.
- [[eligibility-trace]] — uses: TD(lambda) and actor-critic methods combine delta with eligibility traces to assign temporal credit.
[To be populated during integration]