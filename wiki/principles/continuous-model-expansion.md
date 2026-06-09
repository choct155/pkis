---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
contrasts-with:
- bayes-factor
- bayesian-model-averaging
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:principle:continuous-model-expansion
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch07
tags:
- model-building
- model-comparison
- hierarchical-models
- sensitivity-analysis
- robustness
- gelman
title: Continuous Model Expansion
understanding: 0
uses:
- hierarchical-bayesian-models
---

## Definition
A methodological stance, central to Gelman's Bayesian workflow, that prefers embedding competing discrete models inside a single larger continuous family — with the original models recovered as special cases — over choosing among or averaging across discrete models. Rather than asking 'which model?', one expands p(y,ω) into p(y,ω,φ) where the new parameters φ (with their own conditional priors p(ω|φ) and hyperprior p(φ)) interpolate between the candidates. The archetype is the 8-schools hierarchical model y_j ~ N(ω_j,σ_j²), ω_j ~ N(μ,τ²): complete pooling (τ=0) and no pooling (τ=∞) are endpoints of the continuous τ ∈ [0,∞), so there is no need to assign discrete probabilities to either extreme.

Motivations for expansion include poor fit revealed by posterior predictive checks, questionable modeling assumptions (e.g. replacing a normal by a t to add robustness), unifying two non-nested models, and incorporating new data (e.g. embedding a single experiment in a hierarchical population model). This principle frames predictive-accuracy measures and cross-validation as tools for understanding fitted models rather than for selecting among them, and it explains the preference for partial pooling over variable selection and for proper, substantively informed priors over Bayes-factor model choice.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[hierarchical-bayesian-models]] — uses: hierarchical models are the canonical continuous expansion (8-schools)
- [[bayesian-model-averaging]] — contrasts-with: continuous expansion preferred over averaging discrete models
- [[bayes-factor]] — contrasts-with: Gelman prefers continuous expansion to discrete model choice via Bayes factors
[To be populated during integration]