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
id: pkis:concept:finite-vs-countable-additivity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch15
tags:
- jaynes
- de-finetti
- kolmogorov
- feller
- improper-prior
- measure-theory
- infinite-sets
title: Finite vs. Countable Additivity
understanding: 0
---

## Definition
Two competing requirements on a probability/interval function over infinite sets. **Finite additivity**: for any partition of a set into finitely many disjoint parts, the measure of the whole equals the sum of the parts. **Countable (sigma-) additivity**: this also holds for partitions into countably many parts, F{I} = sum_k F{I_k}. From the finite sum rule p(A|C)=sum_{i=1}^n p(A_i|C) for n mutually exclusive propositions, Jaynes regards the n -> infinity passage to a convergent series (countable additivity) as innocuous — and if the series fails to converge he would simply refuse to pass to the limit at all.

## Jaynes's reading
For Jaynes the debate is a 'red herring'. de Finetti's advocacy of *finite* additivity (against Kolmogorov's and Feller's countable additivity) is, despite sounding cautious, a 'devious' way of answering yes to the real question: do we admit uniform distributions on infinite sets — can an infinite number of zeros add up to one? Feller's 'weird example' (F=0 on every finite interval (a,b), F=1 on (a,infinity)) is exactly the attempt to build a density everywhere zero that integrates to one; it is comprehensible only as the *too-early* limit r -> infinity of the proper uniform density p(x|r)=1/r on [0,r). Thus 'finite additivity' is a euphemism for reversing the proper order of approaching limits and thereby getting into trouble with non-normalizable distributions. Feller saw this and built his theory (via a continuous monotone CDF G with the natural endpoint limits) so as to be countably additive by construction and avoid the spurious paradoxes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]