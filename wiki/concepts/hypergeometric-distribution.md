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
date_updated: '2026-06-20'
domain:
- bayesian-stats
generalizes:
- binomial-distribution
id: pkis:concept:hypergeometric-distribution
instantiates:
- the-bernoulli-urn
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch03
- lange-applied-probability-ch04
tags:
- jaynes
- sampling-without-replacement
- finite-population
- discrete-distribution
title: Hypergeometric Distribution
understanding: 0
uses:
- exchangeability
---

## Definition
The exact distribution for the number $r$ of red balls obtained when $n$ balls are drawn **without replacement** from an urn of $N$ balls, $M$ of them red:

$$h(r\mid N,M,n) = \frac{\binom{M}{r}\binom{N-M}{n-r}}{\binom{N}{n}},$$

which (with $x!=\Gamma(x+1)$) vanishes automatically outside the feasible range. It is the order-independent sum over the $\binom{n}{r}$ equally-probable drawing orders, each of probability $M!(N-M)!(N-n)!/[(M-r)!(N-M-w)!N!]$ — order-independence being a manifestation of **exchangeability**. The name comes from its relation to the Gauss hypergeometric function $F(a,b,c;t)$, whose generating function it provides.

Key properties: most-probable value $\hat r=\mathrm{INT}[(n+1)(M+1)/(N+2)]$, so the sample fraction $r/n$ tracks the urn fraction $M/N$ (a first 'physical prediction'); the non-obvious **interchange symmetry** $h(r\mid N,M,n)=h(r\mid N,n,M)$ (drawing 10 from 50 red equals drawing 50 from 10 red); and the red/white symmetry $h(n-r\mid N,N-M,n)=h(r\mid N,M,n)$. It generalizes to $k$ colors as the multivariate hypergeometric $h(r_1\cdots r_k\mid N_1\cdots N_k)=\prod_i\binom{N_i}{r_i}/\binom{\sum N_i}{\sum r_i}$, and degenerates to the **binomial distribution** in the limit $N\to\infty$, $M/N\to f$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[exchangeability]] — uses: order-independence of the count probability is a manifestation of exchangeability of the draws
- [[binomial-distribution]] — generalizes: the hypergeometric is the finite-population generalization; the binomial is its infinite-population / with-replacement limit
- [[the-bernoulli-urn]] — instantiates: the hypergeometric is the exact count distribution produced by the without-replacement urn model
[To be populated during integration]