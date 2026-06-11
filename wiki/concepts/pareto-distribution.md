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
contrasts-with:
- gamma-distribution
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability-theory
- statistics
- economics
generalizes:
- zipf-mandelbrot-law
id: pkis:concept:pareto-distribution
instantiates:
- kurtosis-and-tail-behavior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch02
tags:
- pareto
- power-law
- heavy-tails
- zipf
- 80-20
- wealth-distribution
title: Pareto Distribution and Power Laws
understanding: 0
uses:
- pmf-and-pdf
---

## Definition
The **Pareto distribution** with minimum value $m > 0$ and shape parameter $\kappa > 0$ has pdf
$$\mathrm{Pareto}(x \mid m, \kappa) = \kappa m^\kappa x^{-(\kappa+1)}\,\mathbb{I}(x \geq m).$$
On a log-log scale it is linear ($\log p \propto -\kappa \log x$), which is the hallmark of a **power law**. Setting $\kappa = 1.16$ recovers the **80-20 rule** (Pareto principle). **Zipf's law** in linguistics ($p(r) \propto r^{-a}$) is a discrete power law.

### Why it matters
Power-law (heavy-tailed) distributions describe wealth, word frequencies, city sizes, earthquake magnitudes, and network degrees. Standard mean/variance-based statistics and Gaussian models fail for such data; recognizing Pareto behavior is essential for risk management and linguistic modeling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gamma-distribution]] — contrasts-with
- [[zipf-mandelbrot-law]] — generalizes
- [[kurtosis-and-tail-behavior]] — instantiates
- [[pmf-and-pdf]] — uses
[To be populated during integration]