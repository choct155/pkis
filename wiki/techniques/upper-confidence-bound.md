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
contrasts-with:
- epsilon-greedy
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
extends:
- action-value-methods
id: pkis:technique:upper-confidence-bound
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch02
tags:
- bandits
- exploration
- action-selection
- confidence-bound
- optimism
title: Upper Confidence Bound (UCB) Action Selection
understanding: 0
uses:
- confidence-interval
---

## Definition
$$A_t \doteq \arg\max_a\left[Q_t(a) + c\sqrt{\frac{\ln t}{N_t(a)}}\right]$$

A *directed* exploration rule that selects the action whose value estimate plus an uncertainty bonus is largest, preferring actions that are either promising or under-sampled — "optimism in the face of uncertainty."

### Mechanism
The term $c\sqrt{\ln t / N_t(a)}$ measures uncertainty in $Q_t(a)$: $N_t(a)$ is the number of times $a$ has been chosen, and $c>0$ tunes exploration. Selecting $a$ increments $N_t(a)$, shrinking its bonus; selecting other actions increases $t$, slowly inflating $a$'s bonus. The $\ln t$ growth makes bonus increases ever smaller yet unbounded, so all actions are tried eventually but rarely-promising, oft-chosen actions are visited with decreasing frequency. Untried actions ($N_t(a)=0$) are treated as maximizing.

### Why it matters
Unlike $\varepsilon$-greedy's blind random exploration, UCB explores *purposefully*, allocating samples toward actions with the greatest potential to be optimal given their uncertainty. On the 10-armed testbed it generally outperforms $\varepsilon$-greedy (a parameter study found it best overall), modulo an initial sweep through untried arms.

### Limitations
UCB is hard to extend beyond bandits: it copes poorly with nonstationarity and with large state spaces under function approximation, so in advanced RL settings it is usually impractical despite its strong bandit performance. The algorithm shown is UCB1 (Auer, Cesa-Bianchi, and Fischer, 2002).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[confidence-interval]] — uses: selects the upper confidence bound on each action's value
- [[epsilon-greedy]] — contrasts-with: directed optimism-under-uncertainty vs. undirected random exploration
- [[action-value-methods]] — extends: adds an uncertainty bonus to value estimates for directed exploration
[To be populated during integration]