---
title: "Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents"
authors: "Thanh Luong Tuan"
year: 2026
type: paper
domain: [symbolic-subsymbolic, knowledge-representation]
tags: [neurosymbolic, ontology, enterprise-ai, llm, agentic-systems, formal-semantics, compliance, hallucination]
source_url: ""
drive_id: "1K5uMwgNXq3VZ1cRLxmw1a9h-kUKy71Rs"
drive_path: "PKIS/sources/papers/Ontology constrained neural reasoning.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[neurosymbolic-ai]]", "[[formal-ontology]]", "[[agentic-systems]]", "[[asymmetric-neurosymbolic-coupling]]", "[[ontology-reasoning]]"]
---

## Summary

This paper presents a neurosymbolic architecture implemented within the Foundation AgenticOS (FAOS) platform, designed to address LLM limitations in enterprise settings — hallucination, domain drift, and inability to enforce regulatory compliance at the reasoning level. The core contribution is a three-layer ontological framework (Role, Domain, and Interaction ontologies) that provides formal semantic grounding for LLM-based enterprise agents. The key concept introduced is *asymmetric neurosymbolic coupling*: symbolic ontological knowledge constrains agent inputs (context assembly, tool discovery, governance thresholds) while the paper proposes mechanisms for extending this to constrain agent outputs (response validation, reasoning verification, compliance checking). An empirical evaluation across 600 runs in five industry verticals (FinTech, Insurance, Healthcare, Vietnamese Banking, Vietnamese Insurance) demonstrates that ontology-coupled agents significantly outperform ungrounded agents on Metric Accuracy, Regulatory Compliance, and Role Consistency. Performance improvements are greatest where LLM parametric knowledge is weakest — specifically in Vietnam-localized domains. The work contributes a formal enterprise ontology model, a taxonomy of neurosymbolic coupling patterns, and empirical evidence for ontology-grounding as a practical engineering solution to LLM unreliability in regulated domains.

## Key Knowledge Objects

- [[neurosymbolic-ai]] (framework, high) — general neurosymbolic paradigm; this paper contributes an enterprise-specific architecture
- [[formal-ontology]] (concept, high) — ontologies serve as semantic constraints on agent inputs and outputs
- [[asymmetric-neurosymbolic-coupling]] (concept, high) — novel concept: symbolic knowledge constrains neural inputs asymmetrically relative to outputs
- [[agentic-systems]] (framework, high) — LLM-based enterprise agents operating under ontological constraints
- [[ontology-reasoning]] (technique, high) — ontological reasoning applied to constrain and validate agent behavior
- [[knowledge-graph-completion]] (low — technique or problem?) — KG completion as background context for domain ontology maintenance

## Key Extractions

1. **Asymmetric coupling defined**: "Symbolic ontological knowledge constrains agent inputs (context assembly, tool discovery, governance thresholds) while proposing mechanisms for extending this coupling to constrain agent outputs (response validation, reasoning verification, compliance checking)."
2. **Three-layer ontology**: Role ontology (agent identity and responsibilities), Domain ontology (domain-specific knowledge and vocabulary), Interaction ontology (communication protocols and governance rules).
3. **Empirical results**: Ontology-coupled agents outperform ungrounded agents on Metric Accuracy (p < .001, W = .460), Regulatory Compliance (p = .003, W = .318), and Role Consistency (p < .001, W = .614) across 600 controlled runs.
4. **Domain gap finding**: Performance improvements are greatest in Vietnam-localized domains (Vietnamese Banking, Vietnamese Insurance), where LLM parametric knowledge is scarcest — supporting the hypothesis that ontological grounding is most valuable when neural memorization cannot substitute for explicit structured knowledge.
5. **Coupling taxonomy**: The paper proposes a systematic taxonomy of neurosymbolic coupling patterns distinguishing input-side vs. output-side ontological constraints, anticipating future work on bidirectional coupling.

## Connection Candidates

- [[neurosymbolic-ai]] — extends: contributes a specific enterprise architecture and asymmetric coupling taxonomy to the general neurosymbolic framework
- [[formal-ontology]] — uses: ontologies are the core symbolic component, constraining agent context and outputs
- [[agentic-systems]] — uses: the paper's FAOS architecture instantiates agentic design patterns with ontological grounding
- [[ontology-reasoning]] — uses: ontological reasoning enforces compliance and role consistency at inference time
- [[baldazzi-soft-ontological-reasoning]] — contrasts-with: both use ontologies to constrain neural components, but Baldazzi focuses on KG/Datalog chase while this focuses on enterprise agent workflows
- [[description-logic]] — prerequisite-of: formal semantics of the ontology layers rely on DL foundations

## Awaiting Classification

- **knowledge-graph-completion** — candidate types: technique or problem
  - Case for technique: KGC methods (embedding, rule mining) are procedures applied to extend incomplete KGs
  - Case for problem: KGC is the motivating challenge that underlies graph reasoning research
  - What makes this hard: the source treats KGC implicitly as a background maintenance task, not a primary focus — insufficient warrant for a confident assignment here
