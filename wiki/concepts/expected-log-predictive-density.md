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
- statistical-learning
id: pkis:concept:expected-log-predictive-density
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch07
tags:
- predictive-accuracy
- log-score
- lppd
- elpd
- out-of-sample
- model-evaluation
title: Expected Log Predictive Density (elpd)
understanding: 0
uses:
- scoring-rules
- kl-divergence
---

## Definition
The central Bayesian measure of a model's predictive accuracy: the expected log predictive density for new data, elpd = E_f(log p_post(ỹ)) = ∫ (log p_post(ỹ)) f(ỹ) dỹ, where p_post(ỹ) = ∫ p(ỹ|ω) p_post(ω) dω is the posterior predictive density and f is the (unknown) true data-generating distribution. Because it averages the log score over both the posterior of the parameters and the distribution of future data, it is grounded in the logarithmic scoring rule — the unique (up to affine transformation) local and proper scoring rule — and is directly tied to Kullback–Leibler information: in the large-sample limit the model with lowest KL divergence from the truth attains the highest expected log predictive density.

A pointwise version, the expected log pointwise predictive density (elppd = Σ_i E_f(log p_post(ỹ_i))), decomposes the measure data point by point, which is what enables the connection to cross-validation. Since f is unknown, elpd cannot be computed directly; it is estimated by the within-sample log pointwise predictive density (lppd = Σ_i log ∫ p(y_i|ω) p_post(ω) dω, computed by averaging over posterior draws) and then bias-correcting, because lppd evaluated on the data used for fitting systematically overestimates out-of-sample elppd. Every information criterion (AIC, DIC, WAIC) and cross-validation in this setting is a different recipe for estimating elpd from a baseline fit plus an overfitting correction.

Notably the prior density is excluded from this calculation: predictive accuracy summarizes the fit of the data model to data, so the prior is relevant only in that it shapes the posterior of ω (and hence p(y|ω)), not as an additive term.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kl-divergence]] — uses: elpd is tied to Kullback-Leibler information
- [[scoring-rules]] — uses: elpd is built on the logarithmic scoring rule
[To be populated during integration]