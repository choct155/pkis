---
aliases: []
also_type: []
applies:
- decision-trees
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- bagging
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:bumping
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch08
tags:
- bootstrap
- resampling
- model-search
- local-minima
- trees
title: Bumping
understanding: 0
uses:
- bootstrap
---

## Definition
Bumping uses bootstrap sampling to move stochastically through model space in search of a single better model, rather than to average or combine models. From bootstrap samples Z^{*1},...,Z^{*B} a model is fit to each, and the model whose predictions best fit the original training data is chosen: b-hat = argmin_b sum_i [ y_i - f-hat^{*b}(x_i) ]^2, with chosen predictions f-hat^{*b-hat}(x). By convention the original training sample is included among the bootstrap samples, so bumping can always fall back to the original model.

## Operational Mechanism
Perturbing the data shakes the fitting procedure out of poor local solutions: if a few data points cause a bad fit, a bootstrap sample omitting them yields a better one. The canonical illustration is the XOR / pure-interaction problem, where greedy CART finds a useless top split because of balanced classes; bootstrap resampling breaks the balance, so with a modest number of samples (e.g. 20) at least one tree splits near x_1=0 or x_2=0, recovering near-optimal discrimination.

## Conditions
Because bumping compares models on the training data, the candidate models must have roughly equal complexity (e.g. trees grown to the same number of terminal nodes). Bumping is also useful when the fitting criterion is hard to optimize directly (e.g. lack of smoothness): one can optimize a convenient surrogate over the bootstrap samples and then select by the desired criterion on the training sample.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[decision-trees]] — applies: bumping helps greedy tree induction escape poor splits, e.g. on the XOR problem
- [[bagging]] — contrasts-with: both resample via bootstrap, but bumping picks one best model rather than averaging
- [[bootstrap]] — uses: bumping searches model space by fitting the model to bootstrap resamples and selecting the best on training data
[To be populated during integration]