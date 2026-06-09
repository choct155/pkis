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
id: pkis:technique:gradient-bandit-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch02
tags:
- bandits
- policy-gradient
- stochastic-gradient-ascent
- baseline
- preferences
- softmax
title: Gradient Bandit Algorithm
understanding: 0
---

## Definition
$$H_{t+1}(A_t) \doteq H_t(A_t) + \alpha(R_t - \bar{R}_t)(1 - \pi_t(A_t)), \qquad H_{t+1}(a) \doteq H_t(a) - \alpha(R_t - \bar{R}_t)\pi_t(a)\ \ (a \neq A_t)$$

Learns a soft-max policy over action *preferences* by stochastic gradient ascent on expected reward, rather than estimating action values. After each reward, the chosen action's preference rises (and others fall) in proportion to how far the reward exceeds a baseline.

### The reward baseline
$\bar{R}_t$ is the running average of rewards through time $t-1$ and serves as a *baseline*: if $R_t > \bar{R}_t$ the probability of $A_t$ increases, otherwise it decreases, with unselected actions moving oppositely. Shifting all true rewards by a constant has no effect because the baseline adapts instantly; omitting the baseline sharply degrades performance.

### Stochastic gradient ascent
The update is an unbiased sample of $\partial\,\mathbb{E}[R_t]/\partial H_t(a)$. Using $\sum_x \partial\pi_t(x)/\partial H_t(a)=0$, any action-independent baseline $B_t$ may be subtracted without changing the expected update; substituting $B_t=\bar{R}_t$ and the identity $\partial\pi_t(x)/\partial H_t(a)=\pi_t(x)(\mathbb{1}_{a=x}-\pi_t(a))$ recovers the algorithm exactly. Hence it is a true stochastic-gradient method with robust convergence.

### Why it matters
The gradient bandit is the conceptual seed of *policy-gradient* and *actor–critic* reinforcement learning (Williams, 1992): it shows how to optimize a parameterized stochastic policy directly from sampled rewards, and why a baseline reduces gradient variance — without biasing the update — to speed convergence.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]