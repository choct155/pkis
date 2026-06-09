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
- statistical-learning
id: pkis:concept:maximization-bias
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch06
tags:
- maximization-bias
- estimation-bias
- max-operator
- control
- double-learning
title: Maximization Bias
understanding: 0
---

## Definition
Maximization bias is the systematic positive bias that arises when a maximum over estimated values is used as an estimate of the maximum of the true values. It afflicts control algorithms (Q-learning, Sarsa, Expected Sarsa) whose target policies are constructed by maximization.

## The mechanism
Consider a state $s$ with many actions whose true values $q(s,a)$ are all zero but whose estimates $Q(s,a)$ are noisy — scattered above and below zero. The max of the true values is zero, but $\mathbb{E}[\max_a Q(s,a)] > 0$: the maximum of the estimates is positive. The root cause is using the *same* samples both to choose the maximizing action and to estimate its value. In the Maximization Bias example (Fig. 6.5), this makes a guaranteed-suboptimal action appear attractive, and Q-learning initially favors it strongly and persistently over-selects it even at asymptote.

## Double learning as the cure
Split the experience into two independent estimates $Q_1$ and $Q_2$. Use one to *select* the maximizing action and the other to *evaluate* it: $Q_2(\arg\max_a Q_1(a))$ is unbiased, $\mathbb{E}[Q_2(A^*)] = q(A^*)$. Decoupling selection from evaluation removes the bias. This is the idea behind Double Q-learning. Maximization bias and double learning were introduced and extensively investigated by van Hasselt (2010, 2011).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]