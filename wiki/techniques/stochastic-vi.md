---
aliases:
- SVI
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- bayesian-stats
- optimization
extends:
- mean-field-variational-inference
id: pkis:technique:stochastic-vi
knowledge_type: technique
maturity: settled
related_concepts:
- '[[variational-inference]]'
- '[[coordinate-ascent-vi]]'
- '[[elbo]]'
- '[[gradient-descent]]'
sources:
- '[[blei-vi-review]]'
tags:
- variational-methods
- approximate-inference
- stochastic-optimization
title: Stochastic Variational Inference (SVI)
understanding: 0
---

An extension of mean-field CAVI to massive datasets (Hoffman et al. 2013): replace the full-data natural gradient of the ELBO with a noisy estimate computed from a single random datapoint (or minibatch), rescaled as if that point appeared n times; step sizes must satisfy Robbins-Monro conditions; requires no new derivation beyond CAVI, enabling any CAVI implementation to be immediately scaled.

## Connections
- [[mean-field-variational-inference]] — extends

- [[variational-inference]] — specializes: SVI is the scalable extension of mean-field VI using stochastic natural gradient descent
- [[coordinate-ascent-vi]] — extends: SVI replaces exact coordinate updates with stochastic approximations; same update structure, different execution
- [[gradient-descent]] — uses: SVI applies stochastic gradient descent in the natural gradient geometry; step sizes follow Robbins-Monro schedule
- [[elbo]] — uses: SVI maximizes the ELBO using noisy natural gradient estimates from subsampled data

## Reading Path

- [[blei-vi-review]] (unread) — Section 4.3; full SVI derivation including natural gradient, noisy gradient estimator, step-size conditions, and probabilistic topic model demonstration (Algorithm 3)