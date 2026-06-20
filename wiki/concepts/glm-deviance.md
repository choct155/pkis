---
aliases: []
also_type: []
analogous-to:
- kl-divergence
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
date_updated: '2026-06-20'
domain:
- statistics
id: pkis:concept:glm-deviance
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch12
- kroese-statistical-modeling-ch10
tags:
- GLM
- goodness-of-fit
- saturated-model
- likelihood-ratio
- deviance
title: Deviance (GLM)
understanding: 0
uses:
- saturated-model
- calibration
---

## Definition
$$D(y,\hat{\mu}) = 2\sum_{i=1}^N \left[\log p(y_i|\mu_i^*) - \log p(y_i|\hat{\mu}_i)\right]$$

The **deviance** measures the discrepancy between the fitted model (with predictions $\hat{\mu}_i$) and the **saturated model** ($\mu_i^* = $ MLE given only $y_i$), expressed as twice the log-likelihood gap. It is a generalization of the residual sum of squares to any GLM.

### Why it matters
For Poisson regression the deviance simplifies to $2\sum_i[y_i\log(y_i/\hat{\mu}_i)+\hat{\mu}_i-y_i]$. Unlike MSE or MAE, deviance respects the distributional assumptions of the GLM, making it the appropriate measure of fit for count, proportion, and other non-Gaussian responses. It also forms the basis for likelihood-ratio tests of nested GLMs and is closely related to KL divergence between the empirical and fitted distributions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[calibration]] — uses
- [[saturated-model]] — uses
- [[kl-divergence]] — analogous-to: Deviance is twice the KL-based log-likelihood ratio
[To be populated during integration]