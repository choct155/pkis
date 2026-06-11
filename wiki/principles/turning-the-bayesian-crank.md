---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- bayesian-inference
- probabilistic-programming
- methodology
id: pkis:principle:turning-the-bayesian-crank
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch07
tags:
- bayesian-workflow
- inference-engine
- probabilistic-programming
- separation-of-concerns
title: Turning the Bayesian Crank
understanding: 0
---

## Definition
The principle that probabilistic model specification and posterior inference can be cleanly separated: a researcher defines the model (likelihood + prior) and hands it to a generic inference engine, which automatically computes (approximate) posteriors without model-specific derivations.

### Why it matters
This separation-of-concerns ideal underpins probabilistic programming languages (Stan, PyMC, Pyro) and general-purpose inference libraries. It allows domain experts to iterate rapidly on model structure while inference is handled by reusable, well-tested algorithms (MCMC, VI, Laplace). The limiting factors are computational cost and the risk that a generic engine misses model-specific structure that would enable faster, more accurate inference.

### Historical context
The phrase captures the Bayesian workflow articulated in texts like Gelman et al. (BDA) and is the philosophical motivation for universal approximate inference methods such as ADVI, NUTS, and SMC samplers.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]