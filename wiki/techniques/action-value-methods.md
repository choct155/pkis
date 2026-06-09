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
id: pkis:technique:action-value-methods
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch02
tags:
- bandits
- value-estimation
- sample-average
- greedy
title: Action-Value Methods
understanding: 0
---

## Definition
$$Q_t(a) \doteq \frac{\sum_{i=1}^{t-1} R_i \cdot \mathbb{1}_{A_i=a}}{\sum_{i=1}^{t-1} \mathbb{1}_{A_i=a}}$$

Methods that estimate the value of each action and use those estimates to select actions. The natural estimator is the *sample-average*: the mean of rewards actually received for each action.

### Sample-average estimation
The estimate $Q_t(a)$ averages all rewards observed when $a$ was taken (with a default such as $0$ before $a$ has ever been selected). By the law of large numbers, as the number of selections of $a$ grows, $Q_t(a) \to q_*(a)$. It is simple but not necessarily the best estimator.

### Greedy action selection
The simplest selection rule chooses a greedy action, $A_t \doteq \arg\max_a Q_t(a)$, breaking ties arbitrarily. Pure greedy selection always exploits and never samples apparently inferior actions, so it often gets stuck on a suboptimal action whose early samples were unlucky.

### Why it matters
Action-value methods are the conceptual backbone of tabular reinforcement learning: estimate values, then act on them. The sample-average estimator and the greedy rule are the baseline against which exploration strategies ($\varepsilon$-greedy, UCB, optimistic initialization) are measured, and they generalize directly to the action-value functions $Q(s,a)$ of the full RL problem.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]