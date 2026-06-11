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
- probability
- machine-learning
- statistics
id: pkis:concept:chinese-restaurant-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch31
tags:
- dirichlet-process
- partition
- exchangeability
- nonparametric-bayes
- polya-urn
title: Chinese Restaurant Process
understanding: 0
---

## Definition
The Chinese Restaurant Process (CRP) with parameter $\alpha>0$ is a distribution over partitions of $\{1,\ldots,n\}$ obtained by the sequential rule: customer $n+1$ sits at an occupied table $k$ with probability $\frac{n_k}{n+\alpha}$, or starts a new table with probability $\frac{\alpha}{n+\alpha}$, where $n_k$ is the current occupancy of table $k$.

The CRP is the predictive distribution obtained by marginalising out $G\sim\mathrm{DP}(\alpha,H)$ from the DPMM, and generates partitions with a power-law number of clusters.

### Why it matters
The CRP provides an exchangeable, computationally convenient representation of the DP prior on partitions that underpins Gibbs samplers for DPMM and reveals the rich-get-richer (Pólya urn) dynamics central to Bayesian nonparametric clustering.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]