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
id: pkis:technique:sensitivity-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch06
- gelman-bda3-ch17
tags:
- sensitivity-analysis
- robustness
- model-checking
- prior-sensitivity
- model-expansion
- bayesian-stats
title: Sensitivity Analysis (Bayesian)
understanding: 0
---

## Definition
Assessment of how much posterior inferences change when other reasonable probability models replace the present one — differing in prior specification, sampling distribution, or which information (e.g. predictors) is included. It is complementary to model checking: a model can pass posterior predictive checks (the data do not contradict it) yet still yield conclusions sensitive to defensible alternatives, since several models may fit equally well but imply different inferences. In principle it is subsumed by a single comprehensive joint ('super') model that mixes over all plausible realities, whose posterior automatically incorporates all sensitivity; in practice such a super-model is conceptually and computationally infeasible, so one instead examines alternatives directly. Typical moves: reweight a marginal posterior such as p(τ|y) by alternative priors to see when inferences are stable; replace a normal population distribution with a longer-tailed t as a robustness check; and judge alternatives by their practical implications, with any candidate constrained to keep predictions realistic (e.g. plausible SAT-score improvements).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]