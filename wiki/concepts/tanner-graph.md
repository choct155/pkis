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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:concept:tanner-graph
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- sum-product-decoding-ldpc
related_concepts: []
sources:
- mackay-itila-ch47
specializes:
- factor-graph
tags:
- error-correction
- factor-graph
- bipartite-graph
- ldpc
- sparse-graph-codes
title: Tanner Graph (Bipartite Bit-Check Graph)
understanding: 0
---

## Definition
The **Tanner graph** of a linear code is the bipartite graph that encodes its parity-check matrix $\mathbf{H}$: one node per code bit (a *bit node* or variable node) and one node per parity check (a *check node*), with an edge $(n,m)$ drawn exactly when $H_{mn}=1$. Bits connect only to checks and vice versa, so the graph is bipartite. Define the neighbourhoods
$$N(m) \equiv \{n : H_{mn}=1\}, \qquad M(n) \equiv \{m : H_{mn}=1\},$$
so each check $m$ constrains the bits in $N(m)$ to sum to zero mod 2, and each bit $n$ is involved in the checks in $M(n)$.

### Relation to the factor graph
The Tanner graph is a factor graph for the codeword prior
$$P(\mathbf{t}) \propto \prod_m \mathbb{1}\!\left[\textstyle\sum_{n\in N(m)} t_n = 0\right],$$
with bit nodes as variables and check nodes as the indicator factors. Adding per-bit likelihood factors ('dongles') $P(r_n\mid t_n)$ turns it into the factor graph of the posterior used for decoding.

### Structure controls performance
For an LDPC code the Tanner graph is sparse: a regular $(j,k)$ code gives every bit node degree $j$ and every check node degree $k$. The local degrees and the girth (length of the shortest cycle) govern how well iterative decoding works. **Irregular** codes deliberately mix node degrees (some degree 2, some 20) to push performance closer to capacity. Tanner (1981) generalized Gallager's construction by allowing arbitrary subcode constraints at the check nodes.

### Why it matters
The Tanner graph is the data structure on which all practical LDPC decoding runs: message-passing is literally local computation exchanged along its edges. It also unifies block codes, convolutional/turbo codes, and Bayesian networks under the single lens of graphical models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sum-product-decoding-ldpc]] — prerequisite-of: Sum-product decoding runs message passing over the Tanner graph's edges.
- [[factor-graph]] — specializes: The Tanner graph is the factor graph of the codeword prior/posterior, with bit nodes as variables and check nodes as indicator factors.
[To be populated during integration]