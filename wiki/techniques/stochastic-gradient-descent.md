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
date_updated: '2026-06-20'
domain:
- optimization
- statistical-learning
- deep-learning
id: pkis:technique:stochastic-gradient-descent
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch07
- nielsen-nndl-ch03
tags: []
title: Stochastic Gradient Descent (SGD)
understanding: 0
---

## Definition
$$\theta_{i+1} = \theta_i - \gamma_i \Big(\textstyle\sum_{n \in \mathcal{B}_i} \nabla L_n(\theta_i)\Big)^\top$$

A stochastic approximation of gradient descent that replaces the full-data gradient with a cheap, noisy estimate computed on a randomly drawn mini-batch $\mathcal{B}_i \subset \{1,\dots,N\}$ (in the extreme, a single example).

### Mechanism
Many ML objectives decompose as a sum over per-example losses, $L(\theta) = \sum_{n=1}^N L_n(\theta)$ (e.g. the negative log-likelihood $-\sum_n \log p(y_n \mid x_n, \theta)$). Batch gradient descent evaluates the gradient of *every* term per step, which is prohibitive when $N$ is huge. The key insight is that convergence only requires an **unbiased estimate** of the true gradient: the full sum is an empirical estimate of an expectation, so any sub-sample yields a valid (if noisy) descent direction.

### The mini-batch trade-off
Large mini-batches give low-variance estimates, more stable convergence, and exploit vectorized matrix operations, but each step is costlier. Small mini-batches are cheap and their gradient noise can help escape poor local optima. Because the goal in ML is generalization rather than an exact minimizer of the training objective, approximate gradients are usually sufficient.

### Convergence
Under a decreasing learning-rate schedule (Robbins-Monro conditions) and mild assumptions, SGD converges almost surely to a local minimum.

### Why it matters
SGD is the workhorse of large-scale machine learning. Dataset sizes that prohibit batch gradient descent make stochastic approximation essential for training deep networks, topic models, reinforcement-learning agents, and large-scale Gaussian processes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]