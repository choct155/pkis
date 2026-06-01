---
aliases: []
cross_cluster_dependencies: []
date_created: 2026-05-30
date_updated: '2026-06-01'
domain:
- knowledge-representation
frontier_hypotheses:
- domain-specific-benchmark-gap
hypotheses:
- domain-specific-benchmark-gap
id: pkis:research-cluster:evaluation-infrastructure
knowledge_type: research-cluster
origin: research-program
status: active
tags:
- benchmarking
- evaluation-methodology
- domain-specific-evaluation
- nlp-benchmarks
title: Evaluation Infrastructure
uses:
- causal-analysis
---

## Thesis
Standard NLP and ML benchmarks do not exist for the specific tasks and evaluation criteria this research program requires — and building or adapting evaluation methodology is a prerequisite for the experimental program.

## Summary
GLUE, SuperGLUE, and standard NER benchmarks measure general language understanding, not domain-specific ontologically-grounded entity resolution. Required evaluation artifacts: entity resolution benchmark with deliberately ambiguous surface forms; query intent benchmark with implicit expansion cases; calibration evaluation framework for parsed intent distributions; composite result quality rubric.

## Research Program Context
Cross-cutting. A prerequisite for all experimental work. Building the benchmark is itself a potential methodological contribution independent of experimental findings.

## Constituent Hypotheses
- **domain-specific-benchmark-gap** — Standard NLP benchmarks do not adequately evaluate ontology-augmented NED/NER and composite result quality in financial data manufacturing

## Current Frontier
Anchored to `causal-analysis` (experimental-design foundation). Lead (and only) hypothesis **`domain-specific-benchmark-gap`**: standard NLP benchmarks don't evaluate ontology-augmented NED/NER or composite-result quality for financial data manufacturing, so building evaluation methodology is a prerequisite for the whole program. This cluster is a dependency of every other cluster, so it leads the program. Coverage gap: `causal-analysis` is a sourceless stub (needs a canonical source).

## Connections
- [[causal-analysis]] — uses: valid experimental design requires understanding identification and confounding
- [[causal-analysis]] — uses: valid experimental design requires understanding identification and confounding