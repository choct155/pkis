---
aliases:
- EM
also_type: []
analogous-to:
- latent-variable-models
applies:
- gaussian-mixture-models
- modal-approximation
- missing-data-mechanisms
coverage: 10
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- statistical-learning
- bayesian-stats
id: pkis:technique:em-algorithm
knowledge_type: technique
maturity: settled
related_concepts: []
sources:
- '[[hastie-esl]]'
- '[[deisenroth-mml]]'
- '[[sargent-sims-business-cycle-1977]]'
- '[[blei-vi-review]]'
- '[[ganguly-intro-vi]]'
- '[[sjolund-parametric-vi]]'
- '[[yellapragada-variational-bayes]]'
- '[[tanner-tools-statistical-inference]]'
- '[[kroese-statistical-modeling]]'
- '[[lange-applied-probability]]'
tags:
- optimization
- probability-theory
title: Expectation-Maximization (EM) Algorithm
understanding: 0
uses:
- exponential-family
---

Iterative technique for maximum likelihood estimation in latent variable models, alternating between computing expected sufficient statistics under the current parameter estimates (E-step) and maximizing the complete-data likelihood (M-step).

## Reading Path
- [[hastie-esl]] (unread) — general treatment of EM in the context of mixture models and missing data
- [[deisenroth-mml]] (unread) — EM for Gaussian mixture models; covers E-step as computing responsibilities and M-step as updating cluster parameters
- [[sargent-sims-business-cycle-1977]] (unread) — frequency-domain factor analysis algorithm (Geweke) referenced as the estimation method for the unobservable index model; analogous to EM for factor models in spectral domain
- [[blei-vi-review]] (unread) — Section 4: EM as special case of CAVI under conjugate models; complete-conditional structure connection
- [[ganguly-intro-vi]] (unread) — Section 3–5: EM connection via ELBO derivation; CAVI generalizes EM's E-step to non-conjugate models
- [[sjolund-parametric-vi]] (unread) — parametric VI as generalization of EM to non-conjugate models via reparameterization
- [[yellapragada-variational-bayes]] (unread) — MDL loss formulation connects VI to EM for Bayesian neural networks
- [[tanner-tools-statistical-inference-ch04]] (unread) — most thorough treatment in wiki; five standard-error methods including missing information principle; Monte Carlo E-step (MCEM)
- [[kroese-statistical-modeling-ch06]] (unread) — EM as likelihood maximization for latent variable models; Jensen's inequality convergence proof; mixture model examples
- [[lange-applied-probability-ch16]] (unread) — EM reinterpreted as entropy maximization; information-theoretic perspective

## Soft K-means as a precursor to the E-step
MacKay (ITILA Ch. 20) motivates EM through clustering. The soft K-means **assignment step** computes responsibilities $r_k^{(n)} = \exp(-\beta\, d(\mathbf{m}^{(k)},\mathbf{x}^{(n)})) / \sum_{k'} \exp(-\beta\, d(\mathbf{m}^{(k')},\mathbf{x}^{(n)}))$ — a softmax over squared distances — which is exactly the E-step of EM for an equal-weight, isotropic Gaussian mixture with $\Sigma = \beta^{-1} I$. The **update step** $\mathbf{m}^{(k)} = \sum_n r_k^{(n)}\mathbf{x}^{(n)}/R(k)$ is the corresponding M-step for the means. Thus soft K-means is a constrained instance of EM, and ordinary (hard) K-means is its $\beta \to \infty$ limit, where responsibilities collapse to 0/1 and the E-step becomes a hard nearest-mean assignment. This gives a concrete, geometric reading of EM's alternation: responsibility computation (E) followed by responsibility-weighted parameter re-estimation (M).

## Connections
- [[exponential-family]] — uses: For exponential families (e.g. multivariate normal, multinomial) the expected complete-data log posterior is linear in the expected sufficient statistics, so only those need be imputed in the E-step.
- [[missing-data-mechanisms]] — applies: EM finds the posterior mode in missing-data problems by averaging the complete-data log posterior over y_mis (E-step) and maximizing (M-step); it applies to ignorable and, with an explicit inclusion model, nonignorable mechanisms.
- [[modal-approximation]] — applies: EM finds the marginal posterior mode used to anchor a mode-centered distributional approximation in high dimensions where the joint mode is useless.
- [[latent-variable-models]] — analogous-to
- [[gaussian-mixture-models]] — applies: MacKay derives the EM responsibility-weighted mean update specifically as ML for a Gaussian mixture.

## EM as maximum likelihood for a Gaussian mixture (MacKay derivation)
MacKay derives the EM update for a two-Gaussian mixture from scratch as a maximum-likelihood algorithm, exposing why the E/M alternation works. Given equal-width Gaussians with means $\{\mu_k\}$, the posterior responsibility of point $n$ for component $k$ is the softmax/logistic
$$p_{k\mid n} \equiv P(k_n=k\mid x_n,\theta),$$
which for two components reduces to a sigmoid $1/(1+e^{-(w_1 x_n + w_0)})$. The log-likelihood gradient is
$$\frac{\partial L}{\partial\mu_k} = \sum_n p_{k\mid n}\,\frac{x_n-\mu_k}{\sigma^2},$$
and, neglecting the dependence of $p_{k\mid n}$ on $\mu_k$, the second derivative is $-\sum_n p_{k\mid n}/\sigma^2$. An approximate Newton–Raphson step then gives the **responsibility-weighted mean update**
$$\mu_k' = \frac{\sum_n p_{k\mid n}\,x_n}{\sum_n p_{k\mid n}}.$$
This is exactly the E-step (compute $p_{k\mid n}$) / M-step (re-estimate $\mu_k$) of EM, revealed here as an approximate Newton step on the likelihood. The same derivation shows clustering *is* mixture-density modelling.