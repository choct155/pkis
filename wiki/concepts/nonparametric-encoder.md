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
contrasts-with:
- amortized-inference
- variational-inference
- variational-autoencoder
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- probabilistic-modeling
id: pkis:concept:nonparametric-encoder
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch13
tags:
- MAP-inference
- sparse-coding
- amortized-inference
- variational-inference
title: Non-Parametric Encoder (Optimisation-Based Inference)
understanding: 0
uses:
- maximum-a-posteriori-estimation-map
---

## Definition
An inference procedure in which the latent code $\mathbf{h}^*$ for each input $\mathbf{x}$ is computed by solving an optimisation problem at test time rather than by evaluating a fixed parametric function:

$$\mathbf{h}^* = \arg\max_{\mathbf{h}} \, p(\mathbf{h} \mid \mathbf{x}) = \arg\min_{\mathbf{h}} \, [-\log p(\mathbf{h}) - \log p(\mathbf{x}|\mathbf{h})].$$

Contrasts with a **parametric encoder** $\mathbf{h} = f_\phi(\mathbf{x})$ (as in a VAE) which amortises inference by training a neural network.

### Why it matters
The optimisation-based encoder has zero encoder generalisation error: for any $\mathbf{x}$ it finds the globally optimal code under the current decoder, whereas a parametric encoder may fail to generalise to out-of-distribution inputs. This is the key advantage of sparse coding over autoencoder-style models in low-label regimes. The tradeoff is computational cost and the difficulty of backpropagating through the optimisation step for end-to-end training.

### Relationship to amortised inference
Variational autoencoders (VAEs) amortise this optimisation by training a recognition network, trading optimality for speed — the key design choice separating sparse coding from variational autoencoders.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[maximum-a-posteriori-estimation-map]] — uses
- [[variational-autoencoder]] — contrasts-with
- [[variational-inference]] — contrasts-with
- [[amortized-inference]] — contrasts-with
[To be populated during integration]