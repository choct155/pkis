---
aliases: []
also_type: []
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
- information-theory
id: pkis:result:bayesian-occams-razor
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch05
tags:
- Occam-razor
- marginal-likelihood
- model-selection
- model-complexity
- Bayesian
title: Bayesian Occam's Razor Effect
understanding: 0
---

## Definition
For two models $m_1$ (simpler) and $m_2$ (more complex), if both achieve comparable maximum likelihood $p(D|\hat{\theta}_k, m_k)$, the **marginal likelihood** $p(D|m_k)=\int p(D|\theta,m_k)p(\theta|m_k)d\theta$ automatically favours the simpler model:

$$p(D|m_1) > p(D|m_2) \quad \text{(typically)}$$

**Mechanism (conservation of probability mass):** Since $\sum_{D'}p(D'|m)=1$, a complex model that can predict many datasets must spread its probability mass thinly. A simpler model concentrates its prior mass near the good parameters, so it assigns higher average likelihood to the observed data.

### Why it matters
This result shows that Bayesian model selection via marginal likelihoods implements Occam's razor *automatically*, without the need for an explicit penalty term. It provides the conceptual foundation for BIC, AIC, and MDL penalties (all of which are approximations to $-\log p(D|m)$). The Occam factor $\frac{1}{2}\log|\mathbf{H}|$ in the Laplace approximation quantifies the complexity penalty in closed form.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]