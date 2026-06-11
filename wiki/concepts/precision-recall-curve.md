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
- information-retrieval
- statistics
id: pkis:concept:precision-recall-curve
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch05
tags:
- precision
- recall
- F-score
- evaluation
- class-imbalance
- mAP
title: Precision–Recall Curve
understanding: 0
---

## Definition
For a binary classifier parameterised by threshold $\tau$, define:

$$\mathcal{P}(\tau) = \frac{TP_\tau}{TP_\tau + FP_\tau}, \qquad \mathcal{R}(\tau) = \frac{TP_\tau}{TP_\tau + FN_\tau}$$

The **precision–recall (PR) curve** traces $(\mathcal{R}(\tau), \mathcal{P}(\tau))$ as $\tau$ varies. Summary scalars include the **area under the PR curve** (AP) and the **mean average precision** (mAP) averaged over multiple retrieval queries.

### Why it matters
Unlike the ROC curve, precision is sensitive to class imbalance: $\text{Prec} = TPR / (TPR + FPR/r)$ where $r = P/N$, so performance comparisons across datasets with different prevalences require care. PR curves are preferred whenever the concept of a "true negative" is ill-defined or dataset-dependent (e.g., object detection, information retrieval), and when the positive class is rare.

### F-score connection
The $F_\beta$ score, the weighted harmonic mean of precision and recall, summarises a single operating point. $F_1 = 2\mathcal{P}\mathcal{R}/(\mathcal{P}+\mathcal{R})$ is the harmonic (not arithmetic) mean, which is more conservative and forces *both* quantities to be high.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]