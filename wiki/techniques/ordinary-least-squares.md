---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- normal-form-game
- collinearity
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine learning
id: pkis:technique:ordinary-least-squares
instantiates:
- linear-regression
- maximum-likelihood-estimation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch11
tags:
- linear regression
- least squares
- MLE
- normal equations
title: Ordinary Least Squares (OLS)
understanding: 0
uses:
- residual-sum-of-squares
- hat-matrix
- orthogonal-projection
- singular-value-decomposition
- gauss-markov-theorem
---

## Definition
$$\hat{\mathbf{w}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

OLS finds the weight vector that minimises the residual sum of squares $\text{RSS}(\mathbf{w}) = \frac{1}{2}\|\mathbf{X}\mathbf{w}-\mathbf{y}\|_2^2$; the solution is the orthogonal projection of $\mathbf{y}$ onto the column space of $\mathbf{X}$.

### Why it matters
OLS is the canonical closed-form estimator for linear models and is equivalent to MLE under a Gaussian noise assumption. It is the baseline against which regularised methods (ridge, lasso) are measured and underpins the Gauss–Markov theorem on BLUE estimators. Numerically it should be computed via QR or SVD rather than direct matrix inversion to avoid ill-conditioning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[collinearity]] — contrasts-with: collinearity makes X^TX singular
- [[normal-form-game]] — contrasts-with
- [[gauss-markov-theorem]] — uses
- [[singular-value-decomposition]] — uses: numerically preferred solver
- [[orthogonal-projection]] — uses
- [[hat-matrix]] — uses
- [[residual-sum-of-squares]] — uses
- [[maximum-likelihood-estimation]] — instantiates: OLS = MLE under Gaussian noise
- [[linear-regression]] — instantiates
[To be populated during integration]