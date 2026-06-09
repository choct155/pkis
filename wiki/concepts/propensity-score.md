---
aliases: []
also_type: []
applies:
- adjustment-formula-standardization
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- causal-analysis
id: pkis:concept:propensity-score
knowledge_type: concept
maturity: settled
related_concepts:
- - - matching-estimators
- - - selection-bias
- - - potential-outcomes-framework
- - - average-treatment-effect
sources:
- - - cunningham-causal-inference-mixtape
specializes:
- ignorability
tags:
- propensity-score
- matching
- balancing-score
- selection-on-observables
- rosenbaum-rubin
- logit
title: Propensity Score
understanding: 0
uses:
- strong-ignorability
---

The propensity score e(X) = P(D=1|X) is the conditional probability of treatment given observed covariates; Rosenbaum and Rubin (1983) showed it is a *balancing score* — conditioning on e(X) removes selection bias due to X, reducing high-dimensional covariate matching to one-dimensional score matching.

## Reading Path
- [[cunningham-causal-inference-mixtape-ch06]] (unread) — balancing score theorem, propensity score estimation via logit, overlap/common support requirement

## Connections
- [[adjustment-formula-standardization]] — applies: Propensity-score adjustment is an implementation of the back-door adjustment/standardization formula.
- [[strong-ignorability]] — uses: Unbiasedness of propensity-score adjustment holds only when the covariate set satisfies strong ignorability.
- [[ignorability]] — specializes: propensity scores are the unit-level inclusion probabilities under a strongly ignorable design