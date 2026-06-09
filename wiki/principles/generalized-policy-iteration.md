---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
id: pkis:principle:generalized-policy-iteration
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch04
tags:
- dynamic-programming
- policy-evaluation
- policy-improvement
title: Generalized Policy Iteration (GPI)
understanding: 0
---

## Definition
Generalized policy iteration (GPI) is the general principle of letting a *policy-evaluation* process and a *policy-improvement* process interact and converge — independent of the granularity or details of either process.

### Operational mechanism
One process drives the value function toward $v_\pi$ for the current policy; the other drives the policy toward greediness with respect to the current value function. Policy iteration runs each to completion before switching; value iteration interleaves them at one sweep each; asynchronous DP interleaves at the level of single states. All are instances of GPI.

### Why it stabilizes
The two processes both compete and cooperate. Making the policy greedy typically makes the value function inconsistent, and re-evaluating typically makes the policy non-greedy; geometrically, each step drives toward one of two non-orthogonal constraint lines. Yet the joint process is pulled toward optimality. Stability is reached only when the policy is greedy with respect to its own value function — precisely the Bellman optimality condition — so the fixed point is the optimal policy and value function.

### Why it matters
Almost all reinforcement-learning methods are well described as GPI: they maintain an approximate policy and an approximate value function, each pushing the other toward consistency and optimality. GPI is therefore the unifying lens for understanding DP, Monte Carlo, temporal-difference, and actor-critic methods alike.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]