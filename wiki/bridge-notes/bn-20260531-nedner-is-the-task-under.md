---
date_created: '2026-05-31'
id: pkis:bridge-note:bn-20260531-nedner-is-the-task-under
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
rationale: 'NED/NER is THE task under test for this cluster — both hypotheses name
  it as a dependent node and the cluster calls the NED-accuracy prediction ''the most
  directly testable claim, to be instrumented first.'' Direction: named-entity-disambiguation
  is prerequisite-of intensional-grounding, ned-accuracy, and vs-scale. NOTE: this
  technique node does not yet exist; mint it as a technique stub (domains: knowledge-representation,
  deep-learning) at commit.'
source_context: Wiring the intensional-grounding cluster into the corpus graph so
  frontier/queue prioritization can see its dependencies.
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