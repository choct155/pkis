---
id: "pkis:source:sheth-neurosymbolic-why-2023"
aliases: []
title: "Neurosymbolic AI - Why, What, and How"
authors: "Amit Sheth, Kaushik Roy, Manas Gaur"
year: 2023
type: paper
domain: [symbolic-subsymbolic, deep-learning, knowledge-representation]
tags: [neurosymbolic, survey, knowledge-graphs, explainability, safety, lowering-lifting, system-1-system-2, mental-health]
source_url: ""
drive_id: "17sbLqL3RS8grc6JUdaOL6pEnXHHs-b0g"
drive_path: "PKIS/sources/papers/Neurosymbolic AI - Why, What, and How - Sheth, Roy, Gaur.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[neurosymbolic-ai]]", "[[knowledge-graph]]", "[[system-1-system-2-thinking]]", "[[knowledge-infused-learning]]", "[[lowering-lifting-taxonomy]]"]
---

## Summary

This IEEE article by University of South Carolina's AI Institute introduces and overviews the neurosymbolic AI paradigm from a three-part framing: Why (motivations), What (definitions), and How (methods). The "Why" draws on Kahneman's System 1/System 2 distinction — neural networks model System 1 (fast pattern recognition), while symbolic AI is needed for System 2 (deliberative cognition, reasoning, planning, analogy). The "What" proposes a two-category taxonomy with four sub-categories: (1) Structured Knowledge Compression (lowering) — compressing knowledge graphs or formal logic for integration with neural patterns, and (2) Neural Pattern Lifting — extracting structure from neural outputs for mapping back to symbolic knowledge. The paper rates each approach on algorithm-level features (large-scale perception, abstraction, analogy, planning) and application-level features (user-explainability, domain constraints, scalability, continual adaptation). The "How" highlights that end-to-end differentiable intertwined integration (category 2b, exemplified by Process Knowledge-infused Learning / PKiL) achieves high marks across all dimensions and demonstrates a concrete mental health diagnostic application achieving 70% expert satisfaction vs. 47% with pure LLMs. The paper concludes that knowledge graphs — being dynamic, standards-based, and scale-amenable — are the preferred symbolic structure for future neurosymbolic architectures.

## Key Knowledge Objects

- [[neurosymbolic-ai]] (framework, high) — primary subject; lowering/lifting taxonomy and application-level analysis
- [[knowledge-graph]] (concept, high) — recommended as the preferred symbolic structure for future neurosymbolic systems; dynamic and scalable
- [[system-1-system-2-thinking]] (concept, high) — Kahneman's dual-process model as motivating cognitive framework for NSAI
- [[knowledge-infused-learning]] (technique, high) — PKiL: process knowledge infused as trainable map functions to domain concepts
- [[lowering-lifting-taxonomy]] (concept, high) — the paper's two-category taxonomy distinguishing knowledge compression (lowering) from pattern lifting
- [[knowledge-graph-embedding]] (technique, moderate — could be concept) — KGE as one method for compressing knowledge into neural representations

## Key Extractions

1. **Lowering vs. lifting**: "Methods that compress structured symbolic knowledge to integrate with neural patterns and reason using the integrated neural patterns" (lowering) vs. "methods that extract information from neural patterns to allow for mapping to structured symbolic knowledge (lifting) and perform symbolic reasoning."
2. **KG preferred over formal logic**: "Unlike static and brittle symbolic logics, such as first-order logic, [knowledge graphs] are easy to update. In addition to their suitability for enterprise-use cases and established standards for portability, knowledge graphs are part of a mature ecosystem."
3. **PKiL superiority**: End-to-end differentiable methods (category 2b) score high on all four application-level features: user-explainability (H), domain constraints (H), scalability (H), continual adaptation (H). LLM federated pipelines score: L, M, H, L.
4. **Mental health empirical result**: PKiL-based system for suicidality assessment achieved 70% expert satisfaction vs. 47% for OpenAI's text-Davinci-003 federated pipeline.
5. **Safety via symbolic structure**: "Guidelines, policy, and regulations can be encoded via extended forms of knowledge graphs and hence symbolic means, which in turn can provide explainability accountability, rigorous auditing capabilities, and safety."

## Connection Candidates

- [[neurosymbolic-ai]] — extends: adds the lowering/lifting taxonomy and application-level evaluation framework
- [[knowledge-graph]] — uses: KGs as the recommended symbolic structure; positions KGs as superior to formal logic for practical NSAI
- [[system-1-system-2-thinking]] — grounds: System 1/2 provides the cognitive-science justification for the neural-symbolic split
- [[formal-ontology]] — contrasts-with: formal logic/ontology is characterized as "static and brittle" compared to dynamic KGs
- [[sheth-neurosymbolic-why-2023]] — commonly-confused-with: Sheth taxonomy (lowering/lifting) vs. Kautz taxonomy (6 types) — both classify NSAI but by different structural criteria
