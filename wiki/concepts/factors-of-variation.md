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
id: pkis:concept:factors-of-variation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch01
tags:
- disentanglement
- latent-variables
- generative-models
- representation-learning
title: Factors of Variation
understanding: 0
---

## Definition
Factors of variation are the **independent latent sources of influence** that together generate the observed data. They are not necessarily observed directly and need not combine multiplicatively; examples include object identity, pose, lighting, speaker age, accent, or word identity.

Formally, observed data $\mathbf{x}$ is treated as a function $g(z_1, z_2, \ldots, z_k)$ of latent factors $z_i$, each capturing one dimension of variability.

### Why it matters
Most raw sensory data (pixels, waveforms) entangles many factors simultaneously. Learning a representation that **disentangles** these factors — making each $z_i$ recoverable independently — is a central goal of representation learning and greatly simplifies downstream tasks.

### Connection to deep learning
Deep networks build hierarchical representations that progressively separate and identify factors: early layers capture low-level variation (edges, frequencies) while later layers capture semantic variation (object class, speaker identity).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]