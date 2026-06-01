---
aliases: []
cluster_membership:
- structured-validation-truth-discovery
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[formal-ontology]]'
  node_type: concept
  rationale: property constraints are ontological axioms
- node: '[[bayesian-inference]]'
  node_type: concept
  rationale: validation confidence is probabilistic
domain:
- knowledge-representation
evidence_nodes: []
id: pkis:hypothesis:semantic-validation-beyond-syntactic
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: structured-validation-truth-discovery
research_program_role: direct-test
status: open
tags:
- validation
- ontology
- property-constraints
title: Ontological Property Constraints Detect Semantically Invalid Content That Syntactic
  Validation Misses
uses:
- formal-ontology
- bayesian-inference
---

## Formal Statement
Ontological property constraints (domain/range, cardinality, type restrictions) detect semantically invalid content that syntactic or purely statistical validation cannot catch.

## Motivation
Syntactic validity does not imply semantic validity; ontology supplies the constraints that distinguish well-formed-but-wrong from valid.

## Current Evidence
[To be filled]

## Open Questions
Which constraint classes yield the most catch per authoring cost? False-positive rate on valid edge cases?

## Connections
- [[bayesian-inference]] — uses: validation confidence is probabilistic
- [[formal-ontology]] — uses: property constraints are ontological axioms
- [[structured-validation-truth-discovery]] — belongs-to: constituent hypothesis of the structured-validation-truth-discovery cluster