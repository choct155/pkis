---
abbrev: "SMC"
id: "pkis:source:kroese-statistical-modeling"
aliases: ["Statistical Modeling and Simulation (Kroese)"]
title: "[SMC Chan & Kroese] Statistical Modeling and Computation, 2nd ed."
authors: ["Joshua C.C. Chan", "Dirk P. Kroese"]
year: 2025
type: book
domain: [bayesian-stats, statistical-learning, optimization]
tags: [probability-theory, monte-carlo, mcmc, likelihood, bayesian-inference, frequentist, glm, time-series, nonparametric, simulation]
source_url: "https://doi.org/10.1007/978-1-0716-4132-3"
drive_id: "109dpIRkznPIGw7zv4SBfu3bNMnmgxInp"
drive_path: "PKIS/sources/books/kroese-statistical-modeling.pdf"
isbn: "978-1-0716-4131-6"
toc_source: "manual"
status: unread
date_added: 2026-05-20
concepts: ["[[probability-theory]]", "[[gaussian-distribution]]", "[[em-algorithm]]", "[[gibbs-sampler]]", "[[metropolis-algorithm]]", "[[importance-sampling]]", "[[logistic-regression]]", "[[lasso]]", "[[regularization]]", "[[generalized-linear-models]]", "[[bootstrap]]", "[[maximum-likelihood-estimation]]", "[[gaussian-process-regression]]", "[[kernel-density-estimation]]", "[[mcmc]]", "[[hypothesis-testing]]", "[[ridge-regression]]", "[[state-space-models]]", "[[directed-graphical-models]]"]
---

## Summary

*Statistical Modeling and Computation* (2nd ed., 2025) by Chan and Kroese is a comprehensive undergraduate-to-graduate textbook offering an integrated treatment of mathematical statistics and modern computational methods. The book is structured in three parts and uses Julia throughout to make the connection between statistical theory and computational practice explicit.

Part I (Chapters 1–3) builds the foundations of probability: random experiments, probability distributions (discrete and continuous), expectation, transforms, common named distributions, simulation via inverse-transform and acceptance-rejection, and joint distributions including the multivariate normal and limit theorems.

Part II (Chapters 4–8) covers the core framework of statistical inference from both frequentist and Bayesian perspectives. Chapter 4 introduces common statistical models (IID sampling, regression, ANOVA, normal linear model) and adds a new section on statistical learning (training/test loss, bias-variance). Chapter 5 covers estimation (MoM, least squares), confidence intervals, hypothesis testing, cross-validation, and exponential families. Chapter 6 develops likelihood-based inference: score functions, Fisher information, Cramér-Rao, MLE properties, likelihood ratio tests, Newton-Raphson, and the EM algorithm. Chapter 7 treats Monte Carlo sampling: empirical CDF, kernel density estimation, the bootstrap, MCMC, Metropolis-Hastings, and Gibbs sampler. Chapter 8 is Bayesian inference: hierarchical models, common conjugate models, Bayesian networks, posterior asymptotic normality, priors, and Bayesian model comparison.

Part III (Chapters 9–13) addresses advanced models. Chapter 9 covers shrinkage and regularization (James-Stein, ridge, lasso, false discovery rate). Chapter 10 covers generalized linear models (logit, probit, Poisson regression). Chapter 11 covers nonparametric methods (order statistics, nonparametric tests, kernel functions, regression splines, Gaussian process regression). Chapter 12 covers dependent data (AR/MA/ARMA, Gaussian graphical models, random effects, mixed models). Chapter 13 covers state space models (unobserved components, time-varying parameters, stochastic volatility with auxiliary mixture sampling).

The 2nd edition adds two new chapters (shrinkage/regularization and nonparametric methods), switches from MATLAB to Julia, and adds a statistical learning section. A Julia Primer appendix and Mathematical Supplement (proofs) are included.

## Chapters
- [[kroese-statistical-modeling-ch01]] — Ch. 1 — Probability Models
- [[kroese-statistical-modeling-ch02]] — Ch. 2 — Random Variables and Probability Distributions
- [[kroese-statistical-modeling-ch03]] — Ch. 3 — Joint Distributions
- [[kroese-statistical-modeling-ch04]] — Ch. 4 — Common Statistical Models
- [[kroese-statistical-modeling-ch05]] — Ch. 5 — Statistical Inference
- [[kroese-statistical-modeling-ch06]] — Ch. 6 — Likelihood
- [[kroese-statistical-modeling-ch07]] — Ch. 7 — Monte Carlo Sampling
- [[kroese-statistical-modeling-ch08]] — Ch. 8 — Bayesian Inference
- [[kroese-statistical-modeling-ch09]] — Ch. 9 — Shrinkage and Regularization
- [[kroese-statistical-modeling-ch10]] — Ch. 10 — Generalized Linear Models
- [[kroese-statistical-modeling-ch11]] — Ch. 11 — Nonparametric Methods
- [[kroese-statistical-modeling-ch12]] — Ch. 12 — Dependent Data Models
- [[kroese-statistical-modeling-ch13]] — Ch. 13 — State Space Models
## Key Knowledge Objects

- [[maximum-likelihood-estimation]] (technique, high) — MLE with score functions, Fisher information, Cramér-Rao bound, and asymptotic properties
- [[mcmc]] (technique, high) — umbrella framework for MCMC; covers Metropolis-Hastings and Gibbs sampler in unified treatment
- [[bootstrap]] (technique, high) — resampling-based inference for standard errors, confidence intervals, and hypothesis tests
- [[generalized-linear-models]] (technique, high) — unified regression framework extending linear model via link function; covers logit, probit, Poisson
- [[kernel-density-estimation]] (technique, high) — nonparametric density estimation via kernel smoothing
- [[gaussian-process-regression]] (technique, high) — nonparametric Bayesian regression via kernel-defined Gaussian process prior
- [[hypothesis-testing]] (technique, high) — frequentist testing framework: null/alternative hypotheses, test statistics, p-values, power
- [[ridge-regression]] (technique, high) — L2-penalized regression (Tikhonov regularization); James-Stein shrinkage motivation
- [[em-algorithm]] (technique, high) — existing node; treated in Ch. 6 as a likelihood maximization algorithm using E-step/M-step
- [[gibbs-sampler]] (technique, high) — existing node; covered in Ch. 7 as MCMC via sequential conditional sampling
- [[metropolis-algorithm]] (technique, high) — existing node; covered in Ch. 7 as Metropolis-Hastings acceptance-rejection MCMC
- [[lasso]] (technique, high) — existing node; covered in Ch. 9 with false discovery rate and comparison to ridge
- [[logistic-regression]] (technique, high) — existing node; covered in Ch. 10 as the logit model within GLM framework
- [[state-space-models]] (framework, high) — existing node; Ch. 13 covers UCM, TVP, and stochastic volatility with Bayesian estimation
- [[directed-graphical-models]] (framework, high) — existing node; Ch. 8 treats Bayesian networks as a graphical formalism for Bayesian models

## Key Extractions

1. **Integrated frequentist-Bayesian treatment**: The book explicitly develops both perspectives in parallel from Ch. 4 onward. Ch. 8's Bayesian inference is presented as a complement to Ch. 5-6's frequentist approach, not a replacement. Asymptotic normality of the posterior (Bernstein-von Mises) appears in §8.4.

2. **EM algorithm as likelihood maximization**: Ch. 6 positions EM as a general-purpose MLE algorithm for latent variable models, distinct from its Bayesian/data-augmentation use. The key insight: maximizing Q(θ|θ^{(t)}) = E[log p(Y,Z|θ) | Y, θ^{(t)}] guarantees the observed log-likelihood does not decrease.

3. **Bootstrap as distribution-free inference**: Ch. 7 §7.3 presents the bootstrap as a resampling procedure where B bootstrap replications of the statistic provide an empirical sampling distribution. Bias-corrected and accelerated (BCa) intervals are mentioned alongside basic percentile intervals.

4. **GLM unified framework**: Ch. 10 unifies logit, probit, and Poisson regression under the GLM framework via link functions and exponential-family distributions. The latent-variable representation of the probit model (§10.2.3) clarifies the relationship between probit and logit.

5. **Gaussian process regression as kernel regression**: Ch. 11 §11.5 presents GP regression as placing a Gaussian process prior with kernel function k(x,x') over the function space, yielding exact posterior inference via matrix inversion. The posterior predictive mean is equivalent to a kernel regression estimator.

6. **State space models with auxiliary mixture sampling**: Ch. 13 §13.3 covers stochastic volatility via a log-chi-squared approximation (Kim-Shephard-Chib auxiliary mixture approach), making non-Gaussian state-space inference tractable via MCMC.

7. **False discovery rate in high-dimensional testing**: Ch. 9 §9.4 introduces the Benjamini-Hochberg procedure for controlling FDR in multiple comparison settings, situating shrinkage and regularization alongside multiple testing as two responses to the high-dimensional inference problem.

## Connection Candidates

- [[em-algorithm]] — extends: Ch. 6 provides a cleaner mathematical treatment of EM as likelihood maximization than Tanner, with the convergence guarantee via Jensen's inequality
- [[gibbs-sampler]] — uses: Ch. 7 presents the Gibbs sampler as a special case of Metropolis-Hastings with acceptance probability 1 for full conditionals
- [[metropolis-algorithm]] — specializes: Ch. 7 presents Metropolis-Hastings as the general algorithm of which the Metropolis algorithm is the symmetric-proposal special case
- [[state-space-models]] — extends: Ch. 13 adds Bayesian estimation and auxiliary mixture sampling to the state-space framework
- [[directed-graphical-models]] — uses: Ch. 8 uses Bayesian networks to represent conditional independence structure in hierarchical Bayesian models
- [[lasso]] — contrasts-with: Ch. 9 presents ridge and lasso together, motivating the trade-off between L2 (ridge) and L1 (lasso) penalization
- [[intractable-posterior]] — uses: The full Bayesian computation chapters (7, 8, 13) collectively address this problem
- [[variational-inference]] — contrasts-with: This book covers MCMC-based Bayesian inference; VI is the main alternative not covered here
