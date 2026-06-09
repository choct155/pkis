---
aliases: []
also_type: []
analogous-to:
- ridge-regression
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- principal-components-regression
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:partial-least-squares
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch03
tags:
- regression
- dimension-reduction
- derived-inputs
- supervised
- shrinkage
title: Partial Least Squares (PLS)
understanding: 0
uses:
- linear-regression
---

## Definition
A dimension-reduction regression method (Wold, 1975) that, like principal components regression, builds a sequence of orthogonal derived inputs z_1,...,z_M as linear combinations of the standardized predictors and regresses y on them, but unlike PCR it uses the response y in constructing the directions. The first PLS direction weights each input by the strength of its univariate effect on y: phihat_{1j} = <x_j, y>, z_1 = sum_j phihat_{1j} x_j; y is regressed on z_1, the predictors are orthogonalized with respect to z_1, and the process repeats up to M <= p directions (Algorithm 3.3). PLS is not scale-invariant, so inputs are standardized. With M = p it recovers least squares; M < p gives a reduced regression. The mth PLS direction solves max_alpha Corr^2(y, X alpha) Var(X alpha) subject to ||alpha|| = 1 and orthogonality to earlier directions, so PLS seeks directions of both high input variance AND high correlation with the response, a compromise between the ordinary least-squares coefficient and the principal-component directions. In practice the variance term dominates, so PLS behaves much like ridge regression and PCR; it tends to shrink low-variance directions but can inflate some high-variance directions, making it slightly more unstable. The PLS coefficient sequence is also the conjugate-gradient sequence for solving the least-squares normal equations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ridge-regression]] — analogous-to: in practice the variance aspect dominates so PLS behaves much like ridge
- [[principal-components-regression]] — contrasts-with: PLS uses y to build directions (variance AND correlation); PCR uses only input variance
- [[linear-regression]] — uses: regresses y on orthogonal derived directions
[To be populated during integration]