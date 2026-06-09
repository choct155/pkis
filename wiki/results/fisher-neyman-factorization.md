---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:result:fisher-neyman-factorization
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch08
specializes:
- sampling-theory
tags:
- sufficiency
- likelihood
- factorization
- fisher
- sampling-distribution
title: Fisher–Neyman Factorization
understanding: 0
uses:
- exponential-family
---

## Definition
A statistic r(x_1,...,x_n) is sufficient for theta if and only if the sampling density factors as p(x_1,...,x_n|theta) = p(r|theta) b(x_1,...,x_n), where p(r|theta) is the marginal sampling density for r and b does not depend on theta (Fisher 1922; the form Jaynes Eq. 8.9). Equivalently, in a coordinate system y with y_1 = r the density factors as g(y|theta) = q(y_1|theta) m(y_2,...,y_n), so the distribution of the remaining coordinates is parameter-free.

## Why factorization implies sufficiency
Jaynes derives the factorization as the unique condition that makes the posterior depend on the data only through r FOR ALL priors. Demanding 'property R' (posterior depends on data only via r) independently of the prior forces the likelihood ratio g(y|theta')/g(y|theta) to be independent of (y_2,...,y_n), which is exactly the factorization. Substituted into Bayes' theorem the nuisance factor b(x) cancels, giving h(theta|D) proportional to f(theta) p(r|theta): r conveys everything the full data say about theta. The idea generalizes to jointly sufficient statistics and to separate sufficient statistics for distinct parameters.

## Effective (prior-dependent) sufficiency
Fisher required factorization for all priors. Jaynes notes that for a particular subclass of priors spanning a subspace of the Hilbert space of priors, the orthogonality conditions (Eq. 8.5) can hold even when Fisher factorization fails — yielding 'effective sufficient statistics' that depend on the prior. Thus different priors can render different aspects of the data irrelevant. The Cauchy distribution has no sufficient statistic at all: every data value matters.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[exponential-family]] — uses: Exponential-family models are exactly those with finite-dimensional sufficient statistics, the cleanest case of the factorization.
- [[sampling-theory]] — specializes: The factorization is stated in terms of the sampling density of orthodox/sampling theory.
[To be populated during integration]