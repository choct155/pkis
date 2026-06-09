---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:technique:metropolis-hastings
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch11
tags:
- mcmc
- posterior-sampling
- markov-chains
- acceptance-rejection
- asymmetric-proposal
- bayesian-computation
- gelman
title: Metropolis-Hastings Algorithm
understanding: 0
---

## Definition
The Metropolis-Hastings algorithm is the general family of MCMC methods that constructs a Markov chain whose stationary distribution is the target posterior p(ω|y) via a propose-accept rule with an asymmetric jumping (proposal) distribution. It generalizes the basic Metropolis algorithm in two coupled ways: (1) the jumping rule J_t(ω*|ω^{t-1}) need not be symmetric, and (2) to correct for that asymmetry the acceptance ratio is a *ratio of ratios*

  r = [ p(ω*|y) / J_t(ω*|ω^{t-1}) ] / [ p(ω^{t-1}|y) / J_t(ω^{t-1}|ω*) ],   (11.2)

and ω* is accepted with probability min(r, 1), otherwise the chain stays at ω^{t-1} (a rejection still counts as an iteration). The extra factor J_t(ω^{t-1}|ω*)/J_t(ω*|ω^{t-1}) exactly compensates for the proposal asymmetry so that detailed balance — and hence p(ω|y) as the stationary distribution — is preserved; the convergence proof is identical to Metropolis except for relabeling points so that p(ω_b|y)J_t(ω_a|ω_b) ≥ p(ω_a|y)J_t(ω_b|ω_a).

The basic (symmetric) Metropolis algorithm is the special case J_t(ω_a|ω_b) = J_t(ω_b|ω_a), for which the J-ratio is 1 and (11.2) collapses to the density ratio (11.1). The Gibbs sampler is also a special case: its componentwise conditional-draw proposal yields r ≡ 1, so every jump is accepted. Allowing asymmetric proposals can increase the speed of the random walk. The *ideal* jumping rule is J(ω*|ω) ≡ p(ω*|y), which makes r ≡ 1 and produces independent draws — unattainable in practice (it is the very sampling problem MCMC exists to solve), but it identifies what a good proposal approximates. Gelman's four properties of a good jumping distribution: (i) it is easy to sample from J(ω*|ω); (ii) the ratio r is easy to compute; (iii) each jump moves a reasonable distance in parameter space (else the walk crawls); (iv) jumps are not rejected too often (else the walk stands still). These tensions — large enough steps to move, small enough to be accepted — motivate proposal tuning (Gelman recommends a multivariate-normal jumping kernel scaled by 2.4^2/d from a normal approximation, giving acceptance near 0.35 for moderate d).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]