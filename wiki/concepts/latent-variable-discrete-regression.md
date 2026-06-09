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
id: pkis:concept:latent-variable-discrete-regression
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch16
tags:
- latent-variable
- probit
- logistic
- ordered-multinomial
- gibbs-sampler
- data-augmentation
title: Latent-Variable Formulation of Discrete Regression
understanding: 0
---

## Definition
The **latent-variable (data-augmentation) formulation** re-expresses a discrete-data regression as a thresholded continuous regression on unobserved latent values. For binary probit:

$$u_i \sim N(X_i\beta,1), \qquad y_i=\begin{cases}1 & u_i>0\\ 0 & u_i<0,\end{cases}$$

so the discrete model is equivalent to a normal linear model on the hidden $u_i$. For logistic regression the same scheme holds with $u_i$ drawn from a logistic distribution. For ordered multinomial outcomes one introduces cutpoints $c_0<c_1<c_2$ and sets $y_i=j$ according to which interval $u_i$ falls in; one cutpoint is fixed (e.g. $c_0=0$) to resolve non-identifiability.

Intuition: a coarse categorical observation is the visible shadow of a finer continuous quantity; modeling that quantity and then thresholding recovers the discrete model while exposing tractable structure.

### Why it matters
This device serves two ends. Interpretively, the latent variable often has meaning — a continuous measure of partisan preference behind a yes/no vote. Computationally, it is the key to efficient Bayesian inference: conditional on the latent data the problem is linear-Gaussian, enabling Gibbs sampling (Albert–Chib) and variational/HMC schemes for probit and ordered models that would otherwise require awkward Metropolis steps. It also unifies binary, ordered, and multinomial discrete regressions under one continuous-cutpoint picture.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]