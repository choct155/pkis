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
- knowledge-representation
- symbolic-subsymbolic
id: pkis:concept:conjunctive-normal-form
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch07
tags:
- cnf
- clause
- horn-clause
- definite-clause
- normal-form
title: Conjunctive Normal Form (CNF), Clauses, and Horn Clauses
understanding: 0
---

## Definition
A clause is a disjunction of literals; a sentence in conjunctive normal form (CNF) is a conjunction of clauses. Every sentence of propositional logic is logically equivalent to a CNF sentence, which is what makes clause-based inference (resolution, DPLL) universally applicable. Conversion to CNF is a fixed four-step procedure: (1) eliminate ⇔ via (α⇒β)∧(β⇒α); (2) eliminate ⇒ via ¬α∨β; (3) move ¬ inward to literals using double-negation and De Morgan's laws; (4) distribute ∨ over ∧. Restricted clause forms enable far more efficient inference: a definite clause has exactly one positive literal (equivalently an implication whose body is a conjunction of positive literals and whose head is a single atom); a Horn clause has at most one positive literal (definite clauses plus goal clauses with no positive literal); a k-CNF clause has at most k literals.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]