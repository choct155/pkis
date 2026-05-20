---
title: "Logical Neural Networks"
knowledge_type: technique
also_type: []
domain: [symbolic-subsymbolic, deep-learning]
tags: [neurosymbolic, first-order-logic, weighted-logic, bidirectional-inference, truth-bounds, ibm]
related_concepts: [neurosymbolic-ai, logic-tensor-networks, kautz-nsai-taxonomy]
sources: ["[[wan-cognitive-ai-nsai-survey-2023]]", "[[gibaut-nsai-taxonomy-survey-2023]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: evolving
---

Logical Neural Networks (LNN, IBM) are a neurosymbolic framework where every neuron has a meaning as a component in a weighted real-valued logic formula; instead of point truth values, neurons maintain bounds (lower/upper) on truth values for each grounding, and inference is performed bidirectionally — supporting both forward deduction and backward constraint propagation simultaneously.

## Reading Path
- [[wan-cognitive-ai-nsai-survey-2023]] (unread) — profiled as Neuro:Symbolic→Neuro (Type 4); bidirectional dataflow causes high data-movement overhead
- [[gibaut-nsai-taxonomy-survey-2023]] (unread) — detailed treatment of truth bounds, FOL quantifiers, and comparison with LTN
