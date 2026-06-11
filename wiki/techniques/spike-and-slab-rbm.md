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
- deep-learning
- generative-models
- energy-based-models
id: pkis:technique:spike-and-slab-rbm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- real-valued-data
- covariance-modelling
- energy-based
- natural-images
title: Spike-and-Slab RBM (ssRBM)
understanding: 0
---

## Definition
An RBM extension for real-valued data that models conditional covariance via binary **spike** variables $\mathbf{h}\in\{0,1\}^n$ and real-valued **slab** variables $\mathbf{s}\in\mathbb{R}^n$. The energy function is:
$$E_{ss}(\mathbf{x},\mathbf{s},\mathbf{h})=-\sum_i\mathbf{x}^{\top}\mathbf{W}_{:,i}s_i h_i+\tfrac{1}{2}\mathbf{x}^{\top}\!\left(\Lambda+\sum_i\Phi_i h_i\right)\mathbf{x}+\tfrac{1}{2}\sum_i\alpha_i s_i^2-\sum_i\alpha_i\mu_i s_i h_i-\sum_i b_i h_i+\sum_i\alpha_i\mu_i^2 h_i.$$
Marginalising the slabs gives a Gaussian conditional $p(\mathbf{x}|\mathbf{h})$ with non-diagonal covariance; Gibbs sampling remains tractable without matrix inversion. Intuitively, each spike gate controls whether a feature direction is active, and the corresponding slab controls its intensity.

### Why it matters
ssRBMs address the weakness of Gaussian-Bernoulli RBMs in modelling pixel covariance in natural images, and allow contrastive divergence training without HMC. Convolutional ssRBMs produce high-quality image samples, and extensions (S3C, pooling of slabs) improve semi-supervised classification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]