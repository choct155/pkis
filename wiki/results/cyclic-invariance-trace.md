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
- linear-algebra
id: pkis:result:cyclic-invariance-trace
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch02
tags:
- trace
- cyclic permutation
- matrix identity
- Frobenius norm
title: Cyclic Invariance of the Trace
understanding: 0
---

## Definition
$$\operatorname{Tr}(\mathbf{A}\mathbf{B}\mathbf{C}) = \operatorname{Tr}(\mathbf{C}\mathbf{A}\mathbf{B}) = \operatorname{Tr}(\mathbf{B}\mathbf{C}\mathbf{A})$$

More generally, $\operatorname{Tr}\!\left(\prod_{i=1}^n \mathbf{F}^{(i)}\right) = \operatorname{Tr}\!\left(\mathbf{F}^{(n)}\prod_{i=1}^{n-1}\mathbf{F}^{(i)}\right)$, even when individual products change shape, as long as all products are well-defined.

The trace is invariant to cyclic permutations of a matrix product.

### Why it matters
This identity is ubiquitous in matrix calculus: it lets analysts move factors inside traces to simplify derivatives, relate $\operatorname{Tr}(\mathbf{AB})=\operatorname{Tr}(\mathbf{BA})$ for rectangular $\mathbf{A},\mathbf{B}$, and rewrite the Frobenius norm as $\|\mathbf{A}\|_F^2 = \operatorname{Tr}(\mathbf{A}\mathbf{A}^T)$. It appears prominently in the PCA derivation when reducing the Frobenius-norm objective.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]