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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:concept:beta-binomial-distribution
instantiates:
- overdispersion
- mixture-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch17
tags:
- proportion-data
- overdispersion
- mixture
- binomial
title: Beta-Binomial Distribution
understanding: 0
uses:
- beta-distribution
---

## Definition
A robust, overdispersed alternative to the binomial: a **beta mixture of binomials**, $\text{Beta-bin}(m,\alpha,\beta)$. Each observation is binomial with a common number of trials $m$ but an individual success probability $\pi_i$ drawn from a $\text{Beta}(\alpha,\beta)$ distribution, so probabilities vary across units (e.g. test-takers differing in skill in educational testing). With mean probability $\alpha/(\alpha+\beta)$, its variance exceeds that of the binomial with the same probability by a factor $(\alpha+\beta+m)/(\alpha+\beta+1)$. It overcomes the binomial's limitation of having a single free parameter (mean determines variance). When $m=1$ a single trial carries no information to distinguish beta from binomial variation, and the two models have equal variance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[beta-distribution]] — uses: success probabilities follow a Beta(alpha,beta)
- [[mixture-models]] — instantiates: beta mixture of binomials
- [[overdispersion]] — instantiates: canonical overdispersed alternative to the binomial
[To be populated during integration]