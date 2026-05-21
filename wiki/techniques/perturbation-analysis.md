---
title: "Perturbation Analysis"
knowledge_type: technique
also_type: []
domain: [formal-methods, systems-theory, optimization]
tags: [perturbation-analysis, ipa, gradient-estimation, sensitivity-analysis, simulation, stochastic-optimization, discrete-event-systems]
related_concepts: [discrete-event-systems, discrete-event-simulation, markov-chains, generalized-semi-markov-process]
sources: ["[[cassandras-des-intro]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Perturbation analysis (PA) is a technique for estimating the gradient (sensitivity) of a DES performance measure with respect to a parameter directly from a single simulation sample path, avoiding the cost of multiple finite-difference simulation runs; Infinitesimal Perturbation Analysis (IPA) propagates event-time derivatives through the sample path and, under a regularity condition, produces an unbiased gradient estimator.

## Reading Path
- [[cassandras-des-intro-ch11]] (unread) — primary treatment: IPA for GI/G/1 and stochastic timed automata, unbiasedness conditions, SPA for discontinuous cases, concurrent estimation, IPA for stochastic fluid models
