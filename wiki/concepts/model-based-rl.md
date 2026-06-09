---
aliases: []
also_type: []
applies:
- robotics-decision-making
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- expected-vs-sample-updates
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
id: pkis:concept:model-based-rl
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch08
tags:
- reinforcement-learning
- planning
- model-learning
- sample-model
- distribution-model
title: Model-Based Reinforcement Learning
understanding: 0
uses:
- planning-rl
---

## Definition
Reinforcement learning methods that rely on a model of the environment and use planning as their primary component, in contrast to model-free methods that rely on learning from real experience. A model is anything an agent can use to predict how the environment responds to actions, producing a next state and reward for a given state-action pair. Two model types: a distribution model gives all possible next states/rewards with probabilities p(s',r|s,a) (required by dynamic programming for expected updates), while a sample model produces a single sampled transition (sufficient for sample updates and much easier to obtain). Within a planning agent, real experience plays two roles: model-learning (improving the model's fidelity, called system identification in adaptive control) and direct RL (directly improving value/policy). Improving value/policy via the model is indirect RL. Indirect methods make fuller use of limited experience; direct methods are simpler and immune to model bias.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[robotics-decision-making]] — applies: model-based RL reduces real-world sample complexity for robot learning
- [[expected-vs-sample-updates]] — contrasts-with: Distribution models enable expected updates; sample models enable sample updates.
- [[planning-rl]] — uses: Model-based RL relies on planning as its primary component to improve policy from the model.
[To be populated during integration]