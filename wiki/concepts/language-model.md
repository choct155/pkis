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
- information-theory
id: pkis:concept:language-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
tags:
- nlp
- probabilistic-model
- language
title: Language Model
understanding: 0
---

## Definition
A probability distribution over strings of a natural language, assigning to any word sequence its likelihood of occurring. Because natural language admits no crisp Boolean grammaticality boundary (judgments vary across speakers and time, and sentences are ambiguous and vague), a language model replaces the binary grammatical/ungrammatical distinction with a graded probability: 'Do I dare disturb the universe?' receives a reasonable probability while 'Universe dare the I disturb do?' receives a negligible one. With a single model one can predict likely next words (text/email completion), score candidate corrections (spelling, grammar), and rank interpretations; with a pair of models one can compute the most probable translation; with question/answer training pairs one can compute the most likely answer. Any language model is at best an approximation ('All grammars leak' -- Sapir), but even clearly-wrong models are useful, and the language-modeling task itself serves as a common benchmark for progress in language understanding.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]