---
title: "Knowledge Graphs as a Source of Trust for LLM-Powered Enterprise Question Answering"
authors: "Juan Sequeda, Dean Allemang, Bryon Jacob"
year: 2025
type: paper
domain: [knowledge-representation, deep-learning]
tags: [knowledge-graphs, llm, question-answering, enterprise-data, owl, sparql, r2rml, explainability, trust, governed-data, knowledge-engineering, generative-ai]
source_url: "https://doi.org/10.1016/j.websem.2024.100858"
drive_id: "1nDWlbtYWuO4eKAKPwbFOR8gSHF_iXawh"
drive_path: "PKIS/sources/papers/Knowledge Graphs as a Source of Trust for LLM-Powered Enterprise Question Answering - Sequeda, Allemang, Jacob.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[knowledge-graph-question-answering]]", "[[knowledge-graph]]", "[[owl]]", "[[sparql]]", "[[r2rml]]", "[[llm-hallucination]]", "[[retrieval-augmented-generation]]", "[[neurosymbolic-ai]]"]
---

## Summary

**Extraction note**: The Drive file is a PDF of the ScienceDirect-hosted article, but the Drive MCP returned only the JavaScript-disabled landing page. The following summary is based on the abstract, keywords, journal metadata, and conceptual continuity with the companion benchmark paper (sequeda-kg-benchmark-llm-2023). Full body content is unread.

Published in Journal of Web Semantics, Volume 85 (May 2025), this position paper by Sequeda, Allemang, and Jacob argues against the view that Generative AI has rendered Knowledge Graphs and knowledge-based systems obsolete. Drawing on practical experience implementing enterprise question answering systems with LLMs, the authors make a three-part case for KGs as irreplaceable infrastructure: (1) KGs provide a formal framework for evaluating the validity of LLM-generated queries, (2) KGs serve as a foundation for explaining results to users, and (3) KGs offer access to governed and trusted data. This is a position paper that synthesizes industry experience and outlines a research agenda.

The paper is a follow-on to the companion benchmark paper (Sequeda, Allemang, Jacob 2023) that empirically demonstrated a 3x accuracy improvement when LLMs query over KG representations versus raw SQL schemas. Where the benchmark paper establishes the empirical case, this position paper frames the conceptual argument: the role of KGs is not to compete with LLMs but to provide the trust infrastructure — formal query validation, explainability scaffolding, and governed data access — that makes LLM-powered enterprise QA viable. Keywords include OWL, SPARQL, SQL, R2RML, knowledge engineering, confirming the paper operates within the same RDF/OWL/R2RML technical stack.

## Key Knowledge Objects

- [[knowledge-graph-question-answering]] (problem, high) — enterprise NL QA is the application domain; KGs provide the trust layer that makes LLM-generated query validation and result explainability possible
- [[knowledge-graph]] (concept, high) — KG as trust infrastructure for enterprise QA: formal query validation, explainability foundation, governed data access
- [[owl]] (framework, high) — OWL ontology as the formal schema enabling query validation against the enterprise data model
- [[sparql]] (technique, high) — SPARQL as the query language whose correctness against an OWL schema can be formally verified
- [[r2rml]] (technique, high) — R2RML mappings connecting SQL schemas to OWL ontologies; part of the KG trust infrastructure
- [[llm-hallucination]] (concept, high) — the core problem KG trust infrastructure addresses; KGs provide formal structure against which hallucinated queries can be detected
- [[retrieval-augmented-generation]] (technique, high) — KG-augmented enterprise QA is a structured form of RAG; the OWL ontology + KG provides verified, governed context
- [[neurosymbolic-ai]] (framework, high) — the paper's overall architecture — LLM generation constrained by KG formal validation — exemplifies neurosymbolic design

## Key Extractions

1. **Position**: Generative AI has not made KGs obsolete; rather, KGs provide the trust infrastructure that makes LLM-powered enterprise QA viable.

2. **Three KG roles in enterprise QA**: (a) formal framework for validating LLM-generated queries, (b) foundation for explainability of results, (c) access to governed and trusted data.

3. **Publication venue**: Journal of Web Semantics, Vol. 85 (May 2025); DOI: 10.1016/j.websem.2024.100858; Open access under CC BY-NC-ND 4.0.

4. **Keywords**: Knowledge Graph, LLM, Large Language Model, Generative AI, Question answering, Knowledge engineering, SPARQL, SQL, OWL, R2RML — confirming the paper builds on the same technical stack as the companion benchmark paper.

5. **Authors' affiliation**: data.world — same as the 2023 benchmark paper, confirming this is a continuation of the same research program.

**Note**: Body content (methodology, results, discussion sections) could not be extracted from the Drive PDF. The above extractions are from the abstract and paper metadata only.

## Connection Candidates

- [[knowledge-graph-question-answering]] — extends: this paper extends the companion benchmark paper's empirical accuracy argument into a conceptual framework about the three trust roles KGs play in enterprise QA
- [[sequeda-kg-benchmark-llm-2023]] — extends: this position paper is the conceptual follow-on to the 2023 benchmark; the benchmark provides empirical evidence that this paper interprets and frames
- [[owl]] — uses: OWL ontology as the formal validation schema for LLM-generated SPARQL; the formal semantics of OWL enable detection of query validity errors
- [[neurosymbolic-ai]] — uses: the paper exemplifies the neurosymbolic paradigm — neural generation (LLM) + symbolic validation (KG/OWL) — as the architecture for trustworthy enterprise QA
- [[llm-hallucination]] — grounds: KG formal structure provides the grounding mechanism that suppresses or detects LLM hallucinations in enterprise QA contexts
- [[retrieval-augmented-generation]] — extends: governed KG access is a principled form of RAG that adds formal validity checking and provenance beyond standard vector retrieval
- [[formal-ontology]] — uses: formal OWL ontology enables query validation — a capability impossible with informal schema representations like SQL DDL

## Awaiting Classification

- **llm-explainability in KG-QA context** — candidate types: concept or problem
  - Case for concept: explainability as a defined property of KG-grounded QA systems (what IS explainability in this context?)
  - Case for problem: the challenge of providing satisfying explanations for LLM-generated answers grounded in KG evidence
  - What makes this hard: the paper positions explainability as a KG affordance but without body access, the specific mechanism is unclear; the broader explainability concept already exists in the wiki under other sources but no dedicated node for KG-grounded explanation exists
