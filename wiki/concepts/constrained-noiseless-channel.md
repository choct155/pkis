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
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:concept:constrained-noiseless-channel
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- constrained-channel-capacity-eigenvalue
related_concepts: []
sources:
- mackay-itila-ch17
tags:
- channel
- coding
- state-machine
- noiseless-channel
- mackay
title: Constrained Noiseless Channel
understanding: 0
uses:
- finite-automata
---

## Definition
A **constrained noiseless channel** transmits symbols without error, but a set of rules forbids certain strings, so not every sequence over the input alphabet is permitted. Channel A forbids the substring `11` (every 1 must be followed by a 0); channel B forbids `101` and `010` (runs must have length $\ge 2$); channel C forbids `111` and `000` (runs have length $\le 2$). The transmitter is naturally modelled as a finite-state machine: a **state diagram** whose directed edges, labelled by emitted symbols, encode which transitions (hence which strings) are legal.

Because the channel is noiseless, capacity is not a mutual-information maximisation but a *counting* problem. Reusing the identity from the noisy-channel theorem, define
$$C=\lim_{N\to\infty}\frac{1}{N}\log_2 M_N,$$
where $M_N$ is the number of distinguishable strings of length $N$ — one name per valid path through the trellis. For channel A, $M_N$ is the Fibonacci series, so $M_N\sim\gamma^N$ and $C=\log_2\gamma\approx 0.694$ bits per channel use.

### Why it matters
Constrained channels model real hardware: a transmitter needing one clock cycle of recovery after a pulse (channel A), or magnetic disk domains that are unstable when isolated (channel B) or hard to time when long (channel C). Computing capacity tells us the best achievable rate, and the same finite-state formalism then yields practical fixed- and variable-length codes.

### Connection to noisy channels
The definition of capacity as $\lim \frac1N\log M_N$ is borrowed directly from the operational meaning of channel capacity: the asymptotic exponential growth rate of the number of reliably distinguishable messages.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[constrained-channel-capacity-eigenvalue]] — prerequisite-of: Defining the channel and its connection matrix precedes computing its capacity spectrally.
- [[finite-automata]] — uses: The transmitter is modelled as a finite-state machine / state diagram defining legal strings.
[To be populated during integration]