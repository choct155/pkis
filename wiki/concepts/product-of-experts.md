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
- probabilistic-modeling
id: pkis:concept:product-of-experts
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch24
tags:
- EBM
- compositional-models
- generative-models
- soft-constraints
title: Product of Experts (PoE)
understanding: 0
---

## Definition
$$p_{1:K}(x) = \frac{1}{Z}\prod_{k=1}^K p_k(x), \quad E_{1:K}(x) = \sum_{k=1}^K E_k(x)$$

A PoE model combines $K$ expert distributions by multiplying their unnormalized densities (equivalently, summing their energies), assigning high probability only to points that all experts favour simultaneously. This contrasts with a mixture of experts, which selects a single expert per sample.

### Why it matters
PoE naturally implements conjunctive constraints: it can be used to generate data satisfying multiple simultaneous criteria (e.g., stable AND binding proteins). Each energy term acts as a soft constraint. PoE is easy to compose when each expert is an EBM, and the product remains an EBM. It is widely used in multi-modal generation, protein design, and composable diffusion models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]