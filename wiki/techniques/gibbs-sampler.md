---
aliases: []
also_type: []
applies:
- ising-model
- exact-sampling
component_scores:
  alternatives: 4
  conditions: 2
  diagnostics: 2
  failure_modes: 3
  implementation: 3
  operational_mechanism: 4
  principled_mechanism: 3
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:technique:gibbs-sampler
knowledge_type: technique
maturity: settled
related_concepts:
- '[[data-augmentation]]'
- '[[metropolis-algorithm]]'
- '[[directed-graphical-models]]'
- '[[conjugate-prior]]'
- '[[probability-theory]]'
score_date: '2026-06-07'
sources:
- '[[tanner-tools-statistical-inference]]'
- '[[kroese-statistical-modeling]]'
- '[[lange-applied-probability]]'
- '[[kurz-hybrid-modeling-2022]]'
specializes:
- metropolis-algorithm
tags:
- mcmc
- posterior-sampling
- markov-chains
- conditional-distributions
- bayesian-computation
title: Gibbs Sampler
understanding: 2
---

An iterative MCMC algorithm for sampling from a multivariate posterior p(θ_1, ..., θ_d | Y) by cycling through the full conditional distributions: at step t+1, draw θ_i^{(t+1)} from p(θ_i | θ_{-i}^{(t)}, Y) for each i in sequence. Under regularity conditions, the generated chain is ergodic with the joint posterior as its stationary distribution.

The Gibbs sampler is the multi-component generalization of data augmentation (two components). Its key advantage is that full conditionals are often available in closed form (especially with conjugate priors in hierarchical models) even when the joint posterior is intractable. The Griddy Gibbs sampler handles non-standard conditionals by numerical integration on an adaptive grid. Convergence can be assessed via the Gibbs stopper (monitoring changes in the predictive distribution) or control variates.

## Reading Path
- [[tanner-tools-statistical-inference]] (unread) — primary treatment; Chapter 6 covers theory, examples (rat growth, Poisson change-point, GLMs with random effects), convergence diagnostics, Griddy Gibbs, and application to conditional frequentist inference
- [[tanner-tools-statistical-inference-ch06]] (unread) — primary chapter
- [[kroese-statistical-modeling-ch07]] (unread) — integrated treatment within Monte Carlo chapter; presents Gibbs as special case of Metropolis-Hastings
- [[lange-applied-probability-ch07]] (unread) — Gibbs sampling treated as special case of Hastings-Metropolis; convergence analysis
- [[kurz-hybrid-modeling-2022]] (unread) — Gibbs sampling from joint posterior p(ν,d|y) for CERN magnet field reconstruction; blockwise sampling alternating between BEM state vector and mechanical perturbation vectors

## Operational Mechanism
Gibbs sampling updates one parameter at a time by drawing exactly from its full conditional distribution — the distribution of that parameter given the current values of all others and the data. For a model with parameters θ_1, ..., θ_d, one iteration cycles through:

  Draw θ_1^(t+1) ~ p(θ_1 | θ_2^(t), ..., θ_d^(t), y)
  Draw θ_2^(t+1) ~ p(θ_2 | θ_1^(t+1), θ_3^(t), ..., θ_d^(t), y)
  ...
  Draw θ_d^(t+1) ~ p(θ_d | θ_1^(t+1), ..., θ_{d-1}^(t+1), y)

Every draw is accepted — no rejection step required when full conditionals are exact.

Worked example — Normal-Gamma model:
Observations y={2.1, 2.4, 1.9, 2.3, 2.0}, ȳ=2.14, n=5
Priors: μ₀=0, κ₀=1, α₀=1, β₀=1 (weakly informative)
Initialize: μ^(0)=0, τ^(0)=1

Full conditional for μ given τ (conjugate Gaussian):
  κₙ = κ₀ + n = 6
  μₙ = (κ₀μ₀ + nȳ) / κₙ = (0 + 5×2.14)/6 = 1.783
  Draw μ^(t+1) ~ N(1.783, 1/(6τ^(t)))

Full conditional for τ given μ (conjugate Gamma):
  αₙ = α₀ + n/2 = 3.5
  βₙ = β₀ + (1/2)Σᵢ(yᵢ - μ^(t+1))²
  Draw τ^(t+1) ~ Gamma(αₙ, βₙ)

Iteration 1 with μ^(0)=0, τ^(0)=1:
  μₙ = 1.783 → draw μ^(1) ≈ 1.71
  βₙ = 1 + (1/2)[0.152+0.476+0.036+0.348+0.084] = 1.548
  Draw τ^(1) ~ Gamma(3.5, 1.548) ≈ 2.31

The parameters chase each other — μ's conditional depends on τ and vice versa. Neither converges independently; they converge together as the chain explores the joint posterior.

## Why Analytic Closure is Load-Bearing
Gibbs requires exact draws from full conditional distributions. Unlike CAVI, which has the ELBO as an external objective that corrects for approximate gradient steps, Gibbs has no correction mechanism. The correctness of the stationary distribution is entirely load-bearing on each draw being exact.

If conditionals are approximated — say a Gaussian approximation to a skewed conditional — the chain's stationary distribution is the stationary distribution of the approximate chain, not the true joint posterior. The error does not average out. It accumulates into systematic bias that is silent and undetectable from standard diagnostics.

The CAVI contrast makes this precise: the ELBO is a third-party reference that keeps optimization on track even when gradient steps are approximate. Gibbs has no such reference. The only guardrail is the exactness of each conditional draw. Remove that and there is nothing to correct the drift.

This is why Metropolis-within-Gibbs exists: for parameters whose conditionals are not tractable, a Metropolis step is inserted. The acceptance ratio re-introduces a correction mechanism — the likelihood ratio — that tolerates approximate proposals by enforcing detailed balance at each step.

## Relationship to CAVI
Gibbs and CAVI share identical coordinate-wise structure: update one variable at a time, conditioning on the current values of all others, cycling until convergence.

The difference is what each coordinate update does:
- CAVI: moves the variational factor q_j(z_j) to its optimal value under the current other factors — an optimization step targeting the ELBO
- Gibbs: draws a sample from the exact conditional p(θ_j | θ_{-j}, y) — a sampling step

CAVI finds the best factorized approximation to the posterior.
Gibbs constructs samples from the true joint posterior.

CAVI tolerates approximation because the ELBO provides correction.
Gibbs does not tolerate approximation because there is no correction mechanism.

Both degrade when variables are highly correlated — updating one coordinate at a time while holding others fixed produces small effective moves along the ridge of correlation. HMC addresses this by using gradient information to construct proposals that move along the posterior surface rather than across it.

## Connections
- [[exact-sampling]] — applies: Coupled Gibbs sampling is the chain Propp-Wilson use to draw exact Ising samples.
- [[ising-model]] — applies: Gibbs sampling draws each spin from its conditional given neighbours to sample the Ising equilibrium distribution.
- [[metropolis-algorithm]] — specializes: A Gibbs coordinate-update is a Metropolis method whose proposal is always accepted.

## MacKay's View: Gibbs as Parameter-Free Metropolis
MacKay (also calling it the heat-bath method or Glauber dynamics) presents Gibbs sampling as a method for joint distributions over $\ge 2$ variables that works when $P(x)$ is too complex to sample directly but its **full conditionals** $P(x_i\mid\{x_j\}_{j\neq i})$ are tractable. One sweep updates each coordinate in turn:
$$x_i^{(t+1)}\sim P\bigl(x_i \mid x_1^{(t+1)},\dots,x_{i-1}^{(t+1)},x_{i+1}^{(t)},\dots,x_K^{(t)}\bigr).$$

### Gibbs is a special Metropolis method
A single Gibbs coordinate-update is exactly a Metropolis proposal whose **acceptance probability is always 1**: sampling from the conditional is equivalent to proposing from it and never rejecting. Hence Gibbs inherits MCMC convergence ($p^{(t)}\to P$) without any adjustable step-size parameters — its great practical attraction (and the basis of the BUGS software).

### Limitations MacKay stresses
- **Random-walk slowness.** When two variables are strongly correlated (marginal width $L$, conditional width $\epsilon$), axis-aligned Gibbs still needs $\sim(L/\epsilon)^2$ iterations per independent sample — the same penalty as Metropolis.
- **Pathological targets.** For syndrome decoding of an error-correcting code, valid codewords are isolated points with no adjacent valid neighbours, so any single-bit conditional move lands on zero probability and the chain freezes — Gibbs is useless there.
- **Blocking.** Sampling groups of variables jointly (block Gibbs) can mitigate the correlation penalty in big models.

## Application: Gibbs sampling an Ising model
A standard application of Gibbs sampling is simulating an Ising model at equilibrium. Pick a spin $n$ at random; conditioned on its neighbours through the local field $b_n = \sum_{m:(m,n)\in\mathcal{N}} J x_m + H$, set it to $+1$ with probability

$$P(+1 \mid b_n) = \frac{1}{1 + \exp(-2\beta b_n)},$$

otherwise $-1$, then repeat. (The factor of $2$ appears because the states are $\{+1,-1\}$ rather than $\{+1,0\}$.) After enough sweeps this converges to the Boltzmann distribution. A practical subtlety is *equilibration*: it is hard to define or detect when the chain has reached equilibrium. MacKay's crude recipe runs a few hundred sweeps per spin and discards the first third; for $N=100$ spins this needed over $100{,}000$ iterations per temperature. Running the temperature down then back up exposes hysteresis when equilibrium has not been reached.

## Coupled Gibbs Sampling for Exact Samples
Gibbs sampling can be embedded in an exact-sampling scheme. For a ferromagnetic Ising model, couple all chains by having them update the same spin $i$ at each step using a shared uniform draw $u$: compute $a_i = \sum_j J_{ij} x_j$ and set $x_i = +1$ iff $u < 1/(1 + e^{-2a_i})$, else $x_i = -1$. Under the spin-wise partial order ($x \succeq y$ iff $x_i \ge y_i$ for all $i$), this coupled update is **monotone**, so tracking only the all-up and all-down chains certifies coalescence of all $2^N$ histories. Running this with [[coupling-from-the-past]] yields an exact draw from the Ising equilibrium (Propp-Wilson's famous 16-million-spin critical sample). Convergence is fast above the critical temperature but slow below it, where Gibbs itself mixes slowly. See [[monotone-coupling]] and [[exact-sampling]].