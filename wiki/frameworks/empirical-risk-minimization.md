---
title: "Empirical Risk Minimization (ERM)"
knowledge_type: framework
also_type: []
domain: [statistical-learning]
tags: [probability-theory, optimization]
related_concepts: ["[[model-selection-problem]]", "[[bias-variance-tradeoff]]", "[[regularization]]", "[[continuous-optimization]]"]
sources: ["[[deisenroth-mml]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The formal framework underlying supervised learning: choose a hypothesis class and loss function, then minimize average loss on training data as a surrogate for true risk (expected loss over the data-generating distribution); the choice of loss and hypothesis class determines the method — cross-entropy gives logistic regression, hinge loss gives SVMs, squared loss gives OLS.
