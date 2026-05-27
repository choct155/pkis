---
id: "pkis:concept:kl-divergence"
aliases: []
title: "Kullback-Leibler Divergence"
knowledge_type: concept
also_type: []
domain: [bayesian-stats, information-theory]
tags: [probability-theory, information-theory, variational-methods]
related_concepts: ["[[probability-theory]]", "[[elbo]]", "[[variational-inference]]"]
sources: ["[[blei-vi-review]]", "[[ganguly-intro-vi]]", "[[yellapragada-variational-bayes]]", "[[lange-applied-probability]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 4
understanding: 0
maturity: settled
---

An asymmetric non-negative measure of the "extra information" required to encode samples from distribution P using a code optimized for distribution Q: DKL(P‖Q) = E_P[log(P/Q)] ≥ 0, with equality iff P = Q; in variational inference, the reverse KL(q‖p) is minimized (zero-forcing, mode-seeking) while the forward KL(p‖q) would be zero-avoiding but requires access to p.

## Connections

- [[variational-inference]] — used-by: VI minimizes reverse KL(q‖p(z|x)) as its objective; the ELBO equals log p(x) minus this KL
- [[elbo]] — used-by: ELBO = log p(x) − KL(q‖p(z|x)); the KL gap is what ELBO maximization implicitly closes
- [[probability-theory]] — prerequisite-of: understanding KL requires measure-theoretic probability and information theory

## Reading Path

- [[blei-vi-review]] (unread) — Section 2.1; KL as the VI objective; discussion of why forward KL is intractable and reverse KL is tractable
- [[ganguly-intro-vi]] (unread) — Section 2; KL derivation; Figure 2 illustrates forward vs. reverse KL on bimodal distribution; zero-avoiding vs. zero-forcing behavior
- [[yellapragada-variational-bayes]] (unread) — Section 2.2; entropy and KL definitions; role in MDL loss formulation
- [[lange-applied-probability-ch16]] (unread) — entropy chapter grounds KL divergence in information-theoretic context
