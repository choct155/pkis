---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
contrasts-with:
- unbiasedness
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:principle:regression-to-the-mean
instantiates:
- bayesian-inference
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch04
tags:
- shrinkage
- prediction
- unbiasedness
- galton
- partial-pooling
title: Regression to the Mean
understanding: 0
---

## Definition
When two variables are imperfectly correlated, the conditional expectation of one given an extreme value of the other lies between that observed value and the population mean. Formally, for jointly normal variables with correlation rho, E(omega|y) = mu + rho*(y - mu), so the posterior prediction is pulled toward the grand mean by a factor equal to the correlation. The principle, named by Galton in the 19th century from his study of parents' and children's heights, explains why a tall mother's predicted daughter is taller than average but not as tall as the mother. Crucially, the regression prediction is NOT unbiased in the repeated-sampling sense (conditioning on the predicted quantity and resampling the predictor): the unbiased estimate omega-hat = mu + (1/rho)(y - mu) over-extrapolates and produces absurd predictions for extreme y. This is Gelman's central illustration of the limitation of unbiasedness as a principle: it forces an artificial choice of which quantity is the 'parameter' and which is the 'prediction.' Bayesian analysis can be seen as a systematic extension of regression to the mean, properly weighting information from the data against information from the population distribution; hierarchical models implement this as partial pooling, shrinking individual estimates toward a common mean by an amount determined by the data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-inference]] — instantiates: Regression to the mean is Bayesian updating of a prediction toward the population mean; Bayesian analysis generalizes it.
- [[unbiasedness]] — contrasts-with: The regression-prediction example shows the posterior mean is biased while the unbiased estimate over-extrapolates absurdly.
[To be populated during integration]