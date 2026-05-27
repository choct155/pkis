---
id: "pkis:technique:lasso"
aliases: []
title: "Lasso (Least Absolute Shrinkage and Selection Operator)"
knowledge_type: technique
also_type: []
domain: [statistical-learning]
tags: [linear-algebra, regularization, optimization, high-dimensional-statistics]
related_concepts: ["[[regularization]]", "[[bias-variance-tradeoff]]"]
sources: ["[[hastie-esl]]", "[[friedman-rulefit-2005]]", "[[kroese-statistical-modeling]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

## Reading Path
- [[hastie-esl]] (unread) — primary treatment: LARS algorithm, degrees of freedom, comparison with ridge; theoretical sparsity properties
- [[friedman-rulefit-2005]] (unread) — lasso as the fitting mechanism for rule ensembles; support normalization ensures equal a priori rule influence before L1 penalization
- [[kroese-statistical-modeling-ch09]] (unread) — lasso in the shrinkage/regularization chapter alongside ridge and false discovery rate; coordinate descent solution

L1-penalized regression that simultaneously estimates coefficients and performs variable selection by driving some coefficients exactly to zero, unlike L2 (ridge) penalties which only shrink.
