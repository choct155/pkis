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
date_created: '2026-06-01'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:bayesian-inference
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- '[[kroese-statistical-modeling-ch08]]'
tags:
- bayesian
- posterior
- inference
title: Bayesian Inference
understanding: 0
---

## Definition
Inference that treats unknown quantities as random variables and updates beliefs via Bayes' rule, yielding posterior distributions rather than point estimates. Foundational to the program's truth-discovery, calibration, and intent-posterior framings.

## Reading Path
- [[kroese-statistical-modeling-ch08]] — canonical source

## Connections
[To be populated during integration]

## Needs Canonical Source
Resolved — canonical source(s) attached above.

## Forward vs inverse probability
MacKay frames inference as **inverse probability**: given a generative (forward) model $P(d\mid\theta)$, compute $P(\theta\mid d)$ via Bayes' theorem,
$$\text{posterior} = \frac{\text{likelihood}\times\text{prior}}{\text{evidence}}.$$
The **evidence** (marginal likelihood) $P(D\mid H)=\sum_\theta P(D\mid\theta)P(\theta)$ normalizes the posterior. Crucially, **likelihood $\ne$ probability**: $P(d\mid\theta)$ is a probability over $d$ for fixed $\theta$, but a *likelihood* of $\theta$ for fixed observed $d$. Predictions should marginalize over the posterior rather than plug in the single most plausible hypothesis.

## Linear-Gaussian inference yields a closed-form posterior
Deconvolution illustrates Bayesian inference in the fully tractable linear-Gaussian setting. With a Gaussian likelihood $P(\mathbf{d}\mid\mathbf{f})$ and a Gaussian prior $P(\mathbf{f})$, the posterior $P(\mathbf{f}\mid\mathbf{d}) \propto P(\mathbf{d}\mid\mathbf{f})P(\mathbf{f})$ is itself Gaussian. It is therefore fully summarized by its mean, which here coincides with the most probable image $\mathbf{f}_{MP}$, and its covariance
$$\Sigma_{f\mid d} = \big[-\nabla\nabla \log P(\mathbf{f}\mid\mathbf{d})\big]^{-1},$$
the inverse Hessian of the negative log-posterior, which supplies joint error bars on the reconstruction. The evidence $P(\mathbf{d})$, an unimportant normalizer for the point estimate, becomes central at a higher level for comparing noise levels, prior scales, or candidate point spread functions. This is the rare case where the Laplace approximation is exact.

## The three-step Bayesian workflow (Gelman)
Gelman et al. (BDA3, Ch. 1) frame applied Bayesian data analysis as an iterative three-step process rather than a one-shot formula: (1) set up a full probability model — a joint distribution $p(\theta,y)=p(\theta)p(y\mid\theta)$ over all observable and unobservable quantities, consistent with substantive knowledge and the data-collection process; (2) condition on the observed data to obtain and interpret the posterior $p(\theta\mid y)\propto p(\theta)p(y\mid\theta)$; and (3) evaluate model fit and the implications of the posterior — checking how well the model fits, whether conclusions are reasonable, and how sensitive they are to assumptions — then alter or expand the model and repeat. The first step (where do models come from?) is the hardest; advances in step 2 (computation, especially simulation) and step 3 (model checking) reduce the need to get the model right on the first attempt. The central feature distinguishing this paradigm is the direct quantification of uncertainty via probability, which is what permits fitting models with many parameters and complex multilevel specifications.

## Posterior odds and the likelihood ratio
Bayes' rule takes a particularly clean form in odds. The posterior odds for $\theta_1$ versus $\theta_2$ factor as $\frac{p(\theta_1\mid y)}{p(\theta_2\mid y)} = \frac{p(\theta_1)}{p(\theta_2)}\cdot\frac{p(y\mid\theta_1)}{p(y\mid\theta_2)}$ — posterior odds equal prior odds times the likelihood ratio, with the evidence $p(y)$ cancelling. BDA3's hemophilia example makes this concrete: a woman with an affected brother has prior carrier odds $0.5/0.5=1$; two unaffected sons give likelihood ratio $0.25/1=0.25$ (each son of a carrier has a 50% chance of being affected), so posterior odds are $1\times0.25=0.25$, i.e. probability $0.2$. A third unaffected son updates by reusing the prior posterior as the new prior, yielding $0.111$ — illustrating the sequential, order-free nature of Bayesian updating.