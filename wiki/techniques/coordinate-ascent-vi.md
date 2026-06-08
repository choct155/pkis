---
aliases:
- CAVI
also_type: []
component_scores:
  alternatives: 4
  conditions: 3
  diagnostics: 3
  failure_modes: 3
  implementation: 3
  operational_mechanism: 4
  principled_mechanism: 4
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-07'
domain:
- bayesian-stats
- optimization
id: pkis:technique:coordinate-ascent-vi
instantiates:
- variational-free-energy
knowledge_type: technique
maturity: settled
related_concepts:
- '[[variational-inference]]'
- '[[mean-field-approximation]]'
- '[[elbo]]'
- '[[em-algorithm]]'
score_date: '2026-06-07'
sources:
- '[[blei-vi-review]]'
- '[[ganguly-intro-vi]]'
tags:
- variational-methods
- approximate-inference
- optimization
- coordinate-ascent
title: Coordinate Ascent Variational Inference (CAVI)
understanding: 3
---

The canonical optimization algorithm for mean-field variational inference: iteratively update each variational factor q_j(z_j) to its optimal form — q*_j(z_j) ∝ exp(E_{-j}[log p(z,x)]) — holding all other factors fixed, until the ELBO converges; equivalent to coordinate ascent on the ELBO in the space of mean-field factorizations.

## Connections
- [[variational-free-energy]] — instantiates: EM/soft K-means is coordinate descent on the variational free energy (Neal & Hinton).

- [[variational-inference]] — specializes: CAVI is the standard optimization algorithm for mean-field VI
- [[mean-field-approximation]] — uses: CAVI is only applicable when the variational family is mean-field factorized
- [[elbo]] — uses: CAVI maximizes the ELBO by iterating closed-form coordinate updates
- [[em-algorithm]] — commonly-confused-with: both are iterative algorithms with E-step and M-step analogues; EM computes exact conditional expectations, CAVI computes expectations under the variational approximation; EM guarantees global likelihood improvement, CAVI guarantees ELBO improvement

## Reading Path

- [[blei-vi-review]] (unread) — Section 2.4; full derivation of CAVI update from ELBO; Algorithm 1; convergence properties; complete GMM example in Section 3
- [[ganguly-intro-vi]] (unread) — Section 5; CAVI for Gaussian mixture (Algorithm 1); demonstrates convergence within ~60 iterations for 3-component GMM

## Intuition
The mean field assumption does not constrain how you move across the posterior landscape — it constrains which landscape you're allowed to search in the first place. You commit upfront to the submanifold of fully factorized distributions, then CAVI finds the best point on that submanifold via coordinate ascent. The optimization may converge correctly and still be far from the true posterior, because the true posterior may not be close to anything on your submanifold.

Analogy: you've agreed to model wind across a region as a single uniform vector, then you optimize what that vector should be. CAVI finds the best uniform vector. But if the actual field has a hurricane in one corner, no amount of optimization recovers it — the representational commitment was made before the search began.