---
aliases: []
also_type: []
analogous-to:
- false-discovery-rate
applies:
- hypothesis-testing
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- receiver-operating-characteristic-curve
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- evaluation
id: pkis:concept:precision-recall-f-score
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch11
tags:
- evaluation
- classification
- imbalanced-data
- PR-curve
- F1
title: Precision, Recall, and F-Score
understanding: 0
---

## Definition
For a binary classifier predicting a rare positive event, **precision** $p$ is the fraction of predicted positives that are true positives, **recall** $r$ is the fraction of true positives that are detected, and the **F-score** (harmonic mean) is

$$F = \frac{2pr}{p + r}.$$

A PR curve plots precision vs. recall as the decision threshold varies, and summarises the accuracy–coverage tradeoff without being dominated by the majority class.

### Why it matters
Accuracy is misleading on imbalanced datasets (e.g., a disease affecting 1-in-a-million people gives 99.9999% accuracy by always predicting negative). Precision, recall, and F-score remain informative regardless of class imbalance, making them the standard evaluation protocol for detection and retrieval tasks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hypothesis-testing]] — applies
- [[false-discovery-rate]] — analogous-to: Precision = 1 - FDR; both measure the reliability of reported positives
- [[receiver-operating-characteristic-curve]] — contrasts-with: PR curves are preferred over ROC curves for imbalanced datasets where the negative class dominates
[To be populated during integration]