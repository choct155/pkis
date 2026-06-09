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
id: pkis:concept:td-error
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- temporal-difference-learning
related_concepts: []
sources:
- sutton-reinforcement-2018-ch06
tags:
- td-error
- temporal-difference
- bootstrapping
- credit-assignment
title: TD Error
understanding: 0
---

## Definition
The TD error is the quantity in brackets in the TD update — the difference between the current value estimate of a state and a better, bootstrapped estimate formed from the observed reward and the successor's value. It is the error signal that drives temporal-difference learning and recurs throughout reinforcement learning.

## Definition
$$\delta_t \doteq R_{t+1} + \gamma V(S_{t+1}) - V(S_t).$$
(Eq. 6.5) The TD error at time $t$ is the error in the estimate $V(S_t)$, but because it depends on the next reward and next state it is not available until time $t+1$.

## Sum-of-TD-errors identity
If the value array $V$ does not change during an episode (as in Monte Carlo), the Monte Carlo error decomposes exactly into a discounted sum of TD errors:
$$G_t - V(S_t) = \sum_{k=t}^{T-1} \gamma^{k-t}\,\delta_k.$$
(Eq. 6.6) The identity holds only approximately when $V$ is updated during the episode (as in TD(0)), but remains approximately true for small step sizes. Generalizations of this identity are central to the theory and algorithms of TD learning (e.g., eligibility traces and TD(λ)).

## Significance
The TD error generalizes across the algorithms of the chapter: an action-value form $\delta_t = R_{t+1} + \gamma Q(S_{t+1},A_{t+1}) - Q(S_t,A_t)$ underlies Sarsa, and analogous errors drive Q-learning and Expected Sarsa. Every method extended in later chapters retains this same TD-error–driven structure. The TD error also has a notable correspondence to dopamine reward-prediction-error signals in animal learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[temporal-difference-learning]] — prerequisite-of: the TD error is the error signal that defines the TD update
[To be populated during integration]