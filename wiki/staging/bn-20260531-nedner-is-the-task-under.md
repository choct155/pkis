---
date_created: '2026-05-31'
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- named-entity-disambiguation (technique — NED/NER, entity resolution across surface
  variation)
- intensional-grounding
- intensional-grounding-ned-accuracy
- intensional-grounding-vs-scale
origin: conversation
proposed_edge_type: prerequisite-of
proposed_edges: []
rationale: 'NED/NER is THE task under test for this cluster — both hypotheses name
  it as a dependent node and the cluster calls the NED-accuracy prediction ''the most
  directly testable claim, to be instrumented first.'' Direction: named-entity-disambiguation
  is prerequisite-of intensional-grounding, ned-accuracy, and vs-scale. NOTE: this
  technique node does not yet exist; mint it as a technique stub (domains: knowledge-representation,
  deep-learning) at commit.'
resolution_candidates:
  named-entity-disambiguation (technique — NED/NER, entity resolution across surface variation):
  - pkis:research-cluster:intensional-grounding
  - pkis:hypothesis:intensional-grounding-vs-scale
  - pkis:research-cluster:evaluation-infrastructure
review_status: pending
source_context: Wiring the intensional-grounding cluster into the corpus graph so
  frontier/queue prioritization can see its dependencies.
staged_at: '2026-05-31T17:01:08Z'
staged_by: mcp-create-bridge-note
staged_id: e4c43f09-ec71-4a3e-8379-e8249faa8a84
status: unreviewed
title: Named Entity Disambiguation is prerequisite-of the Intensional Grounding cluster
  and its hypotheses
---

## Connection
NED/NER is THE task under test for this cluster — both hypotheses name it as a dependent node and the cluster calls the NED-accuracy prediction 'the most directly testable claim, to be instrumented first.' Direction: named-entity-disambiguation is prerequisite-of intensional-grounding, ned-accuracy, and vs-scale. NOTE: this technique node does not yet exist; mint it as a technique stub (domains: knowledge-representation, deep-learning) at commit.

## Nodes Involved
- [[named-entity-disambiguation (technique — NED/NER, entity resolution across surface variation)]]
- [[intensional-grounding]]
- [[intensional-grounding-ned-accuracy]]
- [[intensional-grounding-vs-scale]]

## Integration Notes
Pending review.
