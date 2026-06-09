---
aliases: []
also_type: []
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
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
extends:
- semi-gradient-td
id: pkis:technique:emphatic-td
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch11
tags:
- off-policy
- emphasis
- interest
- on-policy-distribution
- reweighting
- stable-off-policy
- pseudo-termination
title: Emphatic-TD Methods
understanding: 0
uses:
- importance-sampling
---

## Definition
An off-policy stabilization strategy that, rather than building a true SGD method, reweights semi-gradient TD updates so their distribution is returned to an on-policy distribution — at which point the existing stability guarantees for linear semi-gradient TD (positive-definiteness of the A matrix) again apply. The one-step Emphatic-TD update for episodic state values is w_{t+1} = w_t + alpha M_t rho_t delta_t grad v(S_t, w_t), where the emphasis M_t = gamma rho_{t-1} M_{t-1} + I_t accumulates over time, M_{-1}=0, and the interest I_t is an arbitrary user-specified weighting of how much we care about accurately valuing each state. The method exploits that there are many valid 'on-policy distributions' (any way episodes begin yields a stable distribution as long as all states are updated through termination), and treats discounting as pseudo-termination: a gamma<1 problem is one that terminates and restarts with probability 1-gamma each step. On Baird's counterexample (with I_t=1) the expected-value trajectory converges and the VE goes to zero; however, in practice its variance is so high that consistent empirical convergence is nearly impossible, motivating the variance-reduction discussion. Introduced by Sutton, Mahmood & White (2016).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[importance-sampling]] — uses: Emphasis accumulates IS ratios (M_t = gamma rho_{t-1} M_{t-1} + I_t) to warp the update distribution toward on-policy.
- [[semi-gradient-td]] — extends: Emphatic-TD reweights semi-gradient TD updates (by emphasis M_t) to restore on-policy-like stability.
[To be populated during integration]