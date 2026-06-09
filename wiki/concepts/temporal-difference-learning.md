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
id: pkis:concept:temporal-difference-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch01
- sutton-reinforcement-2018-ch06
- sutton-reinforcement-2018-ch07
- sutton-reinforcement-2018-ch14
tags:
- temporal-difference
- value-estimation
- bootstrapping
- incremental-learning
title: Temporal-Difference Learning
understanding: 0
---

## Definition
Temporal-difference (TD) learning is a class of methods that update value estimates from the *difference between temporally successive estimates of the same quantity*, rather than waiting for a final outcome. After moving from state $S_t$ to $S_{t+1}$, the value estimate of the earlier state is adjusted toward the value of the later state:

$$V(S_t) \leftarrow V(S_t) + \alpha\,[\,V(S_{t+1}) - V(S_t)\,],$$

where $\alpha$ is a small positive step-size parameter governing the learning rate and the bracketed term is the **TD error**. Intuitively, each state "backs up" its successor's estimate, propagating information backward one step at a time.

### Bootstrapping and incrementality
TD methods are *incremental* (they learn online, step by step) and *bootstrap* (they update estimates partly from other estimates rather than from complete returns). With a suitably decreasing step-size, the tic-tac-toe TD player converges to the true win probabilities under optimal play against any fixed opponent.

### A distinctive thread
TD learning is one of the three historical threads of RL—alongside trial-and-error learning and optimal control—and is the one most new and unique to the field, traceable to secondary-reinforcement ideas in animal learning.

### Why it matters
TD learning lets an agent learn from raw experience without a model and without waiting for episodes to end, combining the model-free virtue of Monte Carlo methods with the incrementality of dynamic programming.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]