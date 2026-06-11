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
- deep-learning
id: pkis:concept:greedy-layer-wise-pretraining
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch01
- goodfellow-deeplearning-ch20
tags:
- pretraining
- unsupervised-learning
- initialization
- deep-belief-networks
title: Greedy Layer-Wise Pretraining
understanding: 0
---

## Definition
Greedy layer-wise pretraining is a training strategy for deep networks in which **each layer is trained independently as a shallow model** (often an unsupervised generative model such as an RBM or autoencoder) in sequence from the input upward, before the whole stack is fine-tuned jointly.

Algorithmically: train layer $\ell=1$ on raw inputs; freeze its weights; use its outputs as inputs to train layer $\ell=2$; repeat; then fine-tune all layers end-to-end with supervised signal.

### Why it matters
Hinton et al. (2006) showed this strategy could efficiently initialize deep belief networks, breaking the third AI winter. The key insight is that unsupervised pretraining provides a good initial weight configuration that avoids poor local minima caused by vanishing gradients, enabling effective training of much deeper networks than was previously practical.

### Historical significance
This technique launched the third wave of deep learning (ca. 2006) and popularized the term *deep learning*, even though it has since been largely superseded by better initialization schemes and rectified linear units.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]