---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:framework:basis-function-models
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch20
tags:
- nonparametric-regression
- basis-expansion
- b-splines
- radial-basis-functions
- additive-models
title: Basis Function Models
understanding: 0
---

## Definition
A framework for flexible (nonparametric) regression in which an unknown mean function μ(x) is modeled as a linear combination of prespecified basis functions, μ(x) = Σ_h β_h b_h(x). Because the model is *linear in the coefficients* β once the basis {b_h} is fixed, fitting reduces to (Bayesian) linear regression — a conjugate normal-inverse-χ² / normal-inverse-gamma prior on (β, σ²) yields a closed-form posterior — yet a rich class of nonlinear functions can be approximated by choosing enough basis functions.

## Core Mechanism
The modeling problem becomes a *design choice* (the basis) plus a *coefficient-estimation problem*. The data model is y_i ~ N(w_i β, σ²) with feature row w_i = (b_1(x_i), ..., b_H(x_i)). Common basis families:
- **Gaussian radial basis functions** b_h(x) = exp(−|x − x_h|² / l²): infinitely differentiable, centered at locations x_h with common width l; produce very smooth fits.
- **Cubic B-splines**: piecewise-cubic, defined on a set of knots; each basis function has *compact support*, so the design matrix W is sparse (computationally exploitable). Three-times differentiable, so slightly less smooth than Gaussian RBFs.

Local basis functions (each decaying to zero far from its center x_h) are preferred over global ones like Taylor polynomials, which need many terms and behave badly near boundaries.

## Key Design Levers
- **Number of basis functions H and width/knot spacing**: control the finest scale of variation representable. Features narrower than the basis width are oversmoothed.
- **Data sparsity**: H can exceed n (e.g., 21 coefficients, 54 data points in the chloride example), so prior information is essential. A useful device is to *center the nonparametric prior on a parametric (e.g., linear) function*: μ(x) = β_1 + β_2 x + Σ_h β_h b_h(x), shrinking the fit toward the linear model while allowing deviations. The penalized posterior mean takes a ridge-like form (WᵀW + λI)⁻¹(Wᵀy + λμ̂_0).
- **Smoothing priors**: first-order autoregressive priors on adjacent coefficients yield Bayesian penalized (P-)splines.

## Handling Basis Uncertainty
Two Bayesian strategies for not knowing which basis functions are needed: (1) **variable selection** — spike-and-slab / reversible-jump MCMC over which b_h are included, with model averaging; (2) **shrinkage priors** — continuous priors concentrated near zero with heavy tails that shrink unneeded coefficients toward (but not exactly to) zero, avoiding the 2^H discrete model space.

## Multivariate Extensions and the Curse of Dimensionality
For p > 1 predictors, prespecifying enough basis functions for an unconstrained surface is prohibitive. Remedies: **additive models** μ(x) = μ_0 + Σ_j β_j(x_j) with each β_j a univariate basis expansion (allows a divide-and-conquer Gibbs update); **shape constraints** (e.g., monotone splines via nonnegative coefficients, latent-threshold priors for flat regions); and **tensor-product** bases Σ ω_{h_1...h_p} ∏_j b_{j h_j}(x_j) with shrinkage on the coefficient tensor to collapse onto lower-dimensional structure.

## Relation to Gaussian Processes
Basis function models are an explicit, finite-dimensional construction of flexible function priors; Gaussian process priors (next chapter) are the implicit, kernel-based alternative, often recovered as a limit of basis expansions.

## Reading Path
- [[gelman-bda3-ch20]] — primary treatment: RBF and B-spline bases, conjugate fitting, variable selection vs. shrinkage for basis uncertainty, additive/tensor-product multivariate extensions, chloride and DDE examples.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]