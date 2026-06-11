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
contrasts-with:
- sgd-momentum
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- optimization
extends:
- minibatch-sgd
id: pkis:technique:adagrad
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch08
tags:
- adaptive-learning-rate
- gradient-descent
- deep-learning
title: AdaGrad
understanding: 0
---

## Definition
AdaGrad (Duchi et al., 2011) adapts per-parameter learning rates by dividing by the square root of the cumulative sum of squared gradients:
$$\mathbf{r} \leftarrow \mathbf{r} + \mathbf{g} \odot \mathbf{g}, \qquad \theta \leftarrow \theta - \frac{\epsilon}{\sqrt{\mathbf{r}} + \delta} \odot \mathbf{g},$$
where $\mathbf{r}$ accumulates from the start of training and $\delta$ is a small stabilising constant.

Intuition: parameters that receive large gradients often get smaller effective learning rates, while rarely-updated parameters retain larger learning rates — beneficial for sparse feature settings.

### Why it matters
AdaGrad has provably good regret bounds for online convex optimisation and is the foundation for adaptive-rate methods. Its main weakness for deep learning is that $\mathbf{r}$ grows monotonically, causing the effective learning rate to shrink to near-zero before the network has fully trained. RMSProp and Adam address this by using exponential moving averages instead of cumulative sums.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sgd-momentum]] — contrasts-with: adapts per-parameter rates rather than accumulating gradient direction
- [[minibatch-sgd]] — extends
[To be populated during integration]