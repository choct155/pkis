---
aliases: []
also_type: []
applies:
- average-treatment-effect
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
date_updated: '2026-06-20'
domain:
- causal-inference
- econometrics
- statistics
id: pkis:technique:difference-in-differences-did
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
- cunningham-causal-inference-mixtape-ch10
tags:
- panel-data
- parallel-trends
- ATT
- natural-experiment
- policy-evaluation
title: Difference-in-Differences (DiD)
understanding: 0
uses:
- parallel-trends
- aiptw-double-ml
- structural-causal-model
---

## Definition
**Difference-in-differences** is a causal identification and estimation strategy for panel data with two time periods ($t=0,1$) and binary treatment $A_i$ applied between periods. The classical structural assumption is
$$Y_{ti} \leftarrow W_i + S_t + \tau A_i \mathbf{1}(t=1) + \xi_{ti},$$
which implies the **parallel trends** condition: in the absence of treatment, the expected change in outcomes would be identical for treated and control units. The causal estimand (average treatment effect on the treated) is identified as
$$\tau = \mathbb{E}[Y_{1i}-Y_{0i}|A=1] - \mathbb{E}[Y_{1i}-Y_{0i}|A=0],$$
estimated by the two-way difference
$$\hat{\tau} = \frac{1}{n_A}\sum_{i:A_i=1}(Y_{1i}-Y_{0i}) - \frac{1}{n-n_A}\sum_{i:A_i=0}(Y_{1i}-Y_{0i}).$$

The **conditional parallel trends** generalisation assumes
$$\mathbb{E}^{A=1}[Y_1-Y_0|X,\mathrm{do}(A=0)] = \mathbb{E}[Y_1-Y_0|X,A=0],$$
allowing adjustment for covariates $X$ that make the assumption more credible, and enabling semiparametrically efficient estimation via the same AIPTW machinery.

### Why it matters
DiD permits causal identification in the presence of time-invariant unobserved unit heterogeneity ($W_i$) and time-varying aggregate shocks ($S_t$), neither of which needs to be observed. It is the backbone of natural-experiment studies in economics and policy analysis (e.g., Card–Krueger minimum wage study).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[structural-causal-model]] — uses
- [[aiptw-double-ml]] — uses: Same estimation machinery applies after reformulating DiD as an ATT adjustment problem on differenced outcomes
- [[parallel-trends]] — uses: Parallel trends is the core identification assumption of DiD
- [[average-treatment-effect]] — applies: DiD identifies the ATT under parallel trends
[To be populated during integration]