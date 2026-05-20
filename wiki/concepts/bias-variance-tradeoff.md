---
title: "Bias-Variance Tradeoff"
knowledge_type: concept
also_type: []
domain: [statistical-learning]
tags: [model-selection, probability-theory]
related_concepts: []
related_concepts: ["[[inductive-bias]]", "[[regularization]]", "[[model-selection-problem]]"]
sources: ["[[hastie-esl]]", "[[domingos-useful-things]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

## Reading Path
- [[hastie-esl]] (unread) — mathematical treatment: bias-variance decomposition, squared error, 0-1 loss
- [[domingos-useful-things]] (unread) — §5: intuitive dart-throwing analogy; key insight that strong false assumptions can beat weak true ones given limited data

The decomposition of prediction error into irreducible noise, squared bias (systematic error from model assumptions), and variance (sensitivity to training data), establishing that model complexity must be managed because reducing one component increases the other.
