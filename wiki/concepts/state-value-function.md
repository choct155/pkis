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
id: pkis:concept:state-value-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch03
tags: []
title: State-Value Function
understanding: 0
uses:
- bellman-equation
---

## Definition
$$v_\pi(s) \doteq \mathbb{E}_\pi\!\left[G_t \mid S_t = s\right] = \mathbb{E}_\pi\!\left[\sum_{k=0}^{\infty}\gamma^k R_{t+k+1} \,\Big|\, S_t = s\right]$$

The **state-value function** $v_\pi(s)$ is the expected return starting from state $s$ and following policy $\pi$ thereafter — how good it is to be in $s$ under $\pi$.

### Intuition
"How good" is defined entirely by expected future reward. A high-value state is one from which $\pi$ tends to collect a lot of reward. The value of any terminal state is zero. Crucially, value is policy-relative: the same state has different values under different policies.

### Estimation
If an agent following $\pi$ averages the actual returns observed after each visit to $s$, that average converges to $v_\pi(s)$ as visits grow — the Monte Carlo idea. When states are too many to tabulate, $v_\pi$ is represented as a parameterized function approximator.

### Recursive consistency
$v_\pi$ satisfies the Bellman equation $v_\pi(s) = \sum_a \pi(a\mid s)\sum_{s',r} p(s',r\mid s,a)[r + \gamma v_\pi(s')]$, relating a state's value to those of its successors.

### Why it matters
Nearly all RL algorithms revolve around estimating value functions; $v_\pi$ is the canonical such object and the basis for comparing and improving policies.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bellman-equation]] — uses: v_pi satisfies and is the unique solution of its Bellman equation.
[To be populated during integration]