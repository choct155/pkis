---
aliases: []
also_type: []
applies:
- graphical-model-structure-learning
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:result:graphical-lasso-sparsity-tradeoff
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch30
tags:
- regularization-path
- precision-matrix
- sparsity
- gaussian-graphical-model
title: Graphical Lasso Sparsity–Accuracy Trade-off
understanding: 0
uses:
- graphical-lasso
---

## Definition
In the graphical lasso objective
$$\hat{\Omega}_\lambda = \arg\max_{\Omega \succ 0} \left[ \log \det \Omega - \operatorname{tr}(S\Omega) - \lambda\|\Omega\|_1 \right],$$
the regularisation parameter $\lambda$ continuously controls the sparsity of the recovered graph:
- $\lambda \to \infty$: $\hat{\Omega} \to \operatorname{diag}$, producing an **empty graph** (all nodes independent).
- $\lambda = 0$: $\hat{\Omega} = S^{-1}$ (maximum likelihood), producing a **fully connected graph**.
- Intermediate $\lambda$: sparse graph whose edge set encodes conditional independence structure.

Empirical demonstrations (e.g., cytometry data from Sachs et al. 2005) show that moderate $\lambda$ values recover biologically interpretable protein-interaction networks, while $\lambda=0$ yields a dense, uninterpretable result.

### Why it matters
This monotone relationship between $\lambda$ and sparsity makes the regularisation path of graphical lasso a practical diagnostic: plotting recovered graphs at a sequence of $\lambda$ values reveals which edges are robust (appear at high $\lambda$) versus spurious (appear only at low $\lambda$).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[graphical-model-structure-learning]] — applies
- [[graphical-lasso]] — uses
[To be populated during integration]