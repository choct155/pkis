---
title: "Curse of Dimensionality"
knowledge_type: concept
also_type: []
domain: [statistical-learning]
tags: [probability-theory, high-dimensional-statistics]
related_concepts: ["[[bias-variance-tradeoff]]", "[[regularization]]"]
sources: ["[[hastie-esl]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The phenomenon whereby local methods (nearest neighbors, kernel smoothers) break down in high-dimensional spaces because neighborhoods that are "local" in each dimension become globally sparse, requiring exponentially more data to maintain the same coverage as dimensionality grows.
