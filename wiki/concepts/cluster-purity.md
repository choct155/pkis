---
aliases: []
also_type: []
applies:
- clustering
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
- rand-index
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
id: pkis:concept:cluster-purity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch21
tags:
- clustering-evaluation
- external-metric
- classification
title: Cluster Purity
understanding: 0
---

## Definition
Given $K$ clusters where $N_{ij}$ is the number of points in cluster $i$ belonging to class $j$, $N_i = \sum_j N_{ij}$, and $p_{ij} = N_{ij}/N_i$, the **purity** of cluster $i$ is $p_i = \max_j p_{ij}$, and the overall clustering purity is the weighted average:
$$\text{purity} = \sum_i \frac{N_i}{N} p_i$$
Purity ranges from $0$ (worst) to $1$ (best) but is trivially maximized at $1$ by making each cluster a singleton.

### Why it matters
Purity is a simple, interpretable external evaluation metric for clustering when ground-truth class labels exist. Its key limitation — no penalty for using too many clusters — motivates the use of adjusted metrics like ARI or NMI instead.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[rand-index]] — contrasts-with: purity does not penalize number of clusters; ARI does
- [[clustering]] — applies
[To be populated during integration]