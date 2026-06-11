---
aliases: []
also_type: []
applies:
- bias-variance-tradeoff
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- gradient-boosting
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:bagging
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- random-forests
related_concepts: []
sources:
- hastie-esl-ch08
- hastie-esl-ch15
specializes:
- ensemble-learning
tags:
- ensemble-methods
- variance-reduction
- bootstrap
- resampling
- trees
- wisdom-of-crowds
title: Bagging (Bootstrap Aggregation)
understanding: 0
uses:
- bootstrap
- decision-trees
- cart-decision-trees
---

## Definition
Bagging averages a model's prediction over a collection of bootstrap samples to reduce its variance. For each bootstrap sample Z^{*b}, b=1,...,B (drawn with replacement from the training data), the model is refit to give prediction f-hat^{*b}(x); the bagging estimate is their Monte Carlo average f-hat_bag(x) = (1/B) sum_b f-hat^{*b}(x), an approximation to the 'true' bagging estimate E_{P-hat} f-hat^*(x) under the empirical distribution P-hat. Bagging differs from the original estimate only when the latter is a nonlinear or adaptive function of the data; it is most effective on unstable, high-variance procedures (e.g., unpruned trees).

## Operational Mechanism
Draw B bootstrap replicate datasets, refit the base learner on each, and average (regression) or vote / average class-probability estimates (classification). For a K-class classifier with indicator-vector function f-hat(x), f-hat_bag(x) = [p_1(x),...,p_K(x)] where p_k is the proportion of trees predicting class k, and G-hat_bag(x) = argmax_k f-hat_bag(x). Averaging the underlying class-probability estimates (e.g. terminal-node proportions) rather than the hard-vote indicator vectors gives better probability estimates and lower-variance bagged classifiers, especially for small B.

## Principled Mechanism
Under squared-error loss, averaging reduces variance and leaves bias unchanged: for the ideal aggregate f_ag(x)=E_P f-hat^*(x), E_P[Y - f-hat^*(x)]^2 = E_P[Y - f_ag(x)]^2 + E_P[f-hat^*(x) - f_ag(x)]^2 >= E_P[Y - f_ag(x)]^2, so population aggregation never increases MSE. Via the bootstrap-as-posterior view (Section 8.4), the bagged estimate is an approximate posterior Bayesian mean, while the single training estimate f-hat(x) corresponds to the posterior mode; since the mean minimizes squared-error loss, bagging tends to help. For classification under 0-1 loss bias and variance are non-additive, so bagging a good classifier improves it but bagging a bad one can worsen it (the consensus / 'Wisdom of Crowds' argument requires that the weak learners be independent — bagged trees are not).

## Failure Modes
Bagging does not help, and can hurt, under 0-1 loss when the base classifier is poor; it destroys interpretable structure (a bagged tree is no longer a tree); and it provides little benefit for already-stable procedures like nearest neighbors. It only enlarges the model class modestly — problems needing a much larger hypothesis class (e.g. the diagonal-boundary example) are better served by boosting.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[random-forests]] — prerequisite-of
- [[cart-decision-trees]] — uses: unstable base learner for which bagging is most beneficial
- [[decision-trees]] — uses
- [[gradient-boosting]] — contrasts-with: bagging only modestly enlarges the model class; boosting enlarges it enough to capture structure bagging cannot
- [[bias-variance-tradeoff]] — applies: bagging reduces variance while leaving bias unchanged under squared-error loss
- [[ensemble-learning]] — specializes: bagging is a variance-reduction ensemble method combining bootstrap-resampled base learners
- [[bootstrap]] — uses: bagging averages a base learner refit on B bootstrap resamples of the training data
[To be populated during integration]