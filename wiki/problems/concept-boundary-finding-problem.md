---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-14'
date_updated: '2026-06-14'
domain:
- knowledge-representation
id: pkis:problem:concept-boundary-finding-problem
knowledge_type: problem
linked_nodes: []
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- ganter-formal-1999
- gruninger-methodology-1995
- shimizu-modular-2023
- giglou-llms4ol-2024
tags:
- boundary-finding
- ontology-engineering
- granularity
- instantiation-depth
- formal-concept-analysis
- competency-questions
title: Concept Boundary Finding Problem
understanding: 0
---

## Definition
The concept boundary finding problem is the challenge of determining, in a principled and computable way, what content a knowledge graph node should contain — where one knowledge unit ends and the next begins.

## Why This Is Hard

Boundary finding has two distinct failure modes with different detection signals and different interventions:

**Over-specification (boundary too narrow)**: The node contains only part of what is needed to understand the concept. Queries that should be satisfied by the node consistently require additional retrieval from semantically adjacent nodes. Signal: high residual coverage gap after node retrieval. Related to instantiation depth H(c|node) > 0.

**Under-specification (boundary too wide)**: The node contains content that belongs to adjacent concepts, creating overlap and potential duplication. Signal: high embedding similarity between two nodes; shared competency questions; high content overlap detected by intersection computation across canonical sources.

## The Lumping/Splitting Tradeoff

Boundary decisions are not resolvable from concept content alone. They require a theoretical framework that determines what constitutes 'the same knowledge unit' — the analog of a species concept in biological taxonomy. Without such a criterion, lumping and splitting decisions are made artistically by ontologists rather than systematically.

The arity constraint: a concept that is a prerequisite for multiple other concepts should not be absorbed into any one of its dependents, regardless of co-occurrence frequency. The arity of the prerequisite relationship is diagnostic — high arity favors a standalone node.

## Disciplinary Framing Variance

Independent canonical sources covering the same concept may define different boundaries due to disciplinary framing. MacKay's coding-theoretic treatment of entropy and a statistician's estimation-theoretic treatment carve the same conceptual territory differently. Neither is wrong; they are different formal contexts in the FCA sense. Resolution strategy: take the intersection of content claims across sources as the minimum scope (computable if claim comparison is tractable); represent framing-specific extensions as typed annotations rather than core node content.

## Relationship to Formal Concept Analysis

FCA provides the closest existing formal criterion: a concept is well-bounded when no attribute can be added without losing objects from the extent, and no object can be added without losing attributes from the intent (the maximal rectangle condition). This operates at the schema level; translation to content-level knowledge units requires a formal context definition for knowledge nodes — an open problem.

## Relationship to Competency Questions

The minimum scope of a concept node is the content required to answer all competency questions (queries in C(q)) that depend on that concept. Content beyond this minimum is optional extension. Content below this minimum produces coverage gaps. This provides a use-driven boundary criterion that complements the structure-driven FCA criterion.

## Open Questions

- What is the formal context definition that allows FCA closure operators to be applied to knowledge content rather than schema-level attributes?
- Can intersection computation across canonical sources be automated to a degree that reduces ontologist decisions to binary accept/reject of pre-computed proposals?
- What is the formal criterion for 'the same knowledge unit' — the species concept analog for PKIS nodes?
- How do boundary errors propagate through the graph? A node whose boundary is incorrectly drawn affects all queries that traverse it and all nodes connected to it.
- Is there a computable granularity diagnostic (analogous to class granularity in schema ontologies) for content-level knowledge nodes?

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]