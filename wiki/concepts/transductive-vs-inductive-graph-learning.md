---
aliases: []
also_type: []
analogous-to:
- distribution-shift
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
- graph-learning
id: pkis:concept:transductive-vs-inductive-graph-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch23
tags:
- transductive
- inductive
- graph-generalisation
- GNN
- shallow-embeddings
title: Transductive vs Inductive Graph Learning
understanding: 0
uses:
- shallow-graph-embeddings
- graph-sage
---

## Definition
**Transductive** graph learning operates on a single fixed graph known at training time; the model must only generalise to nodes or edges within that graph (e.g. semi-supervised node classification on a citation network). **Inductive** graph learning trains on a set of graphs (or subgraphs) and must generalise to entirely new, unseen graphs at test time (e.g. classifying molecular structures).

The distinction is fundamental to choosing a graph learning architecture: shallow embedding methods (DeepWalk, GraRep) are transductive because their encoder is an $N$-row lookup table tied to specific node IDs, whereas parameterised encoders such as GCN, GraphSAGE, and GAT are inductive because they compute embeddings as functions of node features and local structure.

### Why it matters
Many real applications require inductive generalisation — predicting properties of molecules not seen during training, detecting fraud in evolving transaction networks, or classifying new users. Inductive methods achieve this by learning aggregation functions rather than per-node parameters, but they require node features $\mathbf{X}$ to be available and well-defined across graphs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[distribution-shift]] — analogous-to
- [[graph-sage]] — uses
- [[shallow-graph-embeddings]] — uses
[To be populated during integration]