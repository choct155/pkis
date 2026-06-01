---
aliases: []
cluster_membership:
- model-evolution
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[distribution-shift]]'
  node_type: concept
  rationale: drift is a special case of distribution shift
- node: '[[formal-ontology]]'
  node_type: concept
  rationale: the concepts being monitored are ontological
domain:
- deep-learning
- bayesian-stats
evidence_nodes: []
id: pkis:hypothesis:concept-drift-detection
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: model-evolution
research_program_role: boundary-condition
status: open
tags:
- concept-drift
- monitoring
- distribution-shift
title: Distributional Monitoring of Ontological Concept Usage Detects Semantic Drift
  Before Downstream Errors
---

## Formal Statement
Distributional monitoring of how ontological concepts are used detects semantic drift before it produces downstream errors.

## Motivation
Concept drift is a special case of distribution shift; catching it early prevents silent degradation of the ontology's referents.

## Current Evidence
[To be filled]

## Open Questions
Detection latency vs false-alarm rate; what usage signal is most drift-sensitive.

## Connections
- [[model-evolution]] — belongs-to: constituent hypothesis of the model-evolution cluster