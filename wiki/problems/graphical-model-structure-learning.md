---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- causal-inference
id: pkis:problem:graphical-model-structure-learning
instantiates:
- model-selection-problem
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- causal-discovery
related_concepts: []
sources:
- murphy-pml2-advanced-ch30
tags:
- graph-structure
- model-selection
- pgm
- causal-discovery
title: Graphical Model Structure Learning
understanding: 0
uses:
- probabilistic-graphical-models
- graphical-lasso
- score-based-dag-learning
- constraint-based-structure-learning
---

## Definition
Given an $N \times D$ data matrix $\mathbf{X}$ assumed to be i.i.d. from some distribution $p(\mathbf{x}; G, \theta)$, infer the graph $G = (V, E)$ (directed or undirected, with $|V| = D$ or including extra latent nodes) that best explains the observed correlations.

Formal objective: select $G$ (and estimate $\theta$) to maximise a penalised score
$$\hat{G} = \arg\max_{G} \; \log p(\mathbf{X} \mid G, \hat{\theta}_G) - \text{pen}(G)$$
or equivalently to minimise a regularised reconstruction loss subject to structural constraints.

### Why it matters
Structure learning is the enabling step for three high-value applications: (i) **scientific understanding** — recovering interaction networks (e.g., protein phosphorylation graphs); (ii) **prediction** — building sparse covariance models for portfolio management or traffic forecasting; (iii) **causal inference** — learning structural causal models (SCMs) to support intervention and counterfactual reasoning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[constraint-based-structure-learning]] — uses
- [[score-based-dag-learning]] — uses
- [[graphical-lasso]] — uses
- [[model-selection-problem]] — instantiates
- [[causal-discovery]] — prerequisite-of
- [[probabilistic-graphical-models]] — uses
[To be populated during integration]