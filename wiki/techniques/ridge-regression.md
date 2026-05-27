---
id: "pkis:technique:ridge-regression"
aliases: []
title: "Ridge Regression"
knowledge_type: technique
also_type: []
domain: [statistical-learning, optimization]
tags: [regularization, l2-penalty, shrinkage, tikhonov, gram-matrix, bias-variance]
related_concepts: ["[[regularization]]", "[[lasso]]", "[[bias-variance-tradeoff]]", "[[bayesian-linear-regression]]"]
sources: ["[[kroese-statistical-modeling]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Ridge regression (Tikhonov regularization) minimizes the penalized least-squares criterion β̂ = argmin ||Y - Xβ||² + λ||β||², shrinking all coefficients toward zero by a factor that depends on the regularization penalty λ, with a closed-form solution (X'X + λI)⁻¹X'Y that avoids the singularity problem in high-dimensional settings.

## Connections
- [[lasso]] — contrasts-with: ridge uses L2 penalty (shrinks coefficients toward zero without zeroing any); lasso uses L1 penalty (produces sparse solutions by setting some to exactly zero)
- [[regularization]] — specializes: ridge is the L2 form of regularization; regularization is the general concept
- [[bias-variance-tradeoff]] — uses: the ridge penalty trades increased bias for reduced variance in coefficient estimates
- [[bayesian-linear-regression]] — equivalent-in-context: ridge regression is equivalent to Bayesian linear regression with a Gaussian prior on β (MAP estimate)

## Reading Path
- [[kroese-statistical-modeling-ch09]] (unread) — primary treatment: James-Stein motivation, ridge regression with Gram matrix, comparison to lasso
- [[hastie-esl-ch03]] (unread) — ESL treatment of ridge alongside other linear regression regularization methods
