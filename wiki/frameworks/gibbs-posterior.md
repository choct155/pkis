---
aliases: []
also_type: []
analogous-to:
- elbo
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
- bayesian-statistics
- statistical-learning-theory
extends:
- empirical-risk-minimization-erm
- variational-inference
generalizes:
- bayesian-inference
id: pkis:framework:gibbs-posterior
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch14
tags:
- PAC-Bayes
- robust inference
- temperature
- generalised Bayes
- distributional ERM
title: Gibbs Posterior and Generalised Bayesian Inference
understanding: 0
uses:
- kl-divergence
---

## Definition
$$\hat{q}(\theta) = \frac{e^{-\lambda r(\theta)}\pi_0(\theta)}{\int e^{-\lambda r(\theta')}\pi_0(\theta')\,d\theta'}$$

The **Gibbs posterior** is the solution to the distributional ERM problem
$$\hat{q} = \arg\min_{q}\; \mathbb{E}_{q}[r(\theta)] + \tfrac{1}{\lambda} D_{\mathrm{KL}}(q\|\pi_0),$$
where $r(\theta)$ is an empirical risk and $\lambda > 0$ is a temperature. Setting $r = -\tfrac{1}{N}\log p(D\mid\theta)$ and $\lambda = N$ recovers the standard Bayes posterior. Replacing KL with a general divergence and $r$ with an arbitrary loss defines **Generalised Bayesian Inference**.

### Why it matters
The Gibbs posterior provides a principled way to combine any loss function with a prior while retaining PAC-Bayes coverage guarantees. It bridges ERM, Bayesian inference, and robust statistics, explaining why Bayesian methods can be superior to point-estimate methods even when the likelihood is misspecified.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[elbo]] — analogous-to
- [[kl-divergence]] — uses
- [[variational-inference]] — extends
- [[bayesian-inference]] — generalizes
- [[empirical-risk-minimization-erm]] — extends
[To be populated during integration]