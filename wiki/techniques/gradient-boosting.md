---
aliases: []
also_type: []
coverage: 2
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
- optimization
id: pkis:technique:gradient-boosting
instantiates:
- forward-stagewise-additive-modeling
- bet-on-sparsity
knowledge_type: technique
maturity: settled
related_concepts:
- '[[ensemble-learning]]'
- '[[bias-variance-tradeoff]]'
sources:
- '[[hastie-esl]]'
- '[[friedman-rulefit-2005]]'
specializes:
- ensemble-learning
tags:
- ensemble-methods
- optimization
title: Gradient Boosting
understanding: 0
uses:
- decision-trees
- gradient-descent
- lasso
---

## Reading Path
- [[hastie-esl]] (unread) — primary theoretical treatment: functional gradient descent, AdaBoost as exponential loss, regularization and shrinkage
- [[friedman-rulefit-2005]] (unread) — MART and ISLE as the tree-ensemble generators feeding RuleFit; gradient boosting used as the base learner before rule extraction

Reinterpretation of boosting as functional gradient descent: each successive weak learner (typically a shallow tree) fits the negative gradient of the loss function at the current model's predictions, building the ensemble by steepest descent in function space.

## Connections
- [[bet-on-sparsity]] — instantiates: boosting's L1-style regularization exploits sparsity per the bet-on-sparsity principle
- [[lasso]] — uses: tree boosting with shrinkage approximates an L1-regularized (lasso) path over the tree dictionary
- [[gradient-descent]] — uses
- [[decision-trees]] — uses
- [[forward-stagewise-additive-modeling]] — instantiates
- [[ensemble-learning]] — specializes