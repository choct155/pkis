---
aliases: []
cluster_membership:
- retrieval-inference-tradeoff
date_created: '2026-06-01'
date_updated: '2026-06-01'
dependent_nodes:
- node: '[[expected-loss]]'
  node_type: concept
  rationale: the cost model is an expected-loss calculation
- node: '[[decision-theory-foundations]]'
  node_type: concept
  rationale: dominance is a decision-theoretic claim
- node: '[[calibration]]'
  node_type: concept
  rationale: the claim depends on calibrated error-rate estimates
domain:
- knowledge-representation
- bayesian-stats
evidence_nodes: []
id: pkis:hypothesis:retrieval-dominates-inference-high-stakes-queries
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: retrieval-inference-tradeoff
research_program_role: direct-test
status: open
tags:
- retrieval
- inference
- cost-error
- decision-theory
title: Ontology-Backed Retrieval Dominates Model Inference on Cost x Error Rate for
  a Well-Defined Query Class
uses:
- expected-loss
- decision-theory-foundations
- calibration
---

## Formal Statement
For a well-defined class of queries answerable by deterministic lookup against a structured store, ontology-backed retrieval dominates stochastic model inference on the joint cost x error-rate criterion, most pronounced at high-frequency, high-stakes queries.

## Motivation
Production systems need reliability where it is cheapest to provide; retrieval over a structured store is both cheaper and lower-error for lookup-answerable queries.

## Current Evidence
[To be filled]

## Open Questions
How to delimit the 'retrieval-answerable' query class operationally? How to price inference error in high-stakes settings?

## Connections
- [[calibration]] — uses: depends on calibrated error-rate estimates
- [[decision-theory-foundations]] — uses: dominance is a decision-theoretic claim
- [[expected-loss]] — uses: cost x error is an expected-loss calculation
- [[retrieval-inference-tradeoff]] — belongs-to: constituent hypothesis of the retrieval-inference-tradeoff cluster