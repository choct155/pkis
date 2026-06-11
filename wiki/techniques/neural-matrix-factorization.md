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
- recommender-systems
id: pkis:technique:neural-matrix-factorization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch22
tags:
- neural-network
- implicit-feedback
- bilinear
- MLP
- embedding
title: Neural Matrix Factorization (NeuMF)
understanding: 0
---

## Definition
$$f(u, i;\theta) = \sigma\!\left(\mathbf{w}^\top\!\left[\mathbf{P}_{u,:} \odot \mathbf{Q}_{i,:},\; \text{MLP}([\tilde{\mathbf{U}}_{u,:}, \tilde{\mathbf{V}}_{i,:}])\right]\right)$$

The model fuses two pathways: (1) a Generalised Matrix Factorisation (GMF) branch computing the element-wise product $\mathbf{P}_{u,:} \odot \mathbf{Q}_{i,:}$ of user/item embeddings, and (2) an MLP branch applied to a concatenation of separate user/item embeddings. A final linear layer combines both representations.

### Why it matters
NeuMF empirically demonstrates that combining bilinear (memorisation) and MLP (generalisation) pathways outperforms either alone on implicit-feedback benchmarks, and is the neural analogue of the wide-and-deep design philosophy in recommendation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]