---
aliases: []
also_type: []
applies:
- confidence-interval
- credible-interval
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
- probability-theory
- statistics
id: pkis:concept:quantile-function
instantiates:
- gaussian-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- inverse-transform-sampling
related_concepts: []
sources:
- murphy-pml1-intro-ch02
tags:
- quantile
- inverse-cdf
- median
- percentile
- confidence-interval
title: Quantile Function (Inverse CDF)
understanding: 0
uses:
- cumulative-distribution-function
---

## Definition
$$P^{-1}(q) = x_q \quad \text{such that} \quad \Pr(X \leq x_q) = q, \quad q \in (0,1)$$

The **quantile function** (also called the percent-point function or inverse CDF) maps a probability level $q$ to the corresponding threshold value $x_q$ of the distribution. The median is $P^{-1}(0.5)$; the lower and upper quartiles are $P^{-1}(0.25)$ and $P^{-1}(0.75)$. For the standard Gaussian $\mathcal{N}(0,1)$, the central 95% interval is $(\Phi^{-1}(0.025),\,\Phi^{-1}(0.975))=(-1.96,1.96)$.

### Why it matters
Quantile functions are essential for constructing confidence and credible intervals, performing inverse-transform sampling, defining robust summary statistics (IQR), and calibrating probabilistic forecasts. Many numerical libraries expose the quantile function as the primary interface to continuous distributions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-distribution]] — instantiates
- [[inverse-transform-sampling]] — prerequisite-of
- [[credible-interval]] — applies
- [[confidence-interval]] — applies
- [[cumulative-distribution-function]] — uses
[To be populated during integration]