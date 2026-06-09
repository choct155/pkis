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
id: pkis:technique:iterative-proportional-fitting
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch16
tags:
- iterative-proportional-fitting
- loglinear-model
- contingency-table
- gibbs-sampler
- bayesian-ipf
- mode-finding
title: Iterative Proportional Fitting
understanding: 0
---

## Definition
**Iterative proportional fitting (IPF)** is an algorithm for fitting loglinear models by repeatedly rescaling a table of expected cell counts so its margins match the model's sufficient statistics. Working with multiplicative factors $\gamma_j=\exp(\beta_j)$ and a margin $y_{j+}=\sum_i x_{ij}(y_i+k_i)$ (data plus prior pseudo-counts), each step updates one parameter:

$$\gamma_j^{\text{new}}=\frac{y_{j+}}{\sum_i x_{ij}\mu_i^{\text{old}}}\,\gamma_j^{\text{old}}, \qquad \mu_i^{\text{new}}=\mu_i^{\text{old}}\Big(\tfrac{\gamma_j^{\text{new}}}{\gamma_j^{\text{old}}}\Big)^{x_{ij}},$$

cycling through all $j$ until convergence to the posterior mode of $\mu$. **Bayesian IPF** turns this into a Gibbs sampler by multiplying each update by a random factor $A/(2y_{j+})$ with $A\sim\chi^2_{2y_{j+}}$, so the sequence of tables becomes draws from the posterior. For multinomial sampling one rescales $\mu$ to the fixed total after each sweep.

Intuition: nudge the fitted table one margin at a time toward the observed margins; injecting calibrated randomness into each nudge converts mode-finding into posterior sampling.

### Why it matters
IPF exploits the special structure of conjugate loglinear models to fit large contingency tables without general nonlinear optimization, and its Bayesian variant gives a clean, easy-to-program Gibbs sampler when interest centers on expected counts. It is the computational backbone for contingency-table analysis and categorical-data imputation where generic GLM solvers would be cumbersome.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]