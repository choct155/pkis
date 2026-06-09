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
id: pkis:concept:sampling-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch03
tags:
- jaynes
- scientific-inference
- forward-problem
- predictive
title: Sampling Distribution (Direct Probability)
understanding: 0
---

## Definition
A sampling distribution answers the **forward (direct) question**: given a hypothesis $H$ about the phenomenon (e.g. the urn contents $(M,N)$), what is the probability $P(D\mid H)$ of obtaining specified data $D$ (e.g. a sequence or count of red and white balls)? The hypergeometric and binomial distributions are the chapter's examples. Jaynes deliberately replaces the older term 'direct probability' — which carried a connotation of reasoning from physical *cause* to *effect* — with 'sampling distribution' in the neutral sense of *reasoning from a specified hypothesis to potentially observable data, whether the link is logical or causal*, since not every sampling distribution admits a causal reading.

Sampling distributions make predictions; agreement with observation supports $H$, and the nature of any discrepancy guides the search for a better hypothesis — the broad basis of scientific inference, and the seed of significance testing. But Jaynes emphasizes that in virtually all real scientific problems the situation is inverted: the data $D$ are known and $H$ is not, so the goal is the **inverse problem** $P(H\mid D)$, which (unlike the sampling calculation) cannot be answered without prior knowledge $P(H)$. Computing the sampling distribution is then a constant subtask but almost never an end in itself.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]