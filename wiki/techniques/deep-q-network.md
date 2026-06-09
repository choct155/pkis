---
aliases: []
also_type: []
applies:
- markov-decision-processes
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
- deep-learning
- optimization
id: pkis:technique:deep-q-network
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch16
tags: []
title: Deep Q-Network (DQN)
understanding: 0
uses:
- convolutional-neural-networks
- backpropagation
- stochastic-gradient-descent
---

## Definition
[To be filled during deepening]

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[stochastic-gradient-descent]] — uses: DQN trains its network by mini-batch stochastic gradient descent (batches of 32) with the RMSProp adaptive per-weight step-size variant.
- [[backpropagation]] — uses: The semi-gradient Q-learning weight updates in DQN compute the gradient of q-hat by backpropagation through the convolutional network.
- [[convolutional-neural-networks]] — uses: DQN uses a deep convolutional ANN as its function approximator to extract task-relevant features from raw 84x84x4 image stacks, automating the feature-design that earlier RL applications did by hand.
- [[markov-decision-processes]] — applies: DQN solves a control problem formulated as an MDP, approximating the optimal action-value function of the underlying MDP via Q-learning.
[To be populated during integration]