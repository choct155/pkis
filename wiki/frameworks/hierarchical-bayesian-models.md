---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- bayesian-stats
id: pkis:framework:hierarchical-bayesian-models
knowledge_type: framework
maturity: settled
related_concepts:
- '[[directed-graphical-models]]'
- '[[bayesian-linear-regression]]'
- '[[conjugate-prior]]'
- '[[mcmc]]'
- '[[automatic-priors]]'
sources:
- '[[capretto-bambi-2022]]'
- gelman-bda3
specializes:
- bayesian-inference
tags:
- probability-theory
- multilevel-models
- shrinkage
title: Hierarchical Bayesian Models
understanding: 0
uses:
- exchangeability
- hyperprior
- conjugate-prior
---

Bayesian models with multiple levels of latent variables where group-specific parameters are themselves drawn from hyperprior distributions; group-specific effects (random effects) are treated as random variables rather than fixed unknowns, enabling partial pooling across groups and yielding posterior distributions for both individual-level and population-level parameters.

## Reading Path
- [[capretto-bambi-2022]] (unread) — Bambi's GLMM formulation as hierarchical Bayesian model; crossed random effects examples with formula notation and NUTS sampling

## Connections
- [[conjugate-prior]] — uses: Conjugate population distributions (beta-binomial, normal-normal) give closed-form conditional posteriors for analytic-plus-numerical computation.
- [[bayesian-inference]] — specializes: Hierarchical Bayesian modeling is a structured special case of Bayesian inference with multiple parameter levels.
- [[hyperprior]] — uses: The hyperprior on φ is what makes the analysis fully Bayesian rather than empirical-Bayes plug-in.
- [[exchangeability]] — uses: Hierarchical models employ exchangeability of the group-level parameters as their core prior structure.