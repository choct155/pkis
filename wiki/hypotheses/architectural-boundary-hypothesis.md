---
aliases: []
cluster_membership:
- embedding-ontology-alignment
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[knowledge-graph-embeddings]]'
  node_type: technique
  rationale: the vector-index leg of the trichotomy
domain:
- knowledge-representation
evidence_nodes: []
id: pkis:hypothesis:architectural-boundary-hypothesis
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: embedding-ontology-alignment
research_program_role: boundary-condition
status: open
tags:
- architecture
- storage
- query-patterns
title: The Property-Graph / Relational / Vector-Index Trichotomy Maps Predictably
  to Query-Pattern Types
---

## Formal Statement
The choice among property graph, relational store, and vector index maps predictably to query-pattern types, so storage architecture can be selected from query characteristics rather than by default.

## Motivation
Misaligned storage is a common source of avoidable cost and error; a predictable mapping makes the choice principled.

## Current Evidence
[To be filled]

## Open Questions
Where do hybrid query patterns break the trichotomy? Cost of maintaining multiple stores.

## Connections
- [[embedding-ontology-alignment]] — belongs-to: constituent hypothesis of the embedding-ontology-alignment cluster