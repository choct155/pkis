---
aliases: []
cross_cluster_dependencies:
- compositional-query-grounding
- parsed-intent-calibration
- composite-credibility
- evaluation-infrastructure
date_created: 2026-05-30
date_updated: '2026-06-01'
domain:
- knowledge-representation
- bayesian-stats
frontier_hypotheses:
- retrieval-dominates-inference-high-stakes-queries
hypotheses:
- retrieval-dominates-inference-high-stakes-queries
- routing-classifier-hypothesis
id: pkis:research-cluster:retrieval-inference-tradeoff
knowledge_type: research-cluster
origin: research-program
status: active
tags:
- retrieval
- inference-cost
- error-propagation
- routing
- cost-modeling
title: Retrieval-Inference Tradeoff
uses:
- expected-loss
- decision-theory-foundations
- calibration
---

## Thesis
For a well-defined class of queries answerable by deterministic lookup against a structured store, ontology-backed retrieval dominates stochastic model inference on the joint criterion of cost × error rate — and this dominance is most pronounced at the high-frequency, high-stakes queries where production systems need reliability most.

## Summary
The cost model must include not just compute cost per query but the expected cost of undetected error propagation. A knowledge graph query has recognizable failure modes. A model inference can produce a plausible-sounding wrong answer — the most dangerous case. The asymmetry in failure mode detectability is arguably more operationally important than raw cost. The routing problem is itself an interesting ML task.

## Research Program Context
Stage 7 (Routing & Retrieval) primary cluster. The expected-cost modeling framework is an identified open problem in the literature — a potential methodological contribution.

## Constituent Hypotheses
- **retrieval-dominates-inference-high-stakes-queries** — Ontology-backed retrieval dominates model inference on cost × error rate for a well-defined query class
- **routing-classifier-hypothesis** — A lightweight query routing classifier trained on query characteristics can reliably distinguish retrieval vs. inference vs. hybrid paths

## Current Frontier
Anchored to `expected-loss`, `decision-theory-foundations`, and `calibration`. Lead hypothesis **`retrieval-dominates-inference-high-stakes-queries`**: for a well-defined query class, ontology-backed retrieval dominates inference on cost x error rate, sharpest at high-frequency high-stakes queries. Supporting: **`routing-classifier-hypothesis`** (a lightweight classifier reliably routes retrieval vs inference vs hybrid). Coverage gaps: `expected-loss`, `decision-theory-foundations`, `calibration` are sourceless stubs.

## Connections
- [[calibration]] — uses: retrieval dominance depends on calibrated error rate estimates
- [[decision-theory-foundations]] — uses: the routing decision is a decision-theoretic problem
- [[expected-loss]] — uses: the cost model is an expected loss calculation
- [[expected-loss]] — uses: the cost model is an expected loss calculation
- [[decision-theory-foundations]] — uses: the routing decision is a decision-theoretic problem
- [[calibration]] — uses: retrieval dominance claim depends on calibrated error rate estimates