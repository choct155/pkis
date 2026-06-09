---
aliases: []
also_type: []
applies:
- sequence-to-sequence-model
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
id: pkis:technique:beam-search-decoding
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch24
tags:
- nlp
- decoding
- search
- machine-translation
title: Beam Search Decoding
understanding: 0
---

## Definition
An approximate search procedure for generating the highest-probability output sequence from a conditional sequence model, where the true objective is to maximize the probability of the whole sequence rather than each token greedily. Greedy decoding picks the single most probable token at each step and commits irrevocably, so it cannot recover from early mistakes (e.g. emitting 'entrada' before 'puerta' in Spanish word order). Beam search instead keeps the top k partial hypotheses at each step, extends each by the top k next tokens, and retains the best k of the resulting k^2 candidates; it terminates when all beams emit the <end> token and outputs the highest-scoring sequence. As neural models grow more accurate, smaller beams suffice: modern neural MT uses beam width 4-8 versus 100+ for older statistical systems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sequence-to-sequence-model]] — applies
[To be populated during integration]