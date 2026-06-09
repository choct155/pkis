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
id: pkis:technique:gelman-rubin-diagnostic
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch11
tags:
- mcmc
- convergence-diagnostics
- potential-scale-reduction
- r-hat
- mixing
- stationarity
- multiple-sequences
- gelman
title: Gelman-Rubin Convergence Diagnostic (R-hat)
understanding: 0
---

## Definition
The Gelman-Rubin diagnostic monitors convergence of iterative simulation by comparing variation *between* multiple independent chains to variation *within* each chain, for each scalar estimand ψ of interest. The logic: only when the distribution of each individual sequence matches the distribution of all sequences pooled can both be approximating the target; before convergence, between-sequence variance exceeds within-sequence variance (chains started from overdispersed points have not yet mixed).

Diagnosis checks two things simultaneously — *mixing* (chains have traced out a common distribution) and *stationarity* (each chain is itself stationary). The modern (BDA3) recipe enforces both by splitting each chain in half after discarding warm-up: with m chains of post-warm-up length n, splitting gives 2 (number of chains) half-sequences (always m ≥ 4), so the first and second halves of each chain must also mix.

For estimand ψ with draws ψ_{ij} (i=1..n within chain, j=1..m chains), compute between- and within-sequence variances:

  B = n/(m-1) Σ_j (ψ̄_{.j} − ψ̄_{..})²
  W = (1/m) Σ_j s²_j,  s²_j = 1/(n-1) Σ_i (ψ_{ij} − ψ̄_{.j})².

The marginal posterior variance is estimated by a weighted average (analogous to the classical cluster-sampling variance estimate):

  var̂⁺(ψ|y) = (n-1)/n · W + (1/n) · B.   (11.3)

This *overestimates* var(ψ|y) when the starting distribution is overdispersed but is unbiased under stationarity or as n→∞; meanwhile W *underestimates* it for finite n (individual chains have not yet ranged over the whole target). The potential scale reduction factor is

  R̂ = sqrt( var̂⁺(ψ|y) / W ),   (11.4)

the factor by which the scale of the current pooled distribution might shrink if simulation continued to n→∞. R̂ → 1 as the chains converge; Gelman's rule of thumb is to keep simulating until R̂ < 1.1 for *all* scalar estimands of interest. Caveats: the diagnostic is mean/variance-based, so it works best for approximately normal marginals — for constrained or long-tailed summaries one should transform first (log of positive quantities, logit of (0,1) quantities, rank transformation for heavy tails). It is not a hypothesis test (no p-value); passing it does not guarantee convergence if important regions of the target were never reached by the starting distribution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]