---
title: "Cross-Validation"
knowledge_type: technique
also_type: []
domain: [statistical-learning]
tags: [model-selection, probability-theory]
related_concepts: ["[[bias-variance-tradeoff]]", "[[model-selection-problem]]"]
sources: ["[[hastie-esl]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Estimation of out-of-sample prediction error by repeatedly partitioning the data into training and validation folds, fitting the model on training folds and evaluating on held-out folds, then averaging the error estimates.
