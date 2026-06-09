---
aliases: []
also_type: []
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
- monte-carlo-estimator
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
generalizes:
- temporal-difference-learning
id: pkis:concept:n-step-bootstrapping
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch07
tags:
- reinforcement-learning
- bootstrapping
- value-estimation
title: n-step Bootstrapping
understanding: 0
---

## Definition
n-step bootstrapping is the family of temporal-difference methods that update an estimate using the next n observed rewards plus the estimated value of the state (or state-action pair) reached n steps later, rather than just the single next reward (one-step TD) or the entire return until termination (Monte Carlo). These methods form a continuous spectrum: n=1 recovers one-step TD, and n equal to the time to termination recovers Monte Carlo, with intermediate values of n typically outperforming either extreme. The conceptual motivation is to escape the 'tyranny of the time step': in one-step TD the same interval governs both how fast actions can change and the interval over which bootstrapping occurs, whereas n-step methods decouple these, letting bootstrapping span a length of time over which a significant, recognizable state change has occurred. n-step methods are also the conceptual stepping stone to eligibility traces (Chapter 12), which achieve bootstrapping over many intervals simultaneously with bounded memory and computation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[monte-carlo-estimator]] — contrasts-with: MC sits at the far (n=infinity) end of the n-step spectrum; n-step methods bootstrap whereas pure MC does not
- [[temporal-difference-learning]] — generalizes: n-step methods generalize one-step TD; n=1 recovers it
[To be populated during integration]