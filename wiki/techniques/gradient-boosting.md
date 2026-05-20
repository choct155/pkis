---
title: "Gradient Boosting"
knowledge_type: technique
also_type: []
domain: [statistical-learning, optimization]
tags: [ensemble-methods, optimization]
related_concepts: ["[[ensemble-learning]]", "[[bias-variance-tradeoff]]"]
sources: ["[[hastie-esl]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Reinterpretation of boosting as functional gradient descent: each successive weak learner (typically a shallow tree) fits the negative gradient of the loss function at the current model's predictions, building the ensemble by steepest descent in function space.
