---
aliases: []
also_type: []
analogous-to:
- loo-cv
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
- deviance-information-criterion
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:concept:waic
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch07
specializes:
- information-criteria
tags:
- information-criteria
- model-comparison
- predictive-accuracy
- watanabe
- singular-models
- bias-correction
title: Widely Applicable Information Criterion (WAIC)
understanding: 0
uses:
- expected-log-predictive-density
- effective-number-of-parameters
---

## Definition
A fully Bayesian information criterion that estimates expected out-of-sample predictive accuracy (elppd) by starting from the computed log pointwise predictive density and subtracting an effective-number-of-parameters correction: elppd_WAIC = lppd − p_WAIC, with WAIC = −2 lppd + 2 p_WAIC reported on the deviance scale. Two corrections are in use — p_WAIC1 (a mean-difference form analogous to p_DIC) and the recommended p_WAIC2 = Σ_i var_post(log p(y_i|ω)), whose per-point variance summation makes it stable and aligns its series expansion with LOO-CV.

Unlike AIC (which plugs in the maximum likelihood estimate) and DIC (which plugs in the posterior mean), WAIC averages over the full posterior, so it evaluates the very posterior predictive density actually used for Bayesian prediction. Because it derives from Watanabe's singular learning theory rather than Fisher's regular-model asymptotics, WAIC remains valid for singular models — mixtures and hierarchical models where the parameter count grows with n and plug-in point estimates are meaningless. It has been shown to be asymptotically equal to Bayesian leave-one-out cross-validation. Its main cost is reliance on a partition of the data into n conditionally independent pieces, which is awkward for time-series, spatial, and network data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[loo-cv]] — analogous-to: WAIC is asymptotically equal to Bayesian LOO-CV
- [[deviance-information-criterion]] — contrasts-with: WAIC averages over posterior; DIC plugs in posterior mean
- [[effective-number-of-parameters]] — uses: p_WAIC is the bias correction
- [[expected-log-predictive-density]] — uses: WAIC estimates elppd
- [[information-criteria]] — specializes: WAIC is a specific information criterion
[To be populated during integration]