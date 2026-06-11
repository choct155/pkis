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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:concept:class-confusion-matrix
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch05
tags:
- evaluation
- binary-classification
- TPR
- FPR
- precision
- recall
title: Class Confusion Matrix
understanding: 0
---

## Definition
A $C\times C$ matrix $\mathbf{C}$ where entry $C_{ij}$ counts the number of examples with true label $i$ predicted as label $j$. For binary classification the four cells are $\{TN, FP, FN, TP\}$. Row-normalising gives $p(\hat{y}|y)$, yielding **sensitivity/recall/TPR** and **specificity/TNR**. Column-normalising gives $p(y|\hat{y})$, yielding **precision/PPV** and **NPV**.

### Why it matters
All standard binary classification metrics — accuracy, TPR, FPR, FDR, F-score, ROC/AUC — are derived from the confusion matrix. It is the single canonical representation of a classifier's per-class performance at a fixed decision threshold, making it the natural starting point for cost-sensitive analysis and for detecting class-specific failure modes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]