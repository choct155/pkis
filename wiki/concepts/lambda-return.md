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
- optimization
- deep-learning
id: pkis:concept:lambda-return
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch12
tags:
- reinforcement-learning
- temporal-difference
- bootstrapping
title: Lambda-Return
understanding: 0
---

## Definition
A compound update target that averages all n-step returns, each weighted proportionally to lambda^{n-1} and normalized by (1 - lambda) so the weights sum to one: G_t^lambda = (1-lambda) * sum_{n>=1} lambda^{n-1} G_{t:t+n}. The one-step return receives the largest weight (1-lambda), with the weighting fading by a factor of lambda per additional step; after termination the residual weight falls on the conventional return G_t. At lambda=0 the lambda-return reduces to the one-step return (TD), and at lambda=1 it reduces to the full Monte Carlo return, giving a smooth, exponentially-weighted way to interpolate between TD and Monte Carlo. It is the forward-view target underlying the off-line lambda-return algorithm, the online lambda-return algorithm, and (approximately) TD(lambda). The truncated lambda-return G_{t:h}^lambda replaces the time of termination T with a finite horizon h, enabling practical online algorithms.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]