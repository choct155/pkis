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
- deep-learning
id: pkis:technique:residual-block
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch13
- murphy-pml1-intro-ch14
tags:
- ResNet
- skip-connections
- vanishing-gradients
- architecture
title: Residual Block and Skip Connections
understanding: 0
---

## Definition
A residual block wraps a shallow nonlinear sub-network $\mathcal{F}_l$ with an **identity skip connection**:
$$z_{l+1} = \mathcal{F}_l(z_l;\theta_l) + z_l$$
so the sub-network learns the *residual* (delta) relative to the identity map. Chaining residual blocks gives a **ResNet** in which any layer $l$ relates to the output layer $L$ by:
$$z_L = z_l + \sum_{i=l}^{L-1}\mathcal{F}_i(z_i;\theta_i)$$
and the gradient satisfies $\frac{\partial L}{\partial \theta_l} = \frac{\partial z_l}{\partial \theta_l}\frac{\partial L}{\partial z_L}\left(1 + \sum_{i}\frac{\partial \mathcal{F}_i}{\partial z_l}\right)$, so the gradient at depth $l$ always receives a direct copy of $\nabla_{z_L}L$.

### Why it matters
Residual connections are the primary architectural fix for the vanishing-gradient problem in very deep networks. They enabled training of networks with 100+ layers and were central to the 2015 ImageNet breakthrough. They are now ubiquitous in CNNs, Transformers, and MLPs alike.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]