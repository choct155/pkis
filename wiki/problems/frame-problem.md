---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:problem:frame-problem
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch07
tags:
- frame-problem
- qualification-problem
- successor-state-axiom
- fluent
- transition-model
- situation-modeling
title: The Frame Problem and Successor-State Axioms
understanding: 0
---

## Definition
The frame problem (McCarthy & Hayes, 1969) is the difficulty of representing, in logic, what does NOT change when an action is performed. Effect axioms state the changes an action causes (e.g. Forward moves the agent), but say nothing about untouched fluents (state variables indexed by time), so after acting the agent cannot prove that, e.g., it still has its arrow — the information is lost. Naive frame axioms explicitly assert each unchanged proposition, giving O(mn) axioms for m actions and n fluents (the representational frame problem) and O(nt) projection cost (the inferential frame problem). The standard solution (Reiter, 1991) reframes axioms around fluents rather than actions: a successor-state axiom defines F^{t+1} ⇔ (an action makes F true) ∨ (F^t ∧ no action makes F false), exploiting locality (each action changes few fluents) to reduce the axiom set to O(mk). The related qualification problem — enumerating all preconditions/exceptions for an action to succeed — has no complete logical solution and is one motivation for probabilistic models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]