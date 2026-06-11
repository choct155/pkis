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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:concept:canonical-link-function
instantiates:
- logistic-sigmoid-logit
- logistic-regression
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- irls
related_concepts: []
sources:
- bishop-prml-ch04
- murphy-pml1-intro-ch12
specializes:
- link-function
- link-function-mean-function
tags:
- GLM
- exponential-family
- link-function
- activation-function
- natural-parameter
- gradient-simplification
title: Canonical Link Function
understanding: 0
uses:
- generalized-linear-models
- exponential-family
---

## Definition
For a generalised linear model with target distribution in the exponential family $p(t|\eta,s) \propto g(\eta)\exp(\eta t/s)$, the canonical link function is the mapping $f^{-1}(y) = \psi(y)$ such that the natural parameter $\eta = \psi(y) = f^{-1}(y)$, i.e. the link is the inverse of the mean-function $y = -s\,d\ln g/d\eta$. The gradient of the negative log-likelihood then takes the universal form

$$\nabla E(\mathbf{w}) = \frac{1}{s}\sum_{n}(y_n - t_n)\boldsymbol{\phi}_n.$$

Examples: identity link for Gaussian (linear regression), logistic link for Bernoulli (logistic regression), log link for Poisson.

### Why it matters
Using a canonical link collapses the interaction between the activation function derivative and the link function derivative to unity, yielding the clean 'error times feature' gradient. This is not merely algebraic convenience—it ensures the Hessian is positive definite and connects maximum-likelihood estimation to exponential-family sufficient statistics.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[logistic-regression]] — instantiates: Logit is the canonical link for Bernoulli/Binomial
- [[link-function-mean-function]] — specializes
- [[irls]] — prerequisite-of
- [[logistic-sigmoid-logit]] — instantiates: Logistic link is canonical for Bernoulli GLM
- [[link-function]] — specializes
- [[exponential-family]] — uses
- [[generalized-linear-models]] — uses
[To be populated during integration]