---
title: "Tools for Statistical Inference: Methods for the Exploration of Posterior Distributions and Likelihood Functions"
authors: ["Martin A. Tanner"]
year: 1993
type: book
domain: [bayesian-stats, statistical-learning]
tags: [mcmc, posterior-inference, data-augmentation, likelihood, em-algorithm, gibbs-sampler, metropolis-hastings, importance-sampling, laplace-approximation]
source_url: ""
drive_id: "1NicCZQXwgm3VaJRy-EHSi6csBu0f7_a1"
drive_path: "PKIS/sources/papers/tanner-tools-statistical-inference.pdf"
isbn: "978-1-4684-0194-3"
toc_source: "manual"
status: unread
date_added: 2026-05-20
concepts: ["[[data-augmentation]]", "[[gibbs-sampler]]", "[[metropolis-algorithm]]", "[[importance-sampling]]", "[[laplace-approximation]]", "[[em-algorithm]]", "[[bayesian-linear-regression]]"]
---

## Summary

This textbook provides a unified introduction to computational algorithms for likelihood and Bayesian inference, organized around three functional categories: algorithms that maximize (Newton-Raphson, EM, Monte Carlo EM), algorithms that marginalize (Laplace's method, data augmentation, Gibbs sampler), and algorithms that simulate (importance sampling, rejection-acceptance, data augmentation, Gibbs sampler, Metropolis). A cross-cutting taxonomy distinguishes deterministic (Newton-Raphson, EM) from non-iterative Monte Carlo (importance sampling) from iterative Monte Carlo (MCEM, data augmentation, Gibbs, Metropolis) methods.

Central to the book is the data augmentation principle: by augmenting observed data Y with latent variables Z (missing data, sufficient statistics, or parameters), a single complex sampling or maximization problem is replaced by an iterative series of simpler sub-problems. The EM algorithm exploits this for maximum likelihood; data augmentation exploits it for posterior simulation. The Gibbs sampler is presented as a multi-component extension of data augmentation, iteratively drawing from conditionals p(θ_i | θ_{-i}, Y). The Metropolis algorithm is presented as the non-augmentation Markov chain alternative.

The second edition (1993) adds the Metropolis algorithm and convergence assessment methods for Markov chain algorithms (Gibbs stopper, control variates). The final chapter illustrates the Gibbs sampler in the conditional (frequentist) inference paradigm via saddlepoint approximations, demonstrating applicability beyond Bayesian settings. Worked examples include censored regression (Stanford heart transplant data), rat growth data, Poisson change-point detection, and generalized linear models with random effects.

## Chapters

| Ch | Stub | Title |
|---|---|---|
| 1 | [[tanner-tools-statistical-inference-ch01]] | Introduction |
| 2 | [[tanner-tools-statistical-inference-ch02]] | Normal Approximations to Likelihoods and Posteriors |
| 3 | [[tanner-tools-statistical-inference-ch03]] | Nonnormal Approximations (Laplace, Importance Sampling) |
| 4 | [[tanner-tools-statistical-inference-ch04]] | The EM Algorithm |
| 5 | [[tanner-tools-statistical-inference-ch05]] | The Data Augmentation Algorithm |
| 6 | [[tanner-tools-statistical-inference-ch06]] | Markov Chain Monte Carlo: Gibbs Sampler and Metropolis |

## Key Knowledge Objects

- [[data-augmentation]] (technique, high) — introducing latent variables to simplify posterior sampling; two-component version of Gibbs sampler
- [[gibbs-sampler]] (technique, high) — iterative MCMC via sequential sampling from full conditionals; generalization of data augmentation to multi-component case
- [[metropolis-algorithm]] (technique, high) — MCMC via proposal-acceptance mechanism; works directly on posterior without augmentation
- [[importance-sampling]] (technique, high) — non-iterative Monte Carlo via weighting samples from a proposal distribution
- [[laplace-approximation]] (technique, high) — higher-order normal approximation to posterior or likelihood via saddle-point expansion
- [[em-algorithm]] (technique, high) — existing node; Tanner provides extended treatment including standard errors via missing information principle and Monte Carlo E-step

## Key Extractions

1. **Augmentation taxonomy**: The book's central organizing principle: augmentation algorithms (EM, MCEM, data augmentation, Gibbs) introduce latent data Z such that the complete-data problem p(θ|Y,Z) is simpler than the observed-data problem p(θ|Y). The Metropolis algorithm is explicitly non-augmentation — it works directly on p(θ|Y) modulo the normalizing constant.

2. **Data augmentation as two-component Gibbs**: The data augmentation algorithm iterates between (1) drawing Z from p(Z|θ^{(t)}, Y) — the "imputation step" — and (2) drawing θ from p(θ|Z^{(t+1)}, Y) — the "posterior step." The Gibbs sampler generalizes this to d components, cycling through p(θ_i|θ_{-i}, Y) for each i. The same convergence theory applies.

3. **Standard errors after EM**: Four methods for standard errors in the EM context: (i) direct numerical differentiation of the observed log-likelihood; (ii) missing information principle (observed = complete − missing information); (iii) Louis' method (a closed-form expression involving conditional moments); (iv) simulation-based. The missing information principle is analytically elegant but requires computing the conditional Fisher information.

4. **Sampling/Importance Resampling (SIR)**: A bridge between importance sampling and posterior simulation — draw a large sample from an approximation, then resample with replacement according to importance weights. Produces an approximately iid sample from the target. Computationally cheaper than full MCMC when good approximations are available.

5. **Poor Man's Data Augmentation (PMDA)**: A computationally cheaper variant that replaces the exact posterior step with a normal approximation, producing samples from an approximation to the posterior rather than the exact posterior. Useful when the exact conditional is unavailable but a good approximation can be computed.

## Connection Candidates

- [[em-algorithm]] — extends: Tanner provides the most comprehensive treatment in the wiki of EM standard errors and the Monte Carlo E-step (MCEM)
- [[bayesian-linear-regression]] — uses: the algorithms in this book are the computational tools for Bayesian regression when conjugacy does not apply
- [[directed-graphical-models]] — uses: Gibbs sampler is the primary computational tool for posterior inference in hierarchical Bayesian models specified as DAGs
- [[gaussian-mixture-models]] — uses: the EM algorithm (Chapter 4) and data augmentation (Chapter 5) are the two primary algorithms for GMM fitting
- [[probability-theory]] — prerequisite-of: Tanner assumes working knowledge of conditional distributions and sufficient statistics
