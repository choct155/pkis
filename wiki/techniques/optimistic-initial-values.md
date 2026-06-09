---
aliases: []
also_type: []
applies:
- exploration-exploitation-tradeoff
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
extends:
- action-value-methods
id: pkis:technique:optimistic-initial-values
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch02
tags:
- bandits
- exploration
- initialization
- bias
- stationary
title: Optimistic Initial Values
understanding: 0
---

## Definition
$$Q_1(a) \gg q_*(a)\quad\text{for all }a$$

A simple exploration trick: initialize all action-value estimates to a value far higher than any plausible true value, so that early rewards — being lower than expected — "disappoint" the learner into trying other actions even under purely greedy selection.

### How it drives exploration
If each $q_*(a)$ is drawn from a mean-0 unit-variance distribution but $Q_1(a)=+5$, then whatever action is tried first returns a reward below its estimate, so its estimate drops and the greedy learner switches actions. Every action is therefore sampled several times before estimates settle, producing substantial early exploration with no explicit randomization.

### Initialization bias
All the chapter's estimators are biased by $Q_1$. For sample-average methods the bias vanishes once each action has been tried; for constant-$\alpha$ methods it is permanent but decays exponentially. This bias is usually harmless and can encode prior knowledge of expected reward levels.

### Why it matters
Optimistic initialization is a near-free way to bootstrap exploration on *stationary* problems and is widely reused in tabular RL. Its limitation is fundamental: the exploratory drive is *temporary* — it fires only at the start of time. On nonstationary problems, where renewed exploration is needed after the task changes, focusing on initial conditions cannot help, since "the beginning of time occurs only once."

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[action-value-methods]] — extends: tweaks Q_1 initialization to drive early exploration
- [[exploration-exploitation-tradeoff]] — applies: biased initialization induces exploration under greedy selection
[To be populated during integration]