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
- optimisation
id: pkis:technique:levenberg-marquardt-hessian
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch05
tags:
- hessian
- second-order
- quasi-newton
- pruning
title: Levenberg–Marquardt (Outer-Product) Hessian Approximation
understanding: 0
---

## Definition
For a sum-of-squares loss $E = \tfrac{1}{2}\sum_n (y_n - t_n)^2$, the exact Hessian is
$$\mathbf{H} = \sum_n \nabla y_n \nabla y_n^T + \sum_n (y_n - t_n)\nabla\nabla y_n.$$
The **outer-product approximation** (Levenberg–Marquardt) drops the second term, yielding
$$\mathbf{H} \approx \sum_n \mathbf{b}_n \mathbf{b}_n^T, \quad \mathbf{b}_n = \nabla_\mathbf{w} y_n,$$
which is positive semi-definite and requires only first-order backpropagation, giving $O(W^2)$ cost.

For cross-entropy with sigmoid output the analogous approximation is $\mathbf{H}\approx\sum_n y_n(1-y_n)\mathbf{b}_n\mathbf{b}_n^T$.

### Why it matters
Provides a tractable, positive semi-definite surrogate Hessian used in second-order optimisers, network pruning (via inverse Hessian), and the Laplace approximation for Bayesian neural networks. Accuracy degrades when residuals $(y_n - t_n)$ are large.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]