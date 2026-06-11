---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- bayesian-inference
id: pkis:framework:relevance-vector-machine
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch07
- murphy-pml1-intro-ch17
- murphy-pml2-advanced-ch15
tags:
- sparse-bayesian-learning
- ARD
- kernel-methods
- probabilistic-model
- evidence-approximation
title: Relevance Vector Machine (RVM)
understanding: 0
---

## Definition
The RVM (Tipping, 2001) is a Bayesian sparse kernel model that places an independent Gaussian prior with hyperparameter $\alpha_i$ on each weight $w_i$:
$$p(\mathbf{w}|\boldsymbol{\alpha}) = \prod_{i=1}^{M}\mathcal{N}(w_i|0,\alpha_i^{-1}).$$
Hyperparameters are learned by maximising the type-2 marginal likelihood (evidence):
$$p(\mathbf{t}|\mathbf{X},\boldsymbol{\alpha},\beta) = \mathcal{N}(\mathbf{t}|\mathbf{0},\mathbf{C}), \quad \mathbf{C}=\beta^{-1}\mathbf{I}+\boldsymbol{\Phi}\mathbf{A}^{-1}\boldsymbol{\Phi}^T.$$
Optimisation drives many $\alpha_i \to \infty$, collapsing the corresponding weights to zero and removing the associated basis functions. Remaining non-zero weights are associated with *relevance vectors*, analogous to support vectors. For classification, the Laplace approximation replaces the analytic Gaussian integral.

### Why it matters
The RVM avoids the main limitations of SVMs: it provides calibrated posterior predictive distributions, requires no cross-validation to set $C$ or $\varepsilon$, is not restricted to positive-definite kernels, and typically achieves much sparser solutions than the SVM. The automatic relevance determination mechanism gives a principled Bayesian account of sparsity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]