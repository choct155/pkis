---
aliases: []
also_type: []
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
- statistics
- machine-learning
- probability-theory
id: pkis:concept:prior-likelihood-posterior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch01
tags:
- bayesian
- prior
- posterior
- likelihood
- MAP
- regularisation
title: Prior, Likelihood, and Posterior in Bayesian Inference
understanding: 0
---

## Definition
Bayes' theorem applied to parameter estimation reads
$$p(\mathbf{w}|\mathcal{D}) = \frac{p(\mathcal{D}|\mathbf{w})\,p(\mathbf{w})}{p(\mathcal{D})}, \qquad \text{posterior} \propto \text{likelihood} \times \text{prior}.$$
The **prior** $p(\mathbf{w})$ encodes beliefs before observing data; the **likelihood** $p(\mathcal{D}|\mathbf{w})$ measures data fit; the **posterior** $p(\mathbf{w}|\mathcal{D})$ is the updated belief. The normaliser $p(\mathcal{D})=\int p(\mathcal{D}|\mathbf{w})p(\mathbf{w})\,d\mathbf{w}$ is the marginal likelihood.

### Why it matters
This tripartite decomposition is the operational core of Bayesian statistics. MAP estimation (maximising the posterior) corresponds to regularised likelihood — e.g., a Gaussian prior $p(\mathbf{w}|\alpha)=\mathcal{N}(\mathbf{w}|0,\alpha^{-1}I)$ yields L2-regularised least squares with $\lambda=\alpha/\beta$. Full Bayesian treatment requires integrating over **w** (marginalisation) to obtain predictive distributions.

### Frequentist vs Bayesian contrast
Frequentists treat $\mathbf{w}$ as fixed and reason about hypothetical repeated samples; Bayesians treat $\mathbf{w}$ as random and condition on the single observed dataset.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]