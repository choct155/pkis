---
id: "pkis:source:murphy-llm-linguistic-structure-2025"
aliases: []
title: "Fundamental Principles of Linguistic Structure Are Not Represented by o3"
authors: "Elliot Murphy, Evelina Leivada, Vittoria Dentella, Fritz Günther, Gary Marcus"
year: 2025
type: paper
domain: [symbolic-subsymbolic, deep-learning]
tags: [llm, compositionality, syntax, semantics, o3, openai, psycholinguistics, hierarchical-structure, nlp]
source_url: ""
drive_id: "1mmyqnVV1t-tvkw-0N00ATWjB99FxfXpd"
drive_path: "PKIS/sources/papers/Fundamental Principles of Linguistic Structure Are Not Represented by o3 - Murphy, Leivada, Dentella et al.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[compositionality]]", "[[phrase-structure]]", "[[escher-sentences]]", "[[center-embedding]]"]
---

## Summary

This paper evaluates OpenAI's o3-mini-high reasoning model across 26 carefully chosen linguistic tasks, covering basic linear-order competencies, phrase structure generalization, Escher sentences, center-embedding, paradox generation, syntactic violation generation, scope ambiguities, grammaticality assessment, graded acceptability, Jabberwocky modifications, and semantically impossible entities. The findings reveal a consistent pattern: o3 succeeds at tasks relying on surface-level linear statistics (palindromes, letter counting, basic anaphora resolution) but fails systematically at tasks requiring hierarchical compositional syntax-semantics.

Key failures include: (1) incorrectly judging ungrammatical phrase structures derived from novel pseudowords as grammatical; (2) failing to recognize "Escher sentences" as semantically illegal; (3) hallucinating additional words when asked to draw syntactic trees for center-embedded sentences; (4) generating grammatical rather than ungrammatical sentences when explicitly asked for violations; (5) identifying only 1 of 10 partially acceptable sentences correctly in graded acceptability tasks; (6) producing semantically anomalous rather than truly compositionally impossible entities.

The authors argue these failures are not incidental but reflect a fundamental architectural limitation: LLMs model horizontal (sequential, distributional) relations but not vertical (hierarchical, compositional) ones. They distinguish between o3's capacity to handle "mono-configurational" syntactic assessments versus multi-step compositional reasoning that requires evaluating multiple parses against semantic interpretations. The paper advocates for neuro-symbolic or predicate-argument-structure approaches as a path forward, rather than simply scaling compute.

## Key Knowledge Objects

- [[compositionality]] (concept, high) — the principle that the meaning of a complex expression is determined by its structure and constituent meanings; tested as absent in o3
- [[phrase-structure]] (concept, high) — hierarchical organization of sentences into nested constituents via phrase structure rules; o3 fails to generalize these
- [[center-embedding]] (concept, high) — a sentence construction where a clause is embedded within another in a recursive fashion, stressing working memory; o3 fails to handle grammaticality of these
- escher-sentences (low — concept or result?) — comparative illusions with semantically illegal cardinality comparisons where surface acceptability conflicts with deep ungrammaticality
- [[graded-acceptability]] (concept, moderate — could be principle) — the gradient spectrum of linguistic acceptability that humans are sensitive to but o3 largely misses

## Key Extractions

1. "Deep learning is hitting a wall with respect to compositionality (Marcus 2022) … it is hitting [a [stubbornly [resilient wall]]] that cannot readily be surmounted to reach human-like compositional reasoning simply through more compute."

2. On phrase structure: when presented with a novel pseudoword structure where an extra word makes it ungrammatical (Prompts 8-9), "the model incorrectly claimed that this was grammatical" with "fallacious reasoning."

3. On Escher sentences: "o3-mini-high failed to parse the comparative illusion, noting only the structural acceptability, despite the sentence being ungrammatical."

4. On graded acceptability: "the model succeeded in identifying the most egregiously unacceptable sentences … However, some of its explanations were either lacking in specificity … and the model struggled considerably with partially acceptable sentences, classifying only two sentences as partially acceptable out of ten."

5. "LLMs seem able to capture certain features of dependencies (Tesnière 1959), but other fundamental principles of language that regulate how constituency, headedness, and incremental node counts yield semantic instructions during parsing remain somewhat elusive."

6. "It is not coherent to claim that LLMs can directly constitute a 'theory of language' (Katzir 2023; Müller 2024)… the representational capacities of LLMs are unbounded in a way that makes their representations arbitrary."

7. Table 1 summary: across 6 successive prompts requesting syntactic violations, o3 generated an unacceptable structure in only 3/6 attempts and never successfully generated a violation causally driven by properties of a prior sentence.

## Connection Candidates

- [[compositionality]] — grounds: the paper's central argument is that o3 lacks a compositional operator; directly addresses what compositionality requires and how it differs from distributional statistics
- [[neurosymbolic-ai]] — extends: paper advocates neuro-symbolic approaches (predicate-argument structure, variable binding, constituent structure) as the path beyond pure LLM scaling
- [[dentella-ai-language-comprehension-2024]] — extends: same research group testing a different model (o3) with different methodology; both papers document systematic LLM failures in linguistic structure
- [[inductive-bias]] — grounds: the failure on hierarchical structure reflects a missing inductive bias toward compositional syntax in the transformer architecture
- [[discourse-representation-theory]] — contrasts-with: DRT provides a formal compositional semantics that o3 demonstrably cannot replicate

## Awaiting Classification

- **escher-sentences** — candidate types: concept or result
  - Case for concept: a defined class of sentence with a clear identity and boundary — comparative illusions with illegal cardinality
  - Case for result: could be framed as a result/finding that certain surface-acceptable comparatives are semantically ungrammatical
  - What makes this hard: the phenomenon is both a defined linguistic construct (concept) and an empirical claim about grammaticality (result-adjacent)
