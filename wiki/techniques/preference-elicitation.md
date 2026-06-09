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
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- agentic-systems
id: pkis:technique:preference-elicitation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- expected-utility-theory
related_concepts: []
sources:
- russell-norvig-aima-ch16
tags:
- decision-theory
- utility
- standard-lottery
- decision-analysis
- human-ai-collaboration
title: Preference Elicitation
understanding: 0
uses:
- multiattribute-utility-theory
---

## Definition
## Definition
**Preference elicitation** is the process of determining a human's utility function by presenting choices and using the observed preferences to pin down the underlying $U$ (R&N Section 16.2.1). It is the operational front end of any decision-theoretic system that acts on a person's behalf.

### The standard-lottery method
Utilities have no absolute scale, so one fixes two anchor outcomes — a best prize $u_\top$ and a worst catastrophe $u_\bot$ — typically as **normalized utilities** $u_\bot=0$, $u_\top=1$. The utility of any prize $S$ is then assessed by offering a choice between $S$ for sure and a **standard lottery** $[p,u_\top;\,(1-p),u_\bot]$, adjusting $p$ until the agent is indifferent; that indifference $p$ *is* $U(S)$. In life-and-death domains $u_\bot$ is death, valued in practice via the **micromort** (one-in-a-million chance of death), the **value of a statistical life** (~US\$10M, 2019), or **QALYs** (quality-adjusted life years).

### Practical pitfalls
Elicited preferences are routinely inconsistent (Allais, Ellsberg paradoxes; framing, anchoring, certainty effects). Keeney and Raiffa found subjects are too risk-averse in the small, but can reconcile their inconsistencies on reflection — paradoxes shrink (not vanish) when choices are explained, and "evolutionarily appropriate" framings (frequencies, animations) elicit choices closer to rationality. Bayesian preference elicitation (Chajewska et al., 2000; Boutilier, 2002) starts from a prior over the utility function and refines it.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[multiattribute-utility-theory]] — uses: MAUT structure reduces the number of elicitation experiments
- [[expected-utility-theory]] — prerequisite-of: elicitation supplies the U that EU maximization requires
- Supplies the utility function required by expected-utility theory.
- Its target structure for many attributes is given by multiattribute utility theory.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]