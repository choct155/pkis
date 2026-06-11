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
- kalman-rts-smoother
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- signal-processing
- machine-learning
- statistics
extends:
- bayes-filter
id: pkis:concept:fixed-lag-smoothing
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch08
tags:
- smoothing
- online-inference
- latency
- state-estimation
title: Fixed Lag Smoothing
understanding: 0
---

## Definition
$$p(\mathbf{z}_{t-\ell}|\mathbf{y}_{1:t}), \quad \ell > 0$$

A compromise between online filtering and offline smoothing: infer the latent state $\ell$ steps in the past given observations up to the current time $t$. The lag $\ell$ controls the accuracy–latency trade-off — larger $\ell$ gives lower posterior uncertainty at the cost of higher delay.

### Why it matters
Fixed-lag smoothing is practically important in real-time applications (e.g., speech enhancement, financial time-series) where some delay is acceptable but full offline processing is not. It naturally interpolates between the Bayes filter ($\ell=0$) and full fixed-interval smoothing ($\ell=T$).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayes-filter]] — extends
- [[kalman-rts-smoother]] — contrasts-with
[To be populated during integration]