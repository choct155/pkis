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
id: pkis:technique:bayesian-neural-network-laplace
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch05
tags:
- laplace
- uncertainty
- model-selection
- evidence-framework
title: Bayesian Neural Network via Laplace Approximation
understanding: 0
---

## Definition
A practical Bayesian treatment of neural networks (MacKay 1992) that approximates the intractable posterior $p(\mathbf{w}|\mathcal{D})$ with a Gaussian centred at the MAP weight vector:
$$q(\mathbf{w}|\mathcal{D}) = \mathcal{N}(\mathbf{w}\mid\mathbf{w}_{\text{MAP}},\,\mathbf{A}^{-1}), \quad \mathbf{A} = \alpha\mathbf{I} + \beta\mathbf{H}$$
where $\mathbf{H}$ is the Hessian of the sum-of-squares error at $\mathbf{w}_{\text{MAP}}$.

**Predictive distribution (regression)**: linearising $y(\mathbf{x},\mathbf{w})$ around $\mathbf{w}_{\text{MAP}}$ yields
$$p(t|\mathbf{x},\mathcal{D}) = \mathcal{N}\!\left(t\mid y(\mathbf{x},\mathbf{w}_{\text{MAP}}),\;\beta^{-1}+\mathbf{g}^T\mathbf{A}^{-1}\mathbf{g}\right)$$
where $\mathbf{g}=\nabla_\mathbf{w}y|_{\mathbf{w}_{\text{MAP}}}$.

**Hyperparameter optimisation**: the log evidence is
$$\ln p(\mathcal{D}|\alpha,\beta) \approx -E(\mathbf{w}_{\text{MAP}}) - \tfrac{1}{2}\ln|\mathbf{A}| + \tfrac{W}{2}\ln\alpha + \tfrac{N}{2}\ln\beta + \text{const}$$
maximised iteratively: $\alpha = \gamma/\mathbf{w}_{\text{MAP}}^T\mathbf{w}_{\text{MAP}}$, $1/\beta = \|\mathbf{y}-\mathbf{t}\|^2/(N-\gamma)$.

### Why it matters
Provides calibrated predictive uncertainty, automatic hyperparameter tuning, and model comparison (via evidence) for nonlinear networks, all at the cost of a single MAP optimisation plus Hessian computation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]