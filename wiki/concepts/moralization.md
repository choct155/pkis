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
- probabilistic-graphical-models
- machine-learning
id: pkis:concept:moralization
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch08
- goodfellow-deeplearning-ch16
tags:
- directed-graph
- undirected-graph
- junction-tree
- conditional-independence
- exact-inference
title: Moralization (Directed-to-Undirected Conversion)
understanding: 0
---

## Definition
Given a directed acyclic graph, the **moral graph** is constructed by:
1. Adding an undirected link between every pair of **co-parents** (parents of the same child node).
2. Dropping all arrow directions.

The resulting clique potentials are set to the original conditional distributions, and the partition function equals 1.

The procedure converts a DAG into an undirected graph whose clique factorisation absorbs every conditional distribution in the DAG factorisation, preserving the joint distribution exactly.

### Why it matters
Moralization is the first step in the **junction tree algorithm** for exact inference on arbitrary graphs. The 'marrying the parents' step is necessary because a conditional $p(x_k \mid \text{pa}_k)$ involves all variables in $\{x_k\} \cup \text{pa}_k$ jointly; they must therefore all belong to a single clique. The cost is the possible loss of conditional independence properties that were present in the directed graph (particularly those arising from v-structures).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]