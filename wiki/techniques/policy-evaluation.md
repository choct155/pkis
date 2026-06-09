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
id: pkis:technique:policy-evaluation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch04
tags:
- dynamic-programming
- prediction
- value-function
title: Policy Evaluation
understanding: 0
---

## Definition
$$v_{k+1}(s) \doteq \sum_a \pi(a|s) \sum_{s', r} p(s', r|s, a)\,[\,r + \gamma\, v_k(s')\,]$$

Policy evaluation (the *prediction problem*) computes the state-value function $v_\pi$ for a fixed policy $\pi$ by iterating the Bellman equation for $v_\pi$ as an update rule until convergence.

### Operational mechanism
Given a known finite MDP and a policy $\pi$, the Bellman equation (4.4) is a system of $|S|$ linear equations in $|S|$ unknowns. Rather than solve it directly, *iterative policy evaluation* starts from an arbitrary $v_0$ (with terminal states set to 0) and repeatedly applies the expected-update operator above. Each sweep replaces every state's value with a probability-weighted average over successor states and immediate rewards — an *expected update*, because it averages over all possible next states rather than a sampled one.

### Convergence
The operator is a $\gamma$-contraction whose unique fixed point is $v_\pi$; the sequence $\{v_k\}$ converges to $v_\pi$ whenever $\gamma < 1$ or termination is guaranteed. In practice the sweep halts when $\max_s |v_{k+1}(s) - v_k(s)| < \theta$. An *in-place* (single-array) variant overwrites values during the sweep and typically converges faster.

### Why it matters
Policy evaluation is the foundational subroutine of dynamic programming: it makes a value function consistent with a given policy, which is one of the two interacting processes that every reinforcement-learning method approximates. Without an accurate evaluation of how good the current policy is, there is no basis for improving it.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]