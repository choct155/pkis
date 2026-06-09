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
- statistical-learning
id: pkis:technique:robit-regression
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch17
specializes:
- robust-inference
tags:
- binary-regression
- latent-variable
- robustness
- logistic
- probit
title: Robit Regression
understanding: 0
uses:
- t-distribution
- latent-variable-models
---

## Definition
A robust alternative to logistic and probit regression for binary outcomes, due to Liu (2004). Standard logistic/probit links are nonrobust with respect to the *predictors*: for large $|X\beta|$ the inverse-link gives fitted probabilities essentially 0 or 1, so a point with extreme predictors that is misclassified exerts outsized influence. Robit replaces the logistic/normal latent-variable distribution in the latent-formulation of binary regression with a t: $u_i \sim t_\nu((X\beta)_i, 1)$, letting the model fit most data while tolerating occasional isolated errors. Because the latent $u_i$ are never observed, $\nu$ is essentially unidentifiable and is fixed rather than estimated; $\nu=4$ closely approximates the logistic link, and $\nu\to\infty$ recovers the probit. Computation uses the normal scale-mixture representation of the t, fitting via the EM algorithm and Gibbs sampler with the latent values $u_i$ and their variances treated as missing data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[logistic-regression]] — contrasts-with: robust alternative to logistic regression; nu=4 approximates the logistic link
- [[latent-variable-models]] — uses: built on the latent continuous-variable formulation of discrete-data regression
- [[robust-inference]] — specializes: robit is robust inference applied to binary regression
- [[t-distribution]] — uses: robit replaces the binary-regression latent distribution with a t
[To be populated during integration]