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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- causal-inference
- statistics
- epidemiology
id: pkis:technique:g-computation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
tags:
- outcome-regression
- standardisation
- ATE
- confounder-adjustment
- causal-estimation
title: G-Computation (Outcome Model Adjustment)
understanding: 0
---

## Definition
**G-computation** (also *outcome regression adjustment* or *standardisation*) estimates the ATE by:
1. Fitting a model $\hat{Q}(a,x) \approx \mathbb{E}[Y|A=a, X=x]$ using any regression/ML method.
2. Predicting counterfactual outcomes for each unit under both treatment levels.
3. Averaging the individual-level contrasts:
$$\hat{\tau}^Q \triangleq \frac{1}{n}\sum_i \hat{Q}(1,x_i) - \hat{Q}(0,x_i).$$

The outer expectation over $P(X)$ is replaced by the empirical distribution, and the conditional expected outcome minimises mean squared error, so standard supervised learning applies directly.

### Why it matters
G-computation translates causal identification under the backdoor criterion into a pure prediction problem, making it compatible with any ML model for $Q$. It is consistent when $\hat{Q}$ is consistent, but—unlike IPTW or AIPTW—it achieves $\sqrt{n}$ rates only when $Q$ itself is estimated at the $\sqrt{n}$ rate. Its main strength is stability when overlap is imperfect (no inverse-propensity weights); its weakness is sensitivity to outcome-model misspecification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]