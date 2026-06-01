---
aliases: []
cluster_membership:
- retrieval-inference-tradeoff
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[decision-theory-foundations]]'
  node_type: concept
  rationale: routing is a decision under uncertainty
- node: '[[calibration]]'
  node_type: concept
  rationale: route confidence must be calibrated
domain:
- deep-learning
- bayesian-stats
evidence_nodes: []
id: pkis:hypothesis:routing-classifier-hypothesis
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: retrieval-inference-tradeoff
research_program_role: boundary-condition
status: open
tags:
- routing
- classifier
- query
title: A Lightweight Query Routing Classifier Can Reliably Distinguish Retrieval vs
  Inference vs Hybrid Paths
---

## Formal Statement
A lightweight classifier trained on query characteristics can reliably route queries among retrieval, inference, and hybrid execution paths.

## Motivation
The dominance result is only actionable if queries can be cheaply classified into the regime where retrieval wins.

## Current Evidence
[To be filled]

## Open Questions
Feature set for routing; cost of misroute vs cost of the classifier itself.

## Connections
- [[retrieval-inference-tradeoff]] — belongs-to: constituent hypothesis of the retrieval-inference-tradeoff cluster