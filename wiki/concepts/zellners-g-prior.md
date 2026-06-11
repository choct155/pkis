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
- statistics
- bayesian-inference
id: pkis:concept:zellners-g-prior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch15
tags:
- prior
- ridge-regression
- scale-invariance
- empirical-bayes
- model-selection
title: Zellner's g-Prior
understanding: 0
---

## Definition
$$p(w \mid \sigma^2) = \mathcal{N}\!\left(w \mid 0,\, g(X^TX)^{-1}\sigma^2\right), \quad g > 0$$

A specific NIG prior for Bayesian linear regression in which the prior covariance of the weights is set proportional to the inverse Fisher information $(X^TX)^{-1}$, scaled by a hyperparameter $g$ that plays the role of $1/\lambda$ in ridge regression.

### Why it matters
The g-prior makes the posterior invariant to affine rescaling of the inputs (e.g., change of measurement units). The posterior shrinks the MLE by the factor $g/(g+1)$, and $g$ can be chosen by cross-validation, empirical Bayes, or hierarchical Bayes, making it a principled and interpretable alternative to ridge regression.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]