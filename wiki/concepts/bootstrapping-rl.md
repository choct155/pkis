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
id: pkis:concept:bootstrapping-rl
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch04
tags:
- dynamic-programming
- value-function
- estimation
title: Bootstrapping (Reinforcement Learning)
understanding: 0
---

## Definition
Bootstrapping is the practice of updating a value estimate of one state on the basis of value estimates of its successor states — that is, updating an estimate from other estimates rather than from complete returns.

### Operational mechanism
Every DP update has the form $V(s) \leftarrow \sum_{s',r} p(s',r|s,a)[r + \gamma V(s')]$: the new value of $s$ depends on the current (estimated) values $V(s')$ of successors. Because the target itself contains an estimate, the method does not wait for a final outcome — it propagates partial, self-referential information through the value function.

### Conditions and contrast
Bootstrapping is distinct from requiring a model. DP both bootstraps and requires a complete model; Monte Carlo methods require neither (they use full sampled returns and do not bootstrap); temporal-difference methods bootstrap without needing a model. These two properties — modeling and bootstrapping — are separable and can be mixed in different combinations.

### Why it matters
Bootstrapping is one of the defining axes along which reinforcement-learning methods differ. It enables online, incremental learning and faster credit assignment, but it also introduces bias and can interact with function approximation and off-policy learning to cause instability (the "deadly triad"). Recognizing whether a method bootstraps is central to understanding its convergence behavior and computational profile.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]