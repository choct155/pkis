---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:concept:gamma-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch23
tags:
- probability-distribution
- positive-real
- conjugate-prior
- waiting-times
- scale-parameter
title: Gamma Distribution
understanding: 0
---

## Definition
The **gamma distribution** is a two-parameter density over a positive real variable $x$. With scale $s>0$ and shape $c>0$,

$$P(x \mid s, c) = \Gamma(x; s, c) = \frac{1}{\Gamma(c)\,s}\left(\frac{x}{s}\right)^{c-1}\exp\!\left(-\frac{x}{s}\right), \qquad 0 \le x < \infty,$$

with mean $sc$ and variance $s^2 c$. Intuitively it is the Gaussian's analogue for quantities confined to $(0,\infty)$: it is the one-parameter exponential distribution multiplied by the polynomial $x^{c-1}$, so the shape $c$ controls how peaked-away-from-zero the density is while $s$ sets the scale. For $c=1$ it collapses to the exponential; for large $c$ it becomes Gaussian-like.

### Reparameterization and the 1/x prior
A positive variable is often better viewed through $l=\ln x$. The induced density $P(l)=P(x)\,x$ is always unimodal and asymmetric, and crucially has no spike at $x=0$ — the spike in $P(x)$ is an artefact of a bad basis. In the limit $sc=1,\ c\to 0$ the gamma tends to the improper, scale-invariant noninformative prior $1/x$, which is uniform in $\ln x$.

### Why it matters
The gamma is the workhorse prior for any inferred positive quantity: the variance (or precision $\tau$) of Gaussian noise, or the rate of a Poisson process. It is also the waiting-time law: the arrival time of the $m$-th event in a Poisson process of rate $\lambda$ is gamma-distributed, $\frac{\lambda(\lambda x)^{m-1}}{(m-1)!}e^{-\lambda x}$. Its reciprocal yields the inverse-gamma, the standard conjugate prior for a Gaussian variance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]