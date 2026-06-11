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
id: pkis:concept:mcmc-mixing-time
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- mcmc
- markov-chains
related_concepts: []
sources:
- goodfellow-deeplearning-ch17
- murphy-pml2-advanced-ch12
tags:
- mcmc
- mixing-time
- convergence
- burn-in
- markov-chain
title: MCMC Mixing and Mixing Time
understanding: 0
uses:
- stochastic-transition-matrix-mcmc
- burn-in-and-warmup
- energy-barrier-mcmc
- gelman-rubin-diagnostic
- effective-sample-size
- stationary-distribution
---

## Definition
The **mixing time** of a Markov chain is the number of steps $t$ required for the total-variation distance between the chain's current distribution $q^{(t)}$ and its stationary distribution $\pi$ to fall below a tolerance $\epsilon$:
$$t_{\text{mix}}(\epsilon) = \min\left\{t : \sup_{x_0} \|q^{(t)}(\cdot \mid x_0) - \pi(\cdot)\|_{\text{TV}} \leq \epsilon \right\}$$

In practice the mixing time governs how long a chain must run ("burn-in") before samples can be treated as draws from the target distribution.

### Why it matters
Slow mixing — caused by high energy barriers between modes, strong variable correlations, or multimodal targets — is the central practical obstacle to MCMC in deep learning. It determines the computational cost of obtaining approximately independent samples and whether heuristic diagnostics (autocorrelation, manual inspection) signal convergence reliably.

### Connection to eigenvalues
For finite state chains, $t_{\text{mix}}$ scales as $\frac{1}{1 - |\lambda_2|}$ where $|\lambda_2|$ is the second-largest eigenvalue of the transition matrix.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[stationary-distribution]] — uses
- [[markov-chains]] — prerequisite-of
- [[effective-sample-size]] — uses
- [[gelman-rubin-diagnostic]] — uses: Gelman-Rubin and similar diagnostics are heuristics for assessing mixing
- [[energy-barrier-mcmc]] — uses: energy barriers are the primary cause of long mixing times
- [[burn-in-and-warmup]] — uses: burn-in length must exceed mixing time for valid samples
- [[mcmc]] — prerequisite-of: understanding mixing time is essential to diagnosing MCMC convergence
- [[stochastic-transition-matrix-mcmc]] — uses: mixing time controlled by second eigenvalue of transition matrix
[To be populated during integration]