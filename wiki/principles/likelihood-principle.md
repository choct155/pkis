---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:principle:likelihood-principle
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch02
tags:
- likelihood
- inference
- bayes
- sufficiency
title: Likelihood Principle
understanding: 0
---

## Definition
All the information the observed data $D$ carry about competing hypotheses is contained in the likelihood — the values $P(D\mid H_i)$ evaluated *at the data that actually occurred*. Two experiments yielding proportional likelihood functions support identical inferences, regardless of which other outcomes were possible but did not happen.

Intuition: only the probability the model assigned to *what actually happened* matters — the probabilities of other outcomes that did not occur are irrelevant.

### Illustration
MacKay's three-door (Monty Hall) variants make this vivid: the host opening door 3 deliberately versus an earthquake popping door 3 open look visually identical, yet give different answers (switch vs. indifferent) because $P(D\mid H_i)$ differs. 'All that matters are the relative values of $P(D\mid H_i)$ for the value of $D$ that actually occurred.'

### Tension with orthodox statistics
The likelihood principle falls directly out of Bayes' theorem (the posterior depends on data only via the likelihood), yet many classical/frequentist procedures — which condition on the full sample space, e.g. p-values and stopping-rule-dependent tests — violate it. It is a sharp dividing line between Bayesian and sampling-theory inference.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]