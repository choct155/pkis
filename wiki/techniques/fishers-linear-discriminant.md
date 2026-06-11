---
aliases: []
also_type: []
analogous-to:
- linear-function-approximation-rl
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- logistic-regression
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- pattern-recognition
id: pkis:technique:fishers-linear-discriminant
instantiates:
- linear-discriminant-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch04
tags:
- linear-discriminant
- dimensionality-reduction
- classification
- between-class-covariance
- within-class-covariance
title: Fisher's Linear Discriminant
understanding: 0
uses:
- linear-separability
- eigendecomposition
---

## Definition
$$\mathbf{w} \propto \mathbf{S}_W^{-1}(\mathbf{m}_2 - \mathbf{m}_1)$$

where $\mathbf{S}_W = \sum_{k}\sum_{n\in C_k}(\mathbf{x}_n-\mathbf{m}_k)(\mathbf{x}_n-\mathbf{m}_k)^T$ is the within-class covariance matrix and $\mathbf{m}_k$ are the class means. The direction $\mathbf{w}$ is found by maximising the Fisher criterion

$$J(\mathbf{w}) = \frac{\mathbf{w}^T\mathbf{S}_B\mathbf{w}}{\mathbf{w}^T\mathbf{S}_W\mathbf{w}}$$

where $\mathbf{S}_B = (\mathbf{m}_2-\mathbf{m}_1)(\mathbf{m}_2-\mathbf{m}_1)^T$ is the between-class covariance. The intuition is to find a one-dimensional projection that simultaneously maximises between-class separation and minimises within-class scatter.

### Why it matters
Fisher's linear discriminant is the canonical dimensionality-reduction approach to two-class (and, via $\mathbf{S}_W^{-1}\mathbf{S}_B$ eigendecomposition, multi-class) linear classification. It is equivalent to least-squares classification under a specific target-coding scheme, and forms the theoretical backbone of Linear Discriminant Analysis.

### Multi-class extension
For $K$ classes one maximises $J(\mathbf{W}) = \text{Tr}\{\mathbf{s}_W^{-1}\mathbf{s}_B\}$ over a projection matrix $\mathbf{W}$; the solution is the leading eigenvectors of $\mathbf{S}_W^{-1}\mathbf{S}_B$. At most $K-1$ informative projection directions exist because $\mathbf{S}_B$ has rank at most $K-1$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[linear-function-approximation-rl]] — analogous-to: Both find weight vectors maximising a ratio criterion over projected representations
- [[logistic-regression]] — contrasts-with: FDA is a discriminant projection; logistic regression directly models posterior
- [[eigendecomposition]] — uses: Multi-class FDA solved via eigenvectors of S_W^{-1} S_B
- [[linear-separability]] — uses
- [[linear-discriminant-analysis]] — instantiates
[To be populated during integration]