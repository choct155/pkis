---
aliases: []
also_type: []
coverage: 2
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
id: pkis:technique:cross-validation
knowledge_type: technique
maturity: settled
prerequisite-of:
- model-selection-problem
related_concepts:
- '[[bias-variance-tradeoff]]'
- '[[model-selection-problem]]'
sources:
- '[[hastie-esl]]'
- '[[kroese-statistical-modeling]]'
tags:
- model-selection
- probability-theory
title: Cross-Validation
understanding: 0
---

Estimation of out-of-sample prediction error by repeatedly partitioning the data into training and validation folds, fitting the model on training folds and evaluating on held-out folds, then averaging the error estimates.

## Reading Path
- [[hastie-esl]] (unread) — primary treatment: k-fold CV, leave-one-out CV, the wrong way to do CV
- [[kroese-statistical-modeling-ch05]] (unread) — CV in the frequentist inference chapter; PRESS statistic for leave-one-out CV in linear models

## Connections
- [[model-selection-problem]] — prerequisite-of