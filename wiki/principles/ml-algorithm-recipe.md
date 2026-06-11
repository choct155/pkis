---
aliases: []
also_type: []
applies:
- supervised-learning
- unsupervised-learning
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
id: pkis:principle:ml-algorithm-recipe
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch05
tags:
- algorithm-design
- cost-function
- optimization
- model-specification
- taxonomy
title: 'ML Algorithm Recipe: Dataset + Cost + Model + Optimizer'
understanding: 0
uses:
- maximum-likelihood-estimation
- regularization
- minibatch-sgd
---

## Definition
Nearly every machine learning algorithm can be decomposed into four interchangeable components:

1. **Dataset** — the observed examples $(\mathbf{X}, \mathbf{y})$ or just $\mathbf{X}$ for unsupervised tasks.
2. **Model** — a parametric family $p_{\text{model}}(\cdot;\boldsymbol{\theta})$ or a function $f(\cdot;\boldsymbol{\theta})$.
3. **Cost function** — typically $J(\boldsymbol{\theta})=-\mathbb{E}_{\hat{p}_{\text{data}}}\log p_{\text{model}} + \Omega(\boldsymbol{\theta})$.
4. **Optimization procedure** — closed-form (normal equations) or iterative (SGD, Adam).

Swapping components independently generates a large taxonomy of algorithms.

### Why it matters
This compositional view demystifies the proliferation of ML algorithms: most differences reduce to choices of model family, loss function, and optimizer. It makes algorithm design systematic and facilitates the transfer of improvements (e.g., a better optimizer) across many methods simultaneously.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[minibatch-sgd]] — uses
- [[regularization]] — uses
- [[maximum-likelihood-estimation]] — uses
- [[unsupervised-learning]] — applies
- [[supervised-learning]] — applies
[To be populated during integration]