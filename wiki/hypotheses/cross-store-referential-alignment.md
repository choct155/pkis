---
aliases: []
cluster_membership:
- compositional-query-grounding
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[knowledge-graph-traversal]]'
  node_type: technique
  rationale: alignment traverses the KG backbone
- node: '[[formal-ontology]]'
  node_type: concept
  rationale: the backbone is an ontology
domain:
- knowledge-representation
evidence_nodes: []
id: pkis:hypothesis:cross-store-referential-alignment
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: compositional-query-grounding
research_program_role: boundary-condition
status: open
tags:
- cross-store
- alignment
- referential-integrity
title: An Ontological Backbone Enables Cross-Store Entity Alignment That Reduces Referential
  Errors
uses:
- knowledge-graph-traversal
- formal-ontology
---

## Formal Statement
Using an ontological backbone as the alignment layer enables cross-store entity alignment that reduces referential errors relative to store-local identifiers.

## Motivation
Heterogeneous stores fragment entity identity; an ontological backbone is the shared referent.

## Current Evidence
[To be filled]

## Open Questions
Alignment under conflicting store schemas; maintenance cost of the backbone.

## Connections
- [[formal-ontology]] — uses: the backbone is an ontology
- [[knowledge-graph-traversal]] — uses: alignment traverses the KG backbone
- [[compositional-query-grounding]] — belongs-to: constituent hypothesis of the compositional-query-grounding cluster