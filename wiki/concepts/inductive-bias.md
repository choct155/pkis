---
title: "Inductive Bias"
knowledge_type: concept
also_type: []
domain: [statistical-learning, bayesian-stats]
tags: [generalization, no-free-lunch, assumptions, hypothesis-space, pac-learning]
related_concepts: ["[[empirical-risk-minimization]]", "[[bias-variance-tradeoff]]", "[[regularization]]", "[[model-selection-problem]]", "[[curse-of-dimensionality]]"]
sources: ["[[domingos-useful-things]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

## Reading Path
- [[domingos-useful-things]] (unread) — §4: data alone is not enough; no-free-lunch; the knowledge lever metaphor

The assumptions a learner encodes beyond the training data in order to generalize. Formalized by Wolpert's no-free-lunch theorems: over all possible functions, every learner performs identically on average — no assumptions means no generalization. In practice, learners make inductive bets (smoothness, limited complexity, similar inputs yield similar outputs) that happen to be correct for the structured problems in the real world. The choice of hypothesis class, loss function, and regularizer are all expressions of inductive bias — making it explicit is more useful than pretending it isn't there.
