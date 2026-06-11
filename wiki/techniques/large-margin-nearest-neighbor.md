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
- metric-learning
id: pkis:technique:large-margin-nearest-neighbor
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch16
tags:
- mahalanobis
- margin
- semidefinite-programming
- nearest-neighbor
- metric-learning
title: Large Margin Nearest Neighbor (LMNN)
understanding: 0
---

## Definition
$$L(M) = (1-\lambda)\underbrace{\sum_{i}\sum_{j\in N_i} d_M(x_i,x_j)^2}_{L_{\text{pull}}} + \lambda\underbrace{\sum_{i}\sum_{j\in N_i}\sum_l \mathbb{I}(y_i\neq y_l)\bigl[m+d_M(x_i,x_j)^2 - d_M(x_i,x_l)^2\bigr]_+}_{L_{\text{push}}}$$

where $d_M$ is the Mahalanobis distance with learned PSD matrix $M$, $N_i$ is the set of $K$ same-class target neighbors of $i$, and $[\cdot]_+$ is the hinge loss. LMNN jointly minimizes distance to target neighbors (*pull*) while enforcing a margin over same-neighborhood impostors (*push*).

### Why it matters
LMNN is the foundational linear metric-learning method: the combined objective is convex in $M$ (solved via semidefinite programming) or unconstrained in $W$ where $M=W^TW$, enabling low-dimensional projections. It directly optimizes the objective of the downstream KNN classifier rather than optimizing a surrogate.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]