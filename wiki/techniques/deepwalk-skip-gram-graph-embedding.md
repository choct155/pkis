---
aliases: []
also_type: []
analogous-to:
- word-embeddings
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- graph-sage
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- graph-learning
- natural-language-processing
id: pkis:technique:deepwalk-skip-gram-graph-embedding
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
specializes:
- shallow-graph-embeddings
- node-embedding
tags:
- DeepWalk
- node2vec
- random-walk
- skip-gram
- graph-embeddings
- matrix-factorization
title: DeepWalk / Skip-gram Graph Embeddings
understanding: 0
uses:
- random-walk
- low-rank-matrix-approximation
---

## Definition
DeepWalk learns node embeddings by running truncated uniform random walks on the graph and then applying the skip-gram objective to the resulting node sequences, treating nodes like words in a corpus.

In the GraphEDM formulation the target similarity matrix is
$$s(\mathbf{W}) = \mathbb{E}_q[\mathbf{D}^{-1}\mathbf{W}^q], \quad q \sim \text{Categorical}([1,\ldots,T_{\max}])$$
and the decoder is an outer product $\hat{\mathbf{W}} = \mathbf{Z}\mathbf{Z}^\top$. Training minimises
$$\mathcal{L} = \log Z(\mathbf{Z}) - \sum_{i,j} s(\mathbf{W})_{ij}\hat{W}_{ij}$$
where the partition function is approximated via hierarchical softmax in $O(N)$.

As shown by Levy & Goldberg and Qiu et al. (NetMF), skip-gram graph methods are equivalent to implicit matrix factorisation of a log-transformed, smoothed powers-of-adjacency matrix.

### Why it matters
DeepWalk (Perozzi et al. 2014) and its extension node2vec (Grover & Leskovec 2016) showed that distributional semantics ideas from NLP transfer to graphs, sparking a wave of graph representation learning research. The implicit matrix-factorisation view unifies them with spectral and matrix-factorisation approaches.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[node-embedding]] — specializes
- [[graph-sage]] — contrasts-with
- [[low-rank-matrix-approximation]] — uses
- [[random-walk]] — uses
- [[word-embeddings]] — analogous-to
- [[shallow-graph-embeddings]] — specializes
[To be populated during integration]