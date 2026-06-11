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
- optimisation
- machine learning
id: pkis:technique:shooting-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch11
tags:
- coordinate descent
- lasso
- optimisation
- glmnet
title: Shooting Algorithm (Coordinate Descent for Lasso)
understanding: 0
---

## Definition
The shooting algorithm cyclically minimises the lasso objective over one coordinate at a time, exploiting the closed-form soft-threshold update:

$$w_d \leftarrow \operatorname{SoftThreshold}\!\left(\frac{c_d}{a_d},\, \frac{\lambda}{a_d}\right), \quad a_d = \sum_n x_{nd}^2, \quad c_d = \sum_n x_{nd}(y_n - \mathbf{w}_{-d}^T\mathbf{x}_{n,-d})$$

Each step is $O(N)$ and the algorithm converges to the global optimum because the lasso objective is convex.

### Why it matters
Coordinate descent for lasso is simple to implement, memory-efficient (no large matrix factorisation), and fast in practice because many coordinates become zero and need not be updated. It generalises to GLMs (glmnet), group lasso, and elastic net. Warm-starting along the regularisation path makes computing the full path nearly as cheap as fitting a single model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]