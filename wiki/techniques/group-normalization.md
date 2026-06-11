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
- optimization
generalizes:
- batch-normalization
id: pkis:technique:group-normalization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch14
tags:
- normalization
- small-batch
- layer-normalization
- instance-normalization
title: Group Normalization
understanding: 0
---

## Definition
A normalization technique that divides the $C$ feature channels into $G$ groups and computes mean and variance within each group (over channels and spatial locations) for each example independently of other batch samples:
$$\mu_i = \frac{1}{|S_i|}\sum_{k\in S_i}z_k, \quad \tilde{z}_i = \gamma_c\frac{z_i-\mu_i}{\sigma_i} + \beta_c$$
where $S_i$ contains all elements sharing the same batch index and the same channel group as index $i$. **Layer normalization** ($G=1$) and **instance normalization** ($G=C$) are special cases.

### Why it matters
Unlike batch normalization, group normalization's statistics are independent of batch size, making it stable for small-batch regimes (object detection, video, 3D CNNs) while preserving the benefits of normalization over raw activations.

### Comparison
Group normalization outperforms batch normalization when batch size $\leq 8$, with batch normalization preferred for large-batch image classification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[batch-normalization]] — generalizes: Layer norm and instance norm are special cases of group norm; all generalize BN
[To be populated during integration]