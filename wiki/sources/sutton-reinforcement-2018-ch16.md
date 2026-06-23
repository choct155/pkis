---
abbrev: "RL"
applies:
- markov-decision-processes
- random-forests
- convolutional-neural-networks
authors: Richard S. Sutton, Andrew G. Barto
coverage: 0
domain:
- optimization
- deep-learning
extends:
- sutton-reinforcement-2018-ch02
- sutton-reinforcement-2018-ch08
id: pkis:source:sutton-reinforcement-2018-ch16
instantiates:
- deep-q-network
maturity: stub
parent_book: pkis:source:sutton-reinforcement-2018
status: unread
tags:
- sutton-reinforcement-2018
title: "[RL Sutton & Barto] Ch. 16 — Applications and Case Studies"
type: chapter
understanding: 0
year: 2018
---

## Summary
[Chapter stub — Reinforcement Learning: An Introduction (2nd ed.) Ch. 16: Applications and Case Studies.]

## Reading Path
- Parent: [[sutton-reinforcement-2018]]

## Connections
- [[sutton-reinforcement-2018-ch08]] — extends: AlphaGo and AlphaGo Zero build on the Monte Carlo tree search (MCTS) decision-time planning procedure introduced in Chapter 8, augmenting it with learned deep policy and value networks.
- [[sutton-reinforcement-2018-ch02]] — extends: The web-personalization case study formulates recommendation as a contextual (associative) bandit problem, the associative extension of the multi-armed bandit setting of Chapter 2, before arguing the MDP formulation captures long-term user value.
- [[convolutional-neural-networks]] — applies: DQN, AlphaGo, and AlphaGo Zero all rely on deep convolutional ANNs as the value/policy function approximator over spatial board or image input.
- [[random-forests]] — applies: Theocharous et al.'s ad-recommendation case study uses random forests as the regression backbone for both greedy CTR optimization and batch-mode Fitted Q Iteration (LTV optimization).
- [[markov-decision-processes]] — applies: Most case studies (DRAM controller, web recommendation, thermal soaring) are formulated as MDPs; the chapter illustrates the art of casting real applications, including state-dependent action sets A(s), as MDPs.
- [[deep-q-network]] — instantiates: Chapter 16 presents the DeepMind Atari DQN result (Mnih et al. 2015) as a central case study.