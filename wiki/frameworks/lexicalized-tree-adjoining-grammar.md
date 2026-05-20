---
title: "Lexicalized Tree Adjoining Grammar"
knowledge_type: framework
also_type: [technique]
domain: [knowledge-representation, symbolic-subsymbolic]
tags: [grammar, natural-language-processing, syntax, ltag, formal-grammar, parsing]
related_concepts: [discourse-representation-theory, ontology-lexicon, semantic-parsing]
sources: ["[[cimiano-ontology-nlp]]", "[[murphy-llm-linguistic-structure-2025]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

Lexicalized Tree Adjoining Grammar (LTAG) is a grammar formalism in which every elementary structure is a tree anchored to a lexical item; trees combine via substitution and adjunction operations, enabling mildly context-sensitive syntactic representation used here as the syntactic backbone for ontology-aligned parsing.

Classification note: assigned as framework (an organized system of syntactic representation with its own architecture, operations, and parsing algorithms) but also technique (a procedure applied to parse and generate sentences).

## Reading Path
- [[cimiano-ontology-nlp-ch03]] (unread) — primary treatment; LTAG elementary trees, substitution, adjunction; alignment of tree nodes to ontology vocabulary
- [[cimiano-ontology-nlp-ch05]] (unread) — automated LTAG entry generation from lemon lexica
- [[murphy-llm-linguistic-structure-2025]] (unread) — §3.2–3.4: tests whether o3 can apply basic phrase structure rules (related to LTAG substitution/adjunction); o3 generates syntactic trees that are inconsistent with the actual string structure — the trees it produces violate the fundamental constituency relationships that LTAG trees encode
