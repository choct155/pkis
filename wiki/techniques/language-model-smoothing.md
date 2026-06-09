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
- deep-learning
- information-theory
- bayesian-stats
id: pkis:technique:language-model-smoothing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
tags:
- nlp
- n-gram
- smoothing
- backoff
- variance-reduction
title: Smoothing (Language Models)
understanding: 0
uses:
- n-gram-language-model
- em-algorithm
---

## Definition
A family of techniques for reserving probability mass for never-seen events in a count-based language model, reducing the high variance of low-frequency n-gram estimates and avoiding catastrophic zero probabilities. Laplace (add-one) smoothing adopts a uniform prior, giving best estimate 1/(N+2) for an event seen zero times in N trials; it is correct in spirit but performs poorly for many NLP applications. Backoff models fall back from an n-gram with low/zero count to the (n-1)-gram. Linear interpolation smoothing blends trigram, bigram, and unigram estimates with weights lambda_3 + lambda_2 + lambda_1 = 1, where the lambdas may be fixed, trained by EM, or made count-dependent (trust higher-order grams when their counts are high). More sophisticated schemes include Witten-Bell and Kneser-Ney; a competing philosophy ('stupid backoff') argues that with a large enough corpus simple smoothing suffices. All variants pursue the same goal: reducing variance in the language model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[em-algorithm]] — uses
- [[n-gram-language-model]] — uses
[To be populated during integration]