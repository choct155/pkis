---
aliases: []
also_type: []
applies:
- linear-regression
- gaussian-distribution
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- statistical-learning
- bayesian-stats
id: pkis:technique:maximum-likelihood-estimation
knowledge_type: technique
maturity: settled
related_concepts:
- '[[probability-theory]]'
- '[[em-algorithm]]'
- '[[hypothesis-testing]]'
- '[[logistic-regression]]'
sources:
- '[[kroese-statistical-modeling]]'
- kroese-statistical-modeling-ch06
- tanner-tools-statistical-inference-ch02
specializes:
- maximum-a-posteriori-estimation-map
- empirical-risk-minimization
- map-estimation
tags:
- likelihood
- estimation
- fisher-information
- cramer-rao
- mle
- asymptotic-theory
title: Maximum Likelihood Estimation
understanding: 0
uses:
- kl-divergence
- empirical-distribution
- sufficient-statistics
- fisher-information
---

Maximum Likelihood Estimation (MLE) finds the parameter value θ̂ that maximizes the likelihood function L(θ; Y) = p(Y|θ) — i.e., the parameter under which the observed data were most probable.

## Reading Path
- [[kroese-statistical-modeling-ch06]] (unread) — primary treatment: score functions, Fisher information, Cramér-Rao bound, asymptotic normality of MLE, likelihood ratio tests, and Newton-Raphson

## Bayesian critique (MacKay)
MacKay (ITILA Ch. 3) frames the Bayesian critique of point estimation: the full posterior $P(\theta\mid D)\propto P(D\mid\theta)P(\theta)$ is 'the unique and complete solution', so 'there is no need to invent estimators, nor criteria for comparing alternative estimators.' MLE corresponds to the mode of the posterior under a flat prior, but it discards the spread the posterior encodes. For prediction, the MLE plug-in differs from the posterior-predictive average (Laplace's rule, $\frac{F_a+1}{F_a+F_b+2}$ vs. $F_a/F$).

## ML for a single Gaussian: closed-form estimators and error bars
For $N$ i.i.d. points $\{x_n\}$ from $\mathcal N(\mu,\sigma^2)$, MacKay derives the maximum-likelihood estimators directly by differentiating the log likelihood. With $\sigma$ known, $\partial_\mu\ln P = -N(\mu-\bar x)/\sigma^2 = 0$ gives $\hat\mu = \bar x$ (the sample mean), for any $\sigma$. The curvature $\partial^2_\mu\ln P = -N/\sigma^2$ yields, via a Gaussian (Laplace) approximation to the likelihood, error bars
$$\sigma_\mu = \sigma/\sqrt N,$$
the points at which the likelihood has fallen by a factor $e^{1/2}$.

With $\mu$ known, differentiating with respect to $\ln\sigma$ (the hygienic choice for a scale parameter) gives $\hat\sigma^2 = S_{\text{tot}}/N$ with $S_{\text{tot}}=\sum_n(x_n-\mu)^2$, and error bars $\sigma_{\ln\sigma}=1/\sqrt{2N}$. Jointly maximizing over both parameters gives $\{\hat\mu,\hat\sigma\}=\{\bar x,\ \sigma_N\}$ with $\sigma_N=\sqrt{S/N}$. Note that $\sigma_N$ is the *biased* ML estimator of the standard deviation (it divides by $N$, not $N-1$) — a low-dimensional example of an unrepresentative ML solution.

## Connections
- [[gaussian-distribution]] — applies
- [[linear-regression]] — applies: OLS is the MLE for Gaussian linear regression
- [[fisher-information]] — uses: MLE achieves Cramér–Rao bound asymptotically
- [[map-estimation]] — specializes: MLE = MAP with uniform prior
- [[sufficient-statistics]] — uses: Sufficient statistics summarise the data for MLE
- [[empirical-distribution]] — uses: MLE minimises KL divergence from the empirical distribution
- [[kl-divergence]] — uses: MLE is equivalent to minimising KL(p_D || p_theta)
- [[empirical-risk-minimization]] — specializes: MLE is ERM with log-loss
- [[maximum-a-posteriori-estimation-map]] — specializes