---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- formal-methods
- systems-theory
- optimization
id: pkis:technique:perturbation-analysis
knowledge_type: technique
maturity: settled
related_concepts:
- discrete-event-systems
- discrete-event-simulation
- markov-chains
- generalized-semi-markov-process
sources:
- '[[cassandras-des-intro]]'
- cassandras-des-intro-ch11
tags:
- perturbation-analysis
- ipa
- gradient-estimation
- sensitivity-analysis
- simulation
- stochastic-optimization
- discrete-event-systems
title: Perturbation Analysis
understanding: 0
---

Perturbation analysis (PA) is a technique for estimating the gradient (sensitivity) of a DES performance measure with respect to a parameter directly from a single simulation sample path, avoiding the cost of multiple finite-difference simulation runs; Infinitesimal Perturbation Analysis (IPA) propagates event-time derivatives through the sample path and, under a regularity condition, produces an unbiased gradient estimator.

## Reading Path
- [[cassandras-des-intro-ch11]] (unread) — primary treatment: IPA for GI/G/1 and stochastic timed automata, unbiasedness conditions, SPA for discontinuous cases, concurrent estimation, IPA for stochastic fluid models