---
title: "Bambi: A Simple Interface for Fitting Bayesian Linear Models in Python"
authors: "Tomás Capretto, Camen Piho, Ravin Kumar, Jacob Westfall, Tal Yarkoni, Osvaldo A. Martin"
year: 2022
type: paper
domain: [bayesian-stats]
tags: [probabilistic-programming, software, generalized-linear-models, hierarchical-models, mcmc]
source_url: "https://arxiv.org/abs/2012.10754"
drive_id: "1lWDIFeFFvMDycfPWuS_5tBNYoXhaVhz6"
drive_path: "PKIS/sources/papers/Bambi - A Simple Interface for Fitting Bayesian Linear Models in Python - Capretto, Piho, Kumar et al.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[bambi-package]]", "[[generalized-linear-models]]", "[[hierarchical-bayesian-models]]", "[[automatic-priors]]", "[[bayesian-linear-regression]]", "[[conjugate-prior]]", "[[mcmc]]"]
---

## Summary

Capretto et al. introduce Bambi (BAyesian Model Building Interface), an open-source Python package that wraps PyMC to provide a formula-based interface for specifying and fitting Generalized Linear Multilevel Models (GLMMs) under a Bayesian framework. The motivation is to lower the barrier to Bayesian statistics for practitioners accustomed to R's lme4/brms formula syntax, while retaining access to PyMC's full flexibility for advanced users.

Bambi's model class accepts R-style formula strings (including the | operator for group-specific/random effects), a pandas DataFrame, a family specification (Gaussian, Binomial, Poisson, etc.), optional custom priors, and a link function. When priors are not specified, Bambi automatically constructs weakly informative priors by scaling Normal(0, σ) slopes to the observed data variance, and HalfStudentT distributions for variance terms — following a principled empirical Bayes-adjacent prior construction that tries to be "weakly informative" across a wide range of scales.

Fitting proceeds via PyMC's NUTS sampler (adaptive dynamic HMC), with ArviZ for sampling diagnostics (R-hat, ESS) and posterior visualization. The paper demonstrates logistic regression, Poisson regression, mixed-effects models with crossed random effects, and custom-prior models. Key design decisions include: automatic handling of categorical predictors (sum-to-zero or treatment coding), formula-driven design matrix construction via Formulaic, and an accessible "learning progression" from default to fully custom models.

## Key Knowledge Objects

- [[bambi-package]] (technique, moderate — could be framework) — Bambi Python package: formula-based interface for Bayesian GLMMs built on PyMC and ArviZ
- [[generalized-linear-models]] (framework, high) — already likely exists or should be checked; extends linear regression to non-Gaussian response distributions via a link function and linear predictor η
- [[hierarchical-bayesian-models]] (framework, high) — Bayesian models with group-specific effects (random effects) treated as random variables with hyperprior distributions; GLMMs are a special case
- [[automatic-priors]] (technique, high) — constructing default weakly informative priors from observed data scale without requiring user specification
- [[bayesian-linear-regression]] (technique, high) — already exists; Bambi implements BLR as the Gaussian family with identity link and conjugate-adjacent weakly informative priors
- [[conjugate-prior]] (concept, high) — already exists; Bambi uses Normal priors for slopes and HalfStudentT for variance, motivated by approximate conjugacy considerations
- [[mcmc]] (technique, high) — Bambi fits models via NUTS (a variant of HMC), accessed through PyMC

## Key Extractions

1. **GLMM formulation**: Y_i ~ D(g^{-1}(η_i), θ); η = Xβ + Zu, where β are common effects and u are group-specific effects. Both β and u are treated as random variables with posterior estimated from data — a key contrast with the frequentist REML approach where u is part of the error term.

2. **Formula interface**: `model = bmb.Model("drugs ~ o + c + e + a + n", data)` specifies a full Bayesian regression; group-specific effects use `(1|group)` notation as in lme4. No explicit prior specification required.

3. **Automatic prior construction**: Slopes receive Normal(0, σ) where σ is set by the data scale (observed variance of predictor / outcome). The Intercept gets a Normal centered at the response mean. Residual SD gets HalfStudentT(ν=4). These are described as "weakly informative."

4. **Sampling diagnostics via ArviZ**: R-hat "should be smaller than 1.01"; effective sample size (ESS) reported for bulk and tails; Monte Carlo standard error (MCSE) for mean and SD. All accessible via `az.summary(idata)`.

5. **NUTS sampler**: "Bambi fits models using an adaptive dynamic Hamiltonian Monte Carlo algorithm [Hoffman and Gelman 2014], Betancourt [2017]." PyMC's NUTS is the default; other samplers accessible via direct PyMC interface.

6. **Mixed effects crossed example**: Crossed random effects (subjects × items) are handled naturally in Bambi via the formula `(1|subject) + (1|item)`, which in PyMC requires careful manual construction.

## Connection Candidates

- [[bayesian-linear-regression]] — uses (technique→technique): Bambi's Gaussian family is BLR with automatic prior selection; extends it to the GLMM case
- [[conjugate-prior]] — uses (technique→concept): Bambi's automatic priors are motivated by approximate conjugacy reasoning (Normal priors for Normal likelihoods)
- [[mcmc]] — uses (technique→technique): Bambi wraps PyMC's NUTS sampler for posterior sampling
- [[generalized-linear-models]] — extends (technique→framework): Bambi implements GLMMs as the union of GLMs with hierarchical random effects under Bayesian treatment
- [[directed-graphical-models]] — uses (framework→concept): Bambi's hierarchical models implicitly define a DGM; the hyperprior structure encodes the conditional independence assumptions
