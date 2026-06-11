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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:framework:generalized-linear-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch15
tags:
- regression
- exponential-family
- canonical-link
- IRLS
- dispersion
title: Generalized Linear Model (GLM)
understanding: 0
---

## Definition
$$p(y_n|x_n, w, \sigma^2) = \exp\!\left[\frac{y_n\eta_n - A(\eta_n)}{\sigma^2} + \log h(y_n, \sigma^2)\right], \quad \eta_n = w^Tx_n$$

where $A(\eta_n)$ is the log-partition (cumulant) function and the link function $\ell$ satisfies $\ell(\mu_n)=\eta_n$, giving $\mathbb{E}[y_n]=A'(\eta_n)$ and $\mathbb{V}[y_n]=A''(\eta_n)\sigma^2$. A GLM is a conditional exponential-family distribution in which the natural parameter is a linear function of the covariates.

### Why it matters
GLMs unify linear regression, logistic regression, Poisson regression, and many other models under a single formalism, enabling a common MLE algorithm (IRLS) and a shared Bayesian inference strategy. The Hessian is always positive semi-definite, so the NLL is convex and the MLE is unique.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]