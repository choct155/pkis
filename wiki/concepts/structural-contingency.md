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
- causal-analysis
id: pkis:concept:structural-contingency
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch10
specializes:
- structural-causal-models
tags:
- causality
- do-operator
- intervention
- structural-causal-models
- autonomy
title: Structural Contingency
understanding: 0
uses:
- do-calculus
---

## Definition
A structural contingency is a hypothetical perturbation of a causal model produced by intervening on (overriding) one of its mechanisms -- a do(.) "miracle" that violates a structural equation such as B=C -- as opposed to a circumstantial contingency, which is merely a different setting U=u of the background variables consistent with the model's existing mechanisms. Pearl's account of actual causation insists that a cause x sustain its effect y against structural rather than circumstantial contingencies. The justification is the autonomy of mechanisms: every causal model stands for a whole family of submodels, one for each state of the do(.) operator, so each mechanism "advertises its possible breakdown," and these advertised breakdowns are precisely the contingencies against which causal explanations should operate (e.g. imagining rifleman B prevented from firing by mechanical failure, even though no failure actually occurred). The contingency set W must be chosen with care: it cannot include all variables mediating X and Y (that would prevent anything from sustaining anything) and unrestricted choice of W can dissolve genuine preemptions, turning noncauses into causes (e.g. W={X}, w'=0 in the desert traveler). This distinction grounds why structural information -- which logical/INUS accounts lack -- is indispensable, and it carries the pragmatics of explanation: which contrary-to-fact world one travels to depends on the explanatory target.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[structural-causal-models]] — specializes: arises from the autonomy of mechanisms in an SCM
- [[do-calculus]] — uses: structural contingencies are do(.) interventions overriding mechanisms
[To be populated during integration]