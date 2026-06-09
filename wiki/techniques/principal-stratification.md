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
- causal-analysis
- bayesian-stats
id: pkis:technique:principal-stratification
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch08
tags:
- causal-inference
- noncompliance
- potential-outcomes
- intermediate-outcomes
- instrumental-variables
title: Principal Stratification
understanding: 0
---

## Definition
A method (Frangakis & Rubin 2002) for causal inference that must adjust for an intermediate, post-treatment outcome C lying on the causal pathway to the final outcome y. Because the observed intermediate C_obs,i = I_i C_i(1) + (1 - I_i) C_i(0) is itself affected by treatment assignment I, it is NOT a covariate and stratifying on it is a common error. Instead one stratifies on the *joint* potential values (C(1), C(0)), which are fixed pre-assignment characteristics of a unit and so behave like a vector covariate — these strata are the *principal strata*. The canonical instance is compliance with assigned treatment, defining compliers (C(1)=1, C(0)=0), never-takers, always-takers, and (absent monotonicity) defiers. In the Indonesian vitamin-A noncompliance experiment, only compliers and noncompliers exist (vitamin A unavailable to controls). One estimates stratum-specific effects: the complier average causal effect (CACE) and noncomplier average causal effect (NACE). The overall assignment effect decomposes as Ybar_1 - Ybar_0 = p_c * CACE + (1 - p_c) * NACE, the *intention-to-treat* (ITT) effect. Under the **exclusion restriction** (no effect of assignment on noncompliers, NACE = 0), the method-of-moments estimate CACE-hat = (ybar_1 - ybar_0) / p_c-hat is exactly the econometric *instrumental-variables* estimate (ITT divided by the compliance proportion). Principal stratification is thus a bridge between potential-outcomes causal inference and instrumental variables, and the Bayesian treatment improves on the IV moment estimate by modeling unknown compliance status (e.g. for controls) as missing data, enabling relaxation of the exclusion restriction and handling of more complex compliance patterns.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]