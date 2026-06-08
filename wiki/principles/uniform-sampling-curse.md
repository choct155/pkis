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
id: pkis:principle:uniform-sampling-curse
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch29
tags:
- monte-carlo
- typical-set
- curse-of-dimensionality
- sampling
- ising-model
- mackay
title: Why Uniform Sampling Fails in High Dimensions
understanding: 0
---

## Definition
Drawing samples $\{x^{(r)}\}$ uniformly from the state space and reweighting by $P^*(x^{(r)})$ to estimate $\Phi$ is a naive Monte Carlo strategy that collapses in high dimensions. The reason is the **typical set**: a high-dimensional distribution concentrates almost all its mass in a region $T$ of volume $|T|\approx 2^{H(X)}$, where $H(X)$ is the entropy. A benign $\varphi$'s expectation is determined by its values on $T$, so a useful estimate requires hitting $T$.

The chance a uniform draw lands in $T$ is $2^{H}/2^{N}$, so the number of samples needed merely to hit it once is
$$R_{\min}\approx 2^{N-H}.$$

### The Ising-model illustration
For a $30\times30$ Ising model near its critical temperature, $H\approx N/2$, giving $R_{\min}\approx 2^{N/2}$. For $N=1000$ this is about $10^{150}$ — roughly the square of the number of particles in the universe. Only at high temperature, where $P$ approaches uniform and $H\to N$, does $R_{\min}\to 1$ and uniform sampling become viable.

### Why it matters
This result motivates *every* sophisticated sampler in the chapter. Importance sampling, rejection sampling, and MCMC all exist to concentrate computational effort on the typical set rather than squandering it on the exponentially vast low-probability bulk of the space. It is the sampling-specific face of the curse of dimensionality, distinct from but closely tied to the geometry of the typical set.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]