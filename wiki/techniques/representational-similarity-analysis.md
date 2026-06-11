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
- neuroscience
- representation-learning
id: pkis:technique:representational-similarity-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
tags:
- representational-geometry
- similarity-measure
- neuroscience
- RSM
title: Representational Similarity Analysis (RSA)
understanding: 0
---

## Definition
RSA compares two representations by first computing **representational similarity matrices** (RSMs) $K_{ij} = k(x_i, x_j)$ and $K'_{ij} = k'(y_i, y_j)$ for all pairs of examples, and then applying a scalar matrix similarity function $s(K, K')$. Common choices are Pearson correlation for within-representation similarity and Spearman rank correlation between the vectorised RSMs. RSA reduces the problem of comparing high-dimensional representation spaces to comparing scalar-valued pairwise similarity structures.

### Why it matters
Originating in computational neuroscience, RSA is widely used to test whether a computational model's internal geometry matches neural activity patterns or another model, without requiring the two representation spaces to be aligned or equal-dimensional.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]