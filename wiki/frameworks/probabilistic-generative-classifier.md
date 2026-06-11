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
- pattern-recognition
id: pkis:framework:probabilistic-generative-classifier
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch04
tags:
- generative-model
- class-conditional-density
- Bayes-theorem
- linear-discriminant
- quadratic-discriminant
- Gaussian-class-conditional
title: Probabilistic Generative Classifier
understanding: 0
---

## Definition
A probabilistic generative classifier models the joint distribution by specifying class-conditional densities $p(\mathbf{x}|C_k)$ and class priors $p(C_k)$, then applies Bayes' theorem to obtain posterior probabilities:

$$p(C_k|\mathbf{x}) = \frac{p(\mathbf{x}|C_k)\,p(C_k)}{\sum_j p(\mathbf{x}|C_j)\,p(C_j)}.$$

When class-conditional densities are Gaussian with a shared covariance, the posterior is a logistic sigmoid (two classes) or softmax (multiple classes) of a linear function of $\mathbf{x}$, yielding linear decision boundaries. Relaxing the shared-covariance assumption produces quadratic discriminant analysis.

### Why it matters
The generative approach separates inference into modelling $p(\mathbf{x}|C_k)$ and $p(C_k)$ independently, allowing synthetic data generation and principled handling of missing data. However it requires more parameters than the discriminative counterpart: for $M$-dimensional Gaussians, $O(M^2)$ vs $O(M)$ parameters. The framework also reveals the exponential-family origin of logistic/softmax posteriors.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]