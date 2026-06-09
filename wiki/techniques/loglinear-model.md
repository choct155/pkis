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
id: pkis:technique:loglinear-model
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch16
tags:
- loglinear-model
- contingency-table
- poisson
- categorical-data
- conditional-independence
- imputation
title: Loglinear Model
understanding: 0
---

## Definition
A **loglinear model** describes association among several categorical variables by treating the cross-classified cell counts of a contingency table as Poisson random variables whose log-means follow a linear model in indicator variables:

$$\log\mu = X\beta,$$

where $X$ is an all-zero/one incidence matrix and $\mu$ are the expected cell counts. It is a subclass of Poisson GLMs. Model choice corresponds to which interactions enter $X$: the **null model** (constant only, equal cell probabilities), the **independence model** (main effects only), the **saturated model** (all interactions, as many parameters as cells), and intermediate models encoding conditional independencies — e.g. including $z_1z_3$ and $z_2z_3$ but not $z_1z_2$ makes $z_1\perp z_2 \mid z_3$.

When a marginal total is fixed by design, the Poisson likelihood specializes to a multinomial (or product-multinomial) one. A conjugate Dirichlet-like prior $p(\mu)\propto\prod_i \mu_i^{k_i-1}$ enables special computation via iterative proportional fitting.

Intuition: read patterns of dependence in a multiway table off the presence or absence of interaction terms in a regression on the log counts.

### Why it matters
Loglinear models are the standard framework for multivariate discrete-data analysis and are central to multiple imputation of categorical data (BDA3 Ch. 18). Their interaction structure gives a precise, testable language for conditional independence among categorical variables, and their Poisson/multinomial duality lets the same machinery serve both unconditional counts and fixed-margin survey designs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]