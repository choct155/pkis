---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- probabilistic-modeling
- generative-models
id: pkis:framework:autoregressive-model-arm
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch22
tags:
- autoregressive
- generative-model
- chain-rule
- sequential-data
- density-estimation
title: Autoregressive Model (ARM)
understanding: 0
---

## Definition
$$p(x_{1:T}) = \prod_{t=1}^{T} p(x_t \mid x_{1:t-1})$$

An autoregressive model (ARM) factorises any joint distribution over $T$ variables via the chain rule of probability, expressing each variable as a conditional distribution over all preceding variables in a fixed ordering. It corresponds to a fully connected DAG where each node depends on all its predecessors.

### Why it matters
ARMs provide an exact, tractable likelihood for sequential data without requiring latent variables, making training straightforward via maximum likelihood. They unify a large family of generative models — from simple Markov chains to transformers — under one principle, but share the common cost of sequential (slow) sampling and no compact latent representation.

### Trade-offs
- **Pros**: exact log-likelihood evaluation, no posterior inference required, applies to any discrete or continuous domain.
- **Cons**: autoregressive sampling is inherently sequential ($O(T)$ steps); conditioning on all past context grows increasingly complex without architectural constraints.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]