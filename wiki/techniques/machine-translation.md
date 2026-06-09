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
- knowledge-representation
id: pkis:technique:machine-translation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
tags:
- nlp
- translation
- seq2seq
- transformer
- bilingual-corpus
title: Machine Translation
understanding: 0
---

## Definition
The task of transforming text in one language into another, typically learned from a bilingual corpus of paired (unannotated) documents from which the system learns to align sentences and phrases and then translate novel sentences. Early-2000s n-gram-based systems conveyed meaning but produced syntactic errors in most sentences, limited by short n-gram windows (information could not flow across a long sentence) and by representing everything at the individual-word level (learning 'black cat' -> 'chat noir' but not the rule that adjectives precede nouns in English and follow them in French). Recurrent sequence-to-sequence models (Sutskever et al., 2015) generalized better via word embeddings and compositional multi-level representations; the transformer's attention mechanism (Vaswani et al., 2018) improved performance further, with hybrid models approaching human-level performance on some language pairs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]