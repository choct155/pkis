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
id: pkis:technique:bayesian-decision-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch09
tags:
- decision-theory
- expected-utility
- posterior-predictive
- cost-benefit
- applied-bayes
title: Bayesian Decision Analysis
understanding: 0
---

## Definition
## Definition
Bayesian decision analysis is the workflow that turns a fitted Bayesian model into a decision by integrating a utility over the posterior. Gelman lays it out in four steps: (1) enumerate the decisions $d$ and outcomes $x$ (outcomes may be vectors mixing observables $\tilde y$ and parameters $\omega$, e.g. dollars and lives); (2) determine the conditional posterior $p(x\mid d)$ for each decision — note the decision itself has no probability, so all quantities are conditioned on $d$; (3) define a utility $U(x)$ collapsing (possibly multi-attribute) outcomes to a scalar; (4) compute and maximize expected utility,
$$ d^* = \arg\max_d\, E\big(U(x)\mid d\big) = \arg\max_d \int U(x)\, p(x\mid d)\, dx. $$
In practice many analyses stop after step 2, reporting expected consequences and leaving the utility trade-off to the decision maker.

### Why it matters
This is the bridge from inference to action: it makes posterior *uncertainty*, not just point estimates, bear on the choice. A key practical lesson is that predictors which are not 'statistically significant' must still be retained — their coefficients enter the expected-utility integral and cannot be set to zero without biasing the decision. Because the expectation averages over the full posterior, hierarchical regression coefficients, predictive variance, and parameter uncertainty all propagate into the cost-benefit calculation, distinguishing genuine Bayesian decision analysis from plug-in point-estimate decision rules.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]