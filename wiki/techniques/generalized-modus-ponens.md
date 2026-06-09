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
- knowledge-representation
- symbolic-subsymbolic
generalizes:
- propositionalization
id: pkis:technique:generalized-modus-ponens
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch09
tags:
- first-order-logic
- logical-inference
- russell-norvig-aima
title: Generalized Modus Ponens
understanding: 0
uses:
- unification
---

## Definition
A lifted version of Modus Ponens that raises the rule from ground propositional logic to first-order logic: given atomic premises p_i', an implication p_1 and ... and p_n => q, and a substitution theta with SUBST(theta,p_i')=SUBST(theta,p_i) for all i, it infers SUBST(theta,q). It makes only the substitutions required for a particular inference, avoiding the wasteful enumeration of propositionalization.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[propositionalization]] — generalizes
- [[unification]] — uses
[To be populated during integration]