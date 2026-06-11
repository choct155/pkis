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
- machine-learning
- Bayesian-statistics
id: pkis:technique:sparse-gp-inducing-points
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch17
- murphy-pml2-advanced-ch18
tags:
- sparse GP
- inducing points
- variational inference
- scalable GP
- pseudo-inputs
title: Sparse GP via Inducing Points
understanding: 0
---

## Definition
A **sparse GP** replaces the $N$ training inputs $X$ with $M \ll N$ learned **inducing points** (pseudo-inputs) $Z$. The latent function values at $Z$, denoted $f_Z$, serve as a sufficient summary:
$$p(f|f_X) \approx p(f|f_Z).$$
Optimising $(Z, f_Z)$ jointly (often via variational inference) reduces GP training from $O(N^3)$ to $O(NM^2+M^3)$ and prediction from $O(N)$ to $O(M)$.

### Why it matters
Sparse GPs make nonparametric Bayesian function estimation practical for large datasets ($N \sim 10^4$–$10^6$). The variational approach (FITC/VFE) provides a rigorous lower bound on the marginal likelihood, enabling principled selection of inducing points and hyperparameters simultaneously.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]