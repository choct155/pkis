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
id: pkis:concept:convolution-of-distributions
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch01
tags:
- probability-theory
- convolution
- sums-of-random-variables
- generating-functions
title: Convolution of Distributions
understanding: 0
uses:
- random-variable
---

## Definition
$$c_n = (a * b)_n = \sum_{i=0}^{n} a_i\, b_{n-i}$$

The convolution of two sequences $\{a_n\}$ and $\{b_n\}$ on the non-negative integers is the sequence whose $n$-th term sums all ways the indices add to $n$; it is the operation that produces the distribution of a sum.

### Probabilistic meaning
If $X$ and $Y$ are independent non-negative integer-valued random variables with mass functions $\{a_k\}$ and $\{b_k\}$, then because $[X+Y=n] = \bigcup_{i=0}^{n}[X=i,\,Y=n-i]$ is a disjoint union,
$$P[X+Y=n] = \sum_{i=0}^{n} a_i\, b_{n-i},$$
so $\{P[X+Y=n]\} = \{P[X=n]\} * \{P[Y=n]\}$. Convolution of two probability mass functions is again a probability mass function.

### Algebraic structure
Convolution is commutative ($X+Y \stackrel{d}{=} Y+X$) and associative ($X+(Y+Z)\stackrel{d}{=}(X+Y)+Z$), so the order of convolving several independent summands is immaterial. The $k$-fold self-convolution $\{p^{*k}_n\}$ gives the distribution of $S_k = X_1 + \cdots + X_k$.

### Why it matters
Convolution is the natural but computationally awkward arithmetic of independent sums. Its decisive simplification — the generating function of a convolution is the *product* of the generating functions ($A(s)B(s)$) — converts a tangled summation into ordinary multiplication, which is why named distributions like the Poisson and binomial are closed under independent addition, and why generating-function methods dominate the study of random sums and branching processes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[random-variable]] — uses: Convolution computes the distribution of a sum of independent non-negative integer-valued random variables.
[To be populated during integration]