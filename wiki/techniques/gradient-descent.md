---
title: "Gradient Descent"
knowledge_type: technique
also_type: []
domain: [optimization, statistical-learning, deep-learning]
tags: [calculus, optimization]
related_concepts: ["[[vector-calculus]]", "[[continuous-optimization]]", "[[convex-optimization]]", "[[gradient-boosting]]"]
sources: ["[[deisenroth-mml]]", "[[liu-kan-2024]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Iterative first-order optimization method that moves in the direction of the negative gradient of the objective function with step size (learning rate) $\alpha$: $\theta_{t+1} = \theta_t - \alpha \nabla_\theta \mathcal{L}(\theta_t)$; the workhorse of ML training, with variants (SGD, Adam, momentum) dominating practice.

## Reading Path
- [[deisenroth-mml]] (unread) — formal treatment with convergence rates
- [[liu-kan-2024]] (unread) — KAN training uses LBFGS (a quasi-Newton method) and stochastic gradient; sparsification loss includes L1 + entropy regularization terms
