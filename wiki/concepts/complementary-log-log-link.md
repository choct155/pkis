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
contrasts-with:
- probit-model
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
id: pkis:concept:complementary-log-log-link
instantiates:
- generalized-linear-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch12
- murphy-pml2-advanced-ch15
specializes:
- link-function-mean-function
- link-function
tags:
- GLM
- link-function
- binary-response
- Gumbel
- survival-analysis
title: Complementary Log-Log Link
understanding: 0
uses:
- poisson-regression
---

## Definition
$$\ell(\mu) = \log(-\log(1-\mu)) \qquad (\text{cloglog link})$$

The complementary log-log (cloglog) link maps $\mu \in (0,1)$ to $\mathbb{R}$ via the inverse of the Gumbel CDF. It arises naturally when binary observations indicate whether at least one Poisson event occurred: if events follow $\operatorname{Poi}(\lambda)$, then $p(y=0) = e^{-\lambda}$, so $1-\mu = e^{-e^\eta}$ and $\eta = \log(-\log(1-\mu))$.

### Why it matters
Unlike the symmetric logit and probit links, the cloglog is **asymmetric**: the approach to 0 and 1 occurs at different rates. It is preferred when the probability of the event is high or when the underlying data-generating process has a Poisson-event structure (e.g. disease incidence, failure-time grouped data). It is the discrete-time analog of the complementary log-log hazard model in survival analysis.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[link-function]] — specializes
- [[poisson-regression]] — uses
- [[generalized-linear-model]] — instantiates
- [[probit-model]] — contrasts-with: Both are non-canonical binary links but cloglog is asymmetric
- [[link-function-mean-function]] — specializes
[To be populated during integration]