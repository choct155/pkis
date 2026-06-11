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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability-theory
- bayesian-statistics
extends:
- exchangeability
- de-finetti-coherence
id: pkis:concept:de-finetti-exchangeability
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
tags:
- de-finetti
- exchangeability
- bayesian-foundations
- iid
- prior
title: Exchangeability (de Finetti)
understanding: 0
uses:
- bayesian-inference
- conjugate-prior
---

## Definition
A sequence of random variables $(x_1,x_2,\ldots)$ is **infinitely exchangeable** if for every $n$ and every permutation $\pi$:
$$p(x_1,\ldots,x_n)=p(x_{\pi_1},\ldots,x_{\pi_n})$$

**De Finetti's theorem** states that an infinite sequence is exchangeable *if and only if* there exists a random variable $\theta$ (possibly infinite-dimensional) and a distribution $p(\theta)$ such that
$$p(x_1,\ldots,x_n)=\int\prod_{i=1}^n p(x_i|\theta)\,p(\theta)\,d\theta$$
i.e., the observations are i.i.d. conditionally on $\theta$.

Exchangeability generalises i.i.d.: an i.i.d. sequence is exchangeable, but not vice versa — correlated observations sharing a latent cause are exchangeable but not i.i.d.

### Why it matters
De Finetti's theorem provides a *logical foundation* for Bayesian inference: if we believe our data sequence is exchangeable (a weak, observable symmetry condition), then the Bayesian model — prior $p(\theta)$, likelihood $p(x|\theta)$, posterior $p(\theta|D)$ — follows as a mathematical necessity, not an arbitrary modelling choice.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[de-finetti-coherence]] — extends
- [[conjugate-prior]] — uses
- [[bayesian-inference]] — uses
- [[exchangeability]] — extends: Existing node on exchangeability; de Finetti's theorem is the representation result
[To be populated during integration]