---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
contrasts-with:
- semi-gradient-td
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
id: pkis:result:baird-counterexample
instantiates:
- the-deadly-triad
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch11
tags:
- off-policy
- divergence
- semi-gradient-td
- deadly-triad
- linear-function-approximation
title: Baird's Counterexample
understanding: 0
uses:
- importance-sampling
---

## Definition
A complete episodic seven-state, two-action MDP (Baird, 1995) that definitively demonstrates divergence of off-policy semi-gradient TD(0) under linear function approximation, even in an otherwise favorable setting. The 'dashed' action moves uniformly to one of six upper states; the 'solid' action moves to a seventh state. The behavior policy picks dashed/solid with probability 6/7 and 1/7 (uniform next-state distribution), while the target policy always takes the solid action. All rewards are zero, so the true value function is v(s)=0, exactly representable by w=0; the eight features are linearly independent and there are more weights (8) than nonterminal states (7). Despite this, semi-gradient TD(0) sends the weights to infinity for any positive step size — and so does the synchronous expected (DP-style) update (Eq. 11.9), showing the instability is not a sampling artifact. The mechanism is the same as the w-to-2w fragment: under off-policy training a transition can repeatedly raise an estimate while the compensating downstream transition is skipped (rho=0). Critically, replacing the uniform update distribution with the on-policy distribution restores guaranteed convergence — the cleanest demonstration that the update distribution, not bootstrapping or function approximation alone, drives the divergence. Related counterexamples exist for Q-learning and for Tsitsiklis & Van Roy's best-least-squares-DP case.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[importance-sampling]] — uses: Divergence hinges on rho_t being 1 or 0 across off-policy transitions.
- [[semi-gradient-td]] — contrasts-with: Counterexample showing off-policy semi-gradient TD(0) diverges where it would converge on-policy.
- [[the-deadly-triad]] — instantiates: Baird's MDP is the canonical complete instance demonstrating deadly-triad divergence.
[To be populated during integration]