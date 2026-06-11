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
- probability-theory
- generative-modeling
id: pkis:concept:implicit-generative-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- generative-model
- likelihood-free
- simulation-based-inference
- GAN
title: Implicit Generative Model
understanding: 0
---

## Definition
An implicit probabilistic model defines a stochastic procedure to generate data without specifying an explicit parametric likelihood $\log q_\theta(x)$. The generating procedure is:
$$x = G_\theta(z'),\quad z'\sim q(z)$$
with the induced density
$$q_\theta(x) = \frac{\partial}{\partial x_1}\cdots\frac{\partial}{\partial x_d}\int_{\{G_\theta(z)\le x\}} q(z)\,dz$$
which is generally intractable. Intuitively, the model is fully specified by its sampling path rather than a closed-form density.

### Why it matters
Implicit models are the natural language for mechanistic simulators (climate, ecology, genetics) and form the backbone of GANs. Because no likelihood is available, they require likelihood-free learning principles based purely on samples, motivating an entire family of two-sample training objectives.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]