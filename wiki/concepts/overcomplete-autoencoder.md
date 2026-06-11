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
id: pkis:concept:overcomplete-autoencoder
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch14
tags:
- overcomplete
- regularization
- identity-function
- representation-learning
title: Overcomplete Autoencoder
understanding: 0
---

## Definition
An overcomplete autoencoder has a code dimension greater than or equal to the input dimension, $\dim(h) \geq \dim(x)$. Without additional constraints, even a linear encoder-decoder pair can learn the trivial identity function, making all codes useless.

Useful representations in overcomplete autoencoders require explicit regularisation (sparsity, contractiveness, noise injection) that prevents the model from exploiting the extra capacity for a trivial solution.

### Why it matters
Overcomplete architectures are important in modern deep learning because they arise naturally in variational autoencoders, generative models, and transformer-style representation learning. Understanding overcomplete autoencoders motivates the full taxonomy of regularised autoencoders and clarifies that capacity alone does not guarantee useful representations—the training objective must be carefully designed.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]