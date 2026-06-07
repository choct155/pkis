---
date_created: '2026-06-07'
id: pkis:bridge-note:bn-20260607-every-inference-algorithm-targeting-a
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- mcmc
- gibbs-sampler
- coordinate-ascent-vi
- hmc
- variational-inference
origin: conversation
proposed_edge_type: ''
rationale: 'Every inference algorithm targeting a posterior needs a mechanism that
  prevents drift away from the correct distribution. The nature of that mechanism
  — the epistemological anchor — determines what failure modes are visible, what approximations
  are tolerable, what diagnostic information is available, and how much geometric
  information about the posterior is used.


  ## Metropolis-Hastings: The Likelihood Ratio

  Anchor: ratio of posterior probabilities at two points. The acceptance rule enforces
  detailed balance at every proposal, correcting for the uninformed proposal distribution.
  Tolerates approximate proposals because the ratio corrects them. Failure mode (getting
  stuck in local regions) is detectable only through multiple chains and trace plots.
  Uses information at two points only.


  ## Gibbs Sampling: Analytic Closure

  Anchor: exact full conditional distribution. No correction mechanism — correctness
  is entirely load-bearing on each draw being exact. Zero tolerance for approximation
  in the conditionals. Failure mode (biased stationary distribution from approximate
  conditionals) is silent. Provides a perfect map but requires that map to be exact.
  Metropolis-within-Gibbs reintroduces a correction mechanism for intractable conditionals.


  ## Coordinate Ascent VI (CAVI): The ELBO

  Anchor: Evidence Lower Bound as optimization objective. Every coordinate update
  evaluated against it. Approximate gradient steps still make progress because the
  objective corrects drift. Convergence is measurable. Failure mode (converging to
  best point on wrong submanifold) is detectable by comparing ELBOs across variational
  families. Tolerates approximation but restricts the search space before optimization
  begins.


  ## Hamiltonian Monte Carlo: Gradient + Hamiltonian Conservation

  Anchor: gradient of log posterior at every leapfrog step + Metropolis acceptance
  using the Hamiltonian. Richer than MH because it uses gradient information along
  an entire trajectory rather than the likelihood ratio at a single point. Failure
  mode (divergent transitions in high-curvature regions) is detectable precisely because
  the gradient changes dramatically in those regions. Richer anchor → richer diagnostics.


  ## The General Principle

  The epistemological anchor determines: (1) what failure modes are visible vs silent;
  (2) what approximations are tolerable vs fatal; (3) what diagnostic information
  is available; (4) how much geometric information about the posterior is used. Methods
  with richer anchors (HMC > MH > Gibbs) produce richer diagnostics and are more robust
  to difficult posterior geometry. Methods with tractable anchors (CAVI > MCMC) produce
  measurable convergence criteria and scale better. Choosing an inference method is
  partly choosing which anchor''s properties best match the problem''s requirements.'
source_context: ''
status: unreviewed
title: 'Epistemological Anchors: What Keeps Each Inference Algorithm on Track'
---

## Connection
Every inference algorithm targeting a posterior needs a mechanism that prevents drift away from the correct distribution. The nature of that mechanism — the epistemological anchor — determines what failure modes are visible, what approximations are tolerable, what diagnostic information is available, and how much geometric information about the posterior is used.

## Metropolis-Hastings: The Likelihood Ratio
Anchor: ratio of posterior probabilities at two points. The acceptance rule enforces detailed balance at every proposal, correcting for the uninformed proposal distribution. Tolerates approximate proposals because the ratio corrects them. Failure mode (getting stuck in local regions) is detectable only through multiple chains and trace plots. Uses information at two points only.

## Gibbs Sampling: Analytic Closure
Anchor: exact full conditional distribution. No correction mechanism — correctness is entirely load-bearing on each draw being exact. Zero tolerance for approximation in the conditionals. Failure mode (biased stationary distribution from approximate conditionals) is silent. Provides a perfect map but requires that map to be exact. Metropolis-within-Gibbs reintroduces a correction mechanism for intractable conditionals.

## Coordinate Ascent VI (CAVI): The ELBO
Anchor: Evidence Lower Bound as optimization objective. Every coordinate update evaluated against it. Approximate gradient steps still make progress because the objective corrects drift. Convergence is measurable. Failure mode (converging to best point on wrong submanifold) is detectable by comparing ELBOs across variational families. Tolerates approximation but restricts the search space before optimization begins.

## Hamiltonian Monte Carlo: Gradient + Hamiltonian Conservation
Anchor: gradient of log posterior at every leapfrog step + Metropolis acceptance using the Hamiltonian. Richer than MH because it uses gradient information along an entire trajectory rather than the likelihood ratio at a single point. Failure mode (divergent transitions in high-curvature regions) is detectable precisely because the gradient changes dramatically in those regions. Richer anchor → richer diagnostics.

## The General Principle
The epistemological anchor determines: (1) what failure modes are visible vs silent; (2) what approximations are tolerable vs fatal; (3) what diagnostic information is available; (4) how much geometric information about the posterior is used. Methods with richer anchors (HMC > MH > Gibbs) produce richer diagnostics and are more robust to difficult posterior geometry. Methods with tractable anchors (CAVI > MCMC) produce measurable convergence criteria and scale better. Choosing an inference method is partly choosing which anchor's properties best match the problem's requirements.

## Nodes Involved
- [[mcmc]]
- [[gibbs-sampler]]
- [[coordinate-ascent-vi]]
- [[hmc]]
- [[variational-inference]]

## Integration Notes
Pending review.