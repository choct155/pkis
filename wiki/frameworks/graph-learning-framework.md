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
- network-science
id: pkis:framework:graph-learning-framework
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch30
tags:
- graphs
- structure-learning
- latent-variable-models
- causal-discovery
title: Graph Learning (Latent Variable & Structure Learning)
understanding: 0
uses:
- latent-variable-models
- probabilistic-graphical-models
- graphical-model-structure-learning
- stochastic-block-model
---

## Definition
$$G = (V, E), \quad x_n \in \mathbb{R}^D, \; n=1,\dots,N$$

Graph learning encompasses two complementary tasks: (1) **latent variable modelling of graphs** — given a known graph $G$, fit a generative model with latent features that explains its structure (e.g., community memberships); and (2) **graphical model structure learning** — given an $N \times D$ data matrix, infer the graph $G$ with $N_G$ nodes (typically $N_G = D$), possibly including hidden nodes not present in the data.

The unifying goal is to extract scientifically interpretable or predictively useful structure from relational data.

### Why it matters
Graph learning bridges probabilistic graphical models and network science: it enables causal discovery, protein-interaction inference, neural connectivity mapping, and financial covariance estimation from raw multivariate observations, making it a foundational step for both understanding and intervention in complex systems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[stochastic-block-model]] — uses
- [[graphical-model-structure-learning]] — uses
- [[probabilistic-graphical-models]] — uses
- [[latent-variable-models]] — uses
[To be populated during integration]