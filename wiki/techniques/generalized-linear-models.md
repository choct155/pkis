---
title: "Generalized Linear Models"
knowledge_type: technique
also_type: [framework]
domain: [statistical-learning, bayesian-stats]
tags: [glm, regression, link-function, exponential-family, logistic-regression, poisson-regression]
related_concepts: ["[[logistic-regression]]", "[[regularization]]", "[[em-algorithm]]", "[[maximum-likelihood-estimation]]"]
sources: ["[[kroese-statistical-modeling]]", "[[capretto-bambi-2022]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Generalized Linear Models (GLMs) extend the normal linear model to non-Gaussian response distributions by specifying three components: a random component (response distribution from the exponential family), a systematic component (linear predictor η = Xβ), and a link function g relating E[Y|X] = μ to the linear predictor via g(μ) = η. Classification note: also_type framework because GLMs provide an organizing system of concepts for a broad class of regression models.

## Connections
- [[logistic-regression]] — specializes: logistic regression is GLM with Bernoulli response and logit link
- [[maximum-likelihood-estimation]] — uses: GLM parameters are estimated via MLE using iteratively reweighted least squares (IRLS)
- [[regularization]] — extends: penalized GLMs (ridge, lasso) add L2/L1 penalties to the GLM log-likelihood

## Reading Path
- [[kroese-statistical-modeling-ch10]] (unread) — primary treatment: GLM framework, logit model, probit model with latent-variable representation, Poisson regression
- [[hastie-esl-ch04]] (unread) — classification methods including logistic regression as a GLM
- [[capretto-bambi-2022]] (unread) — Bambi implements GLMMs (GLMs with group-specific random effects) using Bayesian inference; formula interface supporting Gaussian, Binomial, Poisson and other families
