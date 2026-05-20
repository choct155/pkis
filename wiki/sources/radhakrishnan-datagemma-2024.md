---
title: "Knowing When to Ask — Bridging Large Language Models and Data (DataGemma)"
authors: "Prashanth Radhakrishnan, Jennifer Chen, Bo Xu, Prem Ramaswami, Hannah Pho, Adriana Olmos, James Manyika, R. V. Guha"
year: 2024
type: paper
domain: [knowledge-representation, deep-learning]
tags: [llm, hallucination, retrieval, knowledge-graphs, fine-tuning, statistical-data, data-commons, grounding]
source_url: ""
drive_id: "1bZvU4x_mXPstUwb_e8MAfyTnwlv0cGL-"
drive_path: "PKIS/sources/papers/DataGemma-FullPaper.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[retrieval-augmented-generation]]", "[[in-context-learning]]", "[[knowledge-graph]]", "[[knowledge-graph-question-answering]]"]
---

## Summary

This paper (the DataGemma system paper, also deposited as "Knowing When to Ask") addresses LLM hallucinations on numerical and statistical queries by integrating Gemma/Gemma-2 models with Data Commons — Google's open-source repository of over 250 billion public data points from sources such as the UN, CDC, and national census bureaus. The authors frame the problem around three sub-problems: (1) teaching the LLM when to request external data rather than rely on parametric memory, (2) routing that request to the appropriate source, and (3) generating natural-language queries that a single universal API can fulfil without requiring SQL or schema knowledge.

Two distinct architectures are developed and evaluated. Retrieval Interleaved Generation (RIG) fine-tunes a Gemma 7B/27B model to insert inline Data Commons natural-language queries alongside generated statistics; a post-processing pipeline parses the query into structured components (variable, place, attribute), maps them to Data Commons variable IDs, and retrieves a scalar fact-check value. Retrieval Augmented Generation (RAG) fine-tunes a Gemma-2 9B/27B model to decompose a user query into up to 25 sub-questions, fetches corresponding tables from Data Commons, and passes them to a long-context Gemini 1.5 Pro for final answer synthesis.

On a human-annotated 101-query evaluation set, RIG improved factual accuracy on returned statistics from 5–17% (baseline) to ~58%; RAG achieved 98.6–98.9% accuracy on statistical claims when tables were retrieved. The main coverage bottleneck for both methods is Data Commons dataset gaps (~35–43% of failed queries) rather than model quality. User preference for RIG responses over the baseline was 62–76%; for RAG when tables were used, 92–100%. Both models and their training datasets are released open-source under Apache 2.0.

## Key Knowledge Objects

- [[retrieval-augmented-generation]] (technique, high) — RAG pipeline: decompose user query into sub-questions, retrieve Data Commons tables, augment LLM prompt with serialized tables
- [[knowledge-graph]] (concept, high) — Data Commons functions as a collection of interoperable KGs normalized under Schema.org, with 2.5 trillion RDF-style triples
- [[knowledge-graph-question-answering]] (problem, high) — structured natural-language-to-data querying over a massive public-statistics KG; the paper's core challenge
- [[in-context-learning]] (technique, high) — few-shot CoT prompting used to train Data Commons annotation generation and RAG sub-question generation
- retrieval-interleaved-generation (low — technique or framework?) — inline fine-tuned retrieval calls interleaved with generation; a variant of tool-use that may be its own framework-level pattern
- data-commons-nl-interface (low — technique or framework?) — the NL-to-structured-query translation layer atop Data Commons; straddles technique (query-conversion pipeline) and framework (unified public-data API)

## Key Extractions

1. **RIG factual accuracy:** The 27B fine-tuned RIG model achieved 58.8% accuracy on Data Commons-returned statistical values, compared to only 16.7% accuracy for the base 27B model's own generated values — a 3.5× improvement in grounding to verified data.

2. **RAG statistical claim accuracy:** The RAG approach with 9B fine-tuned model achieved 98.6% accuracy on statistical claims cited in the response, but only 71.9% accuracy on inferred claims (derived reasoning from those statistics), highlighting that numerical grounding does not guarantee correct inference.

3. **Coverage bottleneck:** Only 23–29% of statistical queries in the evaluation set elicited usable Data Commons responses. The dominant reason was Data Commons coverage gaps (30–43% of failed queries), not model failure, providing motivation for expanding the public-data repository.

4. **Natural language as universal API:** The paper adopts natural language queries (not SQL or formal APIs) as the interface to Data Commons, inspired by URL encoding (McCool 1993). This design choice allows fine-tuning on a small corpus (~400–635 examples) because the task reduces to contextual rephrasing rather than structured query synthesis.

5. **User preference:** Human raters with no familiarity with Data Commons preferred RAG answers over baseline Gemini 1.5 Pro 92–100% of the time when statistical tables were actually used — the strongest signal that grounded statistical data meaningfully improves perceived response quality.

6. **LIMA-style data efficiency:** Both RIG and RAG fine-tuning was achieved with fewer than 700 training examples, consistent with the LIMA result (Zhou et al. 2023) that small, high-quality instruction sets suffice for behavior alignment.

## Connection Candidates

- [[retrieval-augmented-generation]] — extends: DataGemma's RAG pipeline is a domain-specific extension of standard RAG, adding a query-decomposition fine-tuning step tailored to structured statistical data rather than unstructured text corpora
- [[knowledge-graph]] — uses: Data Commons operates as a KG (2.5 trillion triples via Schema.org); both RIG and RAG treat it as the ground-truth external knowledge source
- [[knowledge-graph-question-answering]] — specializes: DataGemma addresses a specific KGQA subproblem where the KG is a public-statistics store and questions involve numerical comparisons and arithmetic
- [[in-context-learning]] — uses: few-shot prompting to Gemini 1.5 Pro generates the RIG annotation training set; chain-of-thought examples guide the fine-tuned sub-question generator
- [[tool-use]] — specializes: RIG is an application of Toolformer-style tool-use where the tool is a natural-language data query rather than a code API call

## Awaiting Classification

- **retrieval-interleaved-generation** — candidate types: technique or framework
  - Case for technique: it is a specific procedural pipeline (fine-tune → inline annotation → post-process → retrieve)
  - Case for framework: it defines a new paradigm (interleave retrieval tokens within generation rather than prepend retrieval results) that could organize a family of sub-techniques
  - What makes this hard: the paper uses it as a named system/method designation with its own acronym, suggesting framework-level status, but the implementation is a single pipeline

- **data-commons-nl-interface** — candidate types: technique or framework
  - Case for technique: it is a pipeline (NLP components for variable/place/attribute extraction → query template matching → structured API call)
  - Case for framework: it provides the universal data-access abstraction that both RIG and RAG depend on, and is presented as an independent Google initiative
  - What makes this hard: it lives outside the paper's main contribution and is an upstream dependency whose classification would belong in a separate Data Commons ingest
