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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
id: pkis:technique:platt-scaling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch17
- murphy-pml2-advanced-ch14
tags:
- calibration
- SVM
- probability estimation
- logistic
- post-hoc
title: Platt Scaling
understanding: 0
---

## Definition
Platt scaling converts the real-valued output $f(x)$ of a hard classifier (typically an SVM) into a calibrated probability estimate by fitting a logistic regression:
$$p(y=1|x,a,b) = \sigma(a\,f(x)+b),$$
where scalar parameters $a,b$ are estimated by maximum likelihood on a **held-out validation set** (not the training set, to avoid severe overfitting).

### Why it matters
SVMs do not naturally produce calibrated probabilities; Platt scaling is the standard post-hoc fix. However, because there is no principled reason to interpret the SVM margin as a log-odds, the resulting probabilities can still be poorly calibrated (particularly in regions far from the decision boundary), motivating probabilistic alternatives such as GPs or RVMs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]