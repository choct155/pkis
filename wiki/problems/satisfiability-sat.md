---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
contrasts-with:
- logical-entailment-and-inference
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- optimization
- symbolic-subsymbolic
id: pkis:problem:satisfiability-sat
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch07
tags:
- sat
- np-complete
- phase-transition
- combinatorial-search
- model-finding
title: Boolean Satisfiability (SAT)
understanding: 0
---

## Definition
The decision problem of determining whether a propositional sentence (typically in CNF) is satisfiable — i.e., whether some truth assignment makes it true. SAT was the first problem proved NP-complete (Cook, 1971), and because testing entailment reduces to testing unsatisfiability (α ⊨ β iff α ∧ ¬β is unsatisfiable), SAT sits at the heart of logical inference. A vast range of combinatorial problems — constraint satisfaction, hardware and protocol verification, planning (SATPLAN) — reduce to SAT, so any improvement in SAT algorithms has broad consequences. Two algorithm families dominate: complete backtracking search (DPLL and modern CDCL solvers) and incomplete local search (WALKSAT). Hardness is not uniform: random k-CNF instances exhibit a satisfiability phase transition, with the hardest instances clustered at a critical clause-to-variable ratio.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[logical-entailment-and-inference]] — contrasts-with: Entailment treats unknowns as unusable in a proof; SAT may set them freely — the gap SATPLAN must close.
[To be populated during integration]