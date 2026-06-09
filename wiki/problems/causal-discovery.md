---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- statistical-learning
id: pkis:problem:causal-discovery
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch02
tags:
- structure-learning
- constraint-based
- score-based
- bayesian-networks
title: Causal Discovery
understanding: 0
---

## Definition
The problem of recovering the causal structure (a DAG or an equivalence class of DAGs) that generated a body of data, ideally from nonexperimental observations alone. Pearl frames it as an inductive game scientists play against Nature: Nature holds a stable acyclic system of deterministic functional mechanisms with independent disturbances, exposes only the distribution P[O] over an observed subset O of variables, and the scientist must reconstruct the topology D. Two broad solution families exist: (1) constraint-based methods (IC, PC, IC*) that read patterns of conditional independence off the data and piece together compatible structures; and (2) score-based / Bayesian methods (Cooper-Herskovits, Heckerman, TETRAD's Bayesian scoring) that assign priors to candidate networks and search for the highest-posterior structure. Both implicitly rely on minimality (a preference for less elaborate, more falsifiable theories) and stability/faithfulness (no accidental independencies). Without such restrictions the problem is hopeless: unboundedly many latent-variable models fit any P[O], and any complete acyclic ordering can mimic any distribution. With them, certain dependence patterns force unambiguous causal conclusions, and effective algorithms recover the structure up to Markov-equivalence (the pattern), with latent-variable extensions recovering valid fragments. Empirically Pearl reports networks of tens of variables recovered from fewer than ~5,000 samples in 1990 simulations, and corn->hog price directionality recovered from Wright's 1925 data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]