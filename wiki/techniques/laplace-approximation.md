---
aliases: []
also_type: []
applies:
- marginalization
- marginal-likelihood
- bayesian-inference
- intractable-posterior
component_scores:
  alternatives: 3
  conditions: 2
  diagnostics: 1
  failure_modes: 2
  implementation: 2
  operational_mechanism: 3
  principled_mechanism: 3
contrasts-with:
- variational-inference
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- bayesian-stats
id: pkis:technique:laplace-approximation
knowledge_type: technique
maturity: settled
prerequisite-of:
- bic
- bayesian-logistic-regression
related_concepts:
- '[[probability-theory]]'
- '[[gaussian-distribution]]'
- '[[importance-sampling]]'
- '[[em-algorithm]]'
- '[[bayesian-linear-regression]]'
score_date: '2026-06-07'
sources:
- '[[tanner-tools-statistical-inference]]'
- '[[lange-applied-probability]]'
- lange-applied-probability-ch12
- tanner-tools-statistical-inference-ch02
- tanner-tools-statistical-inference-ch03
tags:
- posterior-approximation
- normal-approximation
- saddle-point
- marginalization
- asymptotic-methods
title: Laplace Approximation
understanding: 1
uses:
- gaussian-distribution
- occam-factor
- hessian-matrix
- maximum-a-posteriori-estimation-map
- energy-function-posterior
- map-reparameterisation-noninvariance
---

A higher-order normal approximation to a posterior distribution or likelihood function obtained by expanding the log-posterior (or log-likelihood) to second order around its mode: the posterior is approximated as N(θ_mode, [−∇²log p(θ|Y)]^{−1}). This is the saddle-point approximation applied to Bayesian computation.

The Laplace approximation enables non-normal corrections to basic normal-based inference (Chapter 2 in Tanner). For posterior moments it yields a more accurate estimate than first-order delta-method approximations. For marginalization, expanding around the conditional mode of the joint integrand enables integration of nuisance parameters without MCMC. Accuracy improves with n. Main limitation: fails when the posterior is multimodal or highly non-ellipsoidal.

## Reading Path
- [[tanner-tools-statistical-inference]] (unread) — primary treatment; Chapter 3 covers Laplace's method for posterior moments and marginalization; motivates MCMC alternatives for non-ellipsoidal posteriors
- [[tanner-tools-statistical-inference-ch03]] (unread) — primary chapter
- [[lange-applied-probability-ch12]] (unread) — Laplace's method and Watson's Lemma for integral approximation

## Connections
- [[map-reparameterisation-noninvariance]] — uses
- [[energy-function-posterior]] — uses
- [[variational-inference]] — contrasts-with
- [[bayesian-logistic-regression]] — prerequisite-of
- [[bic]] — prerequisite-of
- [[maximum-a-posteriori-estimation-map]] — uses
- [[hessian-matrix]] — uses
- [[intractable-posterior]] — applies
- [[bayesian-inference]] — applies
- [[occam-factor]] — uses: The Occam factor is the width term produced when Laplace's method approximates the evidence integral via the posterior Hessian.
- [[marginal-likelihood]] — applies: Approximating the normalizing constant Z_P = integral P*(x) dx is exactly the Bayesian evidence/marginal likelihood; Laplace's det(A) formula yields the standard evidence approximation.
- [[gaussian-distribution]] — uses: The method replaces the peak of P*(x) by a matched Gaussian and uses its normalizing constant sqrt((2pi)^K / det A) as the estimate of Z_P.
- [[marginalization]] — applies: Laplace's method is an approximate technique for performing the otherwise-intractable marginalization integral.

## Approximating a Normalizing Constant (Saddle-Point Form)
MacKay frames Laplace's method primarily as a way to approximate an *integral* — the normalizing constant of an unnormalized density $P^*(x)$:

$$Z_P \equiv \int P^*(x)\,dx.$$

Taylor-expand the log-density about its peak $x_0$:

$$\ln P^*(x) \simeq \ln P^*(x_0) - \tfrac{c}{2}(x-x_0)^2,\qquad c = -\left.\frac{\partial^2}{\partial x^2}\ln P^*(x)\right|_{x_0}.$$

Replacing $P^*$ by the matched unnormalized Gaussian and integrating gives the one-dimensional estimate $Z_Q = P^*(x_0)\sqrt{2\pi/c}$.

In $K$ dimensions, let $\mathbf{A}$ be the Hessian of $-\ln P^*$ at the mode, $A_{ij} = -\partial^2 \ln P^* / \partial x_i\partial x_j|_{x_0}$. Then

$$Z_P \simeq Z_Q = P^*(x_0)\sqrt{\frac{(2\pi)^K}{\det \mathbf{A}}}.$$

The $\det\mathbf{A}$ factor is the engine: it follows from the Gaussian volume integral $\int d^K x\,\exp(-\tfrac12\mathbf{x}^T\mathbf{A}\mathbf{x}) = \sqrt{(2\pi)^K/\det\mathbf{A}}$, provable by an orthogonal transformation to the eigenbasis of $\mathbf{A}$, where the integral separates into one-dimensional factors $\sqrt{2\pi/\lambda_i}$ whose product gives $1/\sqrt{\prod_i\lambda_i} = 1/\sqrt{\det\mathbf{A}}$. Geometrically, $1/\sqrt{\det\mathbf{A}}$ measures the *width* of the posterior peak — a small, sharp peak (large eigenvalues) carries little mass, a broad peak carries much. Physicists call this the saddle-point approximation; it is the same device whether one is normalizing a posterior or evaluating a model's evidence.

## Basis Dependence
A subtle but important defect MacKay highlights: the Laplace approximation is **basis-dependent**. If $x$ is reparameterized by a nonlinear map $u(x)$ — with the density transforming correctly as $P(u) = P(x)\,|dx/du|$ — the approximate normalizing constant $Z_Q$ generally *changes*, even though the true $Z_P$ is basis-independent. The mode of the density and the curvature there are not invariant under nonlinear change of variables, so fitting the Gaussian in a different coordinate system gives a different answer.

This cuts two ways. As a defect, it means the approximation has no canonical value and can mislead if the chosen parameterization happens to be a poor one. As an *opportunity*, it licenses a search for the basis in which the density is most nearly Gaussian — and hence in which Laplace is most accurate. A standard instance: approximating a posterior over a positive rate $\lambda$ versus over $\log\lambda$. The log scale often makes a skewed, hard-bounded posterior far more symmetric and bell-shaped, so the Laplace approximation in $\log\lambda$ typically beats the one taken directly in $\lambda$. The practical lesson is to apply Laplace in a transformed, near-Gaussian coordinate and then map back.

## Application: Gaussian Approximation of a Weight Posterior
For Bayesian neural networks, Laplace's method supplies a deterministic alternative to Monte Carlo. One descends to $w_{MP}$ and Taylor-expands the objective, $M(w)\simeq M(w_{MP})+\tfrac12\Delta w^T A\,\Delta w$, with Hessian $A_{ij}=\partial^2 M/\partial w_i\partial w_j|_{w_{MP}}$; the posterior is then approximated as $\mathcal N(w_{MP},A^{-1})$, so $A^{-1}$ supplies the error bars on the weights.

A neat dimensionality reduction follows for a single neuron: the output depends on $w$ only through the linear activation $a=w\!\cdot\!x$, which is therefore Gaussian, $P(a\mid x,D)=\mathcal N(a_{MP},s^2)$ with $s^2=x^T A^{-1}x$. The marginalized class probability is the convolution of a sigmoid with this Gaussian, well approximated by
$$\psi(a_{MP},s^2)\simeq f\big(\kappa(s)\,a_{MP}\big),\qquad \kappa(s)=\frac{1}{\sqrt{1+\pi s^2/8}}.$$
The factor $\kappa<1$ shrinks the activation toward zero — i.e. moderates the prediction toward 0.5 — in proportion to the posterior uncertainty $s^2$, recovering the same moderation that Monte Carlo marginalization produces.