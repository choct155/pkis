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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:technique:binomial-regression
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch12
tags:
- GLM
- binomial
- logistic-regression
- count-data
title: Binomial Regression
understanding: 0
---

## Definition
$$p(y_n|x_n, N_n, w) = \operatorname{Bin}\!\left(y_n\,\middle|\,\sigma(w^T x_n),\, N_n\right), \quad y_n \in \{0,\ldots,N_n\}$$

Binomial regression models the number of successes in $N_n$ trials as a GLM with the logit canonical link: $\eta_n = w^T x_n$, $A(\eta_n) = N_n\log(1+e^{\eta_n})$, giving
$$\mathbb{E}[y_n] = N_n\sigma(\eta_n), \qquad \mathbb{V}[y_n] = N_n\sigma(\eta_n)(1-\sigma(\eta_n)).$$

### Why it matters
Binary logistic regression is the special case $N_n=1$. The binomial regression framework extends it to aggregate or proportion responses (e.g. number of patients recovering out of $N_n$ treated), and is the canonical way to handle over-dispersed binary outcomes when combined with beta-binomial or quasi-likelihood extensions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]