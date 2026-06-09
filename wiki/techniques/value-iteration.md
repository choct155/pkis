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
id: pkis:technique:value-iteration
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch04
tags:
- dynamic-programming
- bellman-optimality
- optimal-policy
title: Value Iteration
understanding: 0
---

## Definition
$$v_{k+1}(s) \doteq \max_a \sum_{s', r} p(s', r|s, a)\,[\,r + \gamma\, v_k(s')\,]$$

Value iteration solves a finite MDP by turning the Bellman optimality equation into an update rule, combining a single sweep of policy evaluation with policy improvement in one operation.

### Operational mechanism
From an arbitrary $v_0$, repeatedly apply the update above to every state; the only difference from the policy-evaluation update (4.5) is the $\max_a$, which folds in policy improvement. Each sweep is therefore one step of truncated policy evaluation plus one step of improvement. After convergence ($\max_s |v_{k+1}(s)-v_k(s)| < \theta$), output the greedy deterministic policy $\pi(s) = \arg\max_a \sum_{s',r} p(s',r|s,a)[r+\gamma V(s')]$.

### Conditions and convergence
For arbitrary $v_0$, $\{v_k\}$ converges to $v_*$ under the same conditions that guarantee $v_*$ exists ($\gamma < 1$ or guaranteed termination). More generally, interposing several evaluation sweeps between improvement sweeps yields the family of truncated policy iteration algorithms, all of which converge for discounted finite MDPs.

### Why it matters
Value iteration is the second classical DP algorithm and the most direct realization of the Bellman optimality equation as computation. Its single-sweep structure makes it the conceptual bridge to asynchronous and sample-based control methods used throughout reinforcement learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]