---
id: "pkis:technique:coordinate-ascent-vi"
aliases: ["CAVI"]
title: "Coordinate Ascent Variational Inference (CAVI)"
knowledge_type: technique
also_type: []
domain: [bayesian-stats, optimization]
tags: [variational-methods, approximate-inference, optimization, coordinate-ascent]
related_concepts: ["[[variational-inference]]", "[[mean-field-approximation]]", "[[elbo]]", "[[em-algorithm]]"]
sources: ["[[blei-vi-review]]", "[[ganguly-intro-vi]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

The canonical optimization algorithm for mean-field variational inference: iteratively update each variational factor q_j(z_j) to its optimal form — q*_j(z_j) ∝ exp(E_{-j}[log p(z,x)]) — holding all other factors fixed, until the ELBO converges; equivalent to coordinate ascent on the ELBO in the space of mean-field factorizations.

## Connections

- [[variational-inference]] — specializes: CAVI is the standard optimization algorithm for mean-field VI
- [[mean-field-approximation]] — uses: CAVI is only applicable when the variational family is mean-field factorized
- [[elbo]] — uses: CAVI maximizes the ELBO by iterating closed-form coordinate updates
- [[em-algorithm]] — commonly-confused-with: both are iterative algorithms with E-step and M-step analogues; EM computes exact conditional expectations, CAVI computes expectations under the variational approximation; EM guarantees global likelihood improvement, CAVI guarantees ELBO improvement

## Reading Path

- [[blei-vi-review]] (unread) — Section 2.4; full derivation of CAVI update from ELBO; Algorithm 1; convergence properties; complete GMM example in Section 3
- [[ganguly-intro-vi]] (unread) — Section 5; CAVI for Gaussian mixture (Algorithm 1); demonstrates convergence within ~60 iterations for 3-component GMM
