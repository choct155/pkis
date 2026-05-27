---
id: "pkis:concept:qualitative-physical-reasoning"
aliases: []
title: "Qualitative Physical Reasoning"
knowledge_type: concept
also_type: [technique]
domain: [symbolic-subsymbolic, knowledge-representation]
tags: [physical-reasoning, qualitative-reasoning, rules, heuristics, cognitive-models, commonsense-reasoning]
related_concepts: ["[[intuitive-physics-engine]]", "[[noisy-newton-model]]", "[[mental-simulation]]", "[[constraint-propagation]]"]
sources: ["[[davis-marcus-simulation-cognitive-2015]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Non-numerical, non-simulative inference about physical systems using qualitative categories (e.g., "faster," "heavier," "to the left"), ordering relations, topological constraints, and simple rule-based heuristics. Rather than computing precise trajectories, qualitative reasoning asks what direction an object moves, whether one container can hold another, or whether a structure is stable — questions answerable through symbolic rules and ordering constraints without running physics simulations. Davis and Marcus (2015) propose qualitative physical reasoning as one of several non-simulative mechanisms (alongside analogy, causal reasoning, and memory retrieval) that humans employ and that pure simulation accounts cannot explain. Classification note: assigned as concept (a defined theoretical category of reasoning) but also_type technique (a procedural methodology with a body of formal methods in AI).

## Reading Path
- [[davis-marcus-simulation-cognitive-2015]] (unread) — §4.3–4.4: presents qualitative reasoning as a central non-simulative alternative to physics-engine models; examples include container containment rules and support/stability reasoning that resist efficient simulation but yield to simple heuristics
