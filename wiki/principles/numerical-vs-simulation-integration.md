---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
- optimization
id: pkis:principle:numerical-vs-simulation-integration
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch10
tags:
- numerical-integration
- quadrature
- monte-carlo
- posterior-expectation
- curse-of-dimensionality
title: Numerical vs. Simulation Integration
understanding: 0
---

## Definition
Bayesian computation reduces to evaluating integrals of the form E(h(omega)|y) = integral h(omega) p(omega|y) d omega, and the available methods split into two families. SIMULATION (stochastic) methods, such as Monte Carlo and MCMC, draw random samples omega^s from the target and estimate the integral by the sample average (1/S) sum h(omega^s); their error is stochastic and shrinks with more draws, they scale to high dimensions, and general-purpose algorithms exist for wide model classes. DETERMINISTIC methods (numerical integration / 'quadrature') evaluate the integrand at chosen points omega^s with weights w_s reflecting the volume each point represents, sum_s w_s h(omega^s) p(omega^s|y); the simplest is an equal-weight grid, while rules such as Simpson's use local polynomials and Gaussian quadrature exploits known integrand structure for higher accuracy with fewer evaluations. Deterministic rules typically have lower variance than simulation, but the choice of evaluation locations becomes intractable in high dimensions, where dense grids are prohibitively expensive. In practice the most efficient computation often COMBINES the two, plus distributional (analytic) approximations as starting points.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]