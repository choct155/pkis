---
id: "pkis:concept:knowledge-infused-learning"
aliases: []
title: "Knowledge-Infused Learning"
knowledge_type: concept
also_type: [technique]
domain: [symbolic-subsymbolic, deep-learning]
tags: [neurosymbolic, process-knowledge, end-to-end-differentiable, domain-knowledge, safety, explainability]
related_concepts: [neurosymbolic-ai, knowledge-graph, system-1-system-2-thinking]
sources: ["[[sheth-neurosymbolic-why-2023]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

Knowledge-Infused Learning (KiL / PKiL — Process Knowledge-Infused Learning) is a neurosymbolic approach that encodes domain-specific process knowledge (workflows, constraint specifications, diagnostic models) as trainable map functions applied to raw data, converting it to concepts in an expert-defined domain model; the full pipeline is end-to-end differentiable, enabling joint optimization of perception, concept mapping, and constrained response generation.

Classification note: assigned as concept (the named paradigm with a definition) but also_type technique because PKiL is operationally a procedure with specific architectural steps.

## Reading Path
- [[sheth-neurosymbolic-why-2023]] (unread) — introduces PKiL as category 2(b) intertwined NSAI; mental health diagnostic application achieving 70% expert satisfaction vs. 47% for LLMs
