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
- machine-learning
- representation-learning
- generative-models
id: pkis:technique:latent-space-arithmetic
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch20
tags:
- latent-space
- attribute-editing
- disentanglement
- word2vec
- VAE
- GAN
title: Latent Space Arithmetic
understanding: 0
---

## Definition
**Latent space arithmetic** manipulates semantic attributes by computing offset vectors in the latent space of a generative model. Given a binary attribute $i$, define
$$\Delta_i = \bar{z}_i^+ - \bar{z}_i^-,$$
where $\bar{z}_i^+$ and $\bar{z}_i^-$ are the mean encodings of samples with and without attribute $i$, respectively. A new image with attribute strength $s$ is generated as
$$\hat{x} = d\bigl(e(x) + s\,\Delta_i\bigr).$$

Positive $s$ adds the attribute; negative $s$ suppresses it.

### Why it matters
First demonstrated in word2vec (word analogy: king − man + woman ≈ queen) and later in image-domain VAEs/GANs, latent arithmetic shows that semantically meaningful directions can be identified without supervision. It underlies practical applications such as attribute editing in face synthesis and controlled text generation, and provides evidence for the linear representational structure of disentangled latent spaces.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]