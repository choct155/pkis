---
title: "The Model Selection Problem"
knowledge_type: problem
also_type: [concept]
domain: [statistical-learning, bayesian-stats]
tags: [model-selection, probability-theory]
related_concepts: ["[[bias-variance-tradeoff]]", "[[cross-validation]]", "[[regularization]]"]
sources: ["[[hastie-esl]]", "[[steel-bma-forecasting-2011]]", "[[castle-model-selection-algorithms]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

How to choose the right level of model complexity — the model, its hyperparameters, or the size of the function class — given finite data, when training error systematically underestimates prediction error. Classification note: assigned as problem because it motivates a family of techniques (CV, AIC, BIC, MDL, VC bounds), but may also function as a concept in the statistical decision theory sense.

## Reading Path
- [[hastie-esl]] (unread) — foundational treatment: AIC, BIC, VC dimension, cross-validation, bootstrap; theoretical grounding for all standard criteria
- [[steel-bma-forecasting-2011]] (unread) — BMA as the principled Bayesian answer to model uncertainty; prior sensitivity and hierarchical priors over model space
- [[castle-model-selection-algorithms]] (unread) — systematic Monte Carlo benchmark of 21 model selection algorithms; penalty function / bias-variance framework for understanding when each approach dominates in practice
