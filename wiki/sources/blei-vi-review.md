---
id: "pkis:source:blei-vi-review"
aliases: ["Blei VI review", "Variational Inference Review"]
title: "Variational Inference: A Review for Statisticians"
knowledge_type: source
source_type: paper
authors: ["David M. Blei", "Alp Kucukelbir", "Jon D. McAuliffe"]
year: 2017
domain: [bayesian-stats, optimization]
tags: [variational-methods, probability-theory, approximate-inference, exponential-family, stochastic-optimization]
source_url: "https://arxiv.org/abs/1601.00670"
drive_id: "1Fc6LEhsb6rzT95TBaluBMM8wrBbjC7J-"
drive_path: "PKIS/sources/papers/blei-vi-review.pdf"
status: unread
date_added: 2026-05-20
date_updated: 2026-05-20
concepts: ["[[variational-inference]]", "[[elbo]]", "[[mean-field-approximation]]", "[[stochastic-vi]]", "[[coordinate-ascent-vi]]"]
---

Authoritative review of variational inference aimed at statisticians, written with the explicit goal of catalyzing statistical theory research on VI. The paper presents VI as approximating an intractable posterior p(z|x) by finding the member q*(z) of a tractable family Q that minimizes KL(q(z)‖p(z|x)). The ELBO is derived as the tractable surrogate objective. The mean-field family (fully factorized q) is the primary approximating family studied, and Coordinate Ascent Variational Inference (CAVI) is derived as the main optimization algorithm. A complete Bayesian Gaussian mixture example demonstrates the full CAVI algorithm from ELBO derivation through convergence. The paper then develops the exponential family special case: when complete conditionals are in the exponential family, CAVI updates reduce to natural parameter updates. Stochastic Variational Inference (SVI, Hoffman et al. 2013) is derived as the natural-gradient stochastic descent extension, enabling VI to scale to massive datasets by subsampling. The discussion surveys applications across computational biology, neuroscience, NLP, and computer vision; reviews the sparse theoretical results (consistency, asymptotic normality for specific models); and catalogs open problems including alternative divergences, richer variational families, VI-MCMC hybrids, and general statistical theory.

## Key Knowledge Objects

- [[variational-inference]] (technique, high) — the central subject; full algorithmic and theoretical treatment
- [[elbo]] (concept, high) — Evidence Lower Bound: ELBO = E_q[log p(z,x)] − E_q[log q(z)]; exactly equals log p(x) − KL(q‖p(z|x))
- [[mean-field-approximation]] (technique, high) — assumes fully factorized variational family q(z) = ∏_j q_j(z_j); enables tractable CAVI coordinate updates
- [[coordinate-ascent-vi]] (technique, high) — iteratively optimizes each variational factor q_j holding others fixed; each update is the unnormalized geometric mean of the complete conditional
- [[stochastic-vi]] (technique, high) — applies natural gradient descent with noisy subsampled gradients to scale CAVI to massive data; no new derivation needed beyond CAVI

## Key Extractions

1. **ELBO as core objective**: KL(q(z)‖p(z|x)) = log p(x) − ELBO(q). Since KL ≥ 0, ELBO ≤ log p(x). Maximizing ELBO simultaneously maximizes a lower bound on evidence and minimizes KL to posterior. KL cannot be computed directly because it requires the posterior; the ELBO avoids this by using the joint p(z,x).
2. **Mean-field CAVI update rule**: For each factor q_j(z_j) in the mean-field family, the optimal update is q*_j(z_j) ∝ exp(E_{-j}[log p(z,x)]), where the expectation is over all other factors. This is the unnormalized geometric mean of the complete conditional.
3. **Exponential family simplification**: When complete conditionals are in the exponential family — p(z_j|z_{-j},x) = h(z_j)exp(η(z_{-j},x)ᵀt(z_j) − a(η)) — the CAVI update reduces to setting the variational natural parameter equal to the expected natural parameter: φ_j = E_{-j}[η(z_{-j},x)].
4. **Stochastic Variational Inference (SVI)**: The natural gradient of the ELBO with respect to global variational parameters λ is g(λ) = (α + Σ_i E[t(z_i,x_i)]) − λ. SVI approximates this by sampling one datapoint and rescaling: ĝ(λ) = α + n·E_ϕ*_t[t(z_t,x_t)] − λ. Step-size requirements: Σε_t = ∞, Σε²_t < ∞.
5. **Mean-field variance underestimation**: Mean-field independence assumptions lead to systematic underestimation of posterior variance. This is a known limitation documented in the open problems section; structured and hierarchical variational families are proposed remedies.

## Connection Candidates

- [[em-algorithm]] — extends: VI generalizes EM; EM's E-step computes the exact posterior (when tractable), while VI optimizes an approximate one; CAVI and EM have the same coordinate-ascent structure
- [[gaussian-mixture-models]] — uses: the complete GMM example (Section 3) works out every CAVI update in detail; this is the canonical VI illustration
- [[gradient-descent]] — uses: SVI uses stochastic natural gradient descent; standard CAVI is coordinate ascent (not gradient-based)
- [[probability-theory]] — prerequisite-of: understanding exponential family, sufficient statistics, and KL divergence is required to follow Section 4
- [[directed-graphical-models]] — uses: conditional conjugacy and factorization of p(z,x) are expressed via directed graphical model structure (Section 4.2)
