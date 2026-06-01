---
aliases: []
cluster_membership:
- model-evolution
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[knowledge-graph-embeddings]]'
  node_type: technique
  rationale: embedding similarity over concepts
- node: '[[formal-ontology]]'
  node_type: concept
  rationale: structural comparison is over the ontology
domain:
- deep-learning
- knowledge-representation
evidence_nodes: []
id: pkis:hypothesis:shadow-fragmentation-detection
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: model-evolution
research_program_role: boundary-condition
status: open
tags:
- fragmentation
- near-duplicate
- embeddings
title: Embedding Similarity Plus Structural Comparison Detects Near-Duplicate Concept
  Creation Before Fragmentation Compounds
uses:
- knowledge-graph-embeddings
- formal-ontology
---

## Formal Statement
Combining embedding similarity with structural comparison detects near-duplicate concept creation early enough to prevent ontology fragmentation from compounding.

## Motivation
Unchecked near-duplicate concepts fragment the ontology and corrupt downstream aggregation; early detection is cheaper than later merges.

## Current Evidence
[To be filled]

## Open Questions
Similarity threshold vs false-merge risk; structural-comparison features.

## Connections
- [[formal-ontology]] — uses: structural comparison is over the ontology
- [[knowledge-graph-embeddings]] — uses: embedding similarity over concepts
- [[model-evolution]] — belongs-to: constituent hypothesis of the model-evolution cluster