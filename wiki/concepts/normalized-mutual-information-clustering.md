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
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- information-theory
id: pkis:concept:normalized-mutual-information-clustering
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch21
specializes:
- mutual-information
tags:
- clustering-evaluation
- mutual-information
- NMI
- information-theory
title: Normalized Mutual Information for Clustering
understanding: 0
uses:
- entropy
---

## Definition
Given two partitions $U = \{u_1,\ldots,u_R\}$ and $V = \{v_1,\ldots,v_C\}$ of $N$ points, define the empirical joint distribution $p_{UV}(i,j) = |u_i \cap v_j|/N$ and marginals $p_U(i) = |u_i|/N$, $p_V(j) = |v_j|/N$. The mutual information between partitions is:
$$\mathbb{I}(U,V) = \sum_{i,j} p_{UV}(i,j) \log \frac{p_{UV}(i,j)}{p_U(i)p_V(j)}$$
Because $\mathbb{I}$ is maximized by many tiny clusters (low entropy), it is normalized:
$$\text{NMI}(U,V) = \frac{\mathbb{I}(U,V)}{(\mathbb{H}(U) + \mathbb{H}(V))/2} \in [0,1]$$
A chance-adjusted variant and the **variation of information** $H(U|V)+H(V|U)$ (a proper metric on partitions) are related alternatives.

### Why it matters
NMI provides a principled, information-theoretic measure of clustering quality relative to a reference partition that is bounded and comparable across different numbers of clusters.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[entropy]] — uses
- [[clustering]] — applies
- [[mutual-information]] — specializes
[To be populated during integration]