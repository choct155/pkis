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
id: pkis:technique:procrustes-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch14
tags:
- shape-analysis
- morphometrics
- dimension-reduction
title: Procrustes Analysis
understanding: 0
uses:
- singular-value-decomposition
---

## Definition
A method for aligning sets of corresponding landmark points (shapes) by removing translation, rotation, and optionally scale, central to morphometrics and to shape-based PCA. Given two N×p matrices X_1, X_2 of corresponding landmarks, the Procrustes problem min_{μ,R} ‖X_2 − (X_1 R + 1μᵀ)‖_F over an orthonormal R and location μ is solved in closed form by the SVD of the centered cross-product ØX̃_1ᵀØX̃_2 = UDVᵀ: R̂ = UVᵀ, μ̂ = x̄_2 − R̂x̄_1, and the residual is the **Procrustes distance**. A scaled variant adds β with β̂ = trace(D)/‖X_1‖²_F. The **Procrustes average** of L shapes (min over rotations and a mean shape M) is found by an alternating algorithm — rotate all shapes to M, then re-average — and the more general **affine-invariant average** has a non-iterative solution as the top-p eigenvectors of the mean projection matrix H̄ = (1/L)Σ X_ℓ(X_ℓᵀX_ℓ)⁻¹X_ℓᵀ.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[singular-value-decomposition]] — uses: the optimal rotation R̂=UVᵀ comes from the SVD of the centered cross-product matrix
[To be populated during integration]