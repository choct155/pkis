---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability
- statistics
id: pkis:result:log-partition-cumulant-generating
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch03
tags:
- exponential-family
- cumulants
- convexity
- MLE
title: Log Partition Function Generates Cumulants
understanding: 0
---

## Definition
For any exponential family $p(\mathbf{y}|\boldsymbol{\eta}) = h(\mathbf{y})\exp[\boldsymbol{\eta}^T T(\mathbf{y}) - A(\boldsymbol{\eta})]$:
$$\nabla_{\boldsymbol{\eta}} A(\boldsymbol{\eta}) = \mathbb{E}[T(\mathbf{y})]$$
$$\nabla^2_{\boldsymbol{\eta}} A(\boldsymbol{\eta}) = \mathrm{Cov}[T(\mathbf{y})]$$

Higher derivatives of $A$ generate higher-order cumulants of the sufficient statistics.

### Why it matters
Because the Hessian of $A$ is a covariance matrix and hence positive semi-definite, $A$ is convex in $\boldsymbol{\eta}$. This means the log-likelihood $\ell(\boldsymbol{\eta}) = \boldsymbol{\eta}^T T(y) - A(\boldsymbol{\eta})$ is concave, guaranteeing a unique global MLE. The result also provides a universal recipe for moment computation across all exponential-family members.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]