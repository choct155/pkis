---
id: "pkis:technique:decision-trees"
aliases: ["CART"]
title: "Decision Trees (CART)"
knowledge_type: technique
also_type: []
domain: [statistical-learning]
tags: [model-selection]
related_concepts: ["[[ensemble-learning]]", "[[random-forests]]", "[[gradient-boosting]]"]
sources: ["[[hastie-esl]]", "[[friedman-rulefit-2005]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

## Reading Path
- [[hastie-esl]] (unread) — primary CART treatment: split criteria, cost-complexity pruning, missing values, interpretability
- [[friedman-rulefit-2005]] (unread) — trees used as rule-generating mechanisms; each internal node defines a conjunctive rule extracted for the ensemble before lasso fitting

Recursive binary partitioning of the feature space into axis-aligned regions, selecting splits to minimize impurity (classification) or squared error (regression), then pruning via cost-complexity to control overfitting.
