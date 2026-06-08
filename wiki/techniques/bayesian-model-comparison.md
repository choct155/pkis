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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:technique:bayesian-model-comparison
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch03
tags:
- posterior-odds
- bayes-factor
- evidence
- hypothesis-comparison
- likelihood-ratio
title: Bayesian Model Comparison
understanding: 0
---

## Definition
Comparing competing models by applying Bayes' theorem at the level of hypotheses rather than parameters. For models $H_1, H_0$ the posterior odds factor into a prior odds times the evidence ratio:
$$\frac{P(H_1\mid D)}{P(H_0\mid D)} = \frac{P(D\mid H_1)}{P(D\mid H_0)} \cdot \frac{P(H_1)}{P(H_0)}.$$
The data-dependent factor $P(D\mid H_1)/P(D\mid H_0)$ is the ratio of marginal likelihoods (the **Bayes factor**); for a parameter-free model the evidence is just its likelihood.

### Built-in Occam's razor
Because each model's evidence is its likelihood averaged over its prior, an over-flexible model dilutes its predictions and is penalized automatically — no explicit complexity term is added by hand.

### Why it matters
It replaces orthodox null-hypothesis testing with a single coherent quantity. MacKay uses it to defuse the Belgian-euro coin claim: the p-value of 7% suggests bias, but the Bayes factor gives at most ~2.3:1 either way. 'The p-values and significance levels of classical statistics should be treated with extreme caution.'

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]