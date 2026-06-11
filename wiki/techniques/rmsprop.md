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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- optimization
- deep-learning
id: pkis:technique:rmsprop
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch08
tags:
- adaptive-learning-rate
- exponential-moving-average
- deep-learning
title: RMSProp
understanding: 0
---

## Definition
RMSProp (Hinton, 2012) replaces AdaGrad's cumulative squared-gradient accumulator with an exponentially weighted moving average:
$$\mathbf{r} \leftarrow \rho\mathbf{r} + (1-\rho)\mathbf{g}\odot\mathbf{g}, \qquad \theta \leftarrow \theta - \frac{\epsilon}{\sqrt{\mathbf{r}}+\delta}\odot\mathbf{g},$$
where $\rho$ controls the decay rate of the moving average (typically $\rho=0.9$).

Intuition: by forgetting distant gradient history, RMSProp behaves like a fresh AdaGrad instance whenever the optimiser enters a new locally-convex region, maintaining a useful learning rate throughout non-stationary training.

### Why it matters
RMSProp is one of the most widely deployed optimisers for deep learning in practice. It naturally handles non-stationary objectives, which are common in deep networks with many saddle points and varying curvature. It is the second-moment component of Adam and the basis for RMSProp-with-Nesterov-momentum.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]