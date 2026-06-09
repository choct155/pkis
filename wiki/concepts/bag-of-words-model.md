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
- statistical-learning
id: pkis:concept:bag-of-words-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
tags:
- nlp
- naive-bayes
- text-classification
- generative-model
title: Bag-of-Words Model
understanding: 0
---

## Definition
A generative language model that applies naive Bayes to a string of words, P(Class | w_{1:N}) = alpha P(Class) prod_j P(w_j | Class), treating a sentence as an unordered multiset drawn from a class-specific 'bag' of words (draw a bag for the category, then draw words with replacement until an end-of-sentence marker). It is a unigram model: it falsely assumes each word is independent of the others and therefore cannot generate coherent sentences, yet it supports accurate classification because discriminative words ('stocks', 'earnings' vs 'rain', 'cloudy') carry strong category evidence. Its central limitation -- ignoring word order -- means it cannot distinguish 'first quarter earnings report' (business) from 'fourth quarter touchdown passes' (sports) by their shared word 'quarter'; this motivates order-sensitive n-gram models. The name derives from Harris's (1954) remark that 'language is not merely a bag of words.'

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]