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
id: pkis:technique:policy-improvement
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch04
tags:
- dynamic-programming
- greedy-policy
- policy-improvement-theorem
title: Policy Improvement
understanding: 0
---

## Definition
$$\pi'(s) \doteq \arg\max_a \sum_{s', r} p(s', r|s, a)\,[\,r + \gamma\, v_\pi(s')\,]$$

Policy improvement constructs a new policy $\pi'$ that is greedy with respect to the value function $v_\pi$ of a current policy $\pi$; the resulting $\pi'$ is guaranteed to be at least as good as $\pi$.

### Operational mechanism
For each state, evaluate the action-value $q_\pi(s,a) = \sum_{s',r} p(s',r|s,a)[r + \gamma v_\pi(s')]$ under one step of lookahead and pick the maximizing action. This makes the policy greedy with respect to its own value function.

### Policy improvement theorem
If two deterministic policies satisfy $q_\pi(s, \pi'(s)) \ge v_\pi(s)$ for all $s$, then $v_{\pi'}(s) \ge v_\pi(s)$ for all $s$, with strict improvement wherever the first inequality is strict. The proof repeatedly expands the $q_\pi$ side with the Bellman relation. The greedy policy meets this condition by construction, so it is always an improvement — unless $\pi$ is already optimal, in which case $v_{\pi'} = v_\pi$ satisfies the Bellman optimality equation and both policies are optimal. The theorem extends to stochastic policies.

### Why it matters
Policy improvement turns an evaluated policy into a strictly better one, providing the ratchet that drives the search toward optimality. Paired with policy evaluation it yields policy iteration, and its greedy logic underlies value iteration and nearly all control methods in reinforcement learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]