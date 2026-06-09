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
- statistical-learning
id: pkis:concept:receiver-operating-characteristic-curve
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch09
tags:
- classification-evaluation
- decision-threshold
title: ROC Curve, Sensitivity and Specificity
understanding: 0
---

## Definition
Tools for summarizing the threshold-dependent performance of a binary classifier. Sensitivity is the probability of predicting the positive class (e.g. disease/spam) given the true state is positive (true positive rate); specificity is the probability of predicting the negative class given the true state is negative (true negative rate). Because a classifier converts a continuous score or class probability into a decision via a threshold (the Bayes rule classifies to class 1 when its probability exceeds L_01/(L_01+L_10), set by the misclassification-loss ratio), sensitivity and specificity trade off against each other as the threshold/loss varies. The receiver operating characteristic (ROC) curve plots sensitivity against specificity (or against 1-specificity) as the threshold sweeps across its range, giving a loss-free comparison of rules; a uniformly higher curve dominates. The area under the ROC curve (AUC), also called the c-statistic, is a common scalar summary and equals the Mann-Whitney U / Wilcoxon rank-sum statistic for the score separation between the two groups. Caveat: AUC can be insensitive to an added predictor that is highly significant by deviance, so per-sample reclassification is often more informative.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]