---
aliases: []
also_type: []
applies:
- structural-breaks
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- time-series
id: pkis:technique:bayesian-online-changepoint-detection
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch29
tags:
- changepoint-detection
- online-learning
- Bayesian
- run-length
- time-series
title: Bayesian Online Changepoint Detection (BOCPD)
understanding: 0
uses:
- hidden-semi-markov-model
- particle-filter
- conjugate-prior
---

## Definition
An exact online algorithm for inferring the posterior distribution over the current run length $r_t$ (time since last changepoint) in a sequential data stream:

$$p(r_t \mid y_{1:t}) \propto p(y_t \mid y_{1:t-1}, r_t)\, p(r_t \mid y_{1:t-1})$$

where the prior predictive propagates as $p(r_t \mid y_{1:t-1}) = \sum_{r_{t-1}} p(r_t \mid r_{t-1})\, p(r_{t-1} \mid y_{1:t-1})$ and the hazard function $H(\tau) = p_g(\tau) / \sum_{t=\tau}^{\infty} p_g(t)$ controls changepoint probability. Each update costs $O(t)$, giving $O(T^2)$ overall; particle filtering reduces this to $O(TN)$.

### Why it matters
BOCPD (Adams & MacKay 2007, Fearnhead & Liu 2007) provides a principled Bayesian treatment of changepoint detection that naturally quantifies uncertainty, supports online updating, and integrates conjugate-exponential segment models for closed-form marginal likelihoods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[structural-breaks]] — applies
- [[conjugate-prior]] — uses
- [[particle-filter]] — uses
- [[hidden-semi-markov-model]] — uses
[To be populated during integration]