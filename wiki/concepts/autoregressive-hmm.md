---
aliases: []
also_type: []
applies:
- structural-breaks
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
- machine-learning
- statistics
- time-series
- econometrics
extends:
- hidden-markov-model
id: pkis:concept:autoregressive-hmm
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch29
specializes:
- state-space-model
tags:
- HMM
- autoregressive
- regime-switching
- time-series
title: Autoregressive HMM (AR-HMM)
understanding: 0
uses:
- autoregressive-model
---

## Definition
An HMM in which the observation at time $t$ depends on both the current hidden state $z_t$ and the previous observation $y_{t-1}$ (or the last $L$ observations):

$$p(y_t \mid y_{t-L:t-1}, z_t = j, \theta) = \mathcal{N}\!\left(y_t \,\Big|\, \sum_{\ell=1}^L W_{j,\ell}\, y_{t-\ell} + \mu_j,\, \Sigma_j\right)$$

This model combines two Markov chains: one on hidden variables (capturing long-range regime switches) and one on observations (capturing short-range autocorrelation). In econometrics this is known as a **Markov regime-switching model**.

### Why it matters
AR-HMMs overcome the conditional independence assumption of standard HMMs, allowing the model to capture both discrete regime changes and continuous within-regime dynamics. Because the visible nodes are observed, adding direct observation-to-observation arcs does not complicate posterior inference over hidden states.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[state-space-model]] — specializes
- [[structural-breaks]] — applies
- [[autoregressive-model]] — uses
- [[hidden-markov-model]] — extends
[To be populated during integration]