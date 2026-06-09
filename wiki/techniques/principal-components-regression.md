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
contrasts-with:
- ridge-regression
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:principal-components-regression
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch03
tags:
- regression
- dimension-reduction
- pca
- derived-inputs
- shrinkage
title: Principal Components Regression (PCR)
understanding: 0
uses:
- principal-component-analysis
- linear-regression
---

## Definition
A dimension-reduction regression method that regresses the response on a small number M <= p of derived inputs formed as the leading principal components of the (standardized) input matrix. The derived columns are z_m = X v_m, where v_m are the principal-component (eigen) directions of X^T X; because the z_m are orthogonal, the PCR fit is a sum of univariate regressions, yhat^pcr(M) = ybar*1 + sum_{m=1}^M thetahat_m z_m with thetahat_m = <z_m,y>/<z_m,z_m>, and the implied coefficients on the original variables are betahat^pcr(M) = sum_{m=1}^M thetahat_m v_m. PCR is not scale-invariant, so inputs are standardized first. With M = p it returns the ordinary least-squares estimate; with M < p it gives a reduced regression. PCR is closely related to ridge regression: both operate via the principal components, but where ridge shrinks each principal-component coordinate smoothly by a factor d_j^2/(d_j^2 + lambda), PCR discards (truncates to zero) the p - M smallest-eigenvalue components entirely and leaves the rest unshrunk. PCR keys only on high input variance and ignores the response when constructing directions, in contrast to partial least squares.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ridge-regression]] — contrasts-with: PCR hard-truncates low-variance components; ridge shrinks them smoothly
- [[linear-regression]] — uses: least-squares regression of y on the derived orthogonal components
- [[principal-component-analysis]] — uses: regresses on the leading principal-component directions of the input matrix
[To be populated during integration]