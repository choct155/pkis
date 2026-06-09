---
aliases:
- MCMC
also_type:
- framework
applies:
- ergodic-theorem-markov
component_scores:
  alternatives: 4
  conditions: 2
  diagnostics: 3
  failure_modes: 3
  implementation: 3
  operational_mechanism: 4
  principled_mechanism: 4
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:technique:mcmc
knowledge_type: technique
maturity: settled
related_concepts:
- '[[markov-chains]]'
- '[[gibbs-sampler]]'
- '[[metropolis-algorithm]]'
- '[[probability-theory]]'
- '[[intractable-posterior]]'
score_date: '2026-06-07'
sources:
- '[[lange-applied-probability]]'
- '[[kroese-statistical-modeling]]'
- '[[capretto-bambi-2022]]'
- '[[kurz-hybrid-modeling-2022]]'
specializes:
- numerical-vs-simulation-integration
tags:
- mcmc
- markov-chains
- simulation
- bayesian-computation
- sampling
title: Markov Chain Monte Carlo (MCMC)
understanding: 2
uses:
- posterior-geometry-coordinate-systems
---

A class of algorithms that construct a Markov chain whose stationary distribution is the target distribution (typically a posterior), enabling sampling from intractable distributions by running the chain until convergence; the Metropolis-Hastings and Gibbs sampler are the foundational instances.

Classification note: assigned as technique but also_type framework because MCMC is both a computational procedure and a family of sub-techniques organized by the same principle.

## Connections
- [[ergodic-theorem-markov]] — applies: MCMC relies on ergodic convergence of P^n to the target stationary distribution
- [[numerical-vs-simulation-integration]] — specializes: MCMC is a simulation method that scales integration to high dimensions.
- [[posterior-geometry-coordinate-systems]] — uses: Non-centered parameterization flattens funnel geometry for MCMC/HMC
- [[gibbs-sampler]] — generalizes: Gibbs is MCMC restricted to full conditional distributions; a special case of Hastings-Metropolis
- [[metropolis-algorithm]] — generalizes: the Hastings-Metropolis acceptance rule is the canonical MCMC mechanism
- [[markov-chains]] — uses: MCMC constructs a Markov chain whose stationary distribution is the target posterior
- [[intractable-posterior]] — uses: MCMC is the primary tool for computing intractable posterior integrals

## Reading Path
- [[lange-applied-probability-ch07]] (unread) — Hastings-Metropolis, Gibbs sampling, convergence of independence sampler, simulated annealing
- [[kroese-statistical-modeling-ch07]] (unread) — unified Monte Carlo chapter: MCMC fundamentals, Metropolis-Hastings, and Gibbs sampler alongside bootstrap and KDE
- [[capretto-bambi-2022]] (unread) — Bambi uses PyMC's NUTS (adaptive dynamic HMC) as default sampler; R-hat and ESS diagnostics via ArviZ
- [[kurz-hybrid-modeling-2022]] (unread) — Gibbs sampling used for joint posterior p(ν,d|y) in magnet characterization; blockwise sampling by move

## Operational Mechanism
Markov chain Monte Carlo constructs a Markov chain whose stationary distribution is the target posterior p(θ|x). Because the normalizing constant p(x) cancels in the acceptance ratio, only the unnormalized posterior — the likelihood times the prior — is required.

The Metropolis-Hastings algorithm is the foundational instance:
1. Start at θ_current (arbitrary initialization)
2. Propose θ* ~ q(θ*|θ_current), typically N(θ_current, σ²)
3. Compute acceptance ratio α = p(x|θ*)p(θ*) / p(x|θ_current)p(θ_current)
4. Accept θ* with probability min(1, α); otherwise remain at θ_current
5. Record θ_current; repeat

The p(x) normalizing constant cancels exactly in step 3. This is the hinge the entire algorithm turns on: you never need to compute the intractable integral.

## Principled Mechanism
The acceptance rule enforces detailed balance: for any two points A and B, the probability flux from A to B equals the flux from B to A in the long run.

For point A more probable than B by factor r > 1:
- Chain visits A r times more often than B
- From A, proposes B and accepts with probability 1/r → flux A→B = r × (1/r) = 1
- From B, proposes A and accepts with probability 1 → flux B→A = 1 × 1 = 1
- Equal flux in both directions. Detailed balance holds.

The asymmetry in acceptance probabilities is exactly compensated by the asymmetry in visiting frequencies. The acceptance rule is not a heuristic for finding high-probability regions — it is the precise mathematical condition required to make long-run visiting frequency mirror posterior probability.

Accepting worse proposals with probability α is probability matching, not optimization. The chain must visit low-probability regions in proportion to their actual posterior mass. If only uphill moves were accepted, the chain would converge to the mode and stay there — MAP estimation, not posterior sampling.

## Burn-in and Mixing
Burn-in is the initial period before the chain reaches its stationary distribution. Early samples reflect the arbitrary initialization rather than the posterior and are discarded. Burn-in length depends on how far the initialization is from the high-probability region and how efficiently the chain travels there.

Mixing refers to how efficiently the chain explores the posterior once it has reached the stationary distribution. A well-mixed chain moves freely through all high-probability regions, producing samples that cover the full posterior. A poorly-mixed chain gets stuck, generating highly correlated samples that cover little of the posterior.

Multiple chains initialized at different random positions provide the primary diagnostic: if all chains converge to visiting the same regions with the same frequencies, convergence is likely. If chains visit different regions, they have not mixed.

## Effective Sample Size
Consecutive MCMC samples are correlated — each sample is proposed near the previous one. The effective sample size (ESS) is the number of independent samples that would give equivalent estimation precision:

ESS = N / (1 + 2 · Σ_k ρ_k)

where ρ_k is the autocorrelation at lag k and the sum runs over all lags until autocorrelations become negligible.

The sum includes all lags, not just lag 1. A chain can have low lag-1 autocorrelation and still have persistent long-range correlation from slow drift. First differences capture only lag-1 structure; the full autocorrelation function is required.

Worked example — two chains of N=10 samples:

Chain A (slow drift): θ = {1.2, 1.4, 1.3, 1.6, 1.5, 1.7, 1.6, 1.9, 1.8, 2.0}
ρ_1≈0.92, ρ_2≈0.80, ρ_3≈0.65, ρ_4≈0.50 → ESS ≈ 10/6.74 ≈ 1.5
Nearly all samples redundant.

Chain B (free mixing): θ = {1.2, 1.9, 0.8, 1.7, 1.1, 1.8, 0.9, 1.6, 1.3, 1.7}
All autocorrelations near zero → ESS ≈ 10/1.14 ≈ 8.8
Almost independent samples.

## Diagnostics
Three diagnostics are necessary but not jointly sufficient:

R-hat compares within-chain variance to between-chain variance across multiple chains. Values near 1.0 indicate chains agree. Values above 1.05 indicate non-convergence. Limitation: R-hat measures chain agreement, not posterior coverage. All chains can agree while stuck in the same local region.

ESS measures information content within the explored region. Low ESS relative to N indicates high autocorrelation and slow mixing. Does not detect unexplored modes.

Trace plots provide visual inspection of mixing and drift. A well-mixed chain looks like white noise around a central value. A poorly-mixed chain shows smooth trends or flat stretches punctuated by occasional jumps.

All three can look acceptable while the chain misses entire regions of the posterior. MCMC provides asymptotic guarantees but no finite-sample certificate of adequate exploration.

## Proposal Distribution
The proposal distribution q(θ*|θ_current) is the primary design choice. For a Gaussian proposal N(θ_current, σ²):

σ too small: near-certain acceptance, tiny steps, slow exploration, high autocorrelation. Acceptance rate approaches 100%. Chain diffuses through parameter space in tiny increments.

σ too large: frequent rejection, chain stays put for long stretches, also high autocorrelation. Acceptance rate collapses toward 0%.

Optimal acceptance rate for Gaussian posteriors in d dimensions: approximately 23.4% (Roberts, Gelman, Gilks 1997). This is where ESS per computation is maximized.

Optimal σ scales as d^(-1/2) — smaller steps required as dimensionality increases, producing slower mixing in high-dimensional problems. This is the precise mechanism behind MCMC's degradation in high-dimensional settings.

Informed proposals: the Laplace approximation centered on the MAP estimate with covariance equal to the inverse Hessian provides a proposal shaped to the posterior geometry. Inherits Laplace failure modes (normality assumption, single mode).

## Failure Modes
High autocorrelation: step size too small (high acceptance) or too large (low acceptance). Both produce low ESS. Target 23% acceptance rate.

Multimodal posteriors: chains initialized near one mode may never cross low-probability valleys to discover other modes. R-hat appears good because all chains agree on the same wrong answer.

High-dimensional mixing degradation: optimal step size shrinks as d^(-1/2). Chains mix increasingly slowly as parameter count grows. Mixing failures become harder to detect.

Funnel geometry in hierarchical models: variance parameter controls scale of group-level parameters. Small variance produces tightly constrained group parameters — a narrow funnel neck. Fixed step sizes calibrated for the wide region cause energy conservation failure in the neck, producing divergent transitions in HMC. Silent failure in Metropolis-Hastings.

Relationship to diagnostics: R-hat cannot detect cases where all chains are stuck in the same local region. ESS cannot detect unexplored modes. Divergent transitions (HMC only) can detect funnel geometry. Richer epistemological anchors produce richer diagnostics.

## MacKay's Foundations: Invariance, Ergodicity, and Chain Construction
MacKay grounds MCMC in the evolution of the *distribution* $p^{(t)}(x)$ of the chain's state (imagine an infinite ensemble of parallel simulators), governed by the transition $T$:
$$p^{(t+1)}(x') = \int d^N x\, T(x';x)\,p^{(t)}(x).$$
The goal is to design $T$ so that $p^{(t)}\to P$ for **any** start. Two properties are required.

### 1. Invariance
$P$ must be an invariant distribution of $T$: $P(x')=\int d^N x\, T(x';x)P(x)$ — equivalently, $P$ is an eigenvector of $T$ with eigenvalue 1. Detailed balance is the usual sufficient condition guaranteeing this.

### 2. Ergodicity
$p^{(t)}\to P$ regardless of $p^{(0)}$. This fails if the chain is **reducible** (the state space splits into mutually unreachable subsets — multiple eigenvalue-1 eigenvectors) or **periodic** (e.g. the random walk on the hypercube alternates parity forever, an eigenvalue of $-1$).

### Building valid chains
Complex transitions are assembled from simple base transitions $B_b$ that each leave $P$ invariant, combined by **mixing** ($T=\sum_b p_b B_b$, pick one at random) or **concatenation** ($T = B_2\circ B_1$, apply in sequence). The base transitions need not individually be ergodic; their combination must be.

### Convergence is the open hard part
MacKay emphasizes that while these conditions guarantee convergence *eventually*, predicting *how long* equilibration and inter-sample decorrelation take is largely unsolved — most theoretical upper bounds are useless in practice, and convergence diagnostics are imperfect.

## Exact Sampling and the Convergence Question
A fundamental weakness of all MCMC methods is that they sample from the target $P(x)$ only *asymptotically*: a finite-$T$ run yields draws from some $P^{(T)}(x)$, and deciding when the chain has 'converged' is generally intractable. **Exact (perfect) sampling** methods, pioneered by Propp and Wilson (1996), resolve this for certain chains by certifying internally that equilibrium has been reached. The key mechanism is *coalescence*: coupled chains started from different states but sharing one random-number stream merge and never separate, signalling that the initial condition has been forgotten. Combined with *coupling from the past* (simulate from progressively earlier $T_0$ until all starts coalesce by $t=0$) and *monotonicity* (track only extreme states), this delivers burn-in-free, bias-free samples. See [[coupling-from-the-past]], [[exact-sampling]], and [[monotone-coupling]].