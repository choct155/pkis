---
aliases: []
also_type: []
applies:
- convolutional-neural-networks
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
- deep-learning
- regularization
id: pkis:concept:parameter-sharing
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch07
specializes:
- regularization
tags:
- parameter-sharing
- convolutional
- regularization
- translation-invariance
- weight-tying
title: Parameter Sharing
understanding: 0
uses:
- inductive-bias
---

## Definition
A model design constraint that forces multiple components of a model (e.g., different spatial locations in a CNN, different time steps in an RNN) to use an identical parameter vector, so that the effective number of free parameters is far smaller than the total number of connections.

Parameter sharing encodes the prior that certain statistics are invariant (e.g., translation invariance in images) and dramatically reduces memory and sample complexity.

### Why it matters
Parameter sharing is the mechanism behind convolutional neural networks and recurrent neural networks. It differs from **parameter tying** (which only penalizes parameter differences via a norm) in that parameters are literally equal, not just encouraged to be close. This halves the memory footprint proportionally and enables learning with far less data by pooling statistical strength across positions or time steps.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[inductive-bias]] — uses
- [[convolutional-neural-networks]] — applies
- [[regularization]] — specializes
[To be populated during integration]