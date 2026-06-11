---
aliases: []
also_type: []
applies:
- maximization-bias
- optimizers-curse
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
extends:
- q-learning
id: pkis:technique:double-q-learning
instantiates:
- deep-q-network
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch06
tags:
- double-q-learning
- double-learning
- maximization-bias
- off-policy
- td-control
title: Double Q-learning
understanding: 0
---

## Definition
Double Q-learning is the application of *double learning* to Q-learning in order to eliminate maximization bias: it maintains two independent action-value estimates and decouples action selection from action evaluation so that the bootstrapped target is unbiased.

## Definition
Two estimates $Q_1$ and $Q_2$ are maintained. On each step a coin flip decides which to update. If heads:
$$Q_1(S_t, A_t) \leftarrow Q_1(S_t, A_t) + \alpha\,\big[\,R_{t+1} + \gamma\,Q_2\big(S_{t+1}, \arg\max_a Q_1(S_{t+1}, a)\big) - Q_1(S_t, A_t)\,\big].$$
(Eq. 6.10) If tails, the roles of $Q_1$ and $Q_2$ are swapped. The maximizing action is chosen with one estimate and *evaluated* with the other, breaking the selection–evaluation coupling that causes the bias. The behavior policy may use both estimates (e.g. ε-greedy in $Q_1 + Q_2$).

## Cost and properties
Double learning doubles the memory requirement but does *not* increase computation per step (only one of the two estimates is updated each step). In the Maximization Bias example it essentially eliminates the harm caused by maximization bias. The idea extends naturally to give double versions of Sarsa and Expected Sarsa. Introduced by van Hasselt (2010, 2011).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[deep-q-network]] — instantiates: Double DQN applies double Q-learning to deep networks
- [[optimizers-curse]] — applies
- [[maximization-bias]] — applies: Double Q-learning exists specifically to eliminate maximization bias
- [[q-learning]] — extends: applies double learning to Q-learning to remove maximization bias
[To be populated during integration]