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
- logistic-regression
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:technique:probit-model
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch16
specializes:
- generalized-linear-models
tags:
- probit
- binary-regression
- glm
- latent-variable
- gibbs-sampler
- link-function
title: Probit Model
understanding: 0
uses:
- link-function
- latent-variable-discrete-regression
---

## Definition
The **probit model** is a generalized linear model for binary or binomial data that uses the inverse normal CDF as its link:

$$\Pr(y_i=1)=\Phi(X_i\beta), \qquad g(\mu)=\Phi^{-1}(\mu).$$

For binomial data $p(y\mid\beta)=\prod_i \binom{n_i}{y_i}\,\Phi(\eta_i)^{y_i}\,(1-\Phi(\eta_i))^{n_i-y_i}$. It is obtained by keeping the normal variation of a linear model but dichotomizing the outcome, and it admits a clean **latent-variable representation**:

$$u_i \sim N(X_i\beta,\,1), \qquad y_i = \mathbb{1}(u_i>0).$$

This form is what makes the probit attractive Bayesianly: conditional on the $u_i$ it is ordinary linear regression, and conditional on $\beta$ the $u_i$ are truncated normals — yielding a simple Gibbs sampler (Albert and Chib).

Intuition: there is a hidden continuous propensity (e.g. partisan preference) that is normally distributed; you only see which side of zero it lands on.

### Why it matters
The probit is the standard binary-choice model in econometrics and a workhorse alternative to logistic regression; in practice the two agree except in the tails. Its latent-normal structure is the computational bridge that turns an intractable discrete-data posterior into a sequence of conjugate Gaussian updates, and it generalizes directly to ordered and multinomial probit models via cutpoints on the latent scale.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[logistic-regression]] — contrasts-with
- [[latent-variable-discrete-regression]] — uses
- [[link-function]] — uses
- [[generalized-linear-models]] — specializes
[To be populated during integration]