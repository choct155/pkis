---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
- bayesian-stats
id: pkis:framework:statistical-decision-theory-regression
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch02
tags:
- decision-theory
- regression
- classification
- loss-function
- probability-theory
title: Statistical Decision Theory for Regression and Classification
understanding: 0
---

## Definition
Hastie's framework (ESL S2.4) that derives the theoretically optimal predictor from a joint distribution Pr(X,Y) and a loss function, before any model is chosen. Given a loss L(Y, f(X)) penalizing prediction errors, one minimizes the Expected Prediction Error EPE(f) = E[L(Y,f(X))] = integral of L over Pr(dx,dy). The key move is to condition on X and minimize pointwise: EPE = E_X E_{Y|X}(L | X), so it suffices to solve argmin_c E_{Y|X}(L | X=x) at each x.

For squared-error loss L = (Y-f(X))^2 the pointwise solution is the conditional mean f(x) = E(Y | X=x), called the **regression function** -- the best prediction under average squared error. For L1 loss E|Y-f(X)| the solution is the conditional median, a more robust but analytically less convenient location estimate. For a categorical output G with a K x K loss matrix L(k,l) (zero on the diagonal), pointwise minimization gives the **Bayes classifier**: under 0-1 loss, classify x to the most probable class, G-hat(x) = argmax_g Pr(g | X=x). Its error rate is the **Bayes rate**, the irreducible classification error.

This is the optimality target that all supervised methods approximate. k-nearest-neighbors implements the recipe directly -- replacing expectation by a sample average and pointwise conditioning by conditioning on a neighborhood (two approximations); under mild conditions, as N,k -> infinity with k/N -> 0, the kNN estimate converges to E(Y|X=x). Linear least squares instead assumes f(x) ~= x^T beta is globally linear and pools over X, yielding beta = [E(XX^T)]^{-1} E(XY). Dummy-variable regression of a binary G followed by thresholding recovers the Bayes classifier because E(Y|X) = Pr(G=G_1 | X). The framework thus separates the *what* (the optimal f given Pr and L) from the *how* (the modeling assumptions used to estimate it from finite data).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]