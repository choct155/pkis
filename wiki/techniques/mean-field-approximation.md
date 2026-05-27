---
id: "pkis:technique:mean-field-approximation"
aliases: []
title: "Mean-Field Variational Approximation"
knowledge_type: technique
also_type: []
domain: [bayesian-stats, optimization]
tags: [variational-methods, approximate-inference, probability-theory]
related_concepts: ["[[variational-inference]]", "[[elbo]]", "[[coordinate-ascent-vi]]"]
sources: ["[[blei-vi-review]]", "[[ganguly-intro-vi]]", "[[sjolund-parametric-vi]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

A variational inference approach that assumes the variational posterior fully factorizes over the latent variables: q(z) = ∏_j q_j(z_j), with each factor governed independently; this independence assumption makes ELBO optimization tractable via coordinate ascent but can systematically underestimate posterior variance.

## Connections

- [[variational-inference]] — specializes: mean-field is the classical and most studied sub-family of VI
- [[elbo]] — uses: mean-field CAVI iteratively maximizes the ELBO by optimizing each factor q_j in closed form
- [[coordinate-ascent-vi]] — uses: mean-field factorization enables coordinate ascent because each factor's optimal form is the unnormalized geometric mean of the complete conditional
- [[em-algorithm]] — commonly-confused-with: EM's E-step and mean-field CAVI have similar iterative structure, but EM uses exact conditional expectations while mean-field uses approximate factorized ones

## Reading Path

- [[blei-vi-review]] (unread) — authoritative treatment; Section 2.3–2.4; CAVI derivation for general exponential families; known limitation of variance underestimation
- [[ganguly-intro-vi]] (unread) — Section 4; introduces mean-field family; Section 5 works through CAVI on Gaussian mixture toy problem
- [[sjolund-parametric-vi]] (unread) — Section on modeling; contrasts mean-field (historical) with parametric/neural-network approach (modern); highlights mean-field's limited applicability
