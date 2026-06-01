---
aliases: []
cluster_membership:
- intensional-grounding
- scaling-foil
contrasts-with:
- scaling-laws
date_created: 2026-05-30
date_updated: 2026-05-30
dependent_nodes:
- node: '[[named-entity-disambiguation]]'
  node_type: technique
  rationale: NED is the task being evaluated
- node: '[[scaling-laws]]'
  node_type: result
  rationale: The hypothesis is a direct challenge to scaling law predictions — requires
    understanding what scaling laws predict for NED tasks
domain:
- knowledge-representation
- deep-learning
evidence_nodes: []
id: pkis:hypothesis:intensional-grounding-vs-scale
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: intensional-grounding
research_program_role: boundary-condition
status: open
tags:
- named-entity-disambiguation
- scaling-foil
- compute-efficiency
title: Ontological Type Constraints Reduce Entity Resolution Errors More Than Equivalent
  Compute Scaling
uses:
- named-entity-disambiguation
---

## Formal Statement
Providing ontological type constraints at inference time reduces entity resolution errors by a greater margin than increasing model size by the compute-equivalent cost of maintaining and querying the ontological structure.

## Motivation
The scaling foil is the central null hypothesis of the research program. This hypothesis tests it directly at the entity resolution task. If true, it provides the strongest possible argument for ontological investment.

## Current Evidence
Neurosymbolic AI as an Antithesis to Scaling Laws (PNAS Nexus 2025) provides empirical support for the general claim that neurosymbolic approaches achieve comparable performance to scaled purely neural approaches at substantially lower parameter count.

## Open Questions
How to equate compute costs across the ontological maintenance + query path vs. the additional model parameters path. Whether the result generalizes beyond the specific entity types in the financial domain.

## Connections
- [[scaling-laws]] — contrasts-with: The hypothesis is a direct challenge to scaling-law predictions: ontological scaffolding beats compute-equivalent scaling.
- [[named-entity-disambiguation]] — uses: Entity resolution / NED is the task on which ontological constraints are compared against compute scaling.
- [[intensional-grounding]] — belongs-to: constituent hypothesis
- [[scaling-foil]] — belongs-to: also a direct test of the scaling foil null hypothesis