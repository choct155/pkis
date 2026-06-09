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
id: pkis:concept:bayes-factor
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch07
tags:
- model-comparison
- marginal-likelihood
- hypothesis-testing
- model-evidence
- improper-priors
title: Bayes Factor
understanding: 0
---

## Definition
The ratio of the marginal likelihoods (marginal data densities) of two competing models, BF(H2;H1) = p(y|H2)/p(y|H1) = ∫ p(ω_2|H2) p(y|ω_2,H2) dω_2 / ∫ p(ω_1|H1) p(y|ω_1,H1) dω_1. It is the factor by which the data update the prior odds between two discrete hypotheses into posterior odds: p(H2|y)/p(H1|y) = [p(H2)/p(H1)] · BF(H2;H1), making accumulation of evidence transparent through multiplication of odds.

Bayes factors are well behaved when the competing models are genuinely discrete, each makes scientific sense with no obvious model in between, and the marginal density p(y|H_i) is proper (e.g. the genetics carrier-status example). They are problematic for inherently continuous problems: assigning positive probability to a point value such as a treatment effect = 0, or to τ = 0 vs τ = ∞ in the 8-schools problem, distorts inference. With improper priors the ratio is undefined (0/0), and even taking proper N(0,A²) priors as limits, the Bayes factor is acutely sensitive to the arbitrary prior variance A² and to problem dimensionality — quantities that are scientifically incidental. This sensitivity is the chief reason Gelman favors continuous model expansion over discrete model choice or averaging via Bayes factors.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]