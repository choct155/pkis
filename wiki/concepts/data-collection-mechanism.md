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
- causal-analysis
- statistical-learning
id: pkis:concept:data-collection-mechanism
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch08
tags:
- study-design
- survey-sampling
- experimental-design
- observational-studies
- missing-data
title: Data-Collection Mechanism (Inclusion Model)
understanding: 0
---

## Definition
The unifying Bayesian device (Rubin 1976; Gelman BDA3 Ch. 8) for handling sample surveys, designed experiments, observational studies, and missing data as a single problem: model the *complete data* y (observed and unobserved) jointly with an *inclusion vector* I that indexes which potential data are observed (I_ij = 1 observed, 0 missing). The joint model factorizes as p(y, I | omega, phi) = p(y | omega) p(I | y, phi), splitting (1) the data model p(y | omega), built as elsewhere in the book, from (2) the inclusion/data-collection model p(I | y, phi), whose parameters phi describe the design but are usually not of scientific interest. The actual likelihood is the *observed-data likelihood* p(y_obs, I | omega, phi) = integral over y_mis of p(y, I | omega, phi). This framework treats intentional missing data (units not sampled in a survey; potential outcomes under treatments not applied) and unintentional missing data (nonresponse, dropout, censoring) uniformly, and shows that the design enters inference only through the inclusion model. When the design is ignorable the inclusion model drops out of parameter inference (though not out of posterior predictive checks, which depend on p(I | x, y, phi) through hypothetical replications y_rep). The chapter's central practical message follows: include in p(y | x, omega) all variables x used in data collection (strata, blocks, clusters, treatment-selection covariates) so that the design becomes ignorable and standard modeling applies. Requires a *stability* assumption (in experiments, SUTVA): y is fixed and I only selects which elements are seen.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]