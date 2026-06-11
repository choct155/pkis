---
aliases: []
also_type: []
analogous-to:
- law-of-total-variance
applies:
- mixture-models
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
- statistics
id: pkis:concept:law-of-total-expectation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- em-algorithm
related_concepts: []
sources:
- murphy-pml1-intro-ch02
tags:
- expectation
- conditional-expectation
- tower-property
- iterated-expectation
title: Law of Total Expectation (Iterated Expectations)
understanding: 0
uses:
- probability-theory
- conditional-independence
- sum-rule
---

## Definition
$$\mathbb{E}[X] = \mathbb{E}_Y\!\left[\mathbb{E}[X|Y]\right] = \sum_y \mathbb{E}[X|Y=y]\,p(Y=y)$$

The **law of total expectation** (also called the law of iterated expectations or tower property) states that the unconditional mean of $X$ equals the expectation over $Y$ of the conditional mean of $X$ given $Y$. It follows from summing/integrating the conditional expectation against the marginal of $Y$.

### Why it matters
This law is the expectation analogue of the sum rule of probability and is used throughout probability, statistics, and ML. It underlies the bias decomposition of estimators, the derivation of the EM algorithm (where the E-step computes a conditional expectation), the law of total variance, and variance-reduction techniques in Monte Carlo estimation such as Rao-Blackwellization.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mixture-models]] — applies
- [[sum-rule]] — uses
- [[conditional-independence]] — uses
- [[em-algorithm]] — prerequisite-of
- [[law-of-total-variance]] — analogous-to
- [[probability-theory]] — uses
[To be populated during integration]