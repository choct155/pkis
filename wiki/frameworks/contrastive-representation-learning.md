---
aliases: []
also_type: []
analogous-to:
- word-embeddings
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
- self-supervised-learning
- representation-learning
id: pkis:framework:contrastive-representation-learning
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
specializes:
- self-supervised-learning
tags:
- SimCLR
- MoCo
- CLIP
- BYOL
- contrastive-loss
- InfoNCE
- multiview
title: Contrastive / Multiview Representation Learning
understanding: 0
uses:
- infonce-loss
---

## Definition
A family of self-supervised learning frameworks that train an encoder $f_\theta$ by requiring that representations of **positive pairs** $(x, x^+)$ — different views of the same underlying datum — are close in embedding space, while representations of **negative pairs** $(x, x^-)$ — views of different data — are far apart. The general objective is:

$$\min_\theta \; \mathbb{E}[\text{attractive terms}(f_\theta(x), f_\theta(x^+))] + \mathbb{E}[\text{repulsive terms}(f_\theta(x), f_\theta(x^-))]$$

Key instantiations include SimCLR (random augmentation pairs + InfoNCE), MoCo (memory queue for negatives), CLIP (image-text pairs), SupCon (label-guided positives), and CMC (cross-modal views).

### Why it matters
Contrastive learning has become the dominant paradigm for unsupervised visual and multimodal representation learning, closing much of the gap with supervised pretraining and enabling zero-shot transfer. The framework cleanly separates view design (what to treat as similar) from objective design (how to encode similarity).

### Variants without explicit negatives
BYOL, SimSiam, DINO, Barlow Twins, and VICReg eliminate explicit negatives and instead prevent collapse via momentum encoders, cross-correlation regularisation, or centering.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[word-embeddings]] — analogous-to: Both learn geometry from co-occurrence/similarity structure
- [[self-supervised-learning]] — specializes
- [[infonce-loss]] — uses
[To be populated during integration]