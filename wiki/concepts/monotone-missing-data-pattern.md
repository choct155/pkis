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
id: pkis:concept:monotone-missing-data-pattern
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch18
tags:
- missing-data
- imputation
- bayesian-computation
- factorization
- survey-sampling
title: Monotone Missing-Data Pattern
understanding: 0
uses:
- data-augmentation
- sufficient-statistics
---

## Definition
A structure of missingness in which the variables can be ordered into blocks y_1, y_2, ..., y_k such that each block is 'more observed' than the next — y_1 is present whenever y_2 is present (but not necessarily conversely), y_2 is present whenever y_3 is, and so on — so the observed/missing boundary forms a staircase. This pattern is computationally privileged because it factorizes the likelihood into k independent pieces, log p(y_obs | psi) = sum_j log p(y_obs_j | y_obs_1,...,y_obs_{j-1}, psi_j), where psi_j parameterizes the conditional distribution of block j given the preceding (more observed) blocks (for multivariate normal data, psi_j is the regression of y_j on y_1,...,y_{j-1}). Under a correspondingly factored prior, one can draw *directly* from the incomplete-data posterior p(omega | y_obs) in sequence — sample psi_1, then psi_2 | psi_1, and so forth — with no iterative imputation needed, and EM mode-finding collapses to one calculation per pattern rather than per observation. Real datasets are often nearly but not exactly monotone (e.g. some survey questions simply not asked in some surveys). For these, a *monotone data augmentation* algorithm imputes only the few values needed to complete the monotone staircase, then exploits the direct posterior draw; this is typically more efficient than ordinary data augmentation when the departure from monotonicity is small, since fewer values are imputed and analytic draws replace simulation. A simple variable ordering heuristic: place the variable with the fewest missing values first, the next-fewest second, and so on.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sufficient-statistics]] — uses: The monotone factorization of the likelihood into block-conditional pieces lets EM operate on per-pattern expected sufficient statistics rather than per-observation.
- [[data-augmentation]] — uses: Monotone data augmentation imputes only the values needed to complete the monotone staircase, then draws directly from the factorized posterior.
[To be populated during integration]