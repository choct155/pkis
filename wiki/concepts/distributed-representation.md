---
aliases: []
also_type: []
applies:
- representation-learning
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
- curse-of-dimensionality
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- cognitive-science
extends:
- smoothness-assumption-ml
generalizes:
- word-embeddings
- contextual-word-embeddings
id: pkis:concept:distributed-representation
instantiates:
- connectionism
- inductive-priors-representation-learning
- restricted-boltzmann-machine
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch01
- goodfellow-deeplearning-ch15
- goodfellow-deeplearning-ch16
tags:
- connectionism
- embeddings
- expressivity
- neural-networks
title: Distributed Representation
understanding: 0
uses:
- exponential-regions-distributed-representation
- neural-networks
- latent-variable-models
---

## Definition
A distributed representation encodes information such that **each input is represented by many features simultaneously, and each feature participates in the representation of many inputs**.

Contrast with a *local* (one-hot / grandmother-cell) representation where a single unit fires for a single concept. With $k$ binary features, a distributed representation can distinguish up to $2^k$ inputs, exponentially more than the $k$ inputs a local representation can distinguish with the same number of units.

### Why it matters
Distributed representations are exponentially more expressive per parameter than local ones, and they enable systematic generalization: a unit encoding *redness* can learn from red cars, red birds, and red trucks simultaneously rather than from one category in isolation.

### Historical note
Introduced prominently by Hinton, McClelland & Rumelhart (1986) during the connectionist wave; it is a foundational motivation for using neural network embeddings throughout modern deep learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[representation-learning]] — applies: representation-learning is implicitly present in several existing nodes
- [[restricted-boltzmann-machine]] — instantiates
- [[latent-variable-models]] — uses
- [[smoothness-assumption-ml]] — extends: Distributed representations extend beyond smoothness to achieve exponential generalisation
- [[curse-of-dimensionality]] — contrasts-with
- [[inductive-priors-representation-learning]] — instantiates
- [[neural-networks]] — uses
- [[exponential-regions-distributed-representation]] — uses
- [[contextual-word-embeddings]] — generalizes
- [[word-embeddings]] — generalizes: Word embeddings are distributed representations of words.
- [[connectionism]] — instantiates: Distributed representation was a central concept introduced in the connectionist movement.
[To be populated during integration]