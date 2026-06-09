---
aliases: []
also_type: []
applies:
- kernel-density-estimation
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- mixture-models
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:logistic-gaussian-process
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch21
tags:
- gaussian-process
- density-estimation
- density-regression
- nonparametric-bayes
- latent-function
title: Logistic Gaussian Process (LGP)
understanding: 0
uses:
- gaussian-process
- covariance-function
- laplace-approximation
---

## Definition
The **logistic Gaussian process (LGP)** turns a Gaussian process into a prior over probability *densities* (not just regression functions), giving a nonparametric Bayesian alternative to mixture models for density estimation and density regression.

## Construction
Draw an unconstrained random surface $f \sim \mathrm{GP}(m, k)$ and map it to a valid density by the **continuous logistic (softmax) transform**, which enforces non-negativity and normalization:
$$p(y \mid f) = \frac{e^{f(y)}}{\int e^{f(y')}\,dy'}.$$
The mean function $m$ is naturally chosen as the log-density of an elicited parametric guess (e.g. a Student-$t$), so the LGP is *centered* on that guess and deviates from it as the data demand; the covariance function $k$ (e.g. squared-exponential or Matérn-$\tfrac52$) sets the smoothness of the resulting density. An equivalent **compactified** form uses a zero-mean GP $W$ on $[0,1]$ and an elicited CDF $G_0$, $p(y)=g_0(y)\,e^{W(G_0(y))}/\!\int e^{W(v)}dv$, which smooths the prior in the tails of $g_0$.

## Density regression
The construction extends directly to conditional densities $p(y\mid x)=e^{f(x,y)}/\!\int e^{f(x,y')}dy'$ with $f$ a GP over the joint $(x,y)$ space, e.g. a squared-exponential kernel with a separate length scale per predictor so unneeded predictors can effectively drop out (nonparametric variable selection).

## Inference
The central difficulty is the normalizing integral in the denominator. In practice $f$ is represented on a finite basis or a discretized grid of the domain; inference then uses MCMC, or a combination of **Laplace's method** for the latent values $f$ with quadrature/CCD integration over the hyperparameters of $m$ and $k$. A practical advantage over mixture-model density estimation: given the hyperparameters and a fixed finite representation, the posterior over $f$ is **unimodal**.

## Latent-variable-regression alternative
A simpler related construction (Kundu & Dunson 2014) induces a density prior via $y_i \sim N(\mu(u_i),\sigma^2),\; u_i \sim U(0,1)$ with $\mu$ a GP: any target density is reachable since $y=F_0^{-1}(u)$, and conditionally on the latent $u_i$ this is ordinary GP regression amenable to data-augmentation sampling. It generalizes to density regression by letting $\mu$ be a GP over $(u,x)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kernel-density-estimation]] — applies: LGP is a Bayesian alternative for the same density-estimation task that KDE addresses non-probabilistically.
- [[mixture-models]] — contrasts-with: Both are nonparametric density estimators; LGP has a unimodal latent posterior given hyperparameters, unlike multimodal mixture posteriors.
- [[laplace-approximation]] — uses: Laplace's method integrates over the latent values f; hyperparameters via quadrature/CCD.
- [[covariance-function]] — uses: The kernel (squared-exponential, Matern) sets the smoothness of the induced density.
- [[gaussian-process]] — uses: LGP draws an unconstrained surface from a GP, then logistic-transforms it into a density.
[To be populated during integration]