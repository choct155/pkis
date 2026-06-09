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
- optimization
id: pkis:technique:expectation-propagation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch13
tags:
- posterior-approximation
- deterministic-approximate-inference
- moment-matching
- exponential-family
- message-passing
title: Expectation Propagation
understanding: 0
---

## Definition
Expectation propagation (EP) is a deterministic iterative algorithm that approximates a target posterior p(omega|y) by a tractable exponential-family distribution g(omega) (typically multivariate normal), where the approximation is factorized to match a factorization of the target, g(omega) = prod_i g_i(omega) approximating f(omega) = prod_i f_i(omega) (e.g. f_0 the prior, each f_i one data-point likelihood). Each iteration refines one factor g_i 'in the context of the whole distribution' via a moment-matching step: (1) form the cavity distribution g_{-i}(omega) proportional to g(omega)/g_i(omega) by removing the current factor; (2) form the tilted distribution g_{-i}(omega) f_i(omega), reinstating the true factor; (3) project the tilted distribution back into the parametric family by matching the expected sufficient statistics (for the normal family, matching mean and variance), giving the updated g; (4) back out the new factor g_i = g / g_{-i} via subtraction of natural parameters. The computational trick is that for a likelihood depending on omega only through a low-dimensional projection (e.g. X_i omega in logistic regression), the moment integrals reduce to one-dimensional quadrature even though omega is high-dimensional. EP updates may be applied immediately after each moment match (sequential EP) or only after all factors are processed (parallel EP, typically faster).

EP minimizes a forward-KL-flavored objective at each local moment-matching step, in contrast to variational Bayes which globally minimizes the reverse KL(g||p). This gives EP its characteristic behavior: unlike usual mean-field VB (which fits only the marginals and underestimates variance), EP fits the joint distribution and tends to capture posterior mass and skew better. Unlike EM, it returns a full distribution rather than a point estimate. EP is not guaranteed to converge; remedies include damping (partial updates after moment matching), a provably convergent double-loop variant, and fractional/power EP, which minimizes an alpha-divergence (a family including the directed KL divergences and Hellinger distance as special cases) to improve stability under vague priors or insufficiently flexible g.

In the BDA3 bioassay logistic-regression example, EP shifts the normal approximation toward the long-tailed mass of the skewed posterior, markedly improving on the plain mode-centered curvature (Laplace) approximation. Drawback: EP requires a likelihood/prior factorization in which the tilted moments can be computed cheaply (closed form or low-dimensional quadrature), so it is harder to apply to arbitrary densities than stochastic methods (Gibbs, Metropolis, HMC).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]