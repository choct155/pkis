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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:concept:predictive-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch14
tags:
- supervised-learning
- discriminative
- regression
- parametric
- non-parametric
title: Predictive Model (Discriminative / Regression)
understanding: 0
---

## Definition
$$p(y \mid f(\mathbf{x};\theta))$$

A **predictive model** estimates a conditional probability distribution over outputs $y \in \mathcal{Y}$ given inputs $\mathbf{x} \in \mathcal{X}$ via a function $f$ fit from labeled data $D = \{(\mathbf{x}_n, y_n)\}_{n=1}^N$. When $\mathcal{Y}$ is discrete the model is called **discriminative**; when $\mathcal{Y} = \mathbb{R}^C$ it is called a **regression model**. Parametric predictive models fix the number of parameters independently of $N$, while non-parametric models grow with $N$.

### Why it matters
Predictive models are the central workhorse of supervised ML; the distinction between parametric/non-parametric and discriminative/generative organises the entire model zoo and drives choices of fitting procedure, evaluation metric, and uncertainty quantification strategy.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]