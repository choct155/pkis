---
aliases: []
cluster_membership:
- embedding-ontology-alignment
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[word-embeddings]]'
  node_type: concept
  rationale: the baseline being extended
- node: '[[knowledge-graph-embeddings]]'
  node_type: technique
  rationale: the mechanism for injecting structure
- node: '[[formal-ontology]]'
  node_type: concept
  rationale: the supervision signal
domain:
- deep-learning
- knowledge-representation
evidence_nodes: []
extends:
- word-embeddings
id: pkis:hypothesis:ontological-supervision-improves-embeddings
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: embedding-ontology-alignment
research_program_role: direct-test
status: open
tags:
- embeddings
- ontological-supervision
- retrieval
title: Training Embeddings With Ontological Structure as Supervision Improves Downstream
  Retrieval and Classification
uses:
- knowledge-graph-embeddings
- formal-ontology
---

## Formal Statement
Embedding models trained with explicit ontological structure as a supervision signal produce representations that better support downstream retrieval, classification, and reasoning than embeddings trained without ontological supervision.

## Motivation
Distributional embeddings systematically misrepresent ontological relationships; supervision with ontology should correct this where it matters downstream.

## Current Evidence
[To be filled]

## Open Questions
What supervision objective best injects ontological structure? Which downstream tasks benefit most?

## Connections
- [[formal-ontology]] — uses: the supervision signal is the ontology
- [[knowledge-graph-embeddings]] — uses: injects structure via KG embeddings
- [[word-embeddings]] — extends: extends distributional embeddings with ontological supervision
- [[embedding-ontology-alignment]] — belongs-to: constituent hypothesis of the embedding-ontology-alignment cluster