---
aliases: []
also_type: []
analogous-to:
- normalized-mutual-information-clustering
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
- statistics
id: pkis:concept:rand-index
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch21
tags:
- clustering-evaluation
- external-index
- contingency-table
- ARI
title: Rand Index and Adjusted Rand Index
understanding: 0
---

## Definition
Given two partitions $U$ and $V$ of $N$ data points, build a $2\times 2$ contingency table over all $\binom{N}{2}$ pairs: $TP$ (same cluster in both), $TN$ (different in both), $FP$ (same in $U$, different in $V$), $FN$ (different in $U$, same in $V$). The **Rand index** is:
$$R = \frac{TP + TN}{TP + FP + FN + TN}$$
The **Adjusted Rand Index (ARI)** corrects for chance agreement under a hypergeometric null (random partitions with fixed cluster sizes):
$$AR = \frac{\text{index} - \mathbb{E}[\text{index}]}{\max \text{index} - \mathbb{E}[\text{index}]}$$
ARI equals $0$ in expectation for random partitions and $1$ for perfect agreement.

### Why it matters
The Rand index provides an interpretable fraction of correct pairwise clustering decisions, analogous to accuracy for supervised classification. ARI removes the upward bias of the raw Rand index when many clusters are used, enabling fair comparison across different values of $K$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[normalized-mutual-information-clustering]] — analogous-to
- [[clustering]] — applies
[To be populated during integration]