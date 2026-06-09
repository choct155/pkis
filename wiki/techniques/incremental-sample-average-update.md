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
id: pkis:technique:incremental-sample-average-update
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch02
specializes:
- action-value-methods
tags:
- bandits
- value-estimation
- online-learning
- step-size
- error-correction
title: Incremental Sample-Average Update
understanding: 0
---

## Definition
$$Q_{n+1} = Q_n + \frac{1}{n}\left[R_n - Q_n\right]$$

An online recurrence that updates a running average of rewards with constant memory and constant per-step computation, avoiding the need to store and re-sum the full reward history.

### Derivation
Starting from $Q_{n+1} = \frac{1}{n}\sum_{i=1}^{n} R_i$, algebra isolates the new reward to give $Q_{n+1} = Q_n + \frac{1}{n}(R_n - Q_n)$, which holds even for $n=1$ (yielding $Q_2 = R_1$). Only $Q_n$ and the count $n$ need be stored.

### The general update form
This rule instantiates a pattern that recurs throughout reinforcement learning:
$$\text{NewEstimate} \leftarrow \text{OldEstimate} + \text{StepSize}\,[\text{Target} - \text{OldEstimate}].$$
The bracketed quantity is an *error*; the estimate moves a fraction (the step size) toward a possibly noisy *Target* (here the reward $R_n$). For the exact sample average the step size is $\alpha_n = 1/n$, which shrinks over time.

### Why it matters
The error-correction update is the algorithmic skeleton of nearly every RL learning rule — temporal-difference learning, Q-learning, and gradient methods all reuse the $\text{old} + \alpha\,[\text{target} - \text{old}]$ template. Choosing the step-size schedule (decaying $1/n$ vs. constant $\alpha$) determines whether the estimate converges or tracks a moving target.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[action-value-methods]] — specializes: constant-memory online form of the sample-average estimator
[To be populated during integration]