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
- statistics
- machine-learning
id: pkis:technique:nadaraya-watson-estimator
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch16
tags:
- kernel-regression
- nonparametric
- weighted-average
- local-methods
- smoothing
title: Nadaraya–Watson Kernel Regression
understanding: 0
---

## Definition
$$\hat{\mu}(x) = \mathbb{E}[y\mid x,D] = \sum_{n=1}^N y_n\, w_n(x), \qquad w_n(x) = \frac{K_h(x-x_n)}{\sum_{n'}K_h(x-x_{n'})}$$

Derived by applying KDE to the joint density $p(x,y\mid D)$ and marginalizing: the conditional mean is a kernel-weighted average of the training responses, where weights depend on proximity to the query point.

### Why it matters
The Nadaraya–Watson estimator is the simplest nonparametric regression method and serves as a conceptual bridge between KDE, local regression (LOESS), and Gaussian process regression. It adapts locally to the data without assuming a parametric form, and reduces to linear regression when a Gaussian joint model is used. Choosing $h$ by cross-validation gives a fully data-driven procedure.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]