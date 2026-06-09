---
aliases: []
also_type:
- framework
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- bayesian-stats
- state-space-models
id: pkis:concept:diffusion-processes
knowledge_type: concept
maturity: settled
related_concepts:
- '[[markov-chains]]'
- '[[probability-theory]]'
- '[[state-space-models]]'
sources:
- '[[lange-applied-probability]]'
tags:
- stochastic-processes
- brownian-motion
- continuous-time
- population-genetics
- first-passage
title: Diffusion Processes
understanding: 0
uses:
- brownian-motion
---

Continuous-time, continuous-state Markov processes characterized by infinitesimal drift and diffusion coefficients; Brownian motion is the canonical example, and the class encompasses models for physical diffusion, population genetics (Wright-Fisher), and financial processes.

## Reading Path
- [[lange-applied-probability-ch11]] (unread) — basic definitions, Brownian motion examples, process moments, first passage, reflection principle, equilibrium distributions
- [[lange-applied-probability-ch13]] (unread) — numerical methods for diffusion processes applied to Wright-Fisher

## Connections
- [[brownian-motion]] — uses: Diffusions dX = mu(X)dt + sigma(X)dB are constructed by driving with Brownian increments dB.