---
aliases: []
also_type: []
analogous-to:
- temporal-difference-error
applies:
- temporal-difference-error
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- neuroscience
- optimization
- deep-learning
id: pkis:result:reward-prediction-error-hypothesis
instantiates:
- sutton-reinforcement-2018-ch15
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch15
tags:
- dopamine
- td-error
- reinforcement-learning
- reward-learning
- neuroscience
title: Reward Prediction Error Hypothesis of Dopamine Neuron Activity
understanding: 0
uses:
- temporal-difference-error
---

## Definition
The hypothesis (first explicitly stated by Montague, Dayan & Sejnowski, 1996, building on Schultz's experiments) that one function of the phasic activity of midbrain dopamine neurons (in the SNpc and VTA) is to broadcast a reward prediction error — specifically a temporal-difference (TD) error delta = R_t + gamma*V(S_t) - V(S_{t-1}) — to target structures throughout the brain, rather than signaling reward itself. The phasic dopamine response (1) fires to unpredicted reward, (2) shifts backward to the earliest reliable predictor of reward as learning proceeds, ceasing for later predictors, and (3) drops below baseline when an expected reward is omitted — all hallmarks of a TD error acting as a reinforcement signal. It is a striking, unplanned convergence: TD learning was developed from computational/optimal-control principles years before the neuroscience experiments revealed dopamine's TD-like behavior. The hypothesis is widely accepted and resilient, though discrepancies (e.g. early-reward timing under a complete-serial-compound representation) require refined stimulus representations and eligibility traces. It also reinterprets the classic Olds-Milner view of dopamine as a 'reward signal': phasic dopamine is better understood as a reinforcement signal (delta), the driver of learning, not primary reward R_t.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sutton-reinforcement-2018-ch15]] — instantiates: The hypothesis is the central result developed in Ch. 15 (Neuroscience).
- [[temporal-difference-error]] — applies: Ch. 15 applies the TD-error concept to interpret midbrain dopamine signaling — a neuroscience domain.
- [[temporal-difference-error]] — analogous-to: Same TD-error structure realized in a different mechanism/domain: dopamine neuromodulation in the mammalian brain vs. an algorithmic update in RL.
- [[temporal-difference-error]] — uses: The hypothesis identifies phasic dopamine activity with the RL temporal-difference error delta.
[To be populated during integration]