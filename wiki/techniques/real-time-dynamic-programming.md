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
id: pkis:technique:real-time-dynamic-programming
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch08
tags:
- reinforcement-learning
- dynamic-programming
- asynchronous-dp
- on-policy
- stochastic-shortest-path
title: Real-Time Dynamic Programming (RTDP)
understanding: 0
---

## Definition
An on-policy, trajectory-sampling version of the value-iteration algorithm (Barto, Bradtke & Singh, 1995). RTDP applies expected value-iteration updates to states visited along real or simulated trajectories, choosing a greedy action at each step; it is a form of asynchronous dynamic programming whose update order is dictated by the visited states (and may also update other states, e.g. those in a limited-horizon lookahead). For stochastic optimal path problems (undiscounted episodic tasks with absorbing zero-reward goal states, a proper policy, strictly negative non-goal rewards, and optimistic-or-equal initial values), RTDP converges with probability one to a policy optimal on the relevant states without needing to visit every state infinitely often, or even at all. On a racetrack benchmark it reached near-optimal control with about half the updates of conventional sweep-based value iteration, leaving ~3% of states never updated. A further advantage over value iteration is that its behavior policy approaches optimality as the value function does, since it always acts greedily. The proof combines asynchronous-DP convergence with Korf's (1990) learning-real-time-A* (LRTA*).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]