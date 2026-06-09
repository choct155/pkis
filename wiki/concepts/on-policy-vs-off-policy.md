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
id: pkis:concept:on-policy-vs-off-policy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch05
tags:
- reinforcement-learning
- exploration
- target-policy
- behavior-policy
- coverage
title: On-policy vs. Off-policy Learning
understanding: 0
---

## Definition
A foundational dichotomy in how RL methods reconcile the need to *explore* with the goal of learning about *optimal* behavior. **On-policy** methods evaluate and improve the very policy used to generate behavior: exploration is built into that single policy (e.g., an $\varepsilon$-soft policy), so the learned policy is near-optimal but never quite deterministic-optimal because it must keep exploring. **Off-policy** methods use two distinct policies: a *target policy* $\pi$ that is learned about and can become the deterministic optimal policy, and a *behavior policy* $b$ that generates the data and stays exploratory. Off-policy learning requires the **coverage** assumption,
$$\pi(a\mid s) > 0 \implies b(a\mid s) > 0,$$
so every action the target could take is occasionally sampled by the behavior policy. On-policy methods are the special case $\pi = b$.

### Why it matters
This distinction structures essentially all of reinforcement learning beyond this chapter. On-policy methods are simpler and lower-variance but settle for a policy that still explores; off-policy methods are more powerful and general — they can learn the optimal deterministic policy while behaving exploratorily, learn from data produced by an existing controller or a human expert, and learn many target policies at once from one stream of experience. The price is higher variance and slower convergence (data comes from the 'wrong' distribution), and the need for correction machinery such as importance sampling. The on-policy/off-policy axis recurs through TD learning (SARSA vs. Q-learning), function approximation, and policy-gradient methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]