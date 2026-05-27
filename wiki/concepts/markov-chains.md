---
id: "pkis:concept:markov-chains"
aliases: []
title: "Markov Chains"
knowledge_type: concept
also_type: [framework]
domain: [bayesian-stats]
tags: [stochastic-processes, probability-theory, markov-property, simulation]
related_concepts:
  - "[[probability-theory]]"
  - "[[diffusion-processes]]"
  - "[[poisson-process]]"
sources:
  - "[[lange-applied-probability]]"
  - "[[cassandras-des-intro]]"
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

A stochastic process in which the future state depends only on the present state, not the full history (the Markov property); discrete-time and continuous-time variants underlie MCMC, queueing theory, population genetics, and reinforcement learning.

Classification note: assigned as concept but also_type framework because the Markov chain is both a mathematical object (concept) and an organizing paradigm for a family of simulation and sampling techniques (framework).

## Reading Path
- [[lange-applied-probability-ch07]] (unread) — discrete-time chains: coupling, convergence rates, MCMC, simulated annealing
- [[lange-applied-probability-ch08]] (unread) — continuous-time chains: backward equations, equilibrium, birth-death processes
- [[lange-applied-probability-ch13]] (unread) — numerical methods for Markov chain computations
- [[cassandras-des-intro-ch07]] (unread) — DES treatment of Markov chains: ergodicity, stationary distributions, queueing applications
- [[cassandras-des-intro-ch06]] (unread) — Markov chains as special case of GSMP (generalized semi-Markov processes)
