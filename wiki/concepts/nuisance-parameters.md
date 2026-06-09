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
id: pkis:concept:nuisance-parameters
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch03
tags:
- bayesian-inference
- marginalization
- multiparameter-models
- posterior
title: Nuisance Parameters
understanding: 0
---

## Definition
In a multiparameter model, nuisance parameters are unknown quantities that are not of direct inferential interest but are nonetheless required to construct a realistic model. Partitioning the parameter vector as omega = (omega_1, omega_2) with omega_1 the parameters of interest and omega_2 the nuisance parameters, the Bayesian target is the marginal posterior p(omega_1 | y) obtained by integrating the joint posterior over omega_2:

$$p(\omega_1 \mid y) = \int p(\omega_1, \omega_2 \mid y)\, d\omega_2 = \int p(\omega_1 \mid \omega_2, y)\, p(\omega_2 \mid y)\, d\omega_2.$$

The second factorization shows the marginal posterior of interest is a mixture of the conditional posteriors p(omega_1 | omega_2, y), weighted by the marginal posterior p(omega_2 | y) of the nuisance parameter; the weights combine evidence from data and prior. A canonical example is the error scale sigma^2 in a measurement problem when only the location mu is of interest. The mixture form is what lets uncertainty about the nuisance parameter propagate correctly into inference about the parameter of interest, rather than fixing omega_2 at a point estimate.

## Practical strategy
The factorization rarely needs explicit integration: one samples the joint posterior by **marginal-then-conditional simulation** — first draw omega_2 from its marginal posterior p(omega_2 | y), then draw omega_1 from the conditional p(omega_1 | omega_2, y) given the drawn value. This performs the integration of (3.1) indirectly and is the workhorse for the normal model with unknown mean and variance.

## Generality
The averaging over omega_2 is interpreted broadly: omega_2 can include a discrete component indexing different sub-models, in which case marginalizing over it is exactly Bayesian model averaging.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]