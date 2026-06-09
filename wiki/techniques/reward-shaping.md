---
aliases: []
also_type: []
applies:
- markov-decision-processes
- credit-assignment-problem
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
id: pkis:technique:reward-shaping
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch17
- russell-norvig-aima-ch22
tags:
- reward-shaping
- potential-function
- policy-invariance
- mdp
- reward-engineering
title: Reward Shaping (Shaping Theorem)
understanding: 0
uses:
- bellman-equation
- reward-signal
---

## Definition
A way of modifying an MDP's reward function to make learning or planning easier without changing the optimal policy. Beyond the trivial freedom of affine rescaling R'(s,a,s')=mR(s,a,s')+b (m>0), the additive decomposition of utilities permits potential-based shaping: for any state function Φ(s) (a 'potential', by analogy to electrical voltage), the transformed reward R'(s,a,s') = R(s,a,s') + γΦ(s') − Φ(s) leaves the optimal policy unchanged. The proof sets Q'(s,a)=Q(s,a)−Φ(s) and shows it satisfies the Bellman equation of the shaped MDP, so the argmax-extracted policies coincide. The term γΦ(s')−Φ(s) acts like a potential gradient that leads the agent 'uphill' in utility; with Φ set to higher values in higher-utility states it makes the immediate reward more directly reflect desirable behavior. In the limiting case Φ(s)=U(s) (the true utility), the greedy policy with respect to the shaped reward is already optimal — there is 'no free lunch' since this requires knowing U, but partial knowledge still helps. This is the formal counterpart of what animal trainers do by rewarding each step toward a target behavior. Due to Ng, Harada & Russell (1999).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[reward-signal]] — uses
- [[credit-assignment-problem]] — applies
- [[bellman-equation]] — uses: The shaping theorem is proven by substituting Q'(s,a)=Q(s,a)-Phi(s) into the Bellman equation and showing it satisfies the shaped MDP's Bellman equation.
- [[markov-decision-processes]] — applies: Potential-based reward shaping transforms an MDP's reward function while provably preserving the optimal policy.
[To be populated during integration]