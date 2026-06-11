---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:framework:hierarchical-dirichlet-process
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch31
tags:
- hierarchical-dirichlet-process
- topic-model
- grouped-data
- nonparametric-bayes
- sharing-clusters
title: Hierarchical Dirichlet Process
understanding: 0
---

## Definition
The Hierarchical Dirichlet Process (HDP; Teh et al. 2006) provides a nonparametric prior for grouped data in which groups share a common but unknown set of mixture components:
$$
G_0 \sim \mathrm{DP}(\gamma, H), \quad G_j \mid G_0 \sim \mathrm{DP}(\alpha, G_0) \quad \forall j.
$$
All group-level measures $G_j$ share atoms drawn from the global measure $G_0$, enabling cross-group sharing of topics or clusters.

### Why it matters
The HDP is the foundation of the HDP-LDA (infinite LDA) topic model, where the number of topics is inferred from data. It is the BNP analogue of hierarchical finite mixture models and enables coherent information sharing across heterogeneous document corpora or time segments.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]