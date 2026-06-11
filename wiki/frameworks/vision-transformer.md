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
contrasts-with:
- convolutional-neural-networks
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- computer-vision
id: pkis:framework:vision-transformer
instantiates:
- transformer-architecture
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch15
tags:
- transformer
- image-classification
- patch-embedding
- pretraining
title: Vision Transformer (ViT)
understanding: 0
uses:
- transfer-learning
- sinusoidal-positional-encoding
---

## Definition
ViT (Dosovitskiy et al., 2021) applies the standard Transformer encoder to image classification by treating non-overlapping $16 \times 16$ pixel patches as tokens:

1. Divide image into $T = HW/16^2$ patches and linearly project each to an embedding $x_i \in \mathbb{R}^d$.
2. Prepend a learnable $[\text{CLASS}]$ token $x_0$.
3. Add sinusoidal or learned positional embeddings.
4. Pass through $N$ standard Transformer encoder blocks.
5. Map the output $e_0$ corresponding to $[\text{CLASS}]$ to the target label $y$.

### Why it matters
ViT demonstrates that the inductive biases of CNNs (locality, equivariance, pooling) are not strictly necessary; a generic attention-based model trained on sufficient data (>14M images) matches or exceeds CNN baselines. It opens the door to unified architectures for vision and language and motivates research on data-efficient vision transformers.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sinusoidal-positional-encoding]] — uses
- [[transfer-learning]] — uses
- [[convolutional-neural-networks]] — contrasts-with
- [[transformer-architecture]] — instantiates
[To be populated during integration]