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
id: pkis:technique:part-of-speech-tagging
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
tags:
- nlp
- sequence-labeling
- hmm
- logistic-regression
- penn-treebank
title: Part-of-Speech Tagging
understanding: 0
---

## Definition
The task of assigning each word in a sentence its part of speech (lexical category / tag): noun, verb, adjective, preposition, determiner, and so on. Tag sets vary; the Penn Treebank uses 45 tags over a 3-million-word annotated corpus. POS tagging is rarely an end in itself but is a useful first step for question answering, translation, and even text-to-speech (the noun 'record' is pronounced unlike the verb 'record'). Two classic model families: (1) a hidden Markov model treats words as observations and tags as hidden states, using a transition model P(C_t | C_{t-1}) and sensor model P(W_t | C_t) estimated by smoothed corpus counts, with the Viterbi algorithm recovering the most probable tag sequence (~97% accuracy); (2) a discriminative logistic-regression tagger (one model per tag) uses rich hand-crafted binary features (word identity, suffixes like '-ous'/'-ly', prefixes, capitalization, neighboring words/tags) and is run as a sequence via greedy, beam, or Viterbi-style search. The HMM's weakness -- everything must be expressed in the transition and sensor models -- is exactly what feature-based logistic regression overcomes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]