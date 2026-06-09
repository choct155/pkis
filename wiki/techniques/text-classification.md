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
- statistical-learning
id: pkis:technique:text-classification
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
tags:
- nlp
- classification
- naive-bayes
- feature-engineering
title: Text Classification
understanding: 0
uses:
- bag-of-words-model
- logistic-regression
---

## Definition
The task of assigning a text to one of a set of predefined categories -- newspaper sections, spam vs non-spam, positive vs negative sentiment, author attribution, language identification. The text is represented as a typically large and sparse feature vector whose entries are word counts (or Boolean presence) over the vocabulary, optionally augmented with non-lexical features (sender, time, subject words, punctuation, uppercase percentage, attachments). Feature selection -- dropping very rare words (high variance) and ubiquitous non-discriminative words like 'the' -- often improves accuracy. Classifiers range from naive Bayes (bag-of-words) through logistic regression, SVMs, and neural networks; character-level models are well suited to language identification and short-string typing (drug name vs person name vs city name). Reported accuracies are high (e.g. 95-98%+ on Reuters categories), and simple linear classifiers often match more complex ones at lower cost.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[logistic-regression]] — uses
- [[bag-of-words-model]] — uses
[To be populated during integration]