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
- deep-learning
- representation-learning
id: pkis:concept:undercomplete-autoencoder
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch14
tags:
- bottleneck
- dimensionality-reduction
- PCA
- feature-learning
title: Undercomplete Autoencoder
understanding: 0
---

## Definition
An undercomplete autoencoder has a code dimension strictly less than the input dimension, $\dim(h) < \dim(x)$, so that the bottleneck forces the model to learn a compressed representation. The training objective is:
$$\min_{f,g}\; L(x,\, g(f(x)))$$
with $\dim(h) < \dim(x)$.

When $f$ and $g$ are linear and $L$ is mean squared error, the learned subspace is identical to the principal subspace found by PCA; nonlinear encoders/decoders learn more powerful generalisations.

### Why it matters
Undercomplete autoencoders provide the simplest mechanism for manifold learning and feature extraction. The linear case gives a rigorous connection to PCA, while the nonlinear case enables learning complex data manifolds. However, if encoder/decoder capacity is too large the model can memorise without generalising, motivating regularised variants.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]