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
- statistics
id: pkis:technique:fishers-linear-discriminant-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch09
tags:
- dimensionality-reduction
- classification
- eigendecomposition
- scatter-matrix
- supervised
title: Fisher's Linear Discriminant Analysis (FLDA)
understanding: 0
---

## Definition
$$J(w) = \frac{w^\top S_B w}{w^\top S_W w}, \qquad w^* = S_W^{-1}(\mu_2 - \mu_1)$$

$$S_B = (\mu_2-\mu_1)(\mu_2-\mu_1)^\top, \quad S_W = \sum_{c}\sum_{n:y_n=c}(x_n-\mu_c)(x_n-\mu_c)^\top$$

FLDA finds the linear projection $w$ (or matrix $W$ in the multi-class case) that maximises the ratio of **between-class scatter** to **within-class scatter**. Maximising $J(w)$ is equivalent to the generalised eigenvalue problem $S_B w = \lambda S_W w$; when $S_W$ is invertible the two-class solution is closed-form: $w = S_W^{-1}(\mu_2-\mu_1)$.

### Why it matters
FLDA is an eigendecomposition-based supervised dimensionality reduction method that explicitly optimises class separability, unlike PCA which is unsupervised. It is a useful hybrid of generative and discriminative ideas: the Gaussianity assumption in the projected space justifies the scatter-ratio criterion, while the criterion itself is discriminative.

### Limitation
The rank of $S_B$ is at most $C-1$, so FLDA can extract at most $K \le C-1$ discriminant dimensions regardless of the original dimensionality $D$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]