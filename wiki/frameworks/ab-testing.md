---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine learning
- business analytics
id: pkis:framework:ab-testing
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch34
tags:
- bandit
- hypothesis testing
- sample size
- exploration-exploitation
- Bayesian decision theory
title: A/B Testing (Test-and-Roll)
understanding: 0
---

## Definition
A/B testing is a two-stage decision procedure: (1) **test phase** — randomly assign $n_0$ subjects to control (arm A) and $n_1$ subjects to treatment (arm B), observe rewards $\mathbf{y}_0, \mathbf{y}_1$; (2) **roll phase** — deploy the winning arm to the remaining $N - n_0 - n_1$ subjects.

Under a Bayesian Gaussian model with $Y_{ij} \sim \mathcal{N}(\mu_j, \sigma_j^2)$ and prior $\mu_j \sim \mathcal{N}(m_j, \tau_j^2)$, the optimal policy chooses the arm with higher posterior mean. The optimal symmetric sample size is:
$$n^* = \sqrt{\frac{N}{4}u^2 + \left(\frac{3}{4}u^2\right)^2} - \frac{3}{4}u^2, \quad u^2 = \sigma^2/\tau^2$$

### Why it matters
Formulates a concrete exploration-exploitation tradeoff: larger test phases reduce decision error but forfeit reward from the roll phase. The Bayesian formulation yields closed-form optimal sample sizes and shows classical frequentist tests often recommend unnecessarily large samples by ignoring the magnitude of the effect.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]