---
aliases: []
cluster_membership:
- evaluation-infrastructure
date_created: '2026-06-01'
date_updated: '2026-06-07'
dependent_nodes:
- node: '[[causal-analysis]]'
  node_type: concept
  rationale: valid experimental design and attribution require identification and
    confounding control
domain:
- knowledge-representation
- deep-learning
evidence_nodes: []
id: pkis:hypothesis:domain-specific-benchmark-gap
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: evaluation-infrastructure
research_program_role: enabling-condition
status: open
tags:
- evaluation
- benchmark
- ned
- financial-data
title: Standard NLP Benchmarks Do Not Adequately Evaluate Ontology-Augmented NED/NER
  and Composite Result Quality
uses:
- causal-analysis
---

## Formal Statement
Standard NLP/ML benchmarks do not adequately evaluate ontology-augmented NED/NER or composite-result quality in financial data manufacturing; purpose-built or adapted evaluation methodology is therefore a prerequisite for the program's experiments.

## Motivation
Every other cluster's claims are only testable against measurements this cluster must define. Without fit-for-purpose benchmarks, apparent gains cannot be attributed to ontological structure versus dataset artifacts.

## Current Evidence
[To be filled]

## Open Questions
What gold-standard construction is feasible for financial entities? How to isolate ontology contribution from base-model capability?

## Connections
- [[causal-analysis]] — uses: benchmark validity rests on sound experimental design and attribution
- [[evaluation-infrastructure]] — belongs-to: constituent hypothesis of the evaluation-infrastructure cluster

## Task Grounding
Mechanism claim: standard NLP benchmarks do not measure the right things for ontology-augmented financial data manufacturing.

Task outcome claim: systems that perform well on standard benchmarks may perform poorly on private markets tasks, and vice versa. Purpose-built evaluation methodology is required to detect real performance differences.

Deployment context: research program validation — without appropriate benchmarks, the program cannot determine whether its hypotheses are confirmed or disconfirmed.

Why the scale foil fails at the task level: GLUE and SuperGLUE performance improvements on large models do not predict performance on structured financial document tasks. The tasks are categorically different in input structure, output requirements, and error consequences.