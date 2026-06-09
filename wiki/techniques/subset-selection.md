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
- lasso
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
- optimization
id: pkis:technique:subset-selection
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch03
tags:
- variable-selection
- model-selection
- regression
- best-subset
- stepwise
title: Subset Selection (Linear Regression)
understanding: 0
uses:
- linear-regression
- cross-validation
---

## Definition
A family of discrete variable-selection strategies for linear regression that retain only a subset of the p predictors and fit least squares on the retained set, motivated by (i) improving prediction accuracy by trading bias for reduced variance and (ii) interpretability of a smaller model. Variants differ in how the subset path is searched. Best-subset regression finds, for each size k in {0,...,p}, the size-k subset with smallest RSS; the leaps-and-bounds procedure (Furnival and Wilson, 1974) makes this feasible up to p ~ 30-40. Because exhaustive search becomes infeasible for larger p, greedy path searches are used: forward-stepwise selection starts from the intercept and sequentially adds the predictor that most improves the fit (exploitable via QR updates, usable even when p >> N); backward-stepwise selection starts from the full model and sequentially drops the variable with the smallest Z-score (requires N > p). Forward-stagewise regression is even more constrained: at each step it adds, to the current coefficient, the simple regression coefficient of the residual on the most-correlated variable, without re-adjusting the other coefficients, so it can take far more than p steps to reach the least-squares fit. The subset size k is the complexity parameter, chosen by cross-validation or AIC (often via the one-standard-error rule). Because selection is discrete, subset methods tend to have high variance; standard errors reported after a search are not valid because they ignore the search process (the bootstrap can help).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cross-validation]] — uses: subset size k chosen by cross-validation (or AIC)
- [[lasso]] — contrasts-with: discrete (high-variance) selection vs. lasso's continuous selection via soft-thresholding
- [[linear-regression]] — uses: fits least squares on the retained subset of predictors
[To be populated during integration]