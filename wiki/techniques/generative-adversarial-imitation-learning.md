---
aliases: []
also_type: []
applies:
- imitation-learning
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- inverse-reinforcement-learning
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- reinforcement-learning
- imitation-learning
- machine-learning
id: pkis:technique:generative-adversarial-imitation-learning
instantiates:
- generative-adversarial-network-framework
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- imitation-learning
- GAN
- reward-learning
- policy
- occupancy-measure
title: Generative Adversarial Imitation Learning (GAIL)
understanding: 0
uses:
- f-divergence
---

## Definition
GAIL frames imitation learning as a GAN game where the generator is a stochastic policy $\pi_\theta$ and the discriminator $D_\phi$ distinguishes between state-action trajectories from expert demonstrations and those from the learned policy:
$$\min_\theta\max_\phi\;\mathbb{E}_{\tau\sim\pi^*}[\log D_\phi(s,a)]+\mathbb{E}_{\tau\sim\pi_\theta}[\log(1-D_\phi(s,a))]$$
The discriminator output serves as a learned reward signal. Under optimality, GAIL minimises the Jensen-Shannon divergence (or more generally, an f-divergence) between the occupancy measures of the expert and the learner.

### Why it matters
GAIL avoids the compounding errors of behavioural cloning and bypasses the ill-posed reward inference of IRL by directly matching trajectory distributions. It scales to high-dimensional continuous control tasks and connects the GAN framework to the reinforcement learning literature.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[f-divergence]] — uses
- [[inverse-reinforcement-learning]] — contrasts-with: IRL explicitly recovers a reward; GAIL uses a discriminator as an implicit reward.
- [[generative-adversarial-network-framework]] — instantiates
- [[imitation-learning]] — applies
[To be populated during integration]