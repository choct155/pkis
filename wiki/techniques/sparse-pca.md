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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
extends:
- principal-component-analysis
id: pkis:technique:sparse-pca
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch14
tags:
- dimension-reduction
- regularization
- lasso
- interpretability
title: Sparse Principal Components
understanding: 0
uses:
- lasso
- procrustes-analysis
---

## Definition
Variants of PCA that produce loading vectors with many zero entries, making the components easier to interpret by identifying the few variables each one involves. All use lasso (L1) penalties on the loadings. The **SCoTLASS** approach (Jolliffe et al., 2003) takes the maximum-variance view: max_v vᵀ(XᵀX)v subject to Σ|v_j| ≤ t and vᵀv = 1 — the absolute-value constraint drives loadings to zero, but the problem is non-convex and hard. The **SPCA** approach (Zou et al., 2006) uses the reconstruction/regression view: min_{θ,v} Σ_i ‖x_i − θvᵀx_i‖² + λ‖v‖² + λ_1‖v‖_1 subject to ‖θ‖=1 (with a ridge term λ for the p≫N case and the L1 term λ_1 inducing sparsity). For K components the criterion is biconvex in (Θ,V): minimizing over V given Θ is K elastic-net problems, minimizing over Θ given V is a Procrustes/SVD step, alternated to convergence. Used in morphometrics (e.g. corpus-callosum shape) to yield parsimonious, interpretable shape-variation components.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[procrustes-analysis]] — uses: the Θ-update in the multi-component SPCA criterion is a Procrustes/SVD step
- [[lasso]] — uses: L1 / elastic-net penalties drive loadings to zero (SCoTLASS, SPCA)
- [[principal-component-analysis]] — extends: adds L1 penalties on loadings to produce sparse, interpretable components
[To be populated during integration]