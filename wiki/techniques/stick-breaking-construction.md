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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
generalizes:
- pitman-yor-process
id: pkis:technique:stick-breaking-construction
instantiates:
- dirichlet-process
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch31
tags:
- dirichlet-process
- stick-breaking
- infinite-mixture
- variational-inference
- nonparametric-bayes
title: Stick-Breaking Construction
understanding: 0
uses:
- beta-distribution
---

## Definition
The stick-breaking construction (Sethuraman 1994) provides an explicit representation of a Dirichlet process draw as a countably infinite discrete distribution. Define:
$$
\beta_k \overset{\text{iid}}{\sim} \mathrm{Beta}(1,\alpha), \quad \pi_k = \beta_k \prod_{j=1}^{k-1}(1-\beta_j), \quad \theta_k \overset{\text{iid}}{\sim} H,
$$
then $G = \sum_{k=1}^{\infty} \pi_k \delta_{\theta_k} \sim \mathrm{DP}(\alpha, H)$.

The name arises from the metaphor of breaking a unit-length stick: at each step one breaks fraction $\beta_k$ off the remaining piece to form weight $\pi_k$.

### Why it matters
The stick-breaking representation makes the Dirichlet process amenable to variational inference and truncated approximations. It also generalises: replacing $\mathrm{Beta}(1,\alpha)$ with other distributions yields Pitman-Yor and other richer priors.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[pitman-yor-process]] — generalizes
- [[beta-distribution]] — uses
- [[dirichlet-process]] — instantiates
[To be populated during integration]