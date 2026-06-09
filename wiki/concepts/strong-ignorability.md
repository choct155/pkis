---
aliases: []
also_type: []
analogous-to:
- confounding
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- ignorability
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- bayesian-stats
id: pkis:concept:strong-ignorability
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch11
specializes:
- confounding
tags:
- causality
- potential-outcomes
- confounding
- admissibility
- propensity-score
- rosenbaum-rubin
title: Strong Ignorability
understanding: 0
---

## Definition
The potential-outcome condition under which a covariate set Z renders treatment assignment unconfounded, written {Y(0), Y(1)} ⊥ X | Z (Rosenbaum and Rubin 1983), where Y(0), Y(1) are the potential outcomes under do(X=0) and do(X=1). When strong ignorability holds, Z is *admissible* (deconfounding) and the causal effect is given by the adjustment estimand P(y|do(x)) = Σ_z P(y|z,x)P(z). Pearl's Chapter 11 reframes strong ignorability through the graphical lens: it is exactly the condition that Z satisfies the back-door criterion, since {Y(0),Y(1)} are represented in the causal graph by the observed and unobserved parents of all nodes on the X→Y paths (a set W), and Z d-separates W from X iff Z is back-door admissible. This identification demystifies a concept Pearl repeatedly calls the 'Achilles' heel' of the potential-outcome approach: because the counterfactuals Y(0), Y(1) are unobservable, no investigator can judge whether the independence holds by inspection. As a result, strong ignorability is used almost exclusively as a *surrogate* for assuming admissibility, rather than as a criterion that protects against bad choices of Z. Pearl argues this opacity (compounded by the false 'more covariates can only help' intuition) drove the misuse of propensity-score matching, since bias reduction is non-monotonic: adjusting away one confounder can unleash bias from a dormant unmeasured confounder.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ignorability]] — contrasts-with: Pearl's strong ignorability (counterfactual no-confounding) is distinct from the Bayesian/missing-data sense of an ignorable inclusion mechanism.
- [[confounding]] — analogous-to: Pearl shows strong ignorability {Y(0),Y(1)}⊥X|Z is the back-door admissibility condition expressed in counterfactual rather than graphical notation.
- [[confounding]] — specializes: Strong ignorability is the potential-outcome statement of no-confounding (admissibility).
[To be populated during integration]