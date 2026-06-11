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
contrasts-with:
- bayesian-inference
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- frequentist-statistics
- machine-learning
id: pkis:technique:bootstrap-sampling-distribution
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
specializes:
- bootstrap
tags:
- bootstrap
- sampling-distribution
- resampling
- MLE
- uncertainty-quantification
title: Bootstrap (Parametric and Non-Parametric)
understanding: 0
uses:
- sampling-distribution
- maximum-likelihood-estimation
- asymptotic-normality-mle
---

## Definition
The **bootstrap** is a Monte Carlo technique for approximating the sampling distribution of an estimator without analytic derivation.

**Parametric bootstrap:** Generate $S$ datasets $\tilde{D}^{(s)}=\{x_n\sim p(x|\hat{\theta})\}_{n=1}^N$ by plugging in the MLE $\hat{\theta}$ for the unknown true parameter, then compute $\hat{\theta}_s=\Theta(\tilde{D}^{(s)})$ for each; the empirical distribution of $\{\hat{\theta}_s\}$ approximates the sampling distribution.

**Non-parametric bootstrap:** Resample $N$ points with replacement from the original dataset $D$; approximately $63.2\%$ of unique data points appear in each resample (since $\Pr(\text{item selected})\to 1-e^{-1}$).

### Why it matters
The bootstrap is model-agnostic and works when closed-form sampling distributions are unavailable (small $N$ or complex estimators). For weakly informative priors and MLE estimators, the bootstrap distribution closely approximates the Bayesian posterior (the 'poor man's posterior'). However, it can be slower than posterior sampling because it requires re-fitting the model $S$ times.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-inference]] — contrasts-with: Bootstrap ≈ 'poor man's posterior' for weak priors
- [[asymptotic-normality-mle]] — uses
- [[maximum-likelihood-estimation]] — uses
- [[sampling-distribution]] — uses
- [[bootstrap]] — specializes
[To be populated during integration]