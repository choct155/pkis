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
- self-supervised-learning
- representation-learning
id: pkis:technique:barlow-twins-loss
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
tags:
- non-contrastive
- redundancy-reduction
- HSIC
- collapse-prevention
- BYOL
title: Barlow Twins Loss
understanding: 0
---

## Definition
A negative-free self-supervised loss that regularises the cross-correlation matrix $C$ between embeddings of two views of the same batch toward the identity:

$$\mathcal{L}_{\text{BT}} = \underbrace{\sum_i (1 - C_{ii})^2}_{\text{invariance}} + \lambda\underbrace{\sum_i \sum_{j \neq i} C_{ij}^2}_{\text{redundancy-reduction}}$$

where $C_{ij} = \frac{\sum_b z^A_{b,i} z^B_{b,j}}{\sqrt{\sum_b (z^A_{b,i})^2}\sqrt{\sum_b (z^B_{b,j})^2}}$. The first term makes representations of both views identical; the second decorrelates different feature dimensions, preventing collapse to a low-rank solution.

### Why it matters
Barlow Twins avoids the large-batch requirement of InfoNCE-based methods, has no momentum encoder, and connects self-supervised learning to classical redundancy-reduction and HSIC-based independence criteria. It achieves competitive ImageNet accuracy with simple implementation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]