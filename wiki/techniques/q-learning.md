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
id: pkis:technique:q-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch06
tags:
- q-learning
- off-policy
- td-control
- action-value
- optimal-policy
- bootstrapping
title: Q-learning
understanding: 0
---

## Definition
Q-learning is the off-policy temporal-difference control algorithm and one of the early breakthroughs of reinforcement learning. Its learned action-value function $Q$ directly approximates the optimal action-value function $q_*$, independent of the policy actually being followed, by bootstrapping from the greedy (max) value of the successor state.

## Definition
$$Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha\,[\,R_{t+1} + \gamma \max_a Q(S_{t+1}, a) - Q(S_t, A_t)\,].$$
(Eq. 6.8) Behavior is typically ε-greedy in $Q$. The defining difference from Sarsa is the $\max_a$ in the target: the target uses the *greedy* successor value rather than the value of the action the behavior policy will actually take. This makes the target policy the greedy policy while the behavior policy explores — hence **off-policy**.

## Convergence
The direct approximation of $q_*$ dramatically simplifies analysis and enabled early convergence proofs. All that is required for convergence is that every state–action pair continues to be visited and updated; under this and a variant of the usual stochastic-approximation step-size conditions, $Q$ converges with probability 1 to $q_*$ (Watkins 1989; Watkins & Dayan 1992; generalized by Jaakkola, Jordan & Singh 1994 and Tsitsiklis 1994).

## Off-policy character and trade-off
Because Q-learning learns the optimal-policy values while behaving exploratorily, its learned greedy policy can be more aggressive than is safe online. In Cliff-Walking it learns the optimal edge-of-cliff path but, due to ε-greedy exploration, occasionally falls off, giving worse online return than Sarsa's safe path — even though Q-learning's learned values are those of the truly optimal policy. If ε is annealed to zero, both converge to the optimal policy.

## Limitation
The $\max_a$ operator over noisy estimates induces a systematic positive maximization bias, which Double Q-learning addresses.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]