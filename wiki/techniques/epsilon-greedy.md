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
id: pkis:technique:epsilon-greedy
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch02
tags:
- bandits
- exploration
- action-selection
- greedy
title: ε-greedy Action Selection
understanding: 0
---

## Definition
$$A_t = \begin{cases} \arg\max_a Q_t(a) & \text{w.p. } 1-\varepsilon \\ \text{random action} & \text{w.p. } \varepsilon \end{cases}$$

A near-greedy action-selection rule that behaves greedily most of the time but, with small probability $\varepsilon$, selects uniformly at random among all actions — the simplest practical way to balance exploration and exploitation.

### Asymptotic guarantee
Because every action is chosen with probability at least $\varepsilon/k$ on every step, in the limit each action is sampled infinitely often, so all $Q_t(a)$ converge to their $q_*(a)$ and the probability of selecting the optimal action converges to more than $1-\varepsilon$. These are asymptotic guarantees and say little about finite-time performance.

### Empirical behavior
On the 10-armed testbed, $\varepsilon$-greedy methods outperform pure greedy in the long run because continued exploration lets them recognize the optimal action. Larger $\varepsilon$ (e.g. $0.1$) explores faster but caps the optimal-action rate; smaller $\varepsilon$ (e.g. $0.01$) learns slowly but eventually does better. Annealing $\varepsilon$ over time can combine both benefits.

### Why it matters
$\varepsilon$-greedy is the default exploration heuristic across reinforcement learning: trivial to implement, robust, and easy to extend beyond bandits to large state spaces and nonstationary problems, where more refined methods like UCB become impractical. Its weakness is *undirected* exploration — it ignores how uncertain or near-greedy each nongreedy action is.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]