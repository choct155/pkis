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
- deep-learning
extends:
- word-embeddings
id: pkis:concept:contextual-word-embeddings
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch24
tags:
- nlp
- embeddings
- polysemy
- representations
title: Contextual Word Embeddings
understanding: 0
uses:
- recurrent-neural-network
- bidirectional-rnn
---

## Definition
A representation that maps a word together with its surrounding context to an embedding vector, so that the same word token receives different vectors depending on usage. Motivated by polysemy: a single static embedding cannot simultaneously capture 'rose' the flower and 'rose' the past tense of rise, nor subtler context-dependent shades ('need' in 'you need to see this' vs 'humans need oxygen'). A contextual model (e.g. a left-to-right RNN, or ELMo) takes two inputs at each step, the noncontextual embedding of the current word and an encoding of the prior context, and outputs a context-sensitive vector; the model is typically trained by next-word prediction and then its internal representations are reused for downstream tasks. Contrast with static word embeddings, which assign one fixed vector per word type. Pretrained contextual representations are far more expensive to train than static embeddings but transfer well across NLP tasks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bidirectional-rnn]] — uses
- [[recurrent-neural-network]] — uses
- [[word-embeddings]] — extends
[To be populated during integration]