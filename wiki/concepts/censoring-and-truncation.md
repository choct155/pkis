---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:concept:censoring-and-truncation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch08
tags:
- partial-data
- missing-data
- likelihood
- survival-analysis
title: Censoring and Truncation
understanding: 0
---

## Definition
Two related partial-observation patterns, distinguished by whether the *number* of unobserved points is known. **Censoring:** values beyond a threshold are not recorded exactly but their existence and count are known — e.g. a scale that reports 'too heavy' for all weighings above 200 kg. Each censored point contributes a tail probability to the likelihood: for 9 censored values above a known point phi, the factor is [Phi(omega - phi)]^9 (with Phi the normal CDF). **Truncation:** points beyond the threshold are entirely absent, with no count available — e.g. only the recorded values are reported and the total number weighed is unknown. The likelihood of each observed point is then a density renormalized by the survival probability, e.g. divided by Phi(200 - omega). Both are nonignorable missing-data mechanisms: ignoring the observation indicators omits the tail factors and gives the *wrong* likelihood. With a *known* censoring/truncation point the analysis is nonignorable-but-known; with an *unknown* point it becomes nonignorable-and-unknown, the hardest case, with the posterior for omega highly sensitive to the model. A key asymmetry: under censoring the observed proportion is powerful information about an unknown censoring point phi, whereas under truncation this information is absent (the unknown N integrates out, and with a noninformative 1/N prior the censored case can be shown equivalent to truncation, e.g. the posterior collapses to N(omega | ybar_obs, 1/91)[1 - Phi(omega - 200)]^{-91}). Rounding, binning, heaping, and coarse categorical data (Heitjan-Rubin coarse data) generalize these patterns, requiring inclusion indicators I_i that point to a *set* in the sample space rather than a 0/1 flag.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]