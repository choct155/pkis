---
aliases: []
also_type: []
applies:
- zipf-mandelbrot-law
- language-model
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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- probability
generalizes:
- dirichlet-process
id: pkis:concept:pitman-yor-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch31
tags:
- pitman-yor
- power-law
- language-model
- nonparametric-bayes
- stick-breaking
title: Pitman-Yor Process
understanding: 0
uses:
- stick-breaking-construction
---

## Definition
The Pitman-Yor process $\mathrm{PY}(d,\alpha,H)$ with discount parameter $0\le d<1$, concentration $\alpha>-d$, and base measure $H$ generalises the Dirichlet process ($d=0$). Its stick-breaking weights are:
$$
\beta_k \sim \mathrm{Beta}(1-d,\, \alpha+kd), \quad \pi_k = \beta_k\prod_{j<k}(1-\beta_j).
$$
The number of clusters grows as $O(n^d)$ — a power law for $d>0$ vs. the logarithmic growth of the DP.

### Why it matters
The Pitman-Yor process generates power-law frequency distributions, making it a natural prior for natural language (Zipf's law), network degree sequences, and other heavy-tailed phenomena. It underlies the hierarchical Pitman-Yor language model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[language-model]] — applies
- [[zipf-mandelbrot-law]] — applies
- [[stick-breaking-construction]] — uses
- [[dirichlet-process]] — generalizes
[To be populated during integration]