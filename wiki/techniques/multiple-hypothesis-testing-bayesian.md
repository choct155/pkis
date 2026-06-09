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
contrasts-with:
- hypothesis-testing
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
generalizes:
- likelihood-ratio-evidence
id: pkis:technique:multiple-hypothesis-testing-bayesian
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch04
specializes:
- bayesian-model-comparison
tags:
- jaynes
- odds
- evidence
- sequential-inference
- model-selection
- dead-hypotheses
title: Bayesian Multiple Hypothesis Testing
understanding: 0
uses:
- likelihood-ratio-evidence
- bayesian-inference
- nuisance-parameters
---

## Definition
Updating the posterior odds of each of n>2 mutually exclusive, exhaustive hypotheses against its negation as data accumulate, where the negation pools all rival hypotheses — so the per-datum evidence increment is generally not additive and the effective comparison is always against whichever rival is currently most plausible.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-model-comparison]] — specializes: discrete multi-hypothesis case of comparing models by posterior odds
- [[nuisance-parameters]] — uses: composite hypotheses handled by integrating out nuisance parameters
- [[hypothesis-testing]] — contrasts-with: Bayesian odds-update vs. frequentist test-statistic/rejection-region procedure
- [[bayesian-inference]] — uses: direct application of Bayes' theorem at the hypothesis level
- [[likelihood-ratio-evidence]] — generalizes: extends the binary odds update to n>2 hypotheses, losing independent additivity
- [[likelihood-ratio-evidence]] — uses: each hypothesis updated by prior-odds times likelihood ratio in evidence/dB form
[To be populated during integration]