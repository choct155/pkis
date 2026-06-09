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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:result:gauss-markov-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch03
tags:
- least-squares
- unbiased-estimator
- variance
- blue
- regression
- bias-variance
title: Gauss-Markov Theorem
understanding: 0
---

## Definition
Among all linear unbiased estimators of a linear combination theta = a^T beta of the regression parameters, the ordinary least-squares estimator thetahat = a^T betahat (with betahat = (X^T X)^{-1} X^T y) has the smallest variance; i.e., least squares is the Best Linear Unbiased Estimator (BLUE). Formally, if thetatilde = c^T y is any other estimator with E(c^T y) = a^T beta, then Var(a^T betahat) <= Var(c^T y) (proof via the triangle inequality, Exercise 3.3); the result extends to the full coefficient vector via the matrix ordering Vhat <= Vtilde (positive-semidefinite difference). The theorem requires only that the errors are uncorrelated with constant variance (no Gaussian assumption). Hastie et al. stress its essential caveat: restricting to unbiased estimators is not necessarily wise. Since MSE = variance + bias^2 and expected prediction error differs from MSE only by the irreducible sigma^2, a biased estimator that trades a little bias for a large reduction in variance can have lower MSE than the least-squares estimator. This motivates the biased shrinkage and selection methods (ridge regression, lasso, subset selection) developed later in the chapter.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]