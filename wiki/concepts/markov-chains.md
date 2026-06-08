---
aliases: []
also_type:
- framework
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:concept:markov-chains
knowledge_type: concept
maturity: settled
related_concepts:
- '[[probability-theory]]'
- '[[diffusion-processes]]'
- '[[poisson-process]]'
sources:
- '[[lange-applied-probability]]'
- '[[cassandras-des-intro]]'
tags:
- stochastic-processes
- probability-theory
- markov-property
- simulation
title: Markov Chains
understanding: 0
---

A stochastic process in which the future state depends only on the present state, not the full history (the Markov property); discrete-time and continuous-time variants underlie MCMC, queueing theory, population genetics, and reinforcement learning.

Classification note: assigned as concept but also_type framework because the Markov chain is both a mathematical object (concept) and an organizing paradigm for a family of simulation and sampling techniques (framework).

## Reading Path
- [[lange-applied-probability-ch07]] (unread) — discrete-time chains: coupling, convergence rates, MCMC, simulated annealing
- [[lange-applied-probability-ch08]] (unread) — continuous-time chains: backward equations, equilibrium, birth-death processes
- [[lange-applied-probability-ch13]] (unread) — numerical methods for Markov chain computations
- [[cassandras-des-intro-ch07]] (unread) — DES treatment of Markov chains: ergodicity, stationary distributions, queueing applications
- [[cassandras-des-intro-ch06]] (unread) — Markov chains as special case of GSMP (generalized semi-Markov processes)

## Maximum-Entropy Chains on Constrained State Machines
A constrained noiseless channel induces a Markov chain over transmitter states. The transition matrix that maximises per-symbol entropy among all legal sequences is built from the leading left-eigenvector of the connection matrix $A$:
$$Q_{s'\mid s}=\frac{e^{(L)}_{s'}A_{s's}}{\lambda e^{(L)}_s},$$
with invariant distribution $\propto e^{(R)}_s e^{(L)}_s$ and asymptotic entropy rate $\log_2\lambda$. See [[constrained-channel-optimal-transitions]].