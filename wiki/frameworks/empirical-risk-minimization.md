---
id: "pkis:framework:empirical-risk-minimization"
aliases: ["ERM"]
title: "Empirical Risk Minimization (ERM)"
knowledge_type: framework
also_type: []
domain: [statistical-learning]
tags: [probability-theory, optimization]
related_concepts: ["[[model-selection-problem]]", "[[bias-variance-tradeoff]]", "[[regularization]]", "[[continuous-optimization]]"]
related_concepts: ["[[model-selection-problem]]", "[[bias-variance-tradeoff]]", "[[regularization]]", "[[continuous-optimization]]", "[[inductive-bias]]"]
sources: ["[[deisenroth-mml]]", "[[domingos-useful-things]]", "[[liu-kan-2024]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

## Reading Path
- [[deisenroth-mml]] (unread) — formal treatment: risk, empirical risk, regularization as Lagrangian
- [[domingos-useful-things]] (unread) — §2: learning = representation + evaluation + optimization; the ERM decomposition made intuitive with Table 1
- [[liu-kan-2024]] (unread) — KAN training minimizes prediction loss plus L1 + entropy sparsification regularization; grid extension provides a non-standard approach to the bias-variance tradeoff

The formal framework underlying supervised learning: choose a hypothesis class and loss function, then minimize average loss on training data as a surrogate for true risk (expected loss over the data-generating distribution); the choice of loss and hypothesis class determines the method — cross-entropy gives logistic regression, hinge loss gives SVMs, squared loss gives OLS.
