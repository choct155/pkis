---
aliases: []
also_type: []
applies:
- expected-utility-theory
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
contrasts-with:
- potential-outcomes-framework
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- bayesian-stats
id: pkis:principle:causal-vs-evidential-decision-theory
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch04
tags:
- causality
- decision-theory
- do-operator
- newcombs-paradox
- interventions
- pearl
title: Causal vs. Evidential Decision Theory
understanding: 0
uses:
- do-calculus
---

## Definition
The principle that a rational agent deciding on an action should maximize expected utility computed with the interventional distribution, U(x) = Σ_y P(y|do(x)) u(y), rather than the **evidential** conditional expectation U_ev(x) = Σ_y P(y|x) u(y) that treats the chosen action as an observed proposition. The evidential approach yields absurdities — avoid the doctor to lower the probability of being ill, don't hurry to work to avoid having overslept — because it conflates an **act** (viewed from outside; predictable; evidence for the actor's motives) with an **action** (an object of free choice, pending deliberation). Conditioning represents passive observation in an unchanging world; an action *changes* the world and so renders the past statistical evidence an act would provide irrelevant to the decision. The do-operator captures the invariant elements of the world under intervention by locally modifying the mechanism (graph/structural equations), supplying information that P(s) alone never determines — contrast with 'imaging' (Lewis/Gärdenfors), which transfers mass to closest worlds but leaves the closeness function unconstrained. This resolves the act/action confusion underlying Newcomb's paradox and Jeffrey's evidential decision theory, and explains why causal models can predict the effects of novel actions never anticipated at model-construction time (vs. influence-diagram approaches that must enumerate every decision variable in advance).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[expected-utility-theory]] — applies
- [[potential-outcomes-framework]] — contrasts-with
- [[do-calculus]] — uses
[To be populated during integration]