---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- semi-supervised-learning
id: pkis:framework:semisupervised-vae
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch21
tags:
- VAE
- semi-supervised
- classification
- latent-class
- M2
title: Semisupervised VAE (M2 Model)
understanding: 0
---

## Definition
The M2 semisupervised VAE augments the latent space with a discrete class variable $y$:

$$p_\theta(x,y) = p_\theta(y)\int p_\theta(x|y,z)\,p_\theta(z)\,dz$$

For labeled data the ELBO lower-bounds $\log p_\theta(x,y)$; for unlabeled data an inference network $q_\phi(y|x)$ acts as an imputing classifier, and the bound lower-bounds $\log p_\theta(x) = -U(x)$. The overall objective combines both bounds with a supervised cross-entropy term:

$$\mathcal{L}(\theta) = \mathbb{E}_{D_L}[L(x,y)] + \mathbb{E}_{D_U}[U(x)] + \alpha\,\mathbb{E}_{D_L}[-\log q_\phi(y|x)]$$

### Why it matters
The M2 model achieves competitive classification accuracy with very few labels by using the generative model as a regulariser. It unifies discriminative and generative objectives in a single principled ELBO framework, and illustrates how latent class variables can be marginalised over in VAEs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]