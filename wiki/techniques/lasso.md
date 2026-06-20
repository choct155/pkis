---
aliases: []
also_type: []
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- statistical-learning
id: pkis:technique:lasso
knowledge_type: technique
maturity: settled
related_concepts:
- '[[regularization]]'
- '[[bias-variance-tradeoff]]'
sources:
- '[[hastie-esl]]'
- '[[friedman-rulefit-2005]]'
- '[[kroese-statistical-modeling]]'
- kroese-statistical-modeling-ch09
tags:
- linear-algebra
- regularization
- optimization
- high-dimensional-statistics
title: Lasso (Least Absolute Shrinkage and Selection Operator)
understanding: 0
uses:
- least-angle-regression-lars
---

## Reading Path
- [[hastie-esl]] (unread) — primary treatment: LARS algorithm, degrees of freedom, comparison with ridge; theoretical sparsity properties
- [[friedman-rulefit-2005]] (unread) — lasso as the fitting mechanism for rule ensembles; support normalization ensures equal a priori rule influence before L1 penalization
- [[kroese-statistical-modeling-ch09]] (unread) — lasso in the shrinkage/regularization chapter alongside ridge and false discovery rate; coordinate descent solution

L1-penalized regression that simultaneously estimates coefficients and performs variable selection by driving some coefficients exactly to zero, unlike L2 (ridge) penalties which only shrink.

## Connections
- [[least-angle-regression-lars]] — uses: the LARS lasso modification computes the entire piecewise-linear lasso path at the cost of one least-squares fit