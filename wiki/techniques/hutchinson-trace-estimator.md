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
- linear-algebra
- numerical-methods
- machine-learning
id: pkis:technique:hutchinson-trace-estimator
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch07
- murphy-pml2-advanced-ch23
tags:
- trace-estimation
- Monte-Carlo
- Hessian
- stochastic-approximation
- implicit-matrix
title: Hutchinson Trace Estimator
understanding: 0
---

## Definition
Given a square matrix $\mathbf{A}$ that is expensive to materialise but for which matrix–vector products $\mathbf{A}\mathbf{v}$ are cheap, the **Hutchinson estimator** approximates $\operatorname{tr}(\mathbf{A})$ via
$$\operatorname{tr}(\mathbf{A}) = \mathbb{E}_{\mathbf{v}}[\mathbf{v}^T\mathbf{A}\mathbf{v}], \quad \mathbf{v} \sim \mathcal{N}(\mathbf{0},\mathbf{I}) \text{ (or Rademacher)}.$$
The identity holds because $\mathbb{E}[\mathbf{v}\mathbf{v}^T] = \mathbf{I}$ and trace is linear. An unbiased Monte Carlo estimate is $\hat{T} = S^{-1}\sum_{s=1}^S \mathbf{v}_s^T \mathbf{A}\mathbf{v}_s$.

### Why it matters
For large neural networks, $\mathbf{A}$ is often the Hessian or the Fisher information matrix, whose trace is needed for second-order optimisation, influence functions, and Bayesian marginal-likelihood estimation. Materialising $\mathbf{A}$ explicitly may cost $O(n^2)$ memory, whereas Hutchinson requires only $O(n)$ memory and $O(Sn)$ time. The same idea extends to approximating $\|\mathbf{A}\|_F^2 = \operatorname{tr}(\mathbf{A}^T\mathbf{A})$ and stochastic log-determinant estimators.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]