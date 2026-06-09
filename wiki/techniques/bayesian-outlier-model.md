---
aliases: []
also_type: []
applies:
- robust-inference
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
- information-theory
extends:
- bayesian-inference
id: pkis:technique:bayesian-outlier-model
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch21
specializes:
- mixture-models
tags:
- outliers
- robustness
- mixture-models
- exchangeability
- jaynes
title: Bayesian Outlier Model (Two-Model Contamination Mixture)
understanding: 0
uses:
- exchangeability
- nuisance-parameters
---

## Definition
Jaynes's fully-Bayesian treatment of outliers: instead of an ad hoc rejection rule (Chauvenet's criterion, two-standard-deviations, etc.), model the data as a two-component probability mixture of a 'good' sampling distribution G(x|theta) carrying the parameter of interest and a 'bad' distribution B(x|eta) that is uninformative about theta:

$$p(x\mid\theta,\eta,u) = u\,G(x\mid\theta) + (1-u)\,B(x\mid\eta),\qquad 0\le u\le 1.\;(21.8)$$

The purity parameter u is the probability any given datum is good. With an **exchangeable** prior on the good/bad indicator sequence q_1...q_n, the de Finetti representation theorem reduces the 2^n possible good/bad labelings to a single generating function g(u): the prior on the latent good/bad assignment is governed by a single mixing density over u. Integrating out the nuisance parameters (eta, u) yields the **quasi-likelihood**

$$\bar L(\theta) = \sum_{\text{subsets } S}\Pr(\text{exactly } S \text{ bad})\;\times\;(\text{likelihood of the good distribution using the data not in } S),\;(21.22)$$

i.e. a weighted average of the good-distribution likelihoods over every hypothesis about which data are good vs bad, weighted by the prior probability of that hypothesis. The marginal posterior f(theta|D,I) proportional to f(theta|I) * Lbar(theta) (21.15) then contains all relevant information.

**Key consequences.** (1) When a datum is *known* to be an outlier (G(x_i|theta)=0 for all theta), every likelihood term containing it vanishes and the posterior is exactly that of the deleted-data analysis — recovering the rejection intuition automatically, *provided* the probability of that outlier is independent of theta. (2) If the probability of the outlier *does* depend on theta, the outlier's value is itself evidence about theta and must not be discarded — a subtlety unaided intuition misses. (3) A single far-out datum drags a Gaussian-only estimate by ~10 sigma, but the same datum under the mixture model is automatically downweighted; the model includes ordinary hypothesis testing as a special case. The mixture model is the constructive engine by which Bayesian analysis delivers robustness without abandoning optimality.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-inference]] — extends: applies Bayes' theorem with a flexible mixture model to the outlier problem
- [[robust-inference]] — applies: the contamination mixture is the constructive mechanism delivering automatic robustness/resistance
- [[nuisance-parameters]] — uses: the bad-distribution parameter eta and purity u are integrated out as nuisance parameters
- [[exchangeability]] — uses: exchangeable prior on the good/bad indicator sequence enables the de Finetti reduction
- [[mixture-models]] — specializes: the good/bad contamination model is a two-component probability mixture
[To be populated during integration]