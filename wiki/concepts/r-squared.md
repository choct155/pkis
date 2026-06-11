---
aliases: []
also_type: []
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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
id: pkis:concept:r-squared
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch11
tags:
- goodness of fit
- linear regression
- variance explained
title: Coefficient of Determination ($R^2$)
understanding: 0
uses:
- ordinary-least-squares
- residual-sum-of-squares
---

## Definition
$$R^2 \triangleq 1 - \frac{\text{RSS}}{\text{TSS}} = 1 - \frac{\sum_n(y_n - \hat{y}_n)^2}{\sum_n(y_n - \bar{y})^2}$$

$R^2$ quantifies the fraction of variance in $y$ explained by the model, relative to a trivial constant-prediction baseline; $R^2=1$ is a perfect fit and $R^2=0$ means the model does no better than predicting the mean.

### Why it matters
$R^2$ is the most widely reported goodness-of-fit statistic for regression models because it is scale-invariant and immediately interpretable. It equals the squared Pearson correlation between $y$ and $\hat{y}$ in the OLS case. A common pitfall is that $R^2$ never decreases when features are added, motivating adjusted-$R^2$ and information-criterion-based alternatives for model comparison.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[residual-sum-of-squares]] — uses
- [[ordinary-least-squares]] — uses
[To be populated during integration]