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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:technique:grid-approximation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch03
tags:
- bayesian-computation
- simulation
- nonconjugate-models
- numerical-integration
title: Grid Approximation of the Posterior
understanding: 0
---

## Definition
A brute-force numerical method for approximating a low-dimensional posterior by evaluating the unnormalized density p(theta) p(y | theta) on a regular grid of points covering the region of appreciable mass, then treating the grid values as a discrete distribution that is normalized to sum to one. It is the simplest route to inference for nonconjugate models (e.g. Bayesian logistic regression for bioassay) when theta has only one or two components.

## Procedure
1. Get a crude estimate (e.g. MLE plus standard errors) to locate and scale the grid.
2. Evaluate the log unnormalized posterior on the grid; subtract the maximum before exponentiating to avoid overflow/underflow.
3. Normalize so total grid probability is 1.
4. Sample by the discrete inverse-CDF method: draw theta_1 from the numerically summed marginal p(theta_1 | y), then theta_2 from the conditional p(theta_2 | theta_1, y); add uniform jitter of one grid-spacing width to restore a continuous distribution.
5. Any posterior summary (including derived quantities such as LD50 = -alpha/beta) is computed directly from the draws.

## Limitations
Grid placement is delicate: too small an area misses mass outside the grid; too coarse a spacing misses features between points. The cost grows exponentially in dimension, so the method is practical only for one or two parameters; higher dimensions require MCMC or other simulation methods (Part III of BDA).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]