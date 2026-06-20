---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- formal-methods
- systems-theory
id: pkis:technique:discrete-event-simulation
knowledge_type: technique
maturity: settled
related_concepts:
- discrete-event-systems
- generalized-semi-markov-process
- queueing-theory
- perturbation-analysis
sources:
- '[[cassandras-des-intro]]'
- cassandras-des-intro-ch10
- cassandras-des-intro-ch11
tags:
- discrete-event-simulation
- event-scheduling
- process-oriented
- monte-carlo
- random-variate-generation
- output-analysis
title: Discrete-Event Simulation
understanding: 0
---

Discrete-event simulation (DES simulation) is a technique for evaluating the performance of a DES by executing its event-scheduling or process-oriented logic computationally, using pseudo-random number generation and variate generation to instantiate stochastic clocks; output analysis provides statistical estimates of performance measures with confidence intervals.

## Reading Path
- [[cassandras-des-intro-ch10]] (unread) — primary treatment: event-scheduling scheme, process-oriented scheme, random number and variate generation, output analysis for terminating and non-terminating simulations