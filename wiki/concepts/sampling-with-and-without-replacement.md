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
id: pkis:concept:sampling-with-and-without-replacement
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch03
tags:
- jaynes
- sampling-theory
- finite-population
- independence
title: Sampling With and Without Replacement
understanding: 0
---

## Definition
The distinction between two drawing protocols and the surprising reversal in their difficulty. **Without replacement** (drawn balls set aside) is conceptually simple and exact: the urn contents change deterministically, each draw is logically relevant to every other, and the count distribution is the hypergeometric $h(r\mid N,M,n)$. It is the right model when 'drawing' is destructive (testing a bulb to failure, dissolving a protein sample).

**With replacement** (each ball recorded and returned before the next draw) is, contrary to first intuition, *conceptually far harder*. A returned ball lies on top and is more likely re-drawn; the true second-draw probability depends on urn shape, ball size, friction, the toss, the reach — details that symmetry made irrelevant in the without-replacement case. Jaynes describes the standard escape — shaking the urn and declaring the problem 'randomized' — as deliberately discarding relevant information to recover the simple Bernoulli rule and hence the **binomial distribution**. It is only an approximation: good for small $n$, but small physical correlations $\epsilon,\delta$ (modeled via a Markov transition matrix) accumulate over many draws, producing long runs and breaking exchangeability. Thus randomized with-replacement sampling from finite $N$ behaves approximately like without-replacement sampling in the $N\to\infty$ limit.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]