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
- statistical-learning
id: pkis:principle:maxima-are-atypical
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch22
tags:
- overfitting
- maximum-likelihood
- map
- typical-set
- curse-of-dimensionality
- basis-dependence
title: Maxima Are Atypical (Pitfalls of ML and MAP)
understanding: 0
---

## Definition
**Maximizing a probability density is a poor way to summarize it.** In high dimensions the point of maximum density is unrepresentative of where the probability *mass* lives — most mass sits in a thin typical-set shell far from the mode. Three concrete failures of point estimation follow.

### Likelihood spikes and overfitting
Maximum likelihood can diverge: in a Gaussian mixture, place one component on a single data point and let its variance $\sigma_k^2\to0$, and the likelihood grows without bound. These spikes have enormous density but negligible *mass* (they occupy a vanishing volume of parameter space), so they are inferentially worthless — the signature of **overfitting**. Hence ML is not a satisfactory general solution to data modelling.

### MAP does not rescue it
Maximizing the Bayesian posterior instead inherits the same pathology: the posterior density also has spikes, and its mode is unrepresentative. In a superposition of Gaussians of differing widths, the density peak sits near the *narrowest* component, not the heaviest — by factors like $\exp(0.01k)$ in $k$ dimensions.

### MAP is basis-dependent
Under a reparameterization $u=f(\theta)$, the density transforms by a Jacobian $P(u)=P(\theta)\,|\partial\theta/\partial u|$, so the location of the maximum *moves*. An inference method whose answer changes with the choice of coordinates is suspect.

### Why it matters
These observations motivate the Bayesian programme of integrating over (marginalizing) the posterior rather than optimizing it, and they explain why naive ML/MAP break down exactly in the high-dimensional, ill-posed problems where good inference matters most.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]