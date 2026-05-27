---
id: "pkis:technique:gradient-boosting"
aliases: []
title: "Gradient Boosting"
knowledge_type: technique
also_type: []
domain: [statistical-learning, optimization]
tags: [ensemble-methods, optimization]
related_concepts: ["[[ensemble-learning]]", "[[bias-variance-tradeoff]]"]
sources: ["[[hastie-esl]]", "[[friedman-rulefit-2005]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

## Reading Path
- [[hastie-esl]] (unread) — primary theoretical treatment: functional gradient descent, AdaBoost as exponential loss, regularization and shrinkage
- [[friedman-rulefit-2005]] (unread) — MART and ISLE as the tree-ensemble generators feeding RuleFit; gradient boosting used as the base learner before rule extraction

Reinterpretation of boosting as functional gradient descent: each successive weak learner (typically a shallow tree) fits the negative gradient of the loss function at the current model's predictions, building the ensemble by steepest descent in function space.
