---
id: "pkis:problem:data-hunger"
aliases: []
title: "Data Hunger"
knowledge_type: problem
also_type: []
domain: [deep-learning]
tags: [sample-efficiency, generalization, few-shot-learning, inductive-bias, training-data]
related_concepts: ["[[inductive-bias]]", "[[transfer-learning]]", "[[compositionality]]"]
sources: ["[[marcus-dl-critical-appraisal-2018]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

The problem that deep learning systems require massive amounts of labeled training data to achieve good performance, contrasting sharply with human ability to learn abstract relationships from one or a few examples. Marcus (2018) argues that humans learn novel concepts (e.g., defining "schmister" as a sister aged 10-21) from a single example and generalize immediately, while deep learning requires thousands to millions of examples. Even 7-month-old infants can acquire abstract language-like rules in two minutes from unlabeled data. Data hunger reflects the absence of strong inductive biases (like the algebraic mind's variable-binding and rule-generalization capacities) that evolution built into human cognition.

## Reading Path
- [[marcus-dl-critical-appraisal-2018]] (unread) — §3.1 develops the data hunger argument with the "schmister" example and infant rule learning experiments; contrasts with Lake et al.'s human-level concept learning from one example
