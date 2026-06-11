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
- probabilistic-graphical-models
- statistical-decision-theory
- machine-learning
id: pkis:concept:mpm-map-mpe-estimators
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch09
tags:
- MAP
- posterior-marginals
- MPE
- decision-theory
- loss-function
- belief-propagation
title: MPM vs MAP vs MPE Estimators
understanding: 0
---

## Definition
Three distinct point estimators for a latent vector $z$ given evidence $y$:

1. **MPM** (Maximiser of Posterior Marginals): $\hat{z}_i = \arg\max_{z_i}\sum_{z_{-i}} p(z\mid y)$ — minimises per-node (bit) error.
2. **MPE** (Most Probable Explanation) / **MAP**: $z^* = \arg\max_z p(z\mid y)$ — minimises sequence (word) error.
3. **MMM** (Maximiser of Max-Marginals): $\tilde{z}_i = \arg\max_{z_i}\max_{z_{-i}} p(z\mid y)$ — equals MAP when max-marginals are unique (on trees).

Key relationship: $\tilde{z} = z^*$ on trees (if unique); MPM $\hat{z}$ does not generally equal $z^*$ and can violate global constraints (e.g., produce invalid codewords).

Intuition: marginalising vs maximising over nuisance variables leads to fundamentally different decisions.

### Why it matters
Choosing the right estimator is a crucial modelling decision tied to the loss function. MPM is preferable when each variable is judged independently (e.g., minimising bit error in communications); MAP/MPE is preferable when global consistency matters (e.g., grammaticality in NLP, valid codewords in coding theory). The distinction is routinely confused in practice.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]