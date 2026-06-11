---
aliases: []
also_type: []
applies:
- determinant
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
- machine-learning
id: pkis:result:weinstein-aronszajn-identity
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch23
tags:
- determinant
- low-rank
- residual-flow
- planar-flow
title: Weinstein–Aronszajn Identity (Matrix Determinant Lemma)
understanding: 0
uses:
- low-rank-approximation
---

## Definition
$$\det(I_D + AB) = \det(I_M + BA),$$
where $A$ is $D \times M$ and $B$ is $M \times D$. This is the rank-$M$ specialisation of the matrix determinant lemma.

### Why it matters
When $M \ll D$, the right-hand side costs $O(M^3)$ instead of $O(D^3)$. In residual flows with bottleneck residual blocks ($F = F_2 \circ F_1$, $F_1 : \mathbb{R}^D \to \mathbb{R}^M$, $F_2 : \mathbb{R}^M \to \mathbb{R}^D$), this identity reduces Jacobian determinant computation to the smaller $M \times M$ matrix. The planar flow ($M=1$) is the extreme case, yielding an $O(D)$ determinant.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[low-rank-approximation]] — uses
- [[determinant]] — applies
[To be populated during integration]