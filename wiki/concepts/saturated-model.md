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
id: pkis:concept:saturated-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch12
tags:
- GLM
- deviance
- goodness-of-fit
- likelihood-ratio-test
title: Saturated Model
understanding: 0
uses:
- generalized-linear-models
---

## Definition
The **saturated model** is the GLM that fits one free parameter per observation: $\mu_i^* = $ the MLE of $\mu_i$ given $y_i$ alone (i.e., $\mu_i^* = y_i$ for Poisson; $\mu_i^* = y_i/N_i$ for binomial). It achieves the maximum possible log-likelihood on the training data.

The deviance is the twice-log-likelihood ratio between the saturated model and any candidate model:
$$D = 2(\ell_{\text{sat}} - \ell_{\text{fit}})$$

### Why it matters
The saturated model serves as the reference ceiling for goodness-of-fit in all GLMs. A model deviance close to zero indicates near-perfect fit; a large deviance signals poor fit. Comparing deviances of nested models yields likelihood-ratio tests with asymptotic $\chi^2$ null distributions. The concept generalises RSS (residual sum of squares) from Gaussian regression to all exponential-family responses.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generalized-linear-models]] — uses
[To be populated during integration]