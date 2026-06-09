---
aliases: []
also_type: []
applies:
- model-selection-problem
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- overfitting-and-underfitting
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
- bayesian-stats
id: pkis:concept:optimism-of-training-error
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- information-criteria
related_concepts: []
sources:
- hastie-esl-ch07
tags:
- model-selection
- generalization-error
- in-sample-error
- Cp
- AIC
title: Optimism of the Training Error
understanding: 0
uses:
- effective-number-of-parameters
---

## Definition
The gap between a model's in-sample prediction error and its training error, capturing how much the training (apparent) error optimistically underestimates the true error because the same data is used both to fit the model and to assess it. Hastie defines op = Err_in - err-bar, where err-bar = (1/N)Σ L(y_i, f-hat(x_i)) is the training error and Err_in = (1/N)Σ E_{Y⁰}[L(Y⁰_i, f-hat(x_i))|T] is the in-sample error (new responses observed at the same training inputs x_i). The average optimism ω = E_y(op) admits a remarkably general closed form for squared-error, 0–1, and other losses: ω = (2/N)Σ_i Cov(y-hat_i, y_i). Thus the bias of err-bar grows with how strongly each observation influences its own prediction — the harder we fit, the larger Cov(y-hat_i, y_i). For a linear fit with d basis functions under the additive-error model, Σ Cov(y-hat_i, y_i) = dσ²_ε, giving E_y(Err_in) = E_y(err-bar) + 2(d/N)σ²_ε: optimism increases linearly with the number of parameters and decreases with sample size. This identity is the foundation of in-sample error estimates: add an estimate of ω to err-bar (the C_p, AIC, and BIC family), and it motivates the effective-number-of-parameters definition df = Σ Cov(y-hat_i, y_i)/σ²_ε. For adaptively chosen bases (e.g., best-subset selection) the simple dσ²_ε relation no longer holds and the true optimism exceeds 2dσ²_ε/N, because the search itself spends degrees of freedom.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[model-selection-problem]] — applies
- [[overfitting-and-underfitting]] — contrasts-with
- [[information-criteria]] — prerequisite-of
- [[effective-number-of-parameters]] — uses
[To be populated during integration]