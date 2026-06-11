---
aliases: []
also_type: []
analogous-to:
- ridge-regression
applies:
- low-rank-approximation
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
- linear-algebra
- machine-learning
generalizes:
- matrix-inverse
id: pkis:technique:moore-penrose-pseudoinverse
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch02
tags:
- pseudoinverse
- least squares
- SVD
- minimum norm
- regularization
title: Moore-Penrose Pseudoinverse
understanding: 0
uses:
- singular-value-decomposition
- column-space-and-span
---

## Definition
$$\mathbf{A}^+ = \mathbf{V}\mathbf{D}^+\mathbf{U}^T$$

where $\mathbf{A} = \mathbf{U}\mathbf{D}\mathbf{V}^T$ is the SVD and $\mathbf{D}^+$ is obtained by replacing each nonzero diagonal entry of $\mathbf{D}$ with its reciprocal. Equivalently, $\mathbf{A}^+ = \lim_{\alpha\to 0}(\mathbf{A}^T\mathbf{A}+\alpha\mathbf{I})^{-1}\mathbf{A}^T$.

The pseudoinverse generalises matrix inversion to rectangular and singular matrices.

### Why it matters
- **Overdetermined systems** ($m > n$): $\mathbf{x} = \mathbf{A}^+\mathbf{b}$ minimises $\|\mathbf{A}\mathbf{x}-\mathbf{b}\|_2$ (least-squares solution).
- **Underdetermined systems** ($m < n$): $\mathbf{x} = \mathbf{A}^+\mathbf{b}$ gives the minimum-norm solution $\arg\min_{\mathbf{A}\mathbf{x}=\mathbf{b}}\|\mathbf{x}\|_2$.
It is the foundation of regularised least squares and ridge regression (the $\alpha$-regularised form).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ridge-regression]] — analogous-to
- [[low-rank-approximation]] — applies
- [[column-space-and-span]] — uses
- [[matrix-inverse]] — generalizes
- [[singular-value-decomposition]] — uses
[To be populated during integration]