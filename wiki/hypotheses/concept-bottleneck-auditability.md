---
aliases: []
cluster_membership:
- learned-symbol-grounding
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[concept-bottleneck-models]]'
  node_type: technique
  rationale: the architecture under test
domain:
- deep-learning
evidence_nodes: []
id: pkis:hypothesis:concept-bottleneck-auditability
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: learned-symbol-grounding
research_program_role: boundary-condition
status: open
tags:
- concept-bottleneck
- auditability
- production
title: Concept Bottleneck Architectures Provide Sufficient Audit Trail for Production
  QA Workflows
uses:
- concept-bottleneck-models
---

## Formal Statement
Concept-bottleneck architectures expose a sufficient, human-interpretable audit trail to support production QA workflows.

## Motivation
The near-term production instantiation of learned symbol grounding stands or falls on whether its concept layer is auditable enough for QA.

## Current Evidence
[To be filled]

## Open Questions
Sufficiency relative to which QA tasks? Accuracy cost of the bottleneck.

## Connections
- [[concept-bottleneck-models]] — uses: the architecture under test
- [[learned-symbol-grounding]] — belongs-to: constituent hypothesis of the learned-symbol-grounding cluster