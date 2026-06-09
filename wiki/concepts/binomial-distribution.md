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
- bayesian-stats
id: pkis:concept:binomial-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch03
tags:
- jaynes
- sampling-with-replacement
- limiting-distribution
- discrete-distribution
title: Binomial Distribution
understanding: 0
---

## Definition
The distribution for the number $r$ of successes in $n$ independent trials each with success probability $f$:

$$b(r\mid n,f) = \binom{n}{r} f^r (1-f)^{n-r},$$

with generating function $G(t)=(1-f+ft)^n$ (Newton's binomial theorem), which immediately gives normalization and moments. Jaynes derives it two ways that illuminate its meaning: (1) as the $N\to\infty$, $M/N\to f$ **limit of the hypergeometric distribution**, where the changing-urn-contents dependence between draws washes out; and (2) as the *approximate* result of randomized sampling with replacement, where shaking the urn is taken to render successive draws independent so that $P(R_k\mid R_{k-1}B)=M/N$ regardless of history.

The binomial is broader than the hypergeometric of equal mean because replacement removes the negative correlation of without-replacement sampling. Jaynes warns that the second derivation is only an approximation: it discards relevant information ('randomization'), is good for small $n$, but for large $n$ small physical correlations accumulate (long runs become far more probable than the binomial predicts), so binomial-based limit theorems are properties of the abstract model, not the real world. The multi-color generalization is the **multinomial distribution** $m(r_1\cdots r_k\mid f_1\cdots f_k)=\frac{r!}{\prod r_i!}\prod f_i^{r_i}$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]