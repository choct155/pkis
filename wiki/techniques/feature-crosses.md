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
- feature-engineering
id: pkis:technique:feature-crosses
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch01
tags:
- interaction-effects
- categorical-data
- feature-engineering
- linear-models
title: Feature Crosses
understanding: 0
---

## Definition
Explicit construction of interaction features by forming the Cartesian product of two or more categorical (or discretized continuous) features. For categorical variables $x_1 \in \{1,\ldots,K_1\}$ and $x_2 \in \{1,\ldots,K_2\}$, the cross adds $K_1 K_2$ new indicator features:
$$\phi_{\text{cross}}(x) = [\mathbb{I}(x_1=k_1, x_2=k_2)]_{k_1,k_2}$$
This allows a linear model to learn a separate weight for every combination.

### Why it matters
Linear models cannot capture interaction effects between features without explicit cross-terms. Feature crosses restore this capacity at the cost of increased dimensionality, and are widely used in industrial recommendation systems where categorical interactions dominate. Polynomial regression is the continuous analogue.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]