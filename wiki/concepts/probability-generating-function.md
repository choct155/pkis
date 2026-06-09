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
id: pkis:concept:probability-generating-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch01
specializes:
- generating-functions
tags:
- probability-theory
- stochastic-processes
- generating-functions
- moments
- limit-theorems
title: Probability Generating Function
understanding: 0
uses:
- convolution-of-distributions
---

## Definition
$$P(s) = E s^{X} = \sum_{k=0}^{\infty} p_k s^k, \qquad 0 \le s \le 1$$

For a non-negative integer-valued random variable $X$ with mass function $\{p_k\}$, the probability generating function (PGF) packs the entire distribution into the coefficients of a power series, so a single analytic object replaces an infinite sequence.

### Recovering the distribution and moments
The PGF *uniquely determines* its sequence: differentiating $n$ times and evaluating at $0$ gives $P^{(n)}(0) = n!\,p_n$. Differentiating and evaluating at $1$ instead yields **factorial moments**, $P^{(n)}(1) = E\big(X(X-1)\cdots(X-n+1)\big)$. In particular $E(X) = P'(1)$ and $\operatorname{Var}(X) = P''(1) + P'(1) - (P'(1))^2$. The tail generating function satisfies $Q(s) = (1-P(s))/(1-s)$, so $\lim_{s\uparrow 1} Q(s) = E(X)$.

### Radius of convergence
Because $P(1) = \sum_k p_k \le 1$, the radius of convergence is at least $1$; $P(1) = 1$ iff $P[X<\infty]=1$, i.e. mass does not escape to infinity.

### Why it matters
The PGF turns three awkward operations into algebra: convolution of independent sums becomes multiplication ($P_{X+Y}=P_X P_Y$), moment computation becomes differentiation, and — via the **Continuity Theorem** ($p_k^{(n)} \to p_k^{(0)}$ for all $k$ iff $P_n(s) \to P_0(s)$ pointwise on $(0,1)$) — proving convergence in distribution reduces to checking pointwise convergence of generating functions, often far easier than manipulating mass functions directly. This is the engine behind the Poisson approximation and the analysis of branching processes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[convolution-of-distributions]] — uses: The gf of a convolution is the product of gfs, the PGF's central computational lever.
- [[generating-functions]] — specializes: The PGF is the probability-distribution specialization of the general generating-function technique.
[To be populated during integration]