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
- kernel-methods
id: pkis:technique:maximum-mean-discrepancy-training
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- implicit-density
- kernel-method
- moment-matching
- generative-model
title: Maximum Mean Discrepancy (MMD) Training
understanding: 0
---

## Definition
A technique for training implicit generative models by minimising the **maximum mean discrepancy** between the model distribution $p_g$ and the data distribution $p_{\mathrm{data}}$:
$$\mathrm{MMD}^2(p,q)=\mathbb{E}_{x,x'\sim p}k(x,x')-2\mathbb{E}_{x\sim p,y\sim q}k(x,y)+\mathbb{E}_{y,y'\sim q}k(y,y'),$$
where $k$ is a positive-definite kernel. MMD is zero iff $p=q$; it implicitly matches all moments in the feature space induced by $k$. Training proceeds via mini-batch estimates of MMD.

### Why it matters
MMD-based training (used in generative moment matching networks) requires no discriminator or approximate inference, making it simpler than GANs or VAEs. Its limitation is sensitivity to batch size and the need for a good kernel; combining the generator with an autoencoder in feature space can improve sample quality.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]