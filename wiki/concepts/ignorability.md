---
aliases: []
also_type: []
applies:
- selection-bias
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- likelihood-principle
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- causal-analysis
id: pkis:concept:ignorability
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch08
tags:
- missing-data
- study-design
- data-collection
- bayesian-inference
title: Ignorability
understanding: 0
uses:
- missing-data-mechanisms
- data-collection-mechanism
- conditional-independence
---

## Definition
A data-collection or missing-data mechanism is *ignorable* (with respect to a proposed model) when the posterior distribution of the model parameters omega computed by conditioning only on the observed data y_obs equals the posterior obtained by also conditioning on the inclusion/observation pattern I. Formally (Rubin 1976), p(omega | x, y_obs) = p(omega | x, y_obs, I), so the inclusion model p(I | x, y, phi) can be left out of the analysis. Two simple sufficient conditions guarantee ignorability for Bayesian inference: (1) **missing at random (MAR)** — given x, the missingness depends only on observed quantities, p(I | x, y, phi) = p(I | x, y_obs, phi); and (2) **distinct parameters** — the missingness parameters phi are a priori independent of the data parameters omega, p(phi | x, omega) = p(phi | x). When both hold, the design is ignorable and standard direct modeling of y_obs is valid. A design is **strongly ignorable** (a.k.a. unconfounded) when p(I | x, y, phi) = p(I | x), i.e. inclusion depends only on fully observed covariates. Ignorability supplies the precise, weak sense in which the likelihood-principle intuition ('inference is conditional on the data, so the design is irrelevant') is true: it holds for the single-model posterior under ignorable designs, but NOT for sensitivity analysis or posterior predictive checks, and NOT for nonignorable designs (e.g. censoring at an unknown point). Crucially, ignorability is a property of a (model, design) pair, not of the design alone — collecting enough covariates can render a complicated design ignorable by making the missingness conditionally independent of the missing values.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[selection-bias]] — applies: nonignorable designs are where selection bias is irreducible without modeling the selection mechanism
- [[conditional-independence]] — uses: MAR is a conditional-independence statement: I independent of y_mis given x and y_obs
- [[likelihood-principle]] — contrasts-with: ignorability is the precise weak sense in which the likelihood-principle intuition holds
- [[data-collection-mechanism]] — uses: ignorability is a property of the inclusion model p(I|y,phi)
- [[missing-data-mechanisms]] — uses: MAR + distinct parameters are the sufficient conditions defining ignorability
[To be populated during integration]