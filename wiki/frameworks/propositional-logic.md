---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:framework:propositional-logic
instantiates:
- expressiveness-tractability-tradeoff
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- logical-entailment-and-inference
related_concepts: []
sources:
- russell-norvig-aima-ch07
specializes:
- knowledge-representation
tags:
- logic
- boolean
- factored-representation
- connectives
title: Propositional Logic
understanding: 0
---

## Definition
A formal language for representing knowledge whose atomic sentences are proposition symbols, each of which is either true or false in a given model. A model is simply an assignment of a truth value to every proposition symbol; with n symbols there are 2^n models. Complex sentences are built recursively from atoms using five logical connectives: negation (¬), conjunction (∧), disjunction (∨), implication (⇒), and biconditional (⇔). The semantics is given by truth tables that compositionally determine the truth of any sentence in any model. Propositional logic is a factored representation: it can express that propositions are known true, known false, or unknown — a strict gain over the atomic (state-enumeration) representations of basic problem-solving agents — but it lacks the expressive power to talk about objects, relations, or universal quantification (the role of first-order logic).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[expressiveness-tractability-tradeoff]] — instantiates: Tractable but inexpressive end of the spectrum; lacks quantification, motivating first-order logic.
- [[knowledge-representation]] — specializes: Propositional logic is a particular (factored) knowledge representation language.
- [[logical-entailment-and-inference]] — prerequisite-of
[To be populated during integration]