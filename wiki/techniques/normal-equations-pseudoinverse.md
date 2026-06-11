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
- linear-algebra
id: pkis:technique:normal-equations-pseudoinverse
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch03
tags:
- least-squares
- closed-form
- design-matrix
- pseudoinverse
title: Normal Equations and Moore-Penrose Pseudoinverse
understanding: 0
---

## Definition
The maximum-likelihood (least-squares) solution for the weight vector of a linear basis function model is obtained by setting $\nabla E_D(\mathbf{w}) = 0$, yielding the **normal equations**:

$$\mathbf{w}_{\text{ML}} = (\boldsymbol{\Phi}^T\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^T\mathbf{t} \equiv \boldsymbol{\Phi}^\dagger \mathbf{t}$$

where $\boldsymbol{\Phi}$ is the $N \times M$ **design matrix** with $\Phi_{nj} = \phi_j(x_n)$, and $\boldsymbol{\Phi}^\dagger = (\boldsymbol{\Phi}^T\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^T$ is the **Moore-Penrose pseudoinverse**.

Geometrically, $\hat{\mathbf{y}} = \boldsymbol{\Phi}\mathbf{w}_{\text{ML}} = \boldsymbol{\Phi}\boldsymbol{\Phi}^\dagger\mathbf{t}$ is the orthogonal projection of the target vector $\mathbf{t}$ onto the column space of $\boldsymbol{\Phi}$.

### Why it matters
Provides a direct, non-iterative solution to regression; the pseudoinverse generalises matrix inversion to non-square (and rank-deficient) matrices. Numerical stability requires SVD when $\boldsymbol{\Phi}^T\boldsymbol{\Phi}$ is near-singular; adding $\lambda\mathbf{I}$ (ridge) restores full rank.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]