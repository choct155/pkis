---
id: "pkis:framework:hierarchical-bayesian-models"
aliases: []
title: "Hierarchical Bayesian Models"
knowledge_type: framework
also_type: []
domain: [bayesian-stats]
tags: [probability-theory, multilevel-models, shrinkage]
related_concepts: ["[[directed-graphical-models]]", "[[bayesian-linear-regression]]", "[[conjugate-prior]]", "[[mcmc]]", "[[automatic-priors]]"]
sources: ["[[capretto-bambi-2022]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Bayesian models with multiple levels of latent variables where group-specific parameters are themselves drawn from hyperprior distributions; group-specific effects (random effects) are treated as random variables rather than fixed unknowns, enabling partial pooling across groups and yielding posterior distributions for both individual-level and population-level parameters.

## Reading Path
- [[capretto-bambi-2022]] (unread) — Bambi's GLMM formulation as hierarchical Bayesian model; crossed random effects examples with formula notation and NUTS sampling
