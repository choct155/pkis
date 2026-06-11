---
aliases: []
also_type: []
analogous-to:
- effective-degrees-of-freedom
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:concept:effective-number-of-parameters-gamma
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch03
specializes:
- effective-number-of-parameters
tags:
- degrees-of-freedom
- regularisation
- evidence-approximation
- model-complexity
title: Effective Number of Parameters ($\gamma$)
understanding: 0
uses:
- evidence-approximation
- regularization
---

## Definition
In a Bayesian linear regression model with weight precision $\alpha$ and noise precision $\beta$, the **effective number of well-determined parameters** is:

$$\gamma = \sum_{i=1}^{M} \frac{\lambda_i}{\alpha + \lambda_i} \in [0, M]$$

where $\lambda_i$ are eigenvalues of $\beta\boldsymbol{\Phi}^T\boldsymbol{\Phi}$. A parameter is *well-determined* when $\lambda_i \gg \alpha$ (data dominates prior); it is *undetermined* (set near zero by prior) when $\lambda_i \ll \alpha$.

### Why it matters
Provides an intuitive measure of the model's effective capacity given both the data and the prior. It corrects the maximum-likelihood noise estimate (replacing $N$ with $N-\gamma$ in the denominator) and appears directly in the evidence re-estimation equations, linking regularisation strength to the number of data-supported degrees of freedom. Analogous to the trace of the hat matrix in classical statistics.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[effective-number-of-parameters]] — specializes
- [[regularization]] — uses
- [[effective-degrees-of-freedom]] — analogous-to
- [[evidence-approximation]] — uses
[To be populated during integration]