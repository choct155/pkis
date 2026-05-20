---
title: "Gaussian Mixture Models (GMM)"
knowledge_type: technique
also_type: [framework]
domain: [bayesian-stats, statistical-learning]
tags: [probability-theory, simulation]
related_concepts: ["[[gaussian-distribution]]", "[[em-algorithm]]", "[[probability-theory]]"]
sources: ["[[deisenroth-mml]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Density estimation model that represents the data distribution as a weighted sum of Gaussian components $p(x) = \sum_k \pi_k \mathcal{N}(x | \mu_k, \Sigma_k)$, fit via the EM algorithm; serves as both a generative model and a soft-clustering technique.
