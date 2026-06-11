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
- probabilistic-modelling
id: pkis:framework:four-tasks-probabilistic-ml
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch01
tags:
- prediction
- generation
- discovery
- control
- taxonomy
title: 'Four Tasks of Probabilistic ML: Prediction, Generation, Discovery, Control'
understanding: 0
---

## Definition
A taxonomy organising probabilistic machine learning into four canonical task types, each corresponding to a distinct model family:

| Task | Model | Goal |
|------|-------|------|
| **Prediction** | $p(y|x)$ | Infer output given input |
| **Generation** | $p(x)$ or $p(x|c)$ | Sample new data, possibly conditioned |
| **Discovery** | $p(z,x)=p(z)p(x|z)$ | Infer latent structure $p(z|x)$ |
| **Control** | $p(y|x,a)$, policy $\pi$ | Make decisions under uncertainty |

This organising principle structures what priors, inference algorithms, and evaluation metrics are appropriate for each problem type.

### Why it matters
Many ML papers conflate these tasks or borrow inappropriate methods from one regime for another. Making the four-way distinction explicit clarifies which tools (discriminative vs. generative vs. latent-variable vs. decision-theoretic) are applicable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]