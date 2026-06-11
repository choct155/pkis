---
aliases: []
also_type: []
analogous-to:
- kernel-ridge-regression
- kernel-regression-rl
contrasts-with:
- kernel-density-estimation
- regularization
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
extends:
- dual-kernel-ridge-regression
generalizes:
- bayesian-linear-regression
- linear-regression
id: pkis:technique:gaussian-process-regression
instantiates:
- gaussian-process
knowledge_type: technique
maturity: settled
related_concepts:
- '[[gaussian-distribution]]'
- '[[conjugate-prior]]'
- '[[kernel-density-estimation]]'
- '[[bayesian-linear-regression]]'
sources:
- '[[kroese-statistical-modeling]]'
- '[[kurz-hybrid-modeling-2022]]'
specializes:
- bayesian-nonparametric-models
tags:
- gaussian-process
- nonparametric
- bayesian-inference
- kernel-functions
- regression
title: Gaussian Process Regression
understanding: 0
uses:
- marginal-likelihood
- laplace-approximation
- cross-validation
- gram-matrix
- covariance-function
- mercer-kernel
- posterior-predictive-distribution
- reproducing-kernel-hilbert-space
---

Gaussian Process Regression (GPR) is a nonparametric Bayesian regression method that places a Gaussian process prior over the function space — a collection of random variables where any finite subset is jointly Gaussian, defined by a mean function m(x) and covariance kernel k(x,x') — yielding exact closed-form posterior inference over functions given observed data.

## Connections
- [[kernel-regression-rl]] — analogous-to
- [[regularization]] — contrasts-with
- [[linear-regression]] — generalizes
- [[reproducing-kernel-hilbert-space]] — uses
- [[bayesian-nonparametric-models]] — specializes
- [[posterior-predictive-distribution]] — uses
- [[kernel-ridge-regression]] — analogous-to: GP posterior mean equals kernel ridge regression prediction
- [[mercer-kernel]] — uses
- [[kernel-density-estimation]] — contrasts-with
- [[covariance-function]] — uses
- [[dual-kernel-ridge-regression]] — extends
- [[bayesian-linear-regression]] — generalizes
- [[gram-matrix]] — uses
- [[gaussian-process]] — instantiates
- [[cross-validation]] — uses: Leave-one-out CV predictions (lppd_loo) are computed cheaply via multivariate-Gaussian identities for model comparison.
- [[laplace-approximation]] — uses: For non-Gaussian likelihoods the marginal likelihood and latent posterior are approximated by Laplace's method.
- [[marginal-likelihood]] — uses: Kernel hyperparameters and noise variance are learned by maximizing/sampling the GP log marginal likelihood.
- [[bayesian-linear-regression]] — generalizes: Bayesian linear regression is GPR with a linear kernel; GPR extends to nonlinear relationships via richer kernels
- [[conjugate-prior]] — uses: the Gaussian likelihood combined with a GP prior yields a GP posterior (exact conjugacy)
- [[kernel-density-estimation]] — contrasts-with: KDE estimates marginal densities; GPR estimates conditional mean functions via kernel-induced covariance structure
- [[variational-inference]] — contrasts-with: VI provides approximate posterior inference for GP models at scale; exact GPR requires O(n³) matrix inversion

## Reading Path
- [[kroese-statistical-modeling-ch11]] (unread) — primary treatment: GP regression, kernel functions, smoothing splines, connection to RKHS
- [[kurz-hybrid-modeling-2022]] (unread) — GP used as surrogate model in Bayesian optimization for free-shape trace pair design; provides mean and uncertainty for Expected Improvement acquisition

## Predictive equations via the partitioned inverse
Because the joint density $P(t_{N+1},\mathbf{t}_N)$ is Gaussian, the predictive conditional $P(t_{N+1}\mid\mathbf{t}_N)$ is itself Gaussian. Writing the $(N{+}1)$-point covariance in block form
$$C_{N+1}=\begin{bmatrix} C_N & \mathbf{k} \\ \mathbf{k}^T & \kappa \end{bmatrix},$$
where $\mathbf{k}$ holds the covariances of the new point with the training points and $\kappa$ its prior variance, the partitioned-inverse identities give a predictive mean and variance that require inverting only $C_N$:
$$\hat{t}_{N+1}=\mathbf{k}^T C_N^{-1}\mathbf{t}_N,\qquad \sigma_{\hat{t}_{N+1}}^2=\kappa-\mathbf{k}^T C_N^{-1}\mathbf{k}.$$
The mean is a *linear* combination of the observed targets (the kernel-weighted predictor), and the variance is the prior variance reduced by what the data explain. One inversion of $C_N$ (cost $O(N^3)$) serves predictions at arbitrarily many new points, independent of the number $H$ of underlying basis functions.

Hyperparameters $\boldsymbol{\theta}$ of the kernel are learned by maximizing the log evidence
$$\ln P(\mathbf{t}_N\mid X_N,\boldsymbol{\theta})=-\tfrac{1}{2}\ln\det C_N-\tfrac{1}{2}\mathbf{t}_N^T C_N^{-1}\mathbf{t}_N-\tfrac{N}{2}\ln 2\pi,$$
whose gradient is available in closed form — a complexity-control problem solved by the Bayesian Occam's razor. For classification, a GP prior is placed on a latent activation $a(\mathbf{x})$ squashed through a logistic link; the non-Gaussian likelihood then requires Laplace, variational, or Monte Carlo approximations.