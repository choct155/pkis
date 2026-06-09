---
aliases: []
also_type: []
applies:
- structural-causal-models
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
contrasts-with:
- potential-outcomes-framework
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
uses:
- minimal-model-causation
- faithfulness-stability
- causal-markov-condition
- d-separation
---

## Definition
The problem of recovering the causal structure (a DAG or an equivalence class of DAGs) that generated a body of data, ideally from nonexperimental observations alone. Pearl frames it as an inductive game scientists play against Nature: Nature holds a stable acyclic system of deterministic functional mechanisms with independent disturbances, exposes only the distribution P[O] over an observed subset O of variables, and the scientist must reconstruct the topology D. Two broad solution families exist: (1) constraint-based methods (IC, PC, IC*) that read patterns of conditional independence off the data and piece together compatible structures; and (2) score-based / Bayesian methods (Cooper-Herskovits, Heckerman, TETRAD's Bayesian scoring) that assign priors to candidate networks and search for the highest-posterior structure. Both implicitly rely on minimality (a preference for less elaborate, more falsifiable theories) and stability/faithfulness (no accidental independencies). Without such restrictions the problem is hopeless: unboundedly many latent-variable models fit any P[O], and any complete acyclic ordering can mimic any distribution. With them, certain dependence patterns force unambiguous causal conclusions, and effective algorithms recover the structure up to Markov-equivalence (the pattern), with latent-variable extensions recovering valid fragments. Empirically Pearl reports networks of tens of variables recovered from fewer than ~5,000 samples in 1990 simulations, and corn->hog price directionality recovered from Wright's 1925 data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[potential-outcomes-framework]] — contrasts-with: Discovery learns structure from association under minimality/stability, vs. the manipulationist 'no causation without manipulation' stance it reframes as virtual control.
- [[structural-causal-models]] — applies: Discovery targets the SCM structure D underlying the data.
- [[d-separation]] — uses: Discovery reads observed independencies as d-separation conditions in the latent DAG.
- [[causal-markov-condition]] — uses: The Markov condition defines what a complete causal model is and is the object minimized.
- [[faithfulness-stability]] — uses: Stability guarantees a unique minimal structure (up to equivalence) and effective recovery.
- [[minimal-model-causation]] — uses: Minimality is the normative criterion selecting among structures that fit P[O].
[To be populated during integration]