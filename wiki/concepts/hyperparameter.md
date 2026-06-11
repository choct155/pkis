---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- bayesian-methods
- statistics
id: pkis:concept:hyperparameter
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch01
tags:
- hyperparameter
- regularisation
- Bayesian-hierarchy
- model-complexity
title: Hyperparameter
understanding: 0
---

## Definition
A **hyperparameter** is a parameter that controls the distribution of model parameters rather than the model output directly. In the polynomial curve-fitting example, $\alpha$ governs the prior precision of **w**:
$$p(\mathbf{w}|\alpha)=\mathcal{N}(\mathbf{w}|\mathbf{0},\alpha^{-1}\mathbf{I}),$$
and $\beta$ governs the noise precision of targets. More generally, $\lambda=\alpha/\beta$ in the regularised error function is a hyperparameter.

### Why it matters
Hyperparameters sit one level above ordinary parameters in the Bayesian hierarchy and can themselves be placed under a prior (yielding a hierarchical Bayesian model) or determined by cross-validation or marginal-likelihood maximisation (empirical Bayes). The effective model complexity is controlled by hyperparameters rather than the raw parameter count.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]