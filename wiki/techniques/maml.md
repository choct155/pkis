---
aliases: []
also_type: []
analogous-to:
- value-of-information
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
- meta-learning
- few-shot-learning
id: pkis:technique:maml
instantiates:
- hierarchical-bayesian-models
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- meta-learning
- few-shot
- gradient-based
- empirical-bayes
- fast-adaptation
title: Model-Agnostic Meta-Learning (MAML)
understanding: 0
uses:
- gradient-descent
---

## Definition
MAML learns an initial parameter vector $\xi$ such that a small number of gradient steps on a new task produces a good task-specific model. The meta-objective is:
$$\xi^* = \arg\max_\xi \frac{1}{J}\sum_{j=1}^J \log p(D^j_{\text{valid}}|\hat{\theta}_j(\xi, D^j_{\text{train}}))$$
where $\hat{\theta}_j = \xi - \eta\nabla_\xi\mathcal{L}(D^j_{\text{train}};\xi)$ after $K$ gradient steps (inner loop), and the outer loop optimises over $\xi$ via second-order gradients through the inner update.

### Why it matters
MAML is equivalent to empirical Bayes with a Gaussian prior centred at $\xi$, providing a probabilistic interpretation. It is *model-agnostic* — applicable to any gradient-based learner — and achieves strong few-shot classification, regression, and RL results. Variants (FOMAML, Reptile) approximate the second-order update for efficiency.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[value-of-information]] — analogous-to: Meta-learning optimises for fast adaptation, analogously to maximising VOI per query in active learning.
- [[gradient-descent]] — uses
- [[hierarchical-bayesian-models]] — instantiates: MAML is equivalent to empirical Bayes MAP estimation with a Gaussian prior centred at ξ.
[To be populated during integration]