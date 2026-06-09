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
id: pkis:framework:semantic-network
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch10
tags:
- semantic-network
- frames
- inheritance
- multiple-inheritance
- default-values
- procedural-attachment
- reification
- existential-graphs
title: Semantic Network
understanding: 0
---

## Definition
Semantic networks are graphical knowledge-representation systems — objects and categories as nodes, labeled links as binary relations — that provide a visualizable notation and efficient inheritance algorithms for inferring an object's properties from its category membership. Tracing to Peirce's existential graphs (1909), Quillian (1961), and Minsky's frames (1975), they are, despite the historic "logic vs. networks" debate, a form of logic: stripped of human-interface convenience, the underlying objects, relations, and quantification are the same.

## Mechanics
- MemberOf and SubsetOf links encode ∈ and ⊂; single-boxed links assert a property of every member of a category (∀x x∈Persons ⇒ Legs(x,2)); double-boxed links assert a relation holding between members and a target category.
- **Inheritance** reasoning follows MemberOf then SubsetOf links upward until a boxed property is found — simple and efficient compared with semidecidable theorem proving.
- **Multiple inheritance** (an object/category with multiple parents) can yield conflicting values; allowed in semantic networks but banned in some OOP languages (Java).

## Expressiveness limits and extensions
- Links are only binary; n-ary assertions require **reification** of the proposition as an event object, forcing a rich ontology of reified concepts.
- Missing relative to full FOL: negation, disjunction, nested functions, existential quantification. **Procedural attachment** fills gaps by calling a special procedure for a relation instead of general inference.
- **Default values**: a category property has only default status and is **overridden** by more specific information (John has one leg though persons have two) — the inheritance algorithm enforces this naturally by stopping at the first value found.

## Reading Path
- [[russell-norvig-aima-ch10]] — §10.5.1: semantic networks, inheritance, defaults, reification, procedural attachment

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]