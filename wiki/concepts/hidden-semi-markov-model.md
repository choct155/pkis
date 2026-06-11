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
- machine-learning
- statistics
- time-series
extends:
- hidden-markov-model
id: pkis:concept:hidden-semi-markov-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch29
specializes:
- generalized-semi-markov-process
tags:
- HMM
- duration-modeling
- segmentation
- semi-Markov
title: Hidden Semi-Markov Model (HSMM)
understanding: 0
uses:
- bayesian-online-changepoint-detection
---

## Definition
An extension of the HMM in which the duration $d_t$ spent in each state is modeled explicitly rather than implicitly through geometric self-transition probabilities. When entering state $j$, a duration is sampled from a state-specific distribution $D_j(\cdot)$; the state is then held fixed while the counter counts down:

$$p(d_t = d' \mid d_{t-1} = d, z_t = j) = \begin{cases} D_j(d') & \text{if } d = 1 \\ 1 & \text{if } d' = d - 1,\, d > 1 \\ 0 & \text{otherwise} \end{cases}$$

Inference takes $O(TK^2 + TKD)$ time where $D$ is the maximum duration. A **segmental HMM** variant uses a segment-level likelihood $p(y_{s_i:e_i} \mid z_{s_i}, d_{s_i})$ instead of per-step likelihoods.

### Why it matters
Standard HMMs impose geometric sojourn-time distributions, which is unrealistic in many domains (speech, biological sequences, activity recognition). HSMMs allow arbitrary parametric or nonparametric duration distributions, enabling far more accurate modeling of segment lengths.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-online-changepoint-detection]] — uses
- [[generalized-semi-markov-process]] — specializes
- [[hidden-markov-model]] — extends
[To be populated during integration]