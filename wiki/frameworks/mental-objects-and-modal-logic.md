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
id: pkis:framework:mental-objects-and-modal-logic
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch10
tags:
- modal-logic
- propositional-attitudes
- possible-worlds
- referential-opacity
- epistemic-logic
- belief
- knowledge
- logical-omniscience
- linear-temporal-logic
title: Modal Logic of Mental Objects
understanding: 0
---

## Definition
A framework for representing knowledge *about* knowledge and belief — the mental objects (beliefs, knowledge) inside an agent's head and the propositional attitudes (Believes, Knows, Wants, Informs) agents hold toward them. The classical approach is **modal logic with possible-worlds semantics** (Hintikka, Kripke).

## The referential-opacity problem
Propositional attitudes do not behave like ordinary predicates. Because equality reasoning is built into first-order logic (**referential transparency**), Knows(Lois, CanFly(Superman)) plus Superman=Clark wrongly yields Knows(Lois, CanFly(Clark)). For attitudes we instead want **referential opacity**: the *term* used matters, because not all agents know which terms co-refer.

## Modal logic solution
- **Modal operators** take sentences (not terms) as arguments: K_A P reads "agent A knows P."
- Semantics uses a collection of **possible worlds** connected by **accessibility relations** (one per modal operator): K_A P is true at world w iff P holds in every world accessible from w. Supports nested knowledge (what A knows about B's knowledge) and disambiguates quantifier scope (∃x K_Bond Spy(x) vs. K_Bond ∃x Spy(x)).
- **Axioms**: distribution (K_a P ∧ K_a(P⇒Q) ⇒ K_a Q); knowledge implies truth (K_a P ⇒ P, "justified true belief"); positive introspection (K_a P ⇒ K_a K_a P).
- **Logical omniscience** is the central defect: agents are assumed to know all consequences of what they know; attempts at resource-bounded rationality have been unsatisfactory.

## Other modalities
Possibility/necessity, and **linear temporal logic** operators X (next), F (finally), G (globally), U (until). The choice of modal logic trades expressive succinctness against inference complexity.

## Reading Path
- [[russell-norvig-aima-ch10]] — §10.4: mental objects, propositional attitudes, modal logic, possible worlds, temporal modalities

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]