---
aliases: []
also_type: []
analogous-to:
- variational-autoencoder
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
- deep-learning
- sparse-coding
- representation-learning
extends:
- sparse-autoencoder
id: pkis:technique:predictive-sparse-decomposition
instantiates:
- amortized-inference
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch14
tags:
- sparse-coding
- amortised-inference
- feature-learning
- alternating-optimisation
title: Predictive Sparse Decomposition (PSD)
understanding: 0
---

## Definition
Predictive sparse decomposition (Kavukcuoglu et al., 2008) is a hybrid model combining a sparse coding dictionary with a parametric encoder-decoder autoencoder, trained by alternately minimising:
$$\|x - g(h)\|^2 + \lambda\|h\|_1 + \gamma\|h - f(x)\|^2$$
over $h$ (with $f(x)$ as warm-start) and over the model parameters.

The encoder $f(x)$ learns to predict the sparse code that would otherwise require iterative optimisation, yielding fast inference at test time.

### Why it matters
PSD bridges the gap between sparse coding (iterative, expensive inference) and parametric autoencoders (fast, amortised inference). It is an early instance of **learned approximate inference** / amortised variational inference: the encoder is trained to approximate the posterior over latent codes. PSD pre-training has been used for object recognition and audio, and conceptually anticipates the variational autoencoder's amortised encoder.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[variational-autoencoder]] — analogous-to
- [[amortized-inference]] — instantiates
- [[sparse-autoencoder]] — extends
[To be populated during integration]