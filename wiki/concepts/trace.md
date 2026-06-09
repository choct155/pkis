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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:concept:trace
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch04
tags: []
title: Trace
understanding: 0
---

## Definition
$$\mathrm{tr}(A) := \sum_{i=1}^{n} a_{ii}$$

The trace of a square matrix is the sum of its diagonal entries; equivalently, it is the sum of the matrix's eigenvalues, and it is the unique function characterizing a linear map that is invariant to the choice of basis alongside the determinant.

### Algebraic properties
The trace is linear, $\mathrm{tr}(A+B)=\mathrm{tr}(A)+\mathrm{tr}(B)$ and $\mathrm{tr}(\alpha A)=\alpha\,\mathrm{tr}(A)$, with $\mathrm{tr}(I_n)=n$. Its defining feature is **cyclic invariance**: $\mathrm{tr}(AB)=\mathrm{tr}(BA)$ and more generally $\mathrm{tr}(AKL)=\mathrm{tr}(KLA)$. A useful special case collapses an outer product to a dot product: $\mathrm{tr}(xy^\top)=y^\top x$. These four properties (linearity, scaling, identity value, cyclicity) uniquely determine the trace.

### Basis invariance and eigenvalues
Under a basis change $B=S^{-1}AS$, cyclic invariance gives $\mathrm{tr}(B)=\mathrm{tr}(S^{-1}AS)=\mathrm{tr}(ASS^{-1})=\mathrm{tr}(A)$, so the trace of a linear mapping is well-defined independent of representation. It satisfies $\mathrm{tr}(A)=\sum_i \lambda_i$ and appears as the coefficient $c_{n-1}=(-1)^{n-1}\mathrm{tr}(A)$ in the characteristic polynomial.

### Why it matters
Together with the determinant and eigenvalues, the trace is one of the few basis-invariant scalar summaries of a matrix, giving an at-a-glance characterization of a linear map. Cyclic invariance makes it ubiquitous in ML derivations: gradients of matrix expressions, expected quadratic forms $\mathbb{E}[x^\top A x]=\mathrm{tr}(A\,\mathrm{Cov}(x))$, and information-theoretic quantities over covariance matrices.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]