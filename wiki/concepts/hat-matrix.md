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
- linear algebra
id: pkis:concept:hat-matrix
instantiates:
- orthogonal-projection
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch11
tags:
- projection
- leverage
- linear regression
- OLS
title: Hat Matrix (Projection Matrix)
understanding: 0
uses:
- ordinary-least-squares
- effective-degrees-of-freedom
---

## Definition
$$H \triangleq \mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T$$

The hat matrix $H$ is the orthogonal projection operator onto the column space of $\mathbf{X}$; it 'puts the hat' on $\mathbf{y}$ via $\hat{\mathbf{y}} = H\mathbf{y}$.

### Why it matters
$H$ is symmetric and idempotent ($H^2 = H$). Its diagonal entries $h_{nn}$ are leverage scores that quantify how much influence observation $n$ exerts on its own fitted value. The effective degrees of freedom of a linear fit equals $\text{tr}(H) = D$ (rank of $\mathbf{X}$), and in ridge regression this generalises to $\sum_j \sigma_j^2/(\sigma_j^2+\lambda)$, providing a smooth notion of model complexity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[effective-degrees-of-freedom]] — uses
- [[ordinary-least-squares]] — uses
- [[orthogonal-projection]] — instantiates
[To be populated during integration]