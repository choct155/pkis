---
aliases: []
also_type: []
applies:
- conjugate-prior
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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:concept:dirichlet-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch23
tags:
- probability-distribution
- conjugate-prior
- multinomial
- simplex
- concentration-parameter
title: Dirichlet Distribution
understanding: 0
uses:
- gamma-distribution
---

## Definition
The **Dirichlet distribution** is a density over an $I$-dimensional probability vector $\mathbf{p}$ with $p_i>0$ and $\sum_i p_i = 1$ — i.e. a distribution over the simplex. Parameterized as $\mathbf{u}=\alpha\mathbf{m}$ with a normalized base measure $\mathbf{m}$ ($\sum_i m_i=1$) and concentration $\alpha>0$,

$$P(\mathbf{p} \mid \alpha\mathbf{m}) = \frac{1}{Z(\alpha\mathbf{m})}\prod_{i=1}^{I} p_i^{\alpha m_i - 1}\,\delta\!\left(\sum_i p_i - 1\right), \qquad Z(\alpha\mathbf{m}) = \frac{\prod_i \Gamma(\alpha m_i)}{\Gamma(\alpha)},$$

with mean $\mathbf{m}$. The beta distribution is exactly the $I=2$ case.

### Role of the concentration parameter
The scalar $\alpha$ controls sharpness, playing the role for $\mathbf{p}$ that the precision $\tau=1/\sigma^2$ plays for a Gaussian. Large $\alpha$ peaks $\mathbf{p}$ tightly around $\mathbf{m}$; small $\alpha$ produces sparse samples where one or two components seize almost all the mass — a Zipf-like power law as $\alpha\to 0$. Operationally, $\alpha$ is the number of pseudo-observations needed before data dominate the prior in predictions.

### Why it matters
The Dirichlet is the conjugate prior for the multinomial/categorical likelihood and for the parameters of mixture and topic models. It satisfies a clean **additivity** property — collapsing categories sums the corresponding hyperparameters — which makes coarse- and fine-grained Bayesians' inferences mutually consistent. The softmax basis $p_i \propto e^{a_i}$ ($\sum_i a_i = 0$) removes the awkward minus-ones from the exponents.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gamma-distribution]] — uses: Dirichlet normalization is built from gamma functions; its components can be generated as normalized independent gamma variates.
- [[conjugate-prior]] — applies: Dirichlet is the conjugate prior for the multinomial/categorical likelihood.
[To be populated during integration]