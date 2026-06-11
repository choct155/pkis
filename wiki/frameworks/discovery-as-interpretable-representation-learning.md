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
- probability
generalizes:
- supervised-learning
- unsupervised-learning
id: pkis:framework:discovery-as-interpretable-representation-learning
instantiates:
- prediction-generation-subroutines-discovery
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch27
tags:
- discovery
- interpretability
- latent-variables
- inverse-problems
- representation-learning
title: Discovery as Interpretable Representation Learning
understanding: 0
uses:
- latent-variable-models
- inverse-modeling-framework
---

## Definition
$$\hat{z}(x) = \arg\max_z p(z|x) = \arg\max_z \log p(z) + \log p(x|z)$$

A meta-goal in machine learning where, rather than optimizing predictive accuracy or generative fidelity alone, the aim is to find a structured, human-meaningful latent representation $z$ of observed high-dimensional data $x$. The latent variables are assumed to causally generate the observations, and interpretability for a domain expert is a first-class requirement.

### Why it matters
Supervised and unsupervised learning optimize measurable objectives (conditional/unconditional likelihood) but do not guarantee that learned features are interpretable or stable. Discovery tasks—common in science, medicine, and engineering—require models whose latent structure can be audited, validated against domain knowledge, and acted upon. This framework situates prediction and generation as subroutines within a broader inverse-modeling pipeline.

### Relationship to inverse problems
When the forward map $z \to x$ is many-to-one (perceptual aliasing), the inverse $x \to z$ is ill-posed; a prior $p(z)$ regularises the solution. Parameter estimation ($\theta$) and even model structure may be simultaneously unknown, leading to joint inference over $(z, \theta, \text{structure})$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[prediction-generation-subroutines-discovery]] — instantiates
- [[unsupervised-learning]] — generalizes
- [[supervised-learning]] — generalizes
- [[inverse-modeling-framework]] — uses
- [[latent-variable-models]] — uses
[To be populated during integration]