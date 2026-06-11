---
aliases: []
also_type: []
analogous-to:
- epsilon-insensitive-loss
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- bayesian-linear-regression
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:technique:conformalized-quantile-regression
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch14
specializes:
- conformal-prediction
tags:
- prediction-intervals
- quantile-regression
- conformal
- pinball-loss
- uncertainty-quantification
title: Conformalized Quantile Regression (CQR)
understanding: 0
---

## Definition
CQR combines **quantile regression** with conformal calibration to produce adaptive prediction intervals with guaranteed marginal coverage. Given quantile estimates $\hat{t}_{\alpha/2}(x)$ and $\hat{t}_{1-\alpha/2}(x)$, define the conformal score
$$s(x,y) = \max\bigl(\hat{t}_{\alpha/2}(x) - y,\; y - \hat{t}_{1-\alpha/2}(x)\bigr),$$
compute the calibration quantile $\hat{q}$, and output the interval
$$T(x) = [\hat{t}_{\alpha/2}(x) - \hat{q},\; \hat{t}_{1-\alpha/2}(x) + \hat{q}].$$
The quantile regression model is trained with the **pinball loss** $\ell_\gamma(y,\hat{t}) = (\gamma - \mathbb{I}(y<\hat{t}))(y-\hat{t})$.

### Why it matters
CQR inherits the distribution-free coverage guarantee of conformal prediction while producing intervals that vary in width with input difficulty — something uniform-width methods cannot do. It is the standard baseline for regression uncertainty quantification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-linear-regression]] — contrasts-with
- [[epsilon-insensitive-loss]] — analogous-to
- [[conformal-prediction]] — specializes
[To be populated during integration]