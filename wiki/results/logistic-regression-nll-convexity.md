---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- optimisation
id: pkis:result:logistic-regression-nll-convexity
instantiates:
- convex-set-and-function
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch10
tags:
- convex-optimisation
- Hessian
- positive-semidefinite
- MLE
- logistic-regression
title: Convexity of Logistic Regression NLL
understanding: 0
uses:
- hessian-matrix
- maximum-likelihood-estimation
- regularization
---

## Definition
The negative log-likelihood of logistic regression,
$$\text{NLL}(w) = -\frac{1}{N}\sum_{n=1}^N[y_n\log\sigma(w^Tx_n)+(1-y_n)\log(1-\sigma(w^Tx_n))]$$
is a **convex** function of $w$. Its Hessian is
$$H(w) = \frac{1}{N}X^T S X, \quad S=\text{diag}(\mu_n(1-\mu_n))$$
which is positive semi-definite for any $w$ because $S\succeq 0$ and $H=\frac{1}{N}X^TSX$ is a sum of positive semi-definite rank-1 matrices. Consequently SGD and Newton's method converge to the **global** MLE.

### Why it matters
Convexity guarantees that gradient-based optimisers find the unique global minimum (when it exists). The result also implies that $\ell_2$ regularisation ($\lambda\|w\|^2$) makes the Hessian $H+2\lambda I$ strictly positive definite, so the MAP problem is strictly convex with a unique solution even when data are linearly separable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[regularization]] — uses
- [[maximum-likelihood-estimation]] — uses
- [[hessian-matrix]] — uses
- [[convex-set-and-function]] — instantiates
[To be populated during integration]