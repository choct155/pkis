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
id: pkis:concept:marginalization
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch24
tags:
- bayesian-inference
- nuisance-parameters
- integration
- posterior
- probability
title: Marginalization
understanding: 0
---

## Definition
Marginalization is the operation of removing an unwanted (nuisance) variable from a joint distribution by summing or integrating over all of its possible values, leaving a distribution over only the variables of interest. For a joint posterior over a parameter of interest $\theta$ and a nuisance parameter $\phi$,

$$P(\theta \mid D) = \int P(\theta, \phi \mid D)\, d\phi = \int P(\theta \mid \phi, D)\, P(\phi \mid D)\, d\phi,$$

with the integral replaced by a sum when $\phi$ is discrete. The result is the *marginal* posterior of $\theta$ that correctly propagates uncertainty about $\phi$ instead of fixing $\phi$ at a point estimate.

### Marginalization vs. maximization

Marginalization is the principled Bayesian alternative to maximization. To answer 'given the data, what is $\theta$?' when a parameter $\phi$ is irrelevant, one does not maximize over $\phi$ (which discards uncertainty and can be basis-dependent); one integrates it out. MacKay's $\sigma_N$ vs. $\sigma_{N-1}$ example illustrates this: maximizing the joint likelihood over $\mu$ gives the biased $\sigma_N$, whereas marginalizing over $\mu$ introduces an Occam/volume factor that shifts the most probable $\sigma$ to the unbiased $\sigma_{N-1} = \sqrt{S/(N-1)}$. The denominator $N-1$ counts the effective noise measurements after one degree of freedom is absorbed by estimating $\mu$.

### Exact vs. approximate

Marginalization can be performed exactly only in special cases: continuous nuisance parameters with conjugate or Gaussian structure (closed-form integrals), or discrete variables with factorizable structure (message-passing). Otherwise it is the hard, intractable core of inference, motivating approximate methods such as Laplace's approximation, variational inference, and Monte Carlo.

### Why it matters

Marginalization is the engine of Bayesian inference: every probabilistic question reduces to forming a joint distribution and integrating away everything not asked about. It is also the source of automatic Occam factors and unbiased estimates, and the central computational bottleneck that the rest of probabilistic modelling works to overcome.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]