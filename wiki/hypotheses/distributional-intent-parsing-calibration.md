---
aliases: []
cluster_membership:
- parsed-intent-calibration
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[calibration]]'
  node_type: concept
  rationale: calibration of the parsed-intent distribution is the criterion
- node: '[[bayesian-inference]]'
  node_type: concept
  rationale: the parse is a posterior over query meaning
- node: '[[formal-ontology]]'
  node_type: concept
  rationale: type constraints come from the ontology
domain:
- knowledge-representation
- bayesian-stats
evidence_nodes: []
id: pkis:hypothesis:distributional-intent-parsing-calibration
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: parsed-intent-calibration
research_program_role: direct-test
status: open
tags:
- intent-parsing
- calibration
- distributional
title: Distributional Query Parsing With Ontological Type Constraints Is Better Calibrated
  Than Point-Estimate Parsing
---

## Formal Statement
Producing a distribution over structured intent representations (constrained by ontological types) is better calibrated than emitting a single point-estimate parse.

## Motivation
A point estimate discards the uncertainty that downstream stages need; a typed distribution carries it explicitly.

## Current Evidence
[To be filled]

## Open Questions
How to elicit a faithful distribution from an LLM parser? What calibration metric over structured objects?

## Connections
- [[parsed-intent-calibration]] — belongs-to: constituent hypothesis of the parsed-intent-calibration cluster