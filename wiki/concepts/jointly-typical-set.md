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
id: pkis:concept:jointly-typical-set
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch10
tags:
- shannon
- typicality
- joint-ensemble
- asymptotic-equipartition
- channel-coding
title: Jointly-Typical Set
understanding: 0
---

## Definition
A pair of sequences $\mathbf{x},\mathbf{y}$ of length $N$ drawn from a joint ensemble $(XY)^N$ is **jointly typical** (to tolerance $\beta$) with respect to $P(x,y)$ if all three of its empirical log-probabilities sit near the corresponding entropies:
$$\left|\tfrac1N\log\tfrac1{P(\mathbf{x})}-H(X)\right|<\beta,\quad \left|\tfrac1N\log\tfrac1{P(\mathbf{y})}-H(Y)\right|<\beta,\quad \left|\tfrac1N\log\tfrac1{P(\mathbf{x},\mathbf{y})}-H(X,Y)\right|<\beta.$$
The jointly-typical set $J_N^\beta$ is the set of all such pairs. Intuitively it is the joint-ensemble analogue of the typical set: not just that $\mathbf{x}$ and $\mathbf{y}$ are each individually typical, but that they fluctuate *together* in the way their dependence demands.

### The joint typicality theorem
Three properties make $J_N^\beta$ the engine of the coding theorem. (1) A genuinely-drawn pair is jointly typical with probability $\to 1$ as $N\to\infty$ (law of large numbers). (2) The set is small: $|J_N^\beta|\le 2^{N(H(X,Y)+\beta)}$. (3) An *independently* drawn pair $\mathbf{x}'\sim X^N$, $\mathbf{y}'\sim Y^N$ (same marginals, no coupling) lands in $J_N^\beta$ only rarely:
$$P\big((\mathbf{x}',\mathbf{y}')\in J_N^\beta\big)\le 2^{-N(I(X;Y)-3\beta)}.$$

### Why it matters
Property (3) is the heart of achievability: the chance that a *wrong* codeword looks jointly typical with the received signal decays as $2^{-NI(X;Y)}$, so up to about $2^{NI(X;Y)}$ codewords can coexist before false matches accumulate. Geometrically, of the $2^{N(H(X)+H(Y))}$ independent typical pairs only $2^{NH(X,Y)}$ are jointly typical, and the ratio is exactly $2^{-NI(X;Y)}$ — mutual information measured as a collision probability.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]