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
id: pkis:concept:link-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- generalized-linear-models
related_concepts: []
sources:
- gelman-bda3-ch16
- kroese-statistical-modeling-ch10
tags:
- glm
- link-function
- canonical-link
- logit
- probit
- regression
title: Link Function
understanding: 0
---

## Definition
The **link function** $g(\cdot)$ is the component of a generalized linear model that connects the linear predictor $\eta = X\beta$ to the mean of the outcome distribution:

$$g(\mu) = \eta = X\beta, \qquad \mu = E(y\mid X) = g^{-1}(X\beta).$$

The link is invertible and maps the (often bounded) mean $\mu$ onto the unbounded real line where a linear model can act freely. Common choices: the identity link $g(\mu)=\mu$ (normal regression), the log link $g(\mu)=\log\mu$ (Poisson), the logit $g(\mu)=\log\frac{\mu}{1-\mu}$ (logistic/binomial), the probit $g(\mu)=\Phi^{-1}(\mu)$, and the asymmetric complementary log-log $g(\mu)=\log(-\log\mu)$.

The **canonical link** is the special link that appears in the exponent when the response density is written in exponential-family form; using it makes the natural parameter equal to $\eta$ and simplifies estimation, but nothing forces this choice (e.g. the probit is non-canonical for the binomial).

Intuition: the link is the "adapter" that lets one shared linear-modeling machinery serve qualitatively different outcome types.

### Why it matters
The link is what makes the GLM *general*: by swapping $g$, the same linear predictor and estimation algorithm handle proportions, counts, and continuous data without violating their natural constraints. It also reshapes interpretation — a unit change in $x_j$ moves $g(\mu)$ linearly, so its effect on $\mu$ itself depends on the current value, forcing analysts to report effects on a reference case rather than as a single slope.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generalized-linear-models]] — prerequisite-of
[To be populated during integration]