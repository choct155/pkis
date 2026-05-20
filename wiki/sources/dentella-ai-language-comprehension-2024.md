---
title: "Testing AI on Language Comprehension Tasks Reveals Insensitivity to Underlying Meaning"
authors: "Vittoria Dentella, Fritz Günther, Elliot Murphy, Gary Marcus, Evelina Leivada"
year: 2024
type: paper
domain: [symbolic-subsymbolic, deep-learning]
tags: [llm, language-comprehension, compositionality, benchmarking, nlp, psycholinguistics, moravecs-paradox]
source_url: ""
drive_id: "1i7uFU04dlll2yRdoPndZI9GAXPs8cGla"
drive_path: "PKIS/sources/papers/Testing AI on Language Comprehension Tasks Reveals Insensitivity to Underlying Meaning - Dentella, Günther, Murphy et al.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[llm-language-comprehension]]", "[[compositional-operator]]", "[[moravecs-paradox]]"]
---

## Summary

This paper systematically evaluates seven state-of-the-art large language models (LLMs) — ChatGPT-3.5, ChatGPT-4, Llama2, Bard, Falcon, Mixtral, and Gemini — on a novel benchmark of 40 simple language comprehension questions. The questions target short sentences with high-frequency constructions (e.g., active/passive voice with 3 or 5 named entities), keeping linguistic complexity at a deliberate minimum. Each question was prompted multiple times in two settings (open-length and one-word response), yielding n=26,680 total datapoints when combined with a human comparison group of 400 participants.

The central finding is that, as a group, LLMs perform at chance accuracy on these elementary comprehension tasks. While some models (ChatGPT-4, Falcon, Llama2) exceed chance, none approach human ceiling performance. Even ChatGPT-4 — the best-performing LLM — is significantly outperformed by the best-performing humans. LLMs are also considerably less stable than humans: they frequently give different answers when the same question is presented multiple times, while human responses are essentially deterministic. Qualitatively, LLM errors are distinctively non-human: irrelevant elaborations, contradictory information, and mixing of unrelated matters.

The authors interpret these results as evidence that LLMs process language as statistical surface patterns rather than compositionally structured meaning. They argue that the outputs of LLMs are "semantic black-boxes" — approximating surface statistics of training data without access to a compositional operator that maps syntactic form to meaning. The paper also challenges the use of LLMs as cognitive theories of language, noting that their unbounded representational capacity makes them Universal Functional Approximators rather than explanatorily grounded scientific models.

## Key Knowledge Objects

- [[llm-language-comprehension]] (problem, high) — the challenge of whether LLMs genuinely understand language vs. pattern-matching surface statistics
- [[compositional-operator]] (concept, moderate — could be principle) — the putative cognitive mechanism mapping hierarchical syntactic structure to meaning, claimed to be absent in LLMs
- moravecs-paradox (low — concept or principle?) — easy tasks for humans (language comprehension) are harder to reverse-engineer for AI than high-level reasoning tasks
- [[moravecs-paradox]] (concept, high) — Moravec's observation that AI systems struggle most with tasks that are effortless for humans

## Key Extractions

1. "Based on a dataset of n=26,680 datapoints, we discovered that LLMs perform at chance accuracy and waver considerably in their answers" when tested on simple language comprehension questions with minimal linguistic complexity.

2. "The intercept in an intercept-only GLMM (accuracy ~ 1 + (1 | test_item)) is not significantly different from zero (β = 0.224, z = 1.71, P = .087), indicating at-chance performance when all LLMs are taken together."

3. "Even the best performing LLM, ChatGPT-4, performs worse than the best performing humans" — specifically, 51 humans perform at ceiling while ChatGPT-4 does not.

4. LLMs are less stable than humans: while humans almost never change answers across repeated trials, LLMs "succeed in consistently providing the same answer" only partially — and Bard/Mixtral show especially poor stability.

5. "If the LLMs' fluent outputs are taken to entail human-like linguistic skills … then it follows that LLMs should possess mastery over all the words, constructions, and rules of use … Our results … suggest that this is not the case: distinctly non-human errors are made."

6. "Intelligence cannot in fact emerge as a side product of statistical inference (van Rooij et al., 2023), nor can the ability to understand meaning (Bender & Koller, 2020)."

7. The one-word setting significantly improved LLM accuracy (β = 1.037, z = 8.872, P < .001), suggesting that format constraints partially remediate surface-level failures — an effect not observed for humans.

## Connection Candidates

- [[neurosymbolic-ai]] — extends-to: the paper's conclusion that LLMs need a compositional mechanism is a motivation for neurosymbolic approaches combining neural pattern matching with symbolic structure
- [[inductive-bias]] — grounds: lack of an appropriate inductive bias toward hierarchical compositional structure is the proposed mechanism for LLM failure
- [[neural-networks]] — contrasts-with: the paper argues neural LLMs lack the architectural primitives needed for compositional language understanding
- [[murphy-llm-linguistic-structure-2025]] — extends: the sister paper examining o3 specifically; same research group, overlapping authors

## Awaiting Classification

- **moravecs-paradox** — candidate types: concept or principle
  - Case for concept: it is a well-defined idea with a clear boundary (easy human skills are hardest to reverse-engineer)
  - Case for principle: it functions as a guiding constraint on AI system design and benchmark selection
  - What makes this hard: it is named observation/empirical generalization that has both definitional content (concept) and normative/guiding force (principle)
