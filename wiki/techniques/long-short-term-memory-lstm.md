---
aliases: []
also_type: []
applies:
- vanishing-gradient-problem
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- deep-learning
extends:
- recurrent-neural-network
id: pkis:technique:long-short-term-memory-lstm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch24
tags:
- nlp
- rnn
- gating
- long-range-dependencies
title: Long Short-Term Memory (LSTM)
understanding: 0
---

## Definition
A recurrent architecture with gating units that mitigate the information-degradation and vanishing-gradient problems of plain RNNs across time steps. Rather than imperfectly reproducing its hidden state at each step (the telephone-game failure of standard RNNs), an LSTM can choose to remember some parts of the input, copying them forward unchanged, and to forget others. This lets it carry a latent feature far across a sentence until needed: for 'The athletes, who all won their local qualifiers... now [compete/competes]', an LSTM can preserve the subject's person and number across many intervening words to enforce subject-verb agreement, where a plain RNN or n-gram model gets confused. A state-of-the-art NLP LSTM typically uses around 1024 hidden dimensions. LSTMs still struggle with very long-range context and were largely superseded by transformers for capturing long-distance dependencies in parallel.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[vanishing-gradient-problem]] — applies
- [[recurrent-neural-network]] — extends
[To be populated during integration]