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
id: pkis:technique:masked-language-modeling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch24
tags:
- nlp
- pretraining
- bidirectional
- self-supervised
- bert
title: Masked Language Modeling
understanding: 0
---

## Definition
A self-supervised pretraining objective in which random tokens of an input sentence are hidden (masked) and a deep bidirectional model (transformer or RNN) is trained to predict the masked tokens from both left and right context. For 'The river [MASK] five feet' the model must recover 'rose'. Unlike a standard left-to-right language model, an MLM conditions each prediction on context from both directions jointly (rather than concatenating separately-trained left-to-right and right-to-left models, which cannot combine bidirectional evidence). The objective requires no labeled data, since each sentence supplies its own labels, and a sentence can be reused with different tokens masked. Pretrained MLM representations (notably BERT, Devlin et al. 2018) transfer to question answering, named entity recognition, classification, sentiment analysis, and natural language inference after fine-tuning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]