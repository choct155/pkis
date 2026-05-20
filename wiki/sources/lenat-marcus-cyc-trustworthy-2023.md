---
title: "Getting from Generative AI to Trustworthy AI: What LLMs Might Learn from Cyc"
authors: "Doug Lenat, Gary Marcus"
year: 2023
type: paper
domain: [symbolic-subsymbolic, knowledge-representation]
tags: [neurosymbolic, cyc, common-sense-reasoning, trustworthy-ai, higher-order-logic, llm-limitations, knowledge-base, confabulation, theory-of-mind, defeasibility]
source_url: "https://arxiv.org/abs/2308.04445"
drive_id: "1c-IKCuH9Wi476zDYtUsYW_8D5hCaP3NR"
drive_path: "PKIS/sources/papers/Getting from Generative AI to Trustworthy AI - What LLMs Might Learn from Cyc - Lenat, Marcus.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[neurosymbolic-ai]]", "[[cyc-knowledge-base]]", "[[common-sense-reasoning]]", "[[trustworthy-ai]]", "[[higher-order-logic-reasoning]]", "[[defeasibility]]"]
---

## Summary

This paper by Lenat and Marcus articulates a 16-desiderata framework for trustworthy general AI, then describes how the Cyc knowledge base system addresses these limitations. The core diagnosis is that LLMs are "untrustworthy, unstable, and brittle" because they are "trained to be plausible, but not necessarily correct" — lacking genuine understanding of knowledge, reasoning, and world models. The 16 desiderata cover: explanation/provenance, deduction, induction, analogy, abductive reasoning, theory of mind, quantifier-fluency, modal-fluency, defeasibility (belief revision), pro/con argumentation, contextual reasoning, meta-knowledge/meta-reasoning, explicit ethics, calibrated uncertainty, creative problem solving, and learning from experience. Against these criteria, the paper describes Cyc's approach: a curated knowledge base of millions of rules of thumb and common-sense facts, expressed in CycL (a higher-order logic), with an inference engine that provides step-by-step proofs with full provenance. The catch acknowledged is the expressiveness-tractability tradeoff: higher-order logic inference is slow, so Cyc uses partitioned contexts (microtheories) and heuristic theorem proving to achieve real-time reasoning without sacrificing expressivity. The paper concludes that any truly trustworthy general AI must hybridize LLMs (for perception, language, scalability) with formal knowledge systems (for reliable reasoning, provenance, and correctness). The paper is notable for being co-authored by the principal architect of Cyc and a prominent LLM critic.

## Key Knowledge Objects

- [[neurosymbolic-ai]] (framework, high) — paper argues for LLM+formal-knowledge hybrid as the path to trustworthy NSAI
- [[cyc-knowledge-base]] (framework, high) — Cyc: curated KB with millions of common-sense rules; CycL higher-order logic; microtheory contexts
- [[common-sense-reasoning]] (concept, high) — the type of broad, everyday knowledge and inference that LLMs lack and Cyc explicitly encodes
- [[trustworthy-ai]] (concept, moderate — could be principle) — 16-desiderata framework for evaluating AI trustworthiness
- [[defeasibility]] (concept, high) — belief revision under new information; default-true conclusions that may need retraction
- [[higher-order-logic-reasoning]] (technique, high) — Cyc's inference in higher-order logic with heuristic partitioning for real-time execution
- [[microtheory-contexts]] (concept, high) — Cyc's partitioned context structure enabling localized reasoning within domain-specific sub-theories
- [[expressiveness-tractability-tradeoff]] (principle, high) — the fundamental tension: richer logic is slower to reason with; Cyc partially overcomes this via microtheories

## Key Extractions

1. **LLM limitation diagnosis**: "The underlying problem is that LLMs understand too little about the nearly limitless richness of how the world works... it mostly comes down to knowledge, reasoning, and world models, none of which is well handled within Large Language Models."
2. **Expressiveness-tractability tradeoff**: "If the logical language is expressive enough to fully represent the meaning of anything we can say in English, then the inference engine runs much too slowly. That's why symbolic AI systems typically settle for some fast but much less expressive logic, such as knowledge graphs."
3. **Defeasibility requirement**: "Much of what one hears, reads, says, believes, and reasons with is only true by default... To be trustworthy, an AI needs to be able to assimilate new information and revise its earlier beliefs and earlier answers."
4. **Hybrid path forward**: "We suggest that any trustworthy general AI will need to hybridize the approaches, the LLM approach and more formal approach." LLMs provide scalable perception; formal KB provides reliable reasoning with provenance.
5. **Context/microtheory architecture**: Cyc uses microtheories (contextual partitions) so that reasoning can stay within the relevant context, avoiding the combinatorial explosion of unrestricted higher-order reasoning.

## Connection Candidates

- [[neurosymbolic-ai]] — uses: Cyc+LLM hybrid is positioned as the concrete implementation path for trustworthy NSAI
- [[common-sense-reasoning]] — uses: Cyc's KB explicitly encodes the common-sense knowledge LLMs cannot reliably acquire from text
- [[knowledge-graph]] — contrasts-with: knowledge graphs are noted as "fast but much less expressive" than full HOL; Cyc goes further with CycL
- [[defeasibility]] — uses: defeasible reasoning (default-true conclusions, belief revision) is one of the 16 desiderata
- [[expressiveness-tractability-tradeoff]] — grounds: the tradeoff motivates Cyc's architectural design (microtheories, heuristic theorem proving)
- [[formal-ontology]] — extends: Cyc's CycL is a significantly richer knowledge representation than standard description-logic ontologies
