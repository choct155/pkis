---
aliases: []
also_type: []
applies:
- binary-logistic-regression
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
- statistics
id: pkis:technique:feature-standardisation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- weight-decay-as-prior
related_concepts: []
sources:
- murphy-pml1-intro-ch10
tags:
- preprocessing
- normalisation
- regularisation
- feature-engineering
- conditioning
title: Feature Standardisation
understanding: 0
uses:
- regularization
---

## Definition
$$\tilde{x}_{nd} = \frac{x_{nd} - \hat{\mu}_d}{\hat{\sigma}_d}, \quad \hat{\mu}_d = \frac{1}{N}\sum_n x_{nd},\quad \hat{\sigma}_d^2 = \frac{1}{N}\sum_n(x_{nd}-\hat{\mu}_d)^2$$

Transforms each feature to zero mean and unit variance. An alternative, **min-max scaling**, maps features to $[0,1]$. Both make feature magnitudes comparable.

### Why it matters
Isotropic regularisers such as $\ell_2$ weight decay implicitly assume all features are on the same scale. Without standardisation, features with large magnitudes receive unfairly small penalties, distorting the MAP estimate. Standardisation also improves conditioning of the Hessian, accelerating gradient-based and second-order optimisation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[weight-decay-as-prior]] — prerequisite-of
- [[regularization]] — uses
- [[binary-logistic-regression]] — applies
[To be populated during integration]