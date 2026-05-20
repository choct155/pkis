---
title: "Laplace Approximation"
knowledge_type: technique
also_type: []
domain: [bayesian-stats]
tags: [posterior-approximation, normal-approximation, saddle-point, marginalization, asymptotic-methods]
related_concepts: ["[[probability-theory]]", "[[gaussian-distribution]]", "[[importance-sampling]]", "[[em-algorithm]]", "[[bayesian-linear-regression]]"]
sources: ["[[tanner-tools-statistical-inference]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

A higher-order normal approximation to a posterior distribution or likelihood function obtained by expanding the log-posterior (or log-likelihood) to second order around its mode: the posterior is approximated as N(θ_mode, [−∇²log p(θ|Y)]^{−1}). This is the saddle-point approximation applied to Bayesian computation.

The Laplace approximation enables non-normal corrections to basic normal-based inference (Chapter 2 in Tanner). For posterior moments it yields a more accurate estimate than first-order delta-method approximations. For marginalization, expanding around the conditional mode of the joint integrand enables integration of nuisance parameters without MCMC. Accuracy improves with n. Main limitation: fails when the posterior is multimodal or highly non-ellipsoidal.

## Reading Path
- [[tanner-tools-statistical-inference]] (unread) — primary treatment; Chapter 3 covers Laplace's method for posterior moments and marginalization; motivates MCMC alternatives for non-ellipsoidal posteriors
- [[tanner-tools-statistical-inference-ch03]] (unread) — primary chapter
