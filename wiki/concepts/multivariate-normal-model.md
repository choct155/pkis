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
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:concept:multivariate-normal-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch03
specializes:
- gaussian-distribution
tags:
- bayesian-inference
- conjugate-prior
- multiparameter-models
- linear-models
title: Multivariate Normal Model (Bayesian)
understanding: 0
uses:
- conjugate-prior
---

## Definition
Bayesian inference for the parameters of a d-dimensional multivariate normal sampling model, y_i ~ N(mu, Sigma) i.i.d., where mu is a length-d mean vector and Sigma a d x d symmetric positive-definite covariance matrix. The likelihood for n observations is

$$p(y_1,\dots,y_n \mid \mu, \Sigma) \propto |\Sigma|^{-n/2} \exp\!\left(-\tfrac{1}{2}\sum_{i=1}^n (y_i-\mu)^T \Sigma^{-1}(y_i-\mu)\right).$$

The model generalizes the univariate normal-with-unknown-mean-and-variance analysis and is the reference machinery underlying Bayesian linear models.

## Known Sigma: Gaussian conjugacy for mu
The conjugate prior for mu is multivariate normal, mu ~ N(mu_0, Lambda_0). The posterior is N(mu_n, Lambda_n) with **precision adding**: Lambda_n^{-1} = Lambda_0^{-1} + n Sigma^{-1}, and posterior mean a precision-weighted average mu_n = Lambda_n(Lambda_0^{-1} mu_0 + n Sigma^{-1} \bar{y}). A flat prior (|Lambda_0^{-1}| -> 0) gives mu | Sigma, y ~ N(\bar{y}, Sigma/n). Because the multivariate normal is closed under marginalization and conditioning, every subvector posterior is again normal, and conditional subvector posteriors take a linear-regression form with coefficients Lambda_n^{(12)}(Lambda_n^{(22)})^{-1}.

## Unknown Sigma: normal-inverse-Wishart
The conjugate prior for (mu, Sigma) is the normal-inverse-Wishart: Sigma ~ Inv-Wishart_{nu_0}(Lambda_0^{-1}), mu | Sigma ~ N(mu_0, Sigma/kappa_0). Posterior parameters update as kappa_n = kappa_0 + n, nu_n = nu_0 + n, mu_n a weighted average of mu_0 and \bar{y}, and Lambda_n = Lambda_0 + S + (kappa_0 n/(kappa_0+n))(\bar{y}-mu_0)(\bar{y}-mu_0)^T where S is the sum-of-squares matrix. The marginal posterior of mu is multivariate t. Noninformative options include the Jeffreys prior p(mu,Sigma) ∝ |Sigma|^{-(d+1)/2} and the scaled inverse-Wishart, which decouples correlations from variances for more flexible covariance modeling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[conjugate-prior]] — uses
- [[gaussian-distribution]] — specializes
[To be populated during integration]