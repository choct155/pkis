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
- bayesian-inference
id: pkis:concept:matrix-normal-inverse-wishart
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch15
tags:
- conjugate-prior
- multivariate-regression
- inverse-Wishart
- matrix-normal
- closed-form
title: Matrix Normal Inverse-Wishart (MNIW) Distribution
understanding: 0
---

## Definition
$$\text{MNIW}(W, \Sigma \mid M_0, V_0, \nu_0, \Psi_0) \triangleq \mathcal{MN}(W \mid M_0, \Sigma, V_0)\,\text{IW}(\Sigma \mid \nu_0, \Psi_0)$$

The joint conjugate prior for the coefficient matrix $W$ and error covariance $\Sigma$ in multivariate linear regression $Y = WX + E$, where $E_i \overset{\text{iid}}{\sim}\mathcal{N}(0,\Sigma)$.

### Why it matters
The MNIW prior yields a closed-form posterior of the same family (closed under Bayes updates), enabling analytic MAP and posterior-predictive computations for multi-output linear regression without resorting to approximate inference. The posterior parameters $(M_1, V_1, \nu_1, \Psi_1)$ have intuitive interpretations as regularised sufficient statistics of the data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]