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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- data-visualization
id: pkis:concept:anscombes-quartet
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch02
tags:
- data-visualization
- summary-statistics
- datasets
- pedagogy
title: Anscombe's Quartet
understanding: 0
---

## Definition
**Anscombe's quartet** consists of four synthetic $(x,y)$ datasets, each of $n=11$ points, that are constructed to have nearly identical low-order summary statistics:
$$\mathbb{E}[x]=9,\; V[x]=11,\; \mathbb{E}[y]\approx 7.5,\; V[y]\approx 4.12,\; \rho\approx 0.816$$
yet exhibit visually and structurally distinct joint distributions (linear, curved, with outlier, and near-vertical).

### Why it matters
Anscombe's quartet is the canonical demonstration that summary statistics — means, variances, and correlations — are grossly insufficient to characterize a distribution. It motivates the necessity of **data visualization** before modeling, underpins the principle that model diagnostics must go beyond aggregate metrics, and inspired later works such as the Datasaurus Dozen. It is a standard teaching tool against over-reliance on numerical summaries.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]