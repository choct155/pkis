---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- bayesian-stats
id: pkis:concept:probability-distribution-relationships
knowledge_type: concept
maturity: settled
related_concepts:
- '[[limiting-distributions]]'
- '[[inverse-transform-sampling]]'
- '[[gaussian-distribution]]'
- '[[probability-theory]]'
sources:
- '[[abdelkader-distribution-relationships-2010]]'
- kroese-statistical-modeling-ch03
- lange-applied-probability-ch14
tags:
- probability-theory
- statistics
title: Probability Distribution Relationships
understanding: 0
---

The structured network of transformation and limiting connections linking common probability distributions: distributions are related either via algebraic transformations of random variables (CDF, Jacobian, or MGF techniques) or via limiting/asymptotic relationships (CLT, Poisson approximation); uniform and Bernoulli distributions are the roots of the continuous and discrete families respectively.

## Reading Path
- [[abdelkader-distribution-relationships-2010]] (unread) — four-diagram survey mapping the complete ecosystem of common distribution relationships, including the Balakrishnan skew-normal family

## Heavy-tailed alternatives to the Gaussian (MacKay Ch. 23)
MacKay catalogs a family of unimodal real-valued densities ordered by tail weight, a useful menu when the Gaussian's quadratic-log tails are too light (its probabilities of $2\sigma\!-\!5\sigma$ deviations are $0.046, 0.003, 6\times10^{-5}, 6\times10^{-7}$ — often unrealistically small, causing a Gaussian model to 'contort itself' around outliers).

- **Mixture of Gaussians** — sums of Gaussians with distinct means/variances and mixing weights $\pi_i$ ($\sum_i\pi_i=1$); heavier-tailed than a single Gaussian.
- **Student-$t$**: $P(x\mid\mu,s,n)\propto\left(1+\frac{(x-\mu)^2}{ns^2}\right)^{-(n+1)/2}$, an infinite mean-$\mu$ Gaussian mixture with $n$ degrees of freedom. Mean exists for $n>1$, variance $\sigma^2=ns^2/(n-2)$ for $n>2$; as $n\to\infty$ it tends to $\mathrm{Normal}(\mu,s)$. Arises in Bayesian inference when a Gaussian's $\sigma$ is itself uncertain.
- **Cauchy**: the $n=1$ Student-$t$; no finite mean or variance — maximally heavy among this family.
- **Biexponential (Laplace)**: $P(x\mid\mu,s)=\frac{1}{2s}\exp(-|x-\mu|/s)$, tails intermediate between Student and Gaussian.
- **Inverse-cosh**: $P(x\mid\beta)\propto[\cosh(\beta x)]^{-1/\beta}$, popular in independent component analysis; biexponential as $\beta\to\infty$, Gaussian as $\beta\to 0$.

For positive variables the analogous catalog is exponential $\subset$ gamma, plus the **log-normal** ($\ln x$ Gaussian) and **inverse-gamma**. For periodic variables, the **Von Mises** distribution $P(\theta)\propto\exp(\beta\cos(\theta-\mu))$ plays the Gaussian's role, with the **wrapped Gaussian** as the Brownian-diffusion alternative.

## Exponential distribution: the building block (MacKay Ch. 23)
The **exponential distribution** is the simplest waiting-time law and the common ancestor of several catalog entries. On the positive reals, $P(x\mid s)=\frac{1}{s}\exp(-x/s)$, $x\in(0,\infty)$, with mean $s$ — e.g. the wait for a bus arriving on average every $s$ minutes (a Poisson process). Its discrete analogue over integers is $P(r\mid f)=f^r(1-f)$, the number of rolls until a six appears ($f=5/6$); writing $\lambda=\ln(1/f)$ gives $P(r\mid f)=(1-f)e^{-\lambda r}$.

It is the $c=1$ special case of the gamma distribution, and summing $m$ i.i.d. exponentials (the $m$-th Poisson arrival time) gives a gamma with shape $m$. This nests it cleanly into the transformation/limiting web alongside the binomial $\to$ Poisson and gamma $\to$ Gaussian limits.