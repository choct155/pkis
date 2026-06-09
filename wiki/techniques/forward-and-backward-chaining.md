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
id: pkis:technique:forward-and-backward-chaining
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch07
specializes:
- resolution-inference
tags:
- forward-chaining
- backward-chaining
- horn-clause
- data-driven
- goal-directed
- logic-programming
title: Forward and Backward Chaining
understanding: 0
uses:
- conjunctive-normal-form
---

## Definition
Two natural inference algorithms for knowledge bases of definite (Horn) clauses, each deciding whether a query atom q is entailed in time linear in the size of the KB. Forward chaining is data-driven: starting from known facts, whenever all premises of an implication are known, its conclusion is added; this repeats until q is derived or no new inference is possible. It is sound (each step is Modus Ponens) and complete (the fixed point defines a model of the KB in which every entailed atom is true). Backward chaining is goal-directed: to prove q, find implications whose conclusion is q and recursively try to prove their premises, bottoming out at known facts. Forward chaining propagates upward through the AND-OR graph of the KB; backward chaining works downward from the goal and often touches far fewer than all facts. Both are the inferential basis of logic programming (Prolog).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[conjunctive-normal-form]] — uses: Operates on definite/Horn clauses, a restricted CNF form.
- [[resolution-inference]] — specializes: A more restricted, efficient inference method for the Horn-clause sublanguage.
[To be populated during integration]