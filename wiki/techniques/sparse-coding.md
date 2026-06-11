---
aliases: []
also_type: []
analogous-to:
- independent-component-analysis
applies:
- unsupervised-learning
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- spike-and-slab
- autoencoder
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- neuroscience
- signal-processing
id: pkis:technique:sparse-coding
instantiates:
- latent-variable-models
- mean-field-recurrent-network-connection
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch13
- goodfellow-deeplearning-ch19
specializes:
- linear-factor-model
tags:
- dictionary-learning
- l1-regularization
- MAP-inference
- unsupervised-learning
- natural-images
title: Sparse Coding
understanding: 0
uses:
- lasso
- nonparametric-encoder
- maximum-a-posteriori-estimation-map
- map-inference-as-approximate-vi
- explaining-away
- regularization
---

## Definition
$$\mathbf{h}^* = \arg\min_{\mathbf{h}} \; \lambda\|\mathbf{h}\|_1 + \beta\|\mathbf{x} - \mathbf{W}\mathbf{h}\|_2^2$$

A linear factor model with a sparsity-inducing prior (e.g., Laplace or Student-t) over latent codes $\mathbf{h}$, trained by alternating between (i) MAP inference of $\mathbf{h}$ given $\mathbf{W}$ (the above $\ell_1$-penalised least-squares problem) and (ii) gradient descent on $\mathbf{W}$ given $\mathbf{h}$.

### Why it matters
Sparse coding demonstrates that using an **optimization-based (non-parametric) encoder** instead of a fixed learned encoder can reduce encoder generalisation error, since the MAP optimisation always finds the best code for the current decoder weights. It also connects dictionary learning to Bayesian inference: the $\ell_1$ penalty is the log-prior under a Laplace distribution. Sparse codes learned from natural images reproduce oriented Gabor-like receptive fields similar to primary visual cortex simple cells.

### Drawbacks
The non-parametric encoder is computationally expensive at test time and does not support straightforward backpropagation, making end-to-end supervised fine-tuning difficult. The factorial sparse prior also leads to poor samples because random subsets of features are activated independently.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[regularization]] — uses
- [[mean-field-recurrent-network-connection]] — instantiates
- [[explaining-away]] — uses
- [[latent-variable-models]] — instantiates
- [[map-inference-as-approximate-vi]] — uses
- [[unsupervised-learning]] — applies
- [[autoencoder]] — contrasts-with
- [[spike-and-slab]] — contrasts-with
- [[independent-component-analysis]] — analogous-to
- [[maximum-a-posteriori-estimation-map]] — uses
- [[nonparametric-encoder]] — uses
- [[lasso]] — uses
- [[linear-factor-model]] — specializes
[To be populated during integration]