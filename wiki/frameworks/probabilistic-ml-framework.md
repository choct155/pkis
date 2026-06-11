---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- probability
id: pkis:framework:probabilistic-ml-framework
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch01
tags:
- probabilistic-modeling
- uncertainty
- bayesian
- unifying-framework
title: Probabilistic Machine Learning Framework
understanding: 0
---

## Definition
A framework in which all unknown quantities—future predictions, model parameters, latent variables—are treated as random variables endowed with probability distributions:
$$p(y|x;\theta),\quad p(x|\theta),\quad p(\theta|\mathcal{D})$$
for supervised, unsupervised, and Bayesian settings respectively. The framework unifies learning, inference, and decision-making under a single probabilistic umbrella.

### Why it matters
By casting ML as probabilistic inference, every model choice becomes a statement about prior beliefs and likelihood, enabling principled uncertainty quantification, optimal decision-making (via expected utility), and connections to information theory, statistical physics, and Bayesian statistics.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]