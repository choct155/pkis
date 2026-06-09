---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- knowledge-representation
id: pkis:technique:grounding-unrolling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch15
tags:
- relational-probability-model
- variable-elimination
- lifted-inference
- propositionalization
- inference
title: Grounding (Unrolling)
understanding: 0
---

## Definition
The most direct inference strategy for relational and open-universe probability models: instantiate the model's dependency statements over all known typed constants to build the equivalent ground Bayesian network, then run standard inference. Grounding is the probabilistic analog of propositionalization in first-order logical inference. Its drawback is that the unrolled network can be enormous (and unknown relations can give variables many parents), so practical systems avoid full grounding by (1) instantiating only variables relevant to the query and evidence (non-ancestors and conditionally independent variables are irrelevant); (2) caching identical repeated factors during variable elimination; (3) for relational uncertainty, sampling complete worlds with MCMC so structure is fixed per state; and (4) lifted inference, which manipulates whole sets of indistinguishable ground factors at once, doing the work of many ground steps.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]