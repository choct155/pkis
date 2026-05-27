---
id: "pkis:problem:intractable-posterior"
aliases: []
title: "Intractable Posterior Inference"
knowledge_type: problem
also_type: []
domain: [bayesian-stats]
tags: [probability-theory, approximate-inference, variational-methods]
related_concepts: ["[[variational-inference]]", "[[probability-theory]]", "[[directed-graphical-models]]"]
sources: ["[[blei-vi-review]]", "[[ganguly-intro-vi]]", "[[sjolund-parametric-vi]]", "[[kroese-statistical-modeling]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 4
understanding: 0
maturity: settled
---

The core challenge of Bayesian statistics: computing the posterior p(z|x) = p(x,z)/p(x) requires evaluating the marginal likelihood p(x) = ∫ p(x|z)p(z)dz, which is intractable for most interesting models because the integral is over all configurations of latent variables and has no closed form; this intractability motivates both MCMC sampling and variational inference as approximate inference strategies.

## Connections

- [[variational-inference]] — addresses: VI converts the integration problem into an optimization problem by searching for the best approximate posterior
- [[em-algorithm]] — addresses: EM bypasses computing p(x) by iteratively lower-bounding it; works when the complete conditional is tractable
- [[directed-graphical-models]] — uses: the graphical structure determines which models admit tractable posteriors vs. which require approximation
- [[probability-theory]] — prerequisite-of: understanding why the marginal likelihood is intractable requires knowledge of probability distributions and integration

## Reading Path

- [[blei-vi-review]] (unread) — Section 2.1; precise statement of the approximate inference problem; MCMC vs. VI comparison
- [[ganguly-intro-vi]] (unread) — Section 2; problem statement for latent variable models; why exact inference is NP-hard on arbitrary graphical models
- [[sjolund-parametric-vi]] (unread) — Introduction; concise framing: the marginal likelihood integral is intractable, VI replaces it with a tractable lower bound
- [[kroese-statistical-modeling-ch07]] (unread) — motivates MCMC as the computational response to intractable posteriors; complementary to VI treatments above
