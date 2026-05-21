---
title: "Discourse Representation Theory"
knowledge_type: framework
also_type: [concept]
domain: [knowledge-representation, symbolic-subsymbolic]
tags: [semantics, natural-language-processing, drt, formal-semantics, discourse, compositional-semantics, dudes]
related_concepts: [formal-ontology, lexicalized-tree-adjoining-grammar, semantic-parsing, ontology-lexicon]
sources: ["[[cimiano-ontology-nlp]]", "[[dentella-ai-language-comprehension-2024]]", "[[murphy-llm-linguistic-structure-2025]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

Discourse Representation Theory (DRT) is a formal semantic framework that represents the meaning of sentences and discourses through *discourse referents* and conditions on those referents; extended as DUDES (Dependency-based Underspecified DRS) for pairing syntactic LTAG structures with ontology-aligned semantic representations.

Classification note: assigned as framework (it organizes an entire approach to NL semantics with conventions around representation, composition, and evaluation) but also functions as a concept (a defined formal apparatus with clear boundary conditions).

## Reading Path
- [[cimiano-ontology-nlp-ch03]] (unread) — primary treatment; DRT formal apparatus; DUDES as the ontology-aligned extension; pairing with LTAG for compositional interpretation
- [[cimiano-ontology-nlp-ch06]] (unread) — worked examples of DUDES composition in practice
- [[dentella-ai-language-comprehension-2024]] (unread) — §3: the 40 comprehension test questions draw on DRT-style constructions (anaphora resolution, quantifier scope, relative clauses) to probe whether LLMs track discourse referents and conditions; LLM failures on these tests implicate DRT-level semantic processing deficits
- [[murphy-llm-linguistic-structure-2025]] (unread) — §3.3: Escher sentences and scope-ambiguity probes require DRT-level semantic representation; o3's failures on Escher sentences (which require tracking referent identity) are consistent with a lack of genuine discourse representation
