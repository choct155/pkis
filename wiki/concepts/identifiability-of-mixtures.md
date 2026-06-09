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
- bayesian-stats
- statistical-learning
id: pkis:concept:identifiability-of-mixtures
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch22
tags:
- mixture-models
- identifiability
- prior-specification
- probability-theory
title: Identifiability of the Mixture Likelihood
understanding: 0
---

## Definition
The conditions under which the parameters of a finite (or continuous) mixture model are determined by the likelihood, and the canonical failures of identifiability specific to mixtures. Parameters are non-identified when the same likelihood function arises from more than one parameter value. Every finite mixture is non-identified in at least one trivial sense: the distribution is invariant to permutation of the component labels (the 'aliasing' / label-ambiguity that underlies label switching). Beyond label permutation, two further identification problems are characteristic: (1) *empty / vanishing components* — an improper or excessively diffuse prior on the mixing weights (e.g. Dirichlet with alpha_h = 0) is problematic when the data do not support all H components; (2) *degenerate variance modes* — with separate per-component variances and an improper prior on (log sigma_h), the posterior has spurious 'uninteresting' modes where one component collapses onto a single observation with zero variance, rendering the posterior improper. Remedies: restrict the parameter space to break the permutation symmetry (order the component means or mixing proportions), use an informative prior that ties specific components to specific subpopulations, and ensure propriety by fixing the ratio of variances or assigning a proper prior to the component variances. Identifiability is also restored in part by partial labels — observations whose component membership is known each contribute a factor with a fixed indicator. Identification failures surface diagnostically during computation: a Gibbs sampler started near zero variance may never escape, and chains may appear non-convergent purely because of aliasing across label permutations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]