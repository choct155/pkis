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
- causal-analysis
- bayesian-stats
id: pkis:concept:controlled-direct-effect
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch04
specializes:
- direct-and-indirect-effects
tags:
- causality
- mediation
- direct-effect
- identification
- pearl
title: Controlled Direct Effect
understanding: 0
uses:
- plan-identification
- do-calculus
---

## Definition
The direct effect of X on Y obtained by physically fixing all other variables. Pearl (Definition 4.5.1) defines it as P(y | do(x), do(s_XY)), where S_XY is the set of all endogenous variables except X and Y — an 'ideal laboratory' in which the experimenter controls every condition. Corollary 4.5.2 shows this reduces to holding fixed only the parents of Y other than X: P(y | do(x), do(pa_Y\X)). Hence the controlled direct effect is identifiable whenever the corresponding 'parents' plan' do(x), do(pa_Y\X) is identifiable — connecting direct-effect estimation directly to the sequential back-door plan-identification machinery (Theorems 4.4.1/4.4.6, Theorem 4.5.3). In **linear** SEMs the controlled direct effect equals the path coefficient on X→Y and is independent of the levels at which the other parents are fixed; in **nonlinear** systems it varies with those levels ('effect modification'), so the holding values must be chosen to represent the target policy. Corollary 4.5.4: the direct effect is in general nonidentifiable if a confounding arc embraces any link X_k→Y. The Berkeley sex-admission example shows that naively adjusting for department (a mediator) can falsely indicate bias, whereas the correct controlled direct effect adjusts for the confounded career-objective covariate within each gender.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[do-calculus]] — uses
- [[plan-identification]] — uses
- [[direct-and-indirect-effects]] — specializes
[To be populated during integration]