---
aliases: []
also_type: []
contrasts-with:
- marginal-likelihood
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
- bayesian-stats
id: pkis:concept:information-criteria
knowledge_type: concept
maturity: settled
related_concepts:
- '[[model-selection-problem]]'
- '[[bias-variance-tradeoff]]'
- '[[regularization]]'
- '[[model-averaging]]'
sources:
- '[[castle-model-selection-algorithms]]'
tags:
- model-selection
- aic
- bic
- sic
- penalized-likelihood
- information-theory
title: Information Criteria
understanding: 0
uses:
- optimism-of-training-error
- effective-number-of-parameters
---

Penalized log-likelihood scores for comparing statistical models that trade off goodness-of-fit (via maximized log-likelihood) against complexity (via a penalty on the number of parameters), enabling automatic model selection without held-out data.

The two canonical forms are: AIC = −2ℓ + 2k (asymptotically efficient; selects the model minimizing expected prediction error) and SIC/BIC = −2ℓ + k·log(n) (consistent; selects the true DGP with probability → 1 as n → ∞ if it is in the candidate set). Small-sample corrections AICc and SICc address the tendency of AIC/SIC to overfit in small samples. The choice between criteria encodes a prior belief: AIC assumes the true model is not in the candidate set; SIC assumes it is.

## Reading Path
- [[castle-model-selection-algorithms]] (unread) — comprehensive Monte Carlo comparison of 21 MSAs; AIC vs SIC performance as a function of signal-to-noise and proportion of relevant variables; penalty function / gauge framework

## Connections
- [[effective-number-of-parameters]] — uses
- [[optimism-of-training-error]] — uses
- [[marginal-likelihood]] — contrasts-with: predictive ICs target out-of-sample fit; BIC/Bayes factors target the marginal likelihood