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
id: pkis:concept:overdispersion
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch16
- gelman-bda3-ch17
tags:
- overdispersion
- glm
- poisson
- binomial
- hierarchical-model
- dispersion-parameter
title: Overdispersion
understanding: 0
---

## Definition
**Overdispersion** is the common situation in which observed data exhibit more variation than the assumed sampling distribution permits. For the binomial and Poisson GLMs the dispersion parameter is fixed (variance is determined by the mean: $\text{Var}(y)=\mu$ for Poisson), so real data with extra heterogeneity violate the model. As Gelman et al. note, "excess dispersion is the rule rather than the exception in most applications."

The Bayesian remedy is to add a latent error term per observation inside the link, turning a fixed-dispersion GLM into a hierarchical model. For an overdispersed Poisson regression:

$$y_i \sim \text{Poisson}\!\left(e^{X_i\beta + \epsilon_i}\right), \qquad \epsilon_i \sim N(0,\sigma_\epsilon^2),$$

where $\sigma_\epsilon^2$ absorbs the surplus variation. For binomial litters one can let a per-group indicator follow a normal (interpretable) or beta (conjugate) distribution.

Intuition: overdispersion signals unmodeled heterogeneity among units; rather than abandon the count/proportion model, you give each unit its own random nudge and estimate how spread out those nudges are.

### Why it matters
Ignoring overdispersion makes posterior intervals far too narrow, producing overconfident inferences and spurious significance. Modeling it via a hierarchical error term restores honest uncertainty and converts a misspecified model into a defensible one; the police stop-and-frisk Poisson regression in BDA3 includes exactly such an $\epsilon_{ep}$ term for this reason.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]