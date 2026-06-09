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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- deep-learning
id: pkis:technique:bidirectional-rnn
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch24
tags:
- nlp
- rnn
- sequence-modeling
- context
title: Bidirectional RNN
understanding: 0
---

## Definition
A recurrent architecture that runs two RNNs over the input, one left-to-right and one right-to-left, and combines their hidden states (usually by concatenation) so that the representation of each position incorporates both preceding and following context. Motivated by tasks where future context disambiguates the present token: in coreference resolution the antecedent of 'him' depends on how the sentence ends, and POS tagging benefits from words to the right. Eye-tracking shows human readers also do not proceed strictly left-to-right. Used for POS tagging, coreference, and as the bidirectional backbone for masked-language-model pretraining; contrast with unidirectional models used for next-word language modeling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]