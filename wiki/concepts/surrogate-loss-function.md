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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- optimization
- deep-learning
id: pkis:concept:surrogate-loss-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch08
tags:
- loss-function
- optimization
- classification
- deep-learning
title: Surrogate Loss Function
understanding: 0
---

## Definition
A surrogate loss function $\tilde{L}(f(x;\theta), y)$ is a proxy objective used in place of the true loss $L^*$ (e.g., 0-1 classification loss) when $L^*$ is intractable to optimize directly. The surrogate is chosen to be differentiable, computationally tractable, and to serve as an upper bound or smooth relaxation of the true loss.

Intuition: rather than minimizing the discontinuous 0-1 loss, one minimizes the negative log-likelihood, which is convex, differentiable, and encourages the model to assign high probability to correct labels.

### Why it matters
Surrogate losses are ubiquitous in deep learning: cross-entropy for classification, hinge loss for SVMs, and squared error for regression are all surrogates for harder combinatorial objectives. Critically, training on a good surrogate can yield *better* test performance than directly minimizing the true loss, because the surrogate extracts more information (e.g., calibrated probabilities rather than just a hard decision). The choice of surrogate interacts with early stopping: training halts when the *true* metric stagnates, not when the surrogate does.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]