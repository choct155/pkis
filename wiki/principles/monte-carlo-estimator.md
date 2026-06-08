---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:principle:monte-carlo-estimator
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- importance-sampling
- mcmc
related_concepts: []
sources:
- mackay-itila-ch29
tags:
- monte-carlo
- expectation
- estimator
- variance
- sampling
- mackay
title: Monte Carlo Estimator
understanding: 0
---

## Definition
The Monte Carlo estimator approximates an expectation under a target density $P(x)$ by averaging a function over independent samples drawn from $P$:
$$\hat{\Phi} \equiv \frac{1}{R}\sum_{r=1}^{R}\varphi(x^{(r)}), \qquad x^{(r)}\sim P(x),$$
as a stand-in for $\Phi = \langle\varphi(x)\rangle = \int d^N x\, P(x)\varphi(x)$. If the samples are genuinely drawn from $P$, then $\hat{\Phi}$ is unbiased ($\mathbb{E}[\hat{\Phi}]=\Phi$) and its variance is $\sigma^2/R$, where $\sigma^2 = \int d^N x\, P(x)(\varphi(x)-\Phi)^2$ is the variance of $\varphi$ under $P$.

This reduces the hard problem of integration (Problem 2) to the problem of sampling (Problem 1): solve sampling, and expectations follow for free.

### Dimension-independence of the variance
The accuracy of $\hat{\Phi}$ depends only on the variance of $\varphi$ and the number $R$ of **independent** samples — not on the dimensionality $N$ of the space. The error shrinks as $1/\sqrt{R}$ regardless of $N$. MacKay notes that as few as a dozen independent samples often suffice: with $R=12$, the precision is $\sigma/\sqrt{12} < \sigma/3$, finer than one usually needs.

### Why it matters
This is the foundational promise of Monte Carlo: integration over thousand-dimensional spaces can succeed where deterministic quadrature ($50^{1000}$ grid points) is impossible. The crucial caveat is the word *independent*: MCMC produces *correlated* draws, so the effective sample size — not the raw iteration count — governs accuracy.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mcmc]] — prerequisite-of: MCMC supplies the (correlated) samples plugged into the Monte Carlo estimator.
- [[importance-sampling]] — prerequisite-of: Importance sampling is a reweighted variant of the basic Monte Carlo estimator.
[To be populated during integration]