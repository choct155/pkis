---
id: "pkis:concept:elbo"
aliases: ["ELBO"]
title: "Evidence Lower Bound (ELBO)"
knowledge_type: concept
also_type: []
domain: [bayesian-stats, optimization]
tags: [variational-methods, probability-theory, information-theory]
related_concepts: ["[[variational-inference]]", "[[kl-divergence]]", "[[probability-theory]]"]
sources: ["[[blei-vi-review]]", "[[ganguly-intro-vi]]", "[[sjolund-parametric-vi]]", "[[yellapragada-variational-bayes]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 4
understanding: 0
maturity: settled
---

A lower bound on the log-evidence log p(x) defined as ELBO(q) = E_q[log p(z,x)] − E_q[log q(z)] = E_q[log p(x|z)] − KL(q(z)‖p(z)); the gap between log p(x) and the ELBO is exactly KL(q(z)‖p(z|x)), so maximizing the ELBO simultaneously minimizes KL divergence to the true posterior and provides a tractable proxy for model evidence.

## Connections

- [[variational-inference]] — used-by: the ELBO is the objective function maximized by all VI algorithms
- [[kl-divergence]] — uses: ELBO = log p(x) − KL(q‖p(z|x)); the KL gap is what ELBO maximization implicitly minimizes
- [[em-algorithm]] — equivalent-in-context: the EM algorithm's Q-function is the ELBO when the complete conditional is tractable; maximizing Q in the M-step is equivalent to maximizing the ELBO

## Reading Path

- [[blei-vi-review]] (unread) — canonical derivation; Equation (2) and Section 2.2; also proves ELBO = E_q[log p(z,x)] − E_q[log q(z)]
- [[ganguly-intro-vi]] (unread) — Section 3; derives ELBO via Jensen's inequality; intuitive explanation as regularized data fit
- [[sjolund-parametric-vi]] (unread) — Section on ELBO; Equation (7)–(8); shows ELBO maximization equivalence to KL minimization
- [[yellapragada-variational-bayes]] (unread) — Section 2.3; ELBO decomposed as energy + entropy: L(x) = E_q[log p(x,z)] + H(q)
