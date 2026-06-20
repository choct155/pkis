---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-20'
domain:
- bayesian-stats
id: pkis:concept:large-sample-bayesian-inference
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch04
- tanner-tools-statistical-inference-ch03
specializes:
- limiting-distributions
tags:
- asymptotics
- posterior-approximation
- normal-approximation
- consistency
- stable-estimation
title: Large-Sample Bayesian Inference
understanding: 0
uses:
- bernstein-von-mises-theorem
- laplace-approximation
- fisher-information
- sufficient-statistics
---

## Definition
The body of asymptotic theory describing how a posterior distribution behaves as the sample size n grows without bound. Its central object is the normal approximation to the joint posterior: when the log-posterior is unimodal and roughly symmetric, a second-order Taylor expansion of log p(omega|y) about the posterior mode omega-hat yields p(omega|y) approx N(omega-hat, [I(omega-hat)]^{-1}), where I(omega) = -d^2/domega^2 log p(omega|y) is the observed information. As n grows, the posterior mode approaches the value omega_0 that minimizes the KL divergence from the true sampling distribution f(y) to the model family p(y|omega), the observed-information curvature approaches n*J(omega_0) (n times the Fisher information), and the likelihood progressively dominates the prior. Three practical consequences follow. (1) Stable estimation: with a fixed model the posterior concentrates to a point as data accumulate, so the precise form of the prior matters little in large samples and matters critically in small ones. (2) Asymptotically the mode and curvature are sufficient statistics, justifying summarizing data by point estimates and standard errors. (3) The approximation is typically more accurate for low-dimensional marginal and conditional distributions than for the full joint, and can often be dramatically improved by reparameterization (e.g. working in log-sigma rather than sigma) before fitting the Gaussian. The chapter catalogs counterexamples where the asymptotics fail: underidentified or nonidentified parameters (flat likelihoods), parameter counts that grow with n (e.g. one mean per observation, Gaussian-process latent variables), aliasing (label switching in mixtures), unbounded likelihoods (variance components collapsing to zero in mixtures), improper posteriors, priors that exclude the convergence point, convergence to the boundary of the parameter space (yielding half-normal or spike limits), and tails where the normal approximation never holds for finite n. The large-sample results are not required to do Bayesian analysis but are valuable as approximations and as conceptual tools.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sufficient-statistics]] — uses: Asymptotically the posterior mode and observed-information curvature are sufficient statistics for the parameter.
- [[limiting-distributions]] — specializes: Posterior asymptotic normality is a specific limiting-distribution result for the parameter posterior as n grows.
- [[fisher-information]] — uses: Asymptotic curvature of the log-posterior approaches n times the Fisher information.
- [[laplace-approximation]] — uses: The normal approximation about the posterior mode is the operational tool of large-sample inference.
- [[bernstein-von-mises-theorem]] — uses: Posterior asymptotic normality and consistency are the central results of the large-sample theory.
[To be populated during integration]