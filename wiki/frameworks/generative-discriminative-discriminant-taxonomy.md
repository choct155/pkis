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
id: pkis:framework:generative-discriminative-discriminant-taxonomy
instantiates:
- generative-vs-discriminative-models
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch01
tags:
- generative-model
- discriminative-model
- discriminant-function
- classification
- posterior
title: Generative vs Discriminative vs Discriminant-Function Approaches
understanding: 0
uses:
- decision-theory-foundations
- bayesian-inference
- naive-bayes-model
- decision-regions-and-boundaries
---

## Definition
Three levels of ambition for solving a classification problem, in decreasing complexity:

**(a) Generative**: Model the joint density $p(\mathbf{x},C_k)$ (equivalently: class-conditional $p(\mathbf{x}|C_k)$ plus priors $p(C_k)$), then apply Bayes' theorem to obtain posteriors. Enables outlier/novelty detection and easy prior adjustment.

**(b) Discriminative**: Directly model the posterior $p(C_k|\mathbf{x})$, bypassing the class-conditional density.

**(c) Discriminant function**: Learn a mapping $f:\mathbf{x}\mapsto$ class label directly, no probabilities. Simplest but loses ability to re-weight for new loss matrices, apply reject option, or combine modular posteriors.

### Why it matters
The taxonomy clarifies the information/computation trade-off: generative models are data-hungry but flexible; discriminant functions are data-efficient for the immediate task but brittle to changing decision criteria. Posterior probabilities are essential for reject options, loss-matrix adjustments, combining independent modules via the naive Bayes factorisation $p(C_k|x_I,x_B)\propto p(C_k|x_I)p(C_k|x_B)/p(C_k)$, and compensating for imbalanced training sets.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[decision-regions-and-boundaries]] — uses
- [[naive-bayes-model]] — uses
- [[bayesian-inference]] — uses
- [[decision-theory-foundations]] — uses
- [[generative-vs-discriminative-models]] — instantiates
[To be populated during integration]