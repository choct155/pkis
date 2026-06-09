---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- social-science-methods
id: pkis:concept:observational-equivalence-sem
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch05
tags:
- model-equivalence
- testability
- d-separation
- v-structures
- saturated-models
title: Observational (Covariance) Equivalence of Structural Models
understanding: 0
---

## Definition
Two structural equation models are observationally equivalent if every distribution one can generate the other can too; for linear-normal data this is covariance equivalence. Theorem 5.2.6: two Markovian linear-normal models are covariance equivalent iff they entail the same zero partial correlations, equivalently iff their graphs share the same edges and the same v-structures (colliders). Consequences: (a) the testable statistical content of a Markovian SEM is exactly the set of zero partial correlations readable by d-separation — one never tests a single model but a whole equivalence class, constructible by inspection by reversing arrows that preserve v-structures (Meek/Chickering: X->Y can be reversed iff all parents of X are parents of Y); (b) the number of local tests needed equals the number of missing edges (sparser graph => more constraints). In semi-Markovian models (correlated errors) zero-partial-correlation equivalence is only necessary, not sufficient, for covariance equivalence, and edge-replacement rules become subtle (v-structures may involve latent variables; remote ancestors matter). Pearl argues the inevitable existence of equivalent models (because causation is not derivable from data alone) does NOT make causal modeling useless — moving from qualitative premises to quantitative coefficients is still informative for policy.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]