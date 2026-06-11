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
- information-theory
- statistics
id: pkis:concept:maximal-information-coefficient
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch06
tags:
- mutual-information
- nonparametric
- dependence
- feature-selection
- equitability
title: Maximal Information Coefficient (MIC)
understanding: 0
---

## Definition
$$\text{MIC}(X,Y) = \max_{G:\,|G_x||G_y|\le B(n)} \frac{\mathbb{I}((X,Y)|_G)}{\log \min(|G_x|,|G_y|)}$$

where $G$ ranges over 2-D grids with at most $B(n)=n^{0.6}$ cells, and $(X,Y)|_G$ is the joint distribution discretised onto $G$.

A normalised, grid-search-based estimate of mutual information that scores any type of statistical relationship (linear or non-linear) on $[0,1]$.

### Why it matters
MIC satisfies **equitability**: equally noisy relationships of any functional form receive similar scores, unlike correlation coefficients that only detect linear dependence. The companion statistic TICe (total information content, summing over all grids) has higher statistical power for small samples. MICe (improved MIC) can be computed in $O(n)$ time. Together they provide a principled, nonparametric alternative to Pearson's $r$ for exploratory data analysis.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]