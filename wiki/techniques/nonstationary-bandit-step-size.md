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
id: pkis:technique:nonstationary-bandit-step-size
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch02
tags:
- bandits
- nonstationary
- step-size
- stochastic-approximation
- recency-weighting
title: Constant Step-Size for Nonstationary Bandits
understanding: 0
---

## Definition
$$Q_{n+1} \doteq Q_n + \alpha\,[R_n - Q_n] = (1-\alpha)^n Q_1 + \sum_{i=1}^{n}\alpha(1-\alpha)^{n-i} R_i$$

Replacing the decaying $1/n$ step size with a constant $\alpha \in (0,1]$ turns the value estimate into an *exponential recency-weighted average*, giving more weight to recent rewards — appropriate when action values change over time.

### Recency weighting
Expanding the recurrence shows the weight on reward $R_i$ is $\alpha(1-\alpha)^{n-i}$, which decays exponentially with how long ago it was observed; the weights plus the $(1-\alpha)^n$ weight on $Q_1$ sum to $1$. The estimate continually tracks the current reward level instead of averaging the whole history equally.

### Convergence conditions
Stochastic-approximation theory guarantees convergence with probability 1 when
$$\sum_{n=1}^{\infty}\alpha_n(a) = \infty \quad\text{and}\quad \sum_{n=1}^{\infty}\alpha_n^2(a) < \infty.$$
The first condition ensures steps are large enough to overcome initial conditions; the second ensures they shrink enough to converge. The sample-average $1/n$ satisfies both; a constant $\alpha$ satisfies the first but not the second — so the estimate never fully converges and keeps responding to recent rewards.

### Why it matters
Nonstationarity is the rule, not the exception, in reinforcement learning: even with a stationary environment, a learner's changing policy makes each action's effective value drift. Not converging is therefore a feature, not a bug — a constant step size lets the agent perpetually adapt, which is why constant-$\alpha$ updates dominate practical RL over theoretically-convergent decaying schedules.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]