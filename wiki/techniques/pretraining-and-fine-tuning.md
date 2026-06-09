---
aliases: []
also_type: []
applies:
- contextual-word-embeddings
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
id: pkis:technique:pretraining-and-fine-tuning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch24
specializes:
- transfer-learning
tags:
- nlp
- transfer-learning
- pretraining
- self-supervised
title: Pretraining and Fine-Tuning
understanding: 0
uses:
- masked-language-modeling
---

## Definition
A form of transfer learning in which a model is first trained on a large amount of general-domain (typically unlabeled) data to acquire broadly useful representations, then refined on a smaller amount of domain- or task-specific data. For NLP this exploits the abundance of unlabeled text (the Internet adds over 100 billion words/day; Common Crawl, Wikipedia) versus the cost of annotation. The progression ran from static embeddings (word2vec 2013, GloVe 2014) to pretrained contextual transformer models (BERT, GPT-2, RoBERTa, T5) after GPU/TPU hardware made them feasible; since 2018 new NLP projects typically start from a downloaded pretrained transformer and fine-tune. Declared 'NLP's ImageNet moment' (Ruder 2018), paralleling the 2012 computer-vision turning point. More training data reliably yields better models (RoBERTa on 2.2 trillion words). Frameworks such as ULMFiT ease fine-tuning without a large target corpus.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[contextual-word-embeddings]] — applies
- [[masked-language-modeling]] — uses
- [[transfer-learning]] — specializes
[To be populated during integration]