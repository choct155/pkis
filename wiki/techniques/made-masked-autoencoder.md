---
aliases: []
also_type: []
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
- machine-learning
- deep-learning
- density-estimation
extends:
- autoencoder
id: pkis:technique:made-masked-autoencoder
instantiates:
- autoregressive-model-arm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch22
tags:
- MADE
- masking
- autoregressive
- autoencoder
- density-estimation
- neural-network
title: MADE (Masked Autoencoder for Density Estimation)
understanding: 0
---

## Definition
MADE implements an autoregressive density estimator using a single autoencoder network in which connection weights are **masked** so that output $\hat{x}_t$ depends only on inputs $x_{1:t-1}$. Formally, a mask matrix $M^W$ applied element-wise to weight matrix $W$ enforces the autoregressive property:
$$\tilde{W} = M^W \odot W, \quad \text{where } M^W_{d',d} = 0 \text{ if } d' \geq d.$$
This turns $T$ separate networks into a single efficient forward pass, reducing compute from $O(T)$ to $O(1)$ network evaluations.

### Why it matters
MADE enables exact autoregressive likelihood computation at the cost of a single forward pass, making it vastly more efficient than training $T$ independent networks. It is the architectural backbone of many modern autoregressive models and can be used with arbitrary orderings via random masking at training time.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[autoregressive-model-arm]] — instantiates
- [[autoencoder]] — extends: MADE is an autoencoder with masked weights enforcing the autoregressive property
[To be populated during integration]