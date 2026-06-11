---
aliases: []
also_type: []
analogous-to:
- restricted-boltzmann-machine
- contrastive-divergence
applies:
- score-matching
- manifold-hypothesis
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
- representation-learning
- generative-models
id: pkis:technique:denoising-autoencoder
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- diffusion-processes
related_concepts: []
sources:
- goodfellow-deeplearning-ch14
- murphy-pml1-intro-ch20
specializes:
- autoencoder
- overcomplete-autoencoder
tags:
- corruption
- score-matching
- manifold-learning
- unsupervised-pretraining
- noise-injection
title: Denoising Autoencoder (DAE)
understanding: 0
uses:
- regularization
---

## Definition
A denoising autoencoder (DAE) is trained to reconstruct a clean input $x$ from a corrupted version $\tilde{x} \sim C(\tilde{x}|x)$, minimising:
$$-\mathbb{E}_{x\sim\hat{p}_{\text{data}}}\,\mathbb{E}_{\tilde{x}\sim C(\tilde{x}|x)}\log p_{\text{decoder}}(x\mid h = f(\tilde{x}))$$
The corruption process $C$ (e.g.~additive Gaussian noise, masking) is a design choice.

By learning to undo corruption, the DAE must implicitly model $p_{\text{data}}(x)$ and the manifold near which data concentrates.

### Why it matters
DAEs provide a principled way to learn high-capacity encoders without collapsing to the identity: reconstruction error alone prevents information loss while the corruption pressure prevents trivial copying. Their reconstruction vector field $g(f(x))-x$ estimates the score $\nabla_x \log p_{\text{data}}(x)$ (Alain & Bengio, 2013), linking DAEs to score matching, energy-based models, and modern diffusion generative models.

### Score estimation connection
With Gaussian corruption $C(\tilde{x}|x)=\mathcal{N}(x, \sigma^2 I)$ and MSE reconstruction loss, the learned reconstruction vector field estimates the data score up to a multiplicative constant, enabling the autoencoder to be used as an implicit generative model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[diffusion-processes]] — prerequisite-of
- [[regularization]] — uses
- [[contrastive-divergence]] — analogous-to: Bengio & Delalleau (2009): autoencoder gradient approximates contrastive divergence training of RBMs
- [[overcomplete-autoencoder]] — specializes
- [[restricted-boltzmann-machine]] — analogous-to: With Gaussian noise and sigmoidal units, DAE training is equivalent to denoising score matching of an RBM
- [[manifold-hypothesis]] — applies
- [[score-matching]] — applies: DAE reconstruction vector field estimates the score of the data distribution (Alain & Bengio, 2013)
- [[autoencoder]] — specializes
[To be populated during integration]