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
- cognitive-science
- representation-learning
id: pkis:framework:analysis-by-synthesis
instantiates:
- latent-variable-models
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
tags:
- generative-models
- latent-variables
- perception
- VAE
- disentanglement
title: Analysis-by-Synthesis
understanding: 0
uses:
- variational-autoencoder
- disentangled-representation-learning
- generative-adversarial-network
---

## Definition
A theory of perception and representation learning postulating that the brain (or a model) understands a percept $x$ by finding a compact latent description $z$ from which $x$ could be **synthesized**:

$$z^* = \arg\min_z \mathcal{D}(x,\, g(z)) + \mathcal{R}(z)$$

where $g$ is a generative (synthesis) model, $\mathcal{D}$ is a reconstruction cost, and $\mathcal{R}$ is a regulariser. The analysis step (inference) inverts the synthesis step, recovering latent factors such as shape, position, and illumination.

### Why it matters
Analysis-by-synthesis provides the conceptual foundation for latent-variable generative approaches to representation learning (VAEs, deep Boltzmann machines). It motivates learning representations that are interpretable as the causal factors that generated the data, rather than discriminative features optimised for a fixed task.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generative-adversarial-network]] — uses
- [[disentangled-representation-learning]] — uses: Aims to recover the latent factors that generated observations
- [[variational-autoencoder]] — uses
- [[latent-variable-models]] — instantiates
[To be populated during integration]