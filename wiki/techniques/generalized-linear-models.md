---
aliases: []
also_type:
- framework
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
- bayesian-stats
generalizes:
- linear-regression
- logistic-regression
id: pkis:technique:generalized-linear-models
knowledge_type: technique
maturity: settled
related_concepts:
- '[[logistic-regression]]'
- '[[regularization]]'
- '[[em-algorithm]]'
- '[[maximum-likelihood-estimation]]'
sources:
- '[[kroese-statistical-modeling]]'
- '[[capretto-bambi-2022]]'
specializes:
- exponential-family
tags:
- glm
- regression
- link-function
- exponential-family
- logistic-regression
- poisson-regression
title: Generalized Linear Models
understanding: 0
uses:
- link-function
- laplace-approximation
- link-function-mean-function
- maximum-likelihood-estimation
- glm-gradient-hessian
- glm-deviance
- generalized-linear-models
---

Generalized Linear Models (GLMs) extend the normal linear model to non-Gaussian response distributions by specifying three components: a random component (response distribution from the exponential family), a systematic component (linear predictor η = Xβ), and a link function g relating E[Y|X] = μ to the linear predictor via g(μ) = η. Classification note: also_type framework because GLMs provide an organizing system of concepts for a broad class of regression models.

## Connections
- [[generalized-linear-models]] — uses: self-link placeholder — remove
- [[glm-deviance]] — uses
- [[glm-gradient-hessian]] — uses
- [[maximum-likelihood-estimation]] — uses
- [[logistic-regression]] — generalizes
- [[link-function-mean-function]] — uses
- [[exponential-family]] — specializes: GLMs are conditional exponential family models with linear natural parameters
- [[laplace-approximation]] — uses
- [[link-function]] — uses
- [[linear-regression]] — generalizes
- [[logistic-regression]] — specializes: logistic regression is GLM with Bernoulli response and logit link
- [[maximum-likelihood-estimation]] — uses: GLM parameters are estimated via MLE using iteratively reweighted least squares (IRLS)
- [[regularization]] — extends: penalized GLMs (ridge, lasso) add L2/L1 penalties to the GLM log-likelihood

## Reading Path
- [[kroese-statistical-modeling-ch10]] (unread) — primary treatment: GLM framework, logit model, probit model with latent-variable representation, Poisson regression
- [[hastie-esl-ch04]] (unread) — classification methods including logistic regression as a GLM
- [[capretto-bambi-2022]] (unread) — Bambi implements GLMMs (GLMs with group-specific random effects) using Bayesian inference; formula interface supporting Gaussian, Binomial, Poisson and other families