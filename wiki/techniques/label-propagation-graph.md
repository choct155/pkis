---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- graph-convolutional-network
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- graph-learning
- semi-supervised-learning
id: pkis:technique:label-propagation-graph
instantiates:
- graph-encoder-decoder-model
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
specializes:
- shallow-graph-embeddings
tags:
- semi-supervised
- graph-smoothness
- homophily
- label-spreading
- transductive
title: Label Propagation on Graphs
understanding: 0
uses:
- graph-laplacian
---

## Definition
Label propagation (Zhu & Ghahramani 2002) assigns labels to unlabelled nodes by minimising a graph-regularised energy:
$$\mathcal{L} = \underbrace{\sum_{i|v_i \in V_L}\|y^N_i - \hat{y}^N_i\|_2^2}_{\text{supervised}} + \beta\underbrace{\sum_{i,j}W_{ij}\|\hat{y}^N_i - \hat{y}^N_j\|_2^2}_{\text{graph smoothness}}$$
subject to $\hat{y}^N_i = y^N_i$ for labeled nodes, iteratively updating each unlabeled node as the weighted average of its neighbours' label distributions until convergence.

The algorithm encodes the homophily assumption: nodes connected by high-weight edges should share similar labels.

### Why it matters
Label propagation is one of the simplest and most effective semi-supervised graph methods. Its graph-Laplacian regulariser is shared by Laplacian Eigenmaps and the SemiEmb neural extension. Label spreading (Zhou et al. 2004) softens the hard constraint on labeled nodes, yielding better robustness to label noise. Both methods are special cases of the GraphEDM framework with a shallow encoder and identity decoder.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[graph-convolutional-network]] — contrasts-with
- [[shallow-graph-embeddings]] — specializes
- [[graph-laplacian]] — uses
- [[graph-encoder-decoder-model]] — instantiates
[To be populated during integration]