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
- optimization
id: pkis:technique:xgboost
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch18
tags:
- boosting
- gradient-boosting
- second-order-optimization
- regularization
- scalability
- tabular-data
title: XGBoost
understanding: 0
---

## Definition
An efficient gradient boosted tree algorithm (Chen & Guestrin 2016) that augments standard gradient tree boosting with: (1) a regularised objective penalising tree complexity,

$$L(f) = \sum_i \ell(y_i, f(x_i)) + \Omega(f), \quad \Omega(f) = \gamma J + \tfrac{1}{2}\lambda\sum_j w_j^2$$

(2) second-order (Newton) approximation of the loss at each step, yielding closed-form optimal leaf weights

$$w_j^* = -\frac{G_{jm}}{H_{jm} + \lambda}, \quad G_{jm} = \sum_{i \in I_j} g_{im},\; H_{jm} = \sum_{i \in I_j} h_{im}$$

and a split-gain criterion

$$\text{gain} = \tfrac{1}{2}\left[\frac{G_L^2}{H_L+\lambda} + \frac{G_R^2}{H_R+\lambda} - \frac{(G_L+G_R)^2}{H_L+H_R+\lambda}\right] - \gamma$$

(3) random feature subsampling at nodes (as in random forests), and (4) engineering optimisations for out-of-core and distributed computation.

XGBoost treats tree learning as a second-order-optimised regularised problem, enabling faster convergence and better generalisation than first-order gradient boosting.

### Why it matters
XGBoost became the dominant algorithm on structured/tabular data competitions (Kaggle), combining strong empirical performance with scalability. The second-order approximation allows principled leaf-weight computation for any twice-differentiable loss, and the regularisation terms $\gamma$ (on number of leaves) and $\lambda$ (on leaf weights) directly control model complexity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]