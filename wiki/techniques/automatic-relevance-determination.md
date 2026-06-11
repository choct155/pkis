---
aliases: []
also_type: []
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
- bayesian-inference
id: pkis:technique:automatic-relevance-determination
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch07
- murphy-pml2-advanced-ch15
tags:
- sparsity
- hyperparameter-optimisation
- evidence-approximation
- Bayesian
- feature-selection
title: Automatic Relevance Determination (ARD)
understanding: 0
---

## Definition
Automatic Relevance Determination assigns a separate precision hyperparameter $\alpha_i$ to each weight $w_i$ in a Gaussian prior $p(w_i|\alpha_i) = \mathcal{N}(w_i|0,\alpha_i^{-1})$. The hyperparameters are optimised by maximising the marginal likelihood (evidence). Parameters for which the marginal likelihood is maximised at $\alpha_i \to \infty$ have posterior distributions concentrated at zero and are effectively pruned. The re-estimation equation
$$\alpha_i^{\text{new}} = \frac{\gamma_i}{m_i^2}, \quad \gamma_i = 1 - \alpha_i\Sigma_{ii}$$
quantifies how well each parameter is determined by the data.

ARD is the mechanism by which Bayesian models can automatically select a sparse set of relevant basis functions or features.

### Why it matters
ARD was introduced by MacKay and Neal in the context of neural networks and generalises naturally to any model expressible as a linear combination of basis functions. In the RVM it explains why many basis functions are pruned: a basis vector poorly aligned with the data is penalised by finite $\alpha_i$ reducing the marginal likelihood. ARD underpins sparse Bayesian learning more broadly.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]