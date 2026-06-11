---
aliases: []
also_type: []
analogous-to:
- noninformative-prior
applies:
- collinearity
contrasts-with:
- gauss-markov-theorem
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
- optimization
extends:
- ordinary-least-squares
id: pkis:technique:ridge-regression
instantiates:
- weight-decay-as-prior
- map-regression-as-regularized-least-squares
knowledge_type: technique
maturity: settled
related_concepts:
- '[[regularization]]'
- '[[lasso]]'
- '[[bias-variance-tradeoff]]'
- '[[bayesian-linear-regression]]'
sources:
- '[[kroese-statistical-modeling]]'
tags:
- regularization
- l2-penalty
- shrinkage
- tikhonov
- gram-matrix
- bias-variance
title: Ridge Regression
understanding: 0
uses:
- principal-component-analysis
- effective-degrees-of-freedom
- ridge-pca-shrinkage
- regularization
- singular-value-decomposition
- regularization-path
---

Ridge regression (Tikhonov regularization) minimizes the penalized least-squares criterion β̂ = argmin ||Y - Xβ||² + λ||β||², shrinking all coefficients toward zero by a factor that depends on the regularization penalty λ, with a closed-form solution (X'X + λI)⁻¹X'Y that avoids the singularity problem in high-dimensional settings.

## Connections
- [[collinearity]] — applies: ridge regularises ill-conditioned X^TX
- [[regularization-path]] — uses
- [[singular-value-decomposition]] — uses
- [[map-regression-as-regularized-least-squares]] — instantiates
- [[regularization]] — uses
- [[ridge-pca-shrinkage]] — uses
- [[weight-decay-as-prior]] — instantiates
- [[ordinary-least-squares]] — extends
- [[gauss-markov-theorem]] — contrasts-with: ridge is a biased estimator that can beat the BLUE on MSE by trading bias for variance
- [[effective-degrees-of-freedom]] — uses: df(lambda) = tr(H_lambda) = sum d_j^2/(d_j^2+lambda) measures the complexity of the ridge fit
- [[principal-component-analysis]] — uses: shrinks coordinates along the principal-component directions by d^2/(d^2+lambda)
- [[noninformative-prior]] — analogous-to
- [[lasso]] — contrasts-with: ridge uses L2 penalty (shrinks coefficients toward zero without zeroing any); lasso uses L1 penalty (produces sparse solutions by setting some to exactly zero)
- [[regularization]] — specializes: ridge is the L2 form of regularization; regularization is the general concept
- [[bias-variance-tradeoff]] — uses: the ridge penalty trades increased bias for reduced variance in coefficient estimates
- [[bayesian-linear-regression]] — equivalent-in-context: ridge regression is equivalent to Bayesian linear regression with a Gaussian prior on β (MAP estimate)

## Reading Path
- [[kroese-statistical-modeling-ch09]] (unread) — primary treatment: James-Stein motivation, ridge regression with Gram matrix, comparison to lasso
- [[hastie-esl-ch03]] (unread) — ESL treatment of ridge alongside other linear regression regularization methods