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
date_created: '2026-06-01'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:concept:bayesian-inference
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- '[[kroese-statistical-modeling-ch08]]'
tags:
- bayesian
- posterior
- inference
title: Bayesian Inference
understanding: 0
---

## Definition
Inference that treats unknown quantities as random variables and updates beliefs via Bayes' rule, yielding posterior distributions rather than point estimates. Foundational to the program's truth-discovery, calibration, and intent-posterior framings.

## Reading Path
- [[kroese-statistical-modeling-ch08]] — canonical source

## Connections
[To be populated during integration]

## Needs Canonical Source
Resolved — canonical source(s) attached above.

## Forward vs inverse probability
MacKay frames inference as **inverse probability**: given a generative (forward) model $P(d\mid\theta)$, compute $P(\theta\mid d)$ via Bayes' theorem,
$$\text{posterior} = \frac{\text{likelihood}\times\text{prior}}{\text{evidence}}.$$
The **evidence** (marginal likelihood) $P(D\mid H)=\sum_\theta P(D\mid\theta)P(\theta)$ normalizes the posterior. Crucially, **likelihood $\ne$ probability**: $P(d\mid\theta)$ is a probability over $d$ for fixed $\theta$, but a *likelihood* of $\theta$ for fixed observed $d$. Predictions should marginalize over the posterior rather than plug in the single most plausible hypothesis.