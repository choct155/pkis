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
- smoothing-splines
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
- optimization
id: pkis:technique:regression-splines
instantiates:
- basis-function-models
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch05
tags:
- splines
- basis-expansion
- piecewise-polynomial
- nonparametric-regression
title: Regression Splines
understanding: 0
uses:
- spline-approximation
---

## Definition
A fixed-knot spline method: a piecewise-polynomial fit in which the analyst chooses the spline order M (M=4 is cubic), the number of knots K, and their placement, then fits the resulting low-dimensional (M≤ a few dozen) basis by ordinary least squares (or, for classification, by penalized logistic regression). An order-M spline is a piecewise polynomial of order M with continuous derivatives up to order M−2; a cubic spline (M=4) is the lowest order whose knot discontinuity is invisible to the eye. The standard basis is the truncated-power basis h_j(X)=X^{j-1}, j=1..M, plus h_{M+ℓ}(X)=(X−ξ_ℓ)_+^{M−1}, ℓ=1..K; an order-M spline with K knots spans an (M+K)-dimensional vector space. The numerically preferable equivalent basis is the B-spline basis (defined recursively via divided differences), whose compact local support makes the design matrix banded and least-squares solvable in O(N) when knots are sorted.

A **natural cubic spline** adds the constraint that the fit be linear beyond the boundary knots, freeing four degrees of freedom (two per boundary) to control the otherwise-explosive boundary variance of unconstrained splines; a natural cubic spline with K knots is represented by K basis functions. In R, bs(x, df=7) builds a cubic-spline basis with interior knots at percentiles; ns(·) builds the natural variant. Knots can be placed at observed-x quantiles, parameterizing the family by degrees of freedom. Regression splines are **projection smoothers** — their hat matrix H_ξ = B(BᵀB)⁻¹Bᵀ is idempotent with M eigenvalues equal to 1 and the rest 0 — in contrast to the shrinking smoothers of smoothing splines. Selecting knot number and placement is combinatorially hard; greedy adaptive procedures such as MARS automate it.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[smoothing-splines]] — contrasts-with: projection smoother (few knots, no penalty) vs shrinking smoother (all knots, roughness penalty)
- [[spline-approximation]] — uses: uses truncated-power / B-spline bases
- [[basis-function-models]] — instantiates: fixed-knot least-squares spline as a concrete basis-expansion method
[To be populated during integration]