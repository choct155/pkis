---
aliases: []
also_type: []
applies:
- gaussian-distribution
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-20'
domain:
- mathematics
- probability
- statistics
id: pkis:technique:completing-the-square-multivariate
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- bayesian-linear-regression
- bayes-rule-for-gaussians
related_concepts: []
sources:
- murphy-pml1-intro-ch03
- carrell-groups-matrices-vectors-ch09
tags:
- algebra
- gaussian
- posterior-derivation
title: Completing the Square (Multivariate)
understanding: 0
---

## Definition
For a quadratic form $f(x) = x^T A x + x^T b + c$ (with $A$ symmetric positive definite), one can rewrite it as:
$$f(x) = (x - h)^T A(x - h) + k, \quad h = -\tfrac{1}{2}A^{-1}b, \quad k = c - \tfrac{1}{4}b^T A^{-1}b$$

This is the vector generalisation of the scalar identity $ax^2 + bx + c = a(x+\frac{b}{2a})^2 + c - \frac{b^2}{4a}$.

### Why it matters
Completing the square is the key algebraic trick for deriving closed-form Gaussian posteriors, computing the log partition function, and identifying sufficient statistics. It converts an unnormalised exponential-quadratic expression into a recognisable Gaussian density plus a constant that becomes the log marginal likelihood.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayes-rule-for-gaussians]] — prerequisite-of
- [[bayesian-linear-regression]] — prerequisite-of
- [[gaussian-distribution]] — applies
[To be populated during integration]