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
- overfitting-and-underfitting
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- bayesian-methods
id: pkis:technique:bayesian-predictive-marginalisation
instantiates:
- marginalization
- posterior-predictive-distribution
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch01
tags:
- marginalisation
- predictive-distribution
- Bayesian
- posterior
- Gaussian
title: Bayesian Predictive Distribution by Marginalisation
understanding: 0
uses:
- prior-likelihood-posterior
- gaussian-distribution
---

## Definition
$$p(t|x,\mathbf{x},\mathbf{t}) = \int p(t|x,\mathbf{w})\,p(\mathbf{w}|\mathbf{x},\mathbf{t})\,d\mathbf{w}$$

Rather than plugging in a point estimate of $\mathbf{w}$, the full Bayesian prediction averages the model's output over the posterior distribution of parameters. For the polynomial regression model with Gaussian likelihood and Gaussian prior, this integral is analytic and yields a Gaussian predictive distribution:
$$p(t|x,\mathbf{x},\mathbf{t})=\mathcal{N}(t|m(x),s^2(x))$$
where the predictive variance $s^2(x)=\beta^{-1}+\boldsymbol{\phi}(x)^T\mathbf{S}\boldsymbol{\phi}(x)$ captures both noise and parameter uncertainty.

### Why it matters
Marginalisation automatically regularises: for an $M=9$ polynomial with a sensible prior, the predictive mean tracks the true function without overfitting, even when the number of parameters exceeds the number of data points. The predictive variance is input-dependent, being larger where training data is sparse — a key advantage over point-estimate methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[overfitting-and-underfitting]] — contrasts-with
- [[gaussian-distribution]] — uses
- [[posterior-predictive-distribution]] — instantiates
- [[marginalization]] — instantiates
- [[prior-likelihood-posterior]] — uses
[To be populated during integration]