---
date_created: '2026-06-13'
id: pkis:bridge-note:bn-20260613-the-retrieval-efficiency-argument-has
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- concept-typed-nodes-dominate-document-nodes-on-coverage
- compositional-query-grounding
- intensional-grounding
origin: conversation
proposed_edge_type: extends
rationale: 'The retrieval efficiency argument has been developed at the level of concept
  nodes versus document nodes. But the full ontological representation has a second
  stratum: the instance layer. A query may need not the concept of a company but a
  specific company — Apple Inc., a specific fund, a specific filing. This is the knowledge
  graph layer of named entities and their relationships, distinct from the conceptual
  coverage layer. Instance coverage contributes to retrieval in a different way: concept
  nodes answer "what is X" and "how does X relate to Y conceptually"; instance nodes
  answer "which specific X satisfies these constraints" and "what are the properties
  of this specific entity." Both layers contribute to query coverage C(q) but through
  different mechanisms. The efficiency argument applies to both layers but the formalization
  differs — instance retrieval is more like entity resolution and property lookup
  than conceptual coverage accumulation. This layer is not yet formalized in the efficiency
  argument and should be treated as a parallel extension alongside the edge information
  content open problem.'
source_context: Conversation on retrieval efficiency — ontological representation
  beyond concept nodes
status: unreviewed
title: Instance layer as distinct graph stratum from concept layer
---

## Connection
The retrieval efficiency argument has been developed at the level of concept nodes versus document nodes. But the full ontological representation has a second stratum: the instance layer. A query may need not the concept of a company but a specific company — Apple Inc., a specific fund, a specific filing. This is the knowledge graph layer of named entities and their relationships, distinct from the conceptual coverage layer. Instance coverage contributes to retrieval in a different way: concept nodes answer "what is X" and "how does X relate to Y conceptually"; instance nodes answer "which specific X satisfies these constraints" and "what are the properties of this specific entity." Both layers contribute to query coverage C(q) but through different mechanisms. The efficiency argument applies to both layers but the formalization differs — instance retrieval is more like entity resolution and property lookup than conceptual coverage accumulation. This layer is not yet formalized in the efficiency argument and should be treated as a parallel extension alongside the edge information content open problem.

## Nodes Involved
- [[concept-typed-nodes-dominate-document-nodes-on-coverage]]
- [[compositional-query-grounding]]
- [[intensional-grounding]]

## Integration Notes
Pending review.