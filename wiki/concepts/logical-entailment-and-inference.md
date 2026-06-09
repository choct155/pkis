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
id: pkis:concept:logical-entailment-and-inference
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- resolution-inference
related_concepts: []
sources:
- russell-norvig-aima-ch07
tags:
- entailment
- model-checking
- soundness
- completeness
- validity
- satisfiability
title: Logical Entailment and Inference
understanding: 0
---

## Definition
Entailment is the semantic relation 'α ⊨ β' holding when β is true in every model in which α is true — equivalently, M(α) ⊆ M(β), where M(·) is the set of models of a sentence. Entailment is the needle-in-haystack target; inference is the syntactic process of finding it: 'KB ⊢_i α' means inference procedure i derives α from KB. An inference procedure is sound (truth-preserving) if it derives only entailed sentences, and complete if it derives every entailed sentence. Three derived notions structure all of logical reasoning: a sentence is valid (a tautology) if true in all models; satisfiable if true in some model; and two sentences are logically equivalent (α ≡ β) if they have the same models. These are linked by the deduction theorem (α ⊨ β iff (α⇒β) is valid) and the refutation identity (α ⊨ β iff (α ∧ ¬β) is unsatisfiable).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[resolution-inference]] — prerequisite-of
[To be populated during integration]