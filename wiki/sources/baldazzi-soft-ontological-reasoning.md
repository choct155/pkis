---
title: "Softening Ontological Reasoning with Large Language Models"
authors: ["Teodoro Baldazzi", "Davide Benedetto", "Luigi Bellomarini", "Emanuel Sallinger", "Adriano Vlad"]
year: 2024
type: paper
domain: [knowledge-representation, symbolic-subsymbolic]
tags: [ontological-reasoning, neurosymbolic, knowledge-graphs, datalog, vadalog, chase-procedure, llm, rule-based-reasoning, explainability]
source_url: ""
drive_id: "1r6lIK8zQsEetsG1SU6lNZnkpLDDOrcvx"
drive_path: "PKIS/sources/papers/baldazzi-soft-ontological-reasoning.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[neurosymbolic-ai]]", "[[ontology-reasoning]]", "[[knowledge-graph]]", "[[retrieval-augmented-generation]]"]
---

## Summary

Baldazzi et al. propose a neurosymbolic solution to a fundamental limitation of logic-based Knowledge Representation and Reasoning (KRR): the inability to handle unstructured natural language data due to the rigidity of formal rule systems. The paper introduces a "soft chase" technique that extends the traditional chase procedure — the core inference mechanism of Datalog-based ontological reasoners like Vadalog — to accommodate unstructured (natural language) input by using an LLM as a "semantic unifier."

In standard KRR, a rule can only activate when an exact syntactic binding (homomorphism) from rule body variables to constants in the database exists. Natural language facts lack the structured format required for these bindings, so critical inferences are missed. The soft chase replaces exact binding identification with LLM-based semantic binding: given a rule verbalized in natural language and candidate NL facts, the LLM generates variable-to-constant mappings based on semantic understanding. A feedback validation loop corrects hallucinated or malformed mappings; a verbalization module converts inferred facts back to natural language; and an LLM-based termination check prevents redundant fact derivation.

The five-phase pipeline (initialization, binding identification, binding validation, rule activation, termination check) is integrated with Vadalog and evaluated on a financial entity ownership reasoning task. Pure soft chase improves recall significantly at the cost of some precision, as LLMs may incorrectly infer ownership from CEO status. Adding RAG-enriched context to the LLM substantially improves both precision and recall by constraining domain-specific inferences. The paper positions itself as the first approach to seamlessly integrate LLMs within a KRR-centric framework (rather than merely using KGs to augment LLMs) throughout the entire reasoning process.

## Key Knowledge Objects

- [[neurosymbolic-ai]] (framework, high) — the overarching paradigm; soft chase is a concrete neurosymbolic technique integrating LLMs with formal logic-based KRR
- [[ontology-reasoning]] (technique, high) — the core KRR capability being extended; chase-based Datalog reasoning over knowledge graphs
- [[knowledge-graph]] (concept, high) — structured KG serves as the base data layer for the ontological reasoning system
- [[retrieval-augmented-generation]] (technique, moderate) — used as an extension to the soft chase to improve LLM accuracy in domain-specific binding identification

## Key Extractions

1. **Soft chase mechanism**: The standard chase procedure's exact-binding requirement is generalized to semantic binding via LLM. The LLM acts as a "semantic unifier," generating variable-to-constant mappings from NL facts to rule bodies, enabling rules to fire on unstructured data.
2. **Feedback validation loop**: After binding identification, a separate LLM validator confirms mapping correctness in a feedback loop (up to a retry limit), reducing hallucinated bindings before rule activation.
3. **Verbalization module**: Newly inferred logical facts are deterministically verbalized into natural language using a glossary of predicate descriptions; this verbalized form feeds the LLM-based termination check that prevents semantic duplicates in the chase.
4. **RAG-enhanced soft chase**: Providing domain knowledge via RAG to the semantic unifier LLM significantly reduces false positive inferences (e.g., preventing inference of share ownership from CEO role), improving precision while maintaining higher recall than standard chase.
5. **Precision-recall tradeoff**: Standard chase: high precision, low recall (misses NL bindings). Soft chase: lower precision, high recall. Soft chase + RAG: highest F1 — demonstrating that domain-specific RAG context is critical for constraining LLM semantic unification.

## Connection Candidates

- [[neurosymbolic-ai]] — specializes: soft chase is a specific neurosymbolic architecture where the symbolic engine (Vadalog) drives inference while the neural component (LLM) handles semantic interpretation
- [[ontology-reasoning]] — extends: soft chase extends standard chase-based ontological reasoning to unstructured NL inputs
- [[knowledge-graph]] — uses: Vadalog KG serves as both the rule system and the fact database for the reasoning process
- [[retrieval-augmented-generation]] — uses: RAG enriches the LLM semantic unifier with domain-specific knowledge, reducing hallucinations in binding identification
- [[directed-graphical-models]] — uses: the chase graph is a directed acyclic graph recording inference derivations with provenance
