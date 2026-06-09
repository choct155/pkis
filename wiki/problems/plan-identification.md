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
- bayesian-stats
id: pkis:problem:plan-identification
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch04
tags:
- causality
- plans
- sequential-decisions
- back-door
- time-varying-confounding
- identification
- pearl
- robins
title: Plan Identification (Sequential Back-Door)
understanding: 0
---

## Definition
The problem of evaluating a **sequential plan** — a time-ordered set of actions (x̂1,…,x̂n), each possibly influenced by earlier actions and observations — from passive observational data, in the presence of unmeasured confounders, some of which (e.g. intermediate covariate Z) are themselves affected by earlier control variables. Known in epidemiology as 'time-varying treatment with time-varying confounders' (Robins 1993); in AI it lets one agent learn to act by watching another whose decision rules are hidden. A central insight (Pearl & Robins 1995): a plan must be analyzed into its constituent actions — treating X1,X2 as a single compound variable creates a spurious bow pattern (via U) that signals nonidentifiability, even though the joint plan P(y|x̂1,x̂2) *is* identifiable. The naive habit of adjusting for an intermediate confounder is a fatal error, since it blocks the very effect being estimated. The **sequential back-door criterion** (Theorem 4.4.1) gives identifiability: for each step k there is a covariate set Z_k of nondescendants of {X_k,…,X_n} d-separating Y from X_k in the mutilated graph, yielding the g-computation formula P(y|x̂1..x̂n) = Σ_z P(y|z,x) ∏_k P(z_k|z_{<k}, x_{<k}). Such plans are 'G-identifiable'; Corollary 4.4.5 gives an effective minimal-set algorithm and Theorem 4.4.6 a non-search variant, though both remain order-dependent (an admissible ordering may exist for one variable order and not another). G-identifiability is sufficient but not necessary for general identifiability (it refuses to condition on descendants of X_k, unlike the front-door criterion).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]