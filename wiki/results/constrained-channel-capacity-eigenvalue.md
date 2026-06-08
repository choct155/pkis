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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:result:constrained-channel-capacity-eigenvalue
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch17
tags:
- perron-frobenius
- eigenvalue
- connection-matrix
- capacity
- spectral
- mackay
title: Capacity of a Constrained Channel as a Leading Eigenvalue
understanding: 0
---

## Definition
The capacity of a constrained noiseless channel equals the base-2 logarithm of the leading (Perron–Frobenius) eigenvalue of its **connection matrix**. Summarise the trellis section by $A$ with $A_{ss'}=1$ if an edge runs from state $s$ to $s'$ and $0$ otherwise. Counting paths is a local message-passing recursion: if $\mathbf{c}^{(n)}$ holds the number of length-$n$ paths ending in each state, then
$$\mathbf{c}^{(n+1)}=A\,\mathbf{c}^{(n)},\qquad \mathbf{c}^{(N)}=A^{N}\mathbf{c}^{(0)},$$
and $M_N=\sum_s c^{(N)}_s$.

### Why it matters
For large $N$, $\mathbf{c}^{(N)}$ is dominated by the principal right-eigenvector and grows as
$$\mathbf{c}^{(N)}\to \text{const}\cdot\lambda_1^{\,N}\,\mathbf{e}^{(R)},$$
so
$$C=\lim_{N\to\infty}\frac1N\log_2 M_N=\log_2\lambda_1.$$
The whole capacity question reduces to one eigenvalue computation. The non-negative, irreducible matrix $A$ guarantees (Perron–Frobenius) a real positive dominant eigenvalue with a positive eigenvector.

### Worked values
Channels A, B and C share connection matrices with the same dominant eigenvalue, the golden ratio $\gamma=\tfrac{1+\sqrt5}{2}=1.618$, giving $C=\log_2\gamma\approx0.694$ bits — they are equivalent up to invertible transforms (accumulator/differentiator, inversion). The two run-length-limited channels of figure 17.9 have $\lambda_1=1.839$ and $1.928$, i.e. capacities $0.879$ and $0.947$ bits.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]