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
- machine learning
generalizes:
- ordinary-least-squares
id: pkis:concept:weighted-least-squares
instantiates:
- maximum-likelihood-estimation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch11
tags:
- heteroskedasticity
- linear regression
- MLE
title: Weighted Least Squares (WLS)
understanding: 0
uses:
- iteratively-reweighted-least-squares
---

## Definition
$$\hat{\mathbf{w}}_\text{wls} = (\mathbf{X}^T\Lambda\mathbf{X})^{-1}\mathbf{X}^T\Lambda\mathbf{y}, \quad \Lambda = \mathrm{diag}(1/\sigma^2(x_n))$$

WLS is the MLE for a heteroskedastic Gaussian regression model in which each observation's variance $\sigma^2(x_n)$ is known, so that observations with lower noise receive higher weight.

### Why it matters
WLS generalises OLS to heteroskedastic settings and is a special case of generalised least squares. It is also the basis for iteratively reweighted least squares (IRLS), which solves GLMs by repeatedly solving a WLS problem with updated weights.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[maximum-likelihood-estimation]] — instantiates
- [[iteratively-reweighted-least-squares]] — uses
- [[ordinary-least-squares]] — generalizes
[To be populated during integration]