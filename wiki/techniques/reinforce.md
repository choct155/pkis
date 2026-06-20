---
aliases: []
also_type: []
analogous-to:
- reparameterization-trick
applies:
- stochastic-gradient-descent
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-20'
domain:
- reinforcement-learning
- optimization
id: pkis:technique:reinforce
instantiates:
- policy-gradient-methods
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-policy-2018
- mohamed-monte-2020
tags:
- policy-gradient
- monte-carlo
- score-function
- log-derivative-trick
- eligibility-vector
title: REINFORCE
understanding: 0
uses:
- monte-carlo-estimator
---

## Definition
The classical Monte Carlo policy-gradient algorithm (Williams, 1992). At each step it updates the policy parameter using the actual return $G_t$ and only the single action $A_t$ taken:
$$\theta_{t+1}\doteq\theta_t+\alpha\,G_t\,\frac{\nabla\pi(A_t\mid S_t,\theta_t)}{\pi(A_t\mid S_t,\theta_t)} \;=\; \theta_t+\alpha\,G_t\,\nabla\ln\pi(A_t\mid S_t,\theta_t),$$
using the identity $\nabla\ln x=\nabla x/x$. The vector $\nabla\ln\pi(A_t\mid S_t,\theta_t)$ is called the eligibility vector (a.k.a. the score function); it is the only place the policy parameterization enters the algorithm.

## Derivation
Starting from the policy gradient theorem, the sum over actions $\sum_a q_\pi(S_t,a)\nabla\pi(a\mid S_t,\theta)$ is converted to an expectation under $\pi$ by multiplying and dividing by $\pi(a\mid S_t,\theta)$, then replacing the action sum by the sampled action $A_t\sim\pi$. Because $\mathbb{E}_\pi[G_t\mid S_t,A_t]=q_\pi(S_t,A_t)$, the sampled quantity $G_t\,\nabla\pi(A_t\mid S_t,\theta)/\pi(A_t\mid S_t,\theta)$ has expectation proportional to $\nabla J$. This is the log-derivative / score-function trick.

## Interpretation
Each update moves $\theta$ in the direction that most increases the probability of repeating $A_t$ in $S_t$, scaled by the return (favor high-return actions) and inversely by the action's probability (so frequently chosen actions are not unfairly advantaged).

## Properties & Limitations
Because it uses the complete return through episode end, REINFORCE is a Monte Carlo method, well defined only for the episodic case with updates made retrospectively after each episode. The expected update is in the true gradient direction, giving good convergence (to a local optimum under standard stochastic-approximation conditions for decreasing $\alpha$), but as a Monte Carlo method it suffers high variance and slow learning. The boxed algorithm includes a $\gamma^t$ factor for the general discounted case (Thomas, 2014).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[reparameterization-trick]] — analogous-to: REINFORCE's log-derivative (score-function) estimator and the reparameterization trick are the two canonical Monte Carlo gradient estimators for expectations over a parameterized distribution; same goal, different mechanism (Mohamed et al. 2020).
- [[stochastic-gradient-descent]] — applies: REINFORCE instantiates generic stochastic gradient ascent (13.1) with a score-function sample whose expectation is proportional to the gradient.
- [[monte-carlo-estimator]] — uses: REINFORCE uses the complete sampled return G_t as a Monte Carlo estimate of q_pi, making it a Monte Carlo gradient method well defined only episodically.
- [[policy-gradient-methods]] — instantiates: REINFORCE is the canonical Monte Carlo instance of the policy-gradient framework.
[To be populated during integration]