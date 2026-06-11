---
aliases: []
also_type: []
analogous-to:
- k-nearest-neighbors
- ridge-regression
contrasts-with:
- gradient-boosting
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
extends:
- bagging
id: pkis:technique:random-forests
instantiates:
- exploration-exploitation-tradeoff
knowledge_type: technique
maturity: settled
related_concepts:
- '[[ensemble-learning]]'
- '[[bias-variance-tradeoff]]'
sources:
- '[[hastie-esl]]'
specializes:
- ensemble-learning
tags:
- ensemble-methods
title: Random Forests
understanding: 0
uses:
- decision-trees
- bootstrap
- cross-validation
- cart-decision-trees
- feature-importance-tree-ensembles
---

Ensemble of decorrelated decision trees, each trained on a bootstrap sample with random feature subsetting at each split, reducing the between-tree correlation and thus the variance of the ensemble's predictions.

## Connections
- [[exploration-exploitation-tradeoff]] — instantiates: random feature subsampling trades bias for decorrelation
- [[feature-importance-tree-ensembles]] — uses
- [[cart-decision-trees]] — uses
- [[cross-validation]] — uses
- [[ridge-regression]] — analogous-to
- [[k-nearest-neighbors]] — analogous-to
- [[gradient-boosting]] — contrasts-with
- [[bootstrap]] — uses
- [[decision-trees]] — uses
- [[bagging]] — extends: random forests improve on bagging by decorrelating the bootstrap-sampled trees via random feature subsetting
- [[ensemble-learning]] — specializes