---
aliases: []
also_type: []
analogous-to:
- language-model-smoothing
applies:
- naive-bayes-assumption
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- natural-language-processing
id: pkis:technique:laplace-smoothing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch09
tags:
- smoothing
- bayesian-inference
- naive-bayes
- dirichlet-prior
- zero-count-problem
title: Laplace (Add-One) Smoothing
understanding: 0
uses:
- dirichlet-distribution
- conjugate-prior
---

## Definition
$$\hat{\theta}_{dck} = \frac{\beta_{dck} + N_{dck}}{\sum_{k'} (\beta_{dck'} + N_{dck'})}, \quad \beta_{dck}=1 \Rightarrow \hat{\theta}_{dc} = \frac{1 + N_{dc1}}{2 + N_{dc}}$$

Add-one (Laplace) smoothing adds a pseudo-count of 1 to every category's empirical count before normalising, corresponding to a uniform Dirichlet prior $\text{Dir}(\mathbf{1})$ over the categorical parameters. More generally, setting $\beta_{dck} > 0$ gives add-$\beta$ smoothing.

### Why it matters
Zero empirical counts (unseen events) cause the MLE to assign zero probability to any future example containing that feature, making the entire posterior zero — a catastrophic failure in classification. Laplace smoothing guarantees strictly positive probability for every combination of feature value and class, at the cost of a slight bias. It is the standard default for discrete naive Bayes classifiers and n-gram language models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[conjugate-prior]] — uses
- [[language-model-smoothing]] — analogous-to
- [[dirichlet-distribution]] — uses
- [[naive-bayes-assumption]] — applies
[To be populated during integration]