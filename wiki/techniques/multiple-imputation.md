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
- statistical-learning
id: pkis:technique:multiple-imputation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch18
tags:
- missing-data
- imputation
- bayesian-computation
- survey-sampling
- uncertainty-quantification
title: Multiple Imputation
understanding: 0
---

## Definition
A two-phase strategy for analyzing data with missing values in which the missing entries are replaced by K > 1 sets of plausible values (the 'multiple imputations'), each drawn from the posterior predictive distribution of the missing data under an imputation model, producing K completed datasets that are then analyzed by standard complete-data methods and whose results are pooled. Unlike single imputation, which produces one completed dataset and thereby understates uncertainty by treating imputed values as if observed, multiple imputation propagates the uncertainty due to nonresponse through the between-imputation variability across the K datasets. The Bayesian justification: a full joint posterior over (parameters, missing data) is computed (e.g. by data augmentation / the Gibbs sampler); the imputer keeps a few random draws y_mis^s of the missing data, *discarding* the parameter inferences, and stores the completed datasets X^s = (X_obs, X_mis^s). A separate downstream analyst then fits the substantive model p(y | X^s, omega) to each completed dataset as if it were fully observed, and combines inferences. With Bayesian simulation, combining is trivial — mix the posterior draws from the separate analyses; with point-estimate-plus-variance output, the moment-matching pooling formulas (Rubin's rules) apply. The key practical virtue is a clean separation of labor: the difficult missing-data modeling (constructing a joint model for the predictor matrix X) is done once by the imputer, while many downstream users can analyze the imputed datasets with familiar complete-data tools without ever modeling the missing-data mechanism. The number of imputations K is typically small (e.g. 3–10) when the fraction of missing information is modest. Imputation is usually carried out under an ignorable (MAR + distinct parameters) model, with sensitivity to plausible nonignorable models explored separately. Data augmentation can itself be viewed as iterative multiple imputation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]