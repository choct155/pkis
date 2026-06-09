---
aliases: []
also_type: []
applies:
- logistic-regression
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:separation-logistic-regression
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch16
tags:
- separation
- logistic-regression
- weakly-informative-prior
- cauchy-prior
- regularization
- nonidentifiability
title: Separation in Logistic Regression
understanding: 0
---

## Definition
**Separation** is a failure mode of discrete-data regression in which a linear combination of predictors perfectly predicts the outcome for some subset of cases. The maximum likelihood estimate then diverges — a coefficient runs to $\pm\infty$ — and Bayesian inference under a flat prior fails too. BDA3's example: in the 1964 election poll, none of the 87 surveyed African Americans reported Republican preference, driving the coefficient for *black* to $-\infty$ (R returns a meaningless finite number that depends only on when iteration stops).

The recommended fix is a **weakly informative prior**, not deletion of predictors. Gelman et al. standardize inputs (binary inputs to differ by 1; others to mean 0, SD 0.5) and place independent Student-$t$ priors centered at 0 — a default Cauchy$(0, 2.5)$ on each coefficient and Cauchy$(0,10)$ on the intercept. This constrains effects to plausible ranges (a change of 5 on the logit scale already spans probability 0.01 to 0.5) and yields finite, stable estimates.

Intuition: when the data alone cannot pin down a coefficient, a gentle prior supplies just enough information to keep the estimate sane without overriding real signal.

### Why it matters
Separation is "surprisingly common" in applied logistic regression, especially with binary predictors, and is routinely mishandled by dropping the strongest predictors — exactly the wrong move. Recognizing it and applying a default weakly informative prior turns a broken fit into a reasonable one (e.g. the bioassay coefficient drops from $10.2\pm6.4$ to $5.4\pm2.2$), and the same prior regularizes ordinary small-sample fits where MLE is unstable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[logistic-regression]] — applies
[To be populated during integration]