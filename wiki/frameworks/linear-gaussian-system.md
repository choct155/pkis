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
- probability
- statistics
- machine-learning
id: pkis:framework:linear-gaussian-system
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch03
tags:
- gaussian
- bayesian-inference
- latent-variables
- kalman-filter
title: Linear Gaussian System
understanding: 0
---

## Definition
A **linear Gaussian system** (LGS) couples a latent Gaussian prior to a noisy linear observation model:
$$p(z) = \mathcal{N}(z | \mu_z, \Sigma_z)$$
$$p(y | z) = \mathcal{N}(y | Wz + b, \Sigma_y)$$

The joint $p(z, y)$ is Gaussian with
$$\mu_{\text{joint}} = \begin{pmatrix}\mu_z \\ W\mu_z + b\end{pmatrix}, \quad \Sigma_{\text{joint}} = \begin{pmatrix}\Sigma_z & \Sigma_z W^T \\ W\Sigma_z & \Sigma_y + W\Sigma_z W^T\end{pmatrix}$$
and the posterior is given by Bayes rule for Gaussians (Equation 3.37).

### Why it matters
LGSs are the backbone of Kalman filtering, sensor fusion, Bayesian linear regression, factor analysis, and principal component analysis. Because the Gaussian family is closed under linear transformations and conditioning, all inference is exact and analytic.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]