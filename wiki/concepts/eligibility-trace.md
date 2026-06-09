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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
- neuroscience
id: pkis:concept:eligibility-trace
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch15
tags:
- reinforcement-learning
- credit-assignment
- synaptic-plasticity
- stdp
- temporal-credit
title: Eligibility Trace
understanding: 0
uses:
- sutton-reinforcement-2018-ch12
---

## Definition
An eligibility trace is a short-term, decaying memory at each parameter (or synapse) recording recent activity, marking that parameter as eligible for modification by a subsequently-arriving reinforcement signal. It bridges the temporal gap between an action/feature and the later reward or TD error that should credit it, addressing the temporal credit-assignment problem. In RL the trace is typically an exponentially/geometrically decaying accumulation (controlled by lambda and gamma) of the gradient of the value or log-policy. Two forms recur: a non-contingent trace (critic) accumulating only presynaptic/feature activity, and a contingent trace (actor) that additionally depends on the postsynaptic/action outcome, enabling structural credit assignment. The concept originated in neuroscience as a conjectured synaptic property (Klopf's hedonistic neuron) and finds modern empirical support in reward-modulated spike-timing-dependent plasticity (STDP), where lasting corticostriatal synaptic change requires a neuromodulatory (dopamine) pulse within a time window after paired pre-/post-synaptic spiking — a biological realization of contingent eligibility with prolonged time courses.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sutton-reinforcement-2018-ch12]] — uses: Eligibility traces are the subject of Ch. 12; Ch. 15 connects them to synaptic plasticity / STDP.
[To be populated during integration]