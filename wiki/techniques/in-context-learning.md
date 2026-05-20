---
title: "In-Context Learning"
knowledge_type: technique
also_type: [concept]
domain: [deep-learning]
tags: [llm, prompting, few-shot, chain-of-thought]
related_concepts: [graph-rag, neural-networks]
sources: ["[[zhang-graphrag-survey]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

A prompting strategy that elicits task-specific behavior from a frozen LLM by providing examples or structured instructions in the input context — without updating model weights — enabling few-shot and zero-shot generalization; in GraphRAG, used to integrate graph-retrieved knowledge via Graph-enhanced Chain-of-Thought and Collaborative KG Refinement.

Classification note: assigned as technique but may also be concept — as a *capability* of LLMs (their ability to generalize from in-context examples) it describes a property of the model, which is conceptual; as a *practice* (prompt design, example selection) it is procedural.
