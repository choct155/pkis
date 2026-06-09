---
aliases: []
also_type: []
analogous-to:
- conjugate-prior
- beta-distribution
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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
generalizes:
- gaussian-distribution
id: pkis:concept:exponential-family
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch06
tags: []
title: Exponential Family
understanding: 0
uses:
- probability-theory
- sufficient-statistics
---

## Definition
$$p(x \mid \theta) = h(x)\,\exp\big(\langle \theta, \phi(x)\rangle - A(\theta)\big)$$

The exponential family is the class of distributions whose density factors into a base measure $h(x)$, an inner product between natural parameters $\theta$ and sufficient statistics $\phi(x)$, and a log-partition normalizer $A(\theta)$.

### Members and natural parameters
Most "named" distributions — Gaussian, Bernoulli, Binomial, Beta, Gamma, Dirichlet, Poisson — are exponential-family members, unified under one form. For the univariate Gaussian, $\phi(x)=[x, x^2]^\top$ with natural parameters $\theta=[\mu/\sigma^2,\ -1/(2\sigma^2)]^\top$; for the Bernoulli, $\phi(x)=x$ and $\theta=\log\frac{\mu}{1-\mu}$ (the logit), whose inverse $\mu=\sigma(\theta)$ is the sigmoid.

### Why it matters
The exponential family is the unique class admitting **finite-dimensional sufficient statistics** under i.i.d. sampling (Pitman–Koopman–Darmois): no matter how much data you collect, $\phi(x)$ of fixed dimension summarizes it. This yields the three desiderata for tractable modeling — closure under Bayesian updating, bounded parameter count, and well-behaved estimation. Critically, **every exponential-family likelihood has a conjugate prior** of matching form, which is why conjugate pairs (Beta–Bernoulli, Gaussian–Gaussian, Dirichlet–Multinomial) exist. This structure underpins generalized linear models, variational inference, and much of probabilistic ML.

### Connections
- [[beta-distribution]] — analogous-to
- [[conjugate-prior]] — analogous-to
- [[sufficient-statistics]] — uses
- [[gaussian-distribution]] — generalizes
- [[probability-theory]] — uses
The form is exactly the $g_\theta(\phi(x))$ piece of the Fisher–Neyman factorization, tying the family directly to sufficient statistics.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]