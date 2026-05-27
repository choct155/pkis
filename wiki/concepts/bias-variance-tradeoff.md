---
id: "pkis:concept:bias-variance-tradeoff"
aliases: []
title: "Bias-Variance Tradeoff"
knowledge_type: concept
also_type: []
domain: [statistical-learning]
tags: [model-selection, probability-theory]
related_concepts: ["[[inductive-bias]]", "[[regularization]]", "[[model-selection-problem]]"]
sources: ["[[hastie-esl]]", "[[domingos-useful-things]]", "[[castle-model-selection-algorithms]]", "[[kroese-statistical-modeling]]", "[[liu-kan-2024]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 4
understanding: 0
maturity: settled
---

## Reading Path
- [[hastie-esl]] (unread) — mathematical treatment: bias-variance decomposition, squared error, 0-1 loss
- [[domingos-useful-things]] (unread) — §5: intuitive dart-throwing analogy; key insight that strong false assumptions can beat weak true ones given limited data
- [[castle-model-selection-algorithms]] (unread) — applies bias-variance decomposition to coefficient UMSE in variable selection; penalty function as the lever controlling the tradeoff in practice
- [[kroese-statistical-modeling-ch04]] (unread) — §4.6.2: approximation vs. statistical error decomposition of test loss; bias-variance in the statistical learning framing
- [[liu-kan-2024]] (unread) — KAN grid extension displays the tradeoff as a U-shaped test loss curve; optimal grid size G ~ (num_params / num_data) is the interpolation threshold

The decomposition of prediction error into irreducible noise, squared bias (systematic error from model assumptions), and variance (sensitivity to training data), establishing that model complexity must be managed because reducing one component increases the other.
