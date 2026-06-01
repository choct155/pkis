---
aliases: []
cluster_membership:
- compositional-query-grounding
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[knowledge-graph-traversal]]'
  node_type: technique
  rationale: expansion walks ontological relations
- node: '[[formal-ontology]]'
  node_type: concept
  rationale: the expansion rules are ontological
domain:
- knowledge-representation
evidence_nodes: []
id: pkis:hypothesis:implicit-entity-expansion-accuracy
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: compositional-query-grounding
research_program_role: direct-test
status: open
tags:
- entity-expansion
- query-grounding
- ontology
title: Ontological Inference Improves Implicit Entity Expansion Accuracy Over Stochastic
  Generation
uses:
- knowledge-graph-traversal
- formal-ontology
---

## Formal Statement
Expanding the implicit entity and field scope of a query via ontological inference is more accurate than expansion by stochastic LLM generation.

## Motivation
Implicit scope expansion is where statistical query understanding fails on the margin cases that matter; ontology supplies the missing structure.

## Current Evidence
[To be filled]

## Open Questions
How to evaluate 'correct' expansion without a gold expansion set? Interaction with query ambiguity.

## Connections
- [[formal-ontology]] — uses: the expansion rules are ontological
- [[knowledge-graph-traversal]] — uses: expansion walks ontological relations
- [[compositional-query-grounding]] — belongs-to: constituent hypothesis of the compositional-query-grounding cluster