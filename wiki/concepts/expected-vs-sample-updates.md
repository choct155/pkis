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
id: pkis:concept:expected-vs-sample-updates
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch08
tags:
- reinforcement-learning
- value-updates
- computation-tradeoff
- branching-factor
- bellman-update
title: Expected vs. Sample Updates
understanding: 0
---

## Definition
A central dimension of variation among value-function updates: an expected update considers all possible next states and rewards (e.g. Q(s,a) <- sum_{s',r} phat(s',r|s,a)[r + gamma max_a' Q(s',a')]), requiring a distribution model; a sample update considers a single sampled transition (e.g. the Q-learning update Q(s,a) <- Q(s,a) + alpha[R + gamma max_a' Q(S',a') - Q(s,a)]), requiring only a sample model or real experience. They coincide when only one next state is possible. The two differ to the extent the environment is stochastic. An expected update is exact (no sampling error) but costs roughly b times as much computation as a sample update, where b is the branching factor (number of possible next states). When time is insufficient to complete expected updates over all pairs (the common case in large problems), sample updates win: error falls as sqrt((b-1)/(bt)), so for moderately large b a tiny fraction of b updates achieves most of the benefit, and many state-action pairs can be improved in the time one expected update takes. Combined with depth of bootstrapping, this dimension organizes DP (one-step expected), TD (one-step sample), Monte Carlo (deep sample), and exhaustive search (deep expected).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]