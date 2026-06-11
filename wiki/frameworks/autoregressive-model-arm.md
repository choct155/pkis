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
generalizes:
- markov-chains
- recurrent-neural-network
- hidden-markov-model
id: pkis:framework:autoregressive-model-arm
instantiates:
- autoregressive-model
- directed-graphical-models
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
uses:
- chain-rule-multivariate
- maximum-likelihood-estimation
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
- [[directed-graphical-models]] — instantiates: ARM corresponds to a fully connected DAG with a fixed variable ordering
- [[maximum-likelihood-estimation]] — uses: ARMs are trained by maximising the exact log-likelihood
- [[hidden-markov-model]] — generalizes: HMM is an ARM where the past is compressed into a stochastic hidden state
- [[recurrent-neural-network]] — generalizes: RNN is an ARM where the past is compressed into a deterministic hidden state
- [[markov-chains]] — generalizes: Markov model is a first-order special case of an ARM
- [[chain-rule-multivariate]] — uses: ARM factorisation directly applies the chain rule of probability
- [[autoregressive-model]] — instantiates: Chapter 22 defines ARMs via the chain rule; autoregressive-model is the existing node for the concept
[To be populated during integration]