---
aliases: []
also_type: []
applies:
- intractable-posterior
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
- probabilistic-inference
extends:
- variational-inference
id: pkis:concept:variational-approximation-bias
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch19
tags:
- variational-inference
- approximation-error
- posterior-bias
- model-identifiability
title: Variational Approximation Bias (Self-Fulfilling Posteriors)
understanding: 0
uses:
- mean-field-variational-inference
---

## Definition
When a model is trained by maximizing the ELBO under a restricted variational family $q$, the model parameters $\theta$ are adapted not only to fit the data but also to make the posterior $p(h|v; \theta)$ easier to approximate by $q$. Specifically, variational learning increases $\mathbb{E}_{h\sim q}\log p(v, h)$, which raises $p(h|v; \theta)$ under regions of high $q$ probability and lowers it elsewhere, causing the true posterior to increasingly resemble $q$.

### Why it matters
This creates a **self-fulfilling prophecy**: a unimodal $q$ family biases training toward models with unimodal posteriors, even if the optimal model under exact inference would have multimodal posteriors. The gap $\log p(v; \theta) - \mathcal{L}(v, \theta, q)$ may appear small after training (the learned $\theta$ is adapted to $q$), but $\theta$ may be far from the true MLE $\theta^* = \arg\max_\theta \log p(v; \theta)$.

### Implication
Evaluating the ELBO gap on a trained model understates the harm from the variational approximation; the true harm can only be assessed by comparing to a model trained with a richer inference procedure.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[intractable-posterior]] — applies
- [[variational-inference]] — extends
- [[mean-field-variational-inference]] — uses
[To be populated during integration]