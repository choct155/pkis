---
id: "pkis:technique:mcmc"
aliases: ["MCMC"]
title: "Markov Chain Monte Carlo (MCMC)"
knowledge_type: technique
also_type: [framework]
domain: [bayesian-stats]
tags: [mcmc, markov-chains, simulation, bayesian-computation, sampling]
related_concepts:
  - "[[markov-chains]]"
  - "[[gibbs-sampler]]"
  - "[[metropolis-algorithm]]"
  - "[[probability-theory]]"
  - "[[intractable-posterior]]"
sources:
  - "[[lange-applied-probability]]"
  - "[[kroese-statistical-modeling]]"
  - "[[capretto-bambi-2022]]"
  - "[[kurz-hybrid-modeling-2022]]"
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

A class of algorithms that construct a Markov chain whose stationary distribution is the target distribution (typically a posterior), enabling sampling from intractable distributions by running the chain until convergence; the Metropolis-Hastings and Gibbs sampler are the foundational instances.

Classification note: assigned as technique but also_type framework because MCMC is both a computational procedure and a family of sub-techniques organized by the same principle.

## Connections
- [[gibbs-sampler]] — generalizes: Gibbs is MCMC restricted to full conditional distributions; a special case of Hastings-Metropolis
- [[metropolis-algorithm]] — generalizes: the Hastings-Metropolis acceptance rule is the canonical MCMC mechanism
- [[markov-chains]] — uses: MCMC constructs a Markov chain whose stationary distribution is the target posterior
- [[intractable-posterior]] — uses: MCMC is the primary tool for computing intractable posterior integrals

## Reading Path
- [[lange-applied-probability-ch07]] (unread) — Hastings-Metropolis, Gibbs sampling, convergence of independence sampler, simulated annealing
- [[kroese-statistical-modeling-ch07]] (unread) — unified Monte Carlo chapter: MCMC fundamentals, Metropolis-Hastings, and Gibbs sampler alongside bootstrap and KDE
- [[capretto-bambi-2022]] (unread) — Bambi uses PyMC's NUTS (adaptive dynamic HMC) as default sampler; R-hat and ESS diagnostics via ArviZ
- [[kurz-hybrid-modeling-2022]] (unread) — Gibbs sampling used for joint posterior p(ν,d|y) in magnet characterization; blockwise sampling by move
