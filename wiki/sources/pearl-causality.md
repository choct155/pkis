---
title: "Causality: Models, Reasoning, and Inference (2nd ed.)"
knowledge_type: source
source_type: book
authors: ["Judea Pearl"]
year: 2009
domain: [causal-analysis, bayesian-stats, knowledge-representation]
tags: [causality, causal-inference, structural-causal-models, counterfactuals, bayesian-networks, interventions, identification]
isbn: "978-0-521-89560-6"
toc_source: "manual"
drive_id: "1M2uZzooDz_AAR3LT4UNBUmAk_nb5OMpW"
status: unread
date_added: 2026-05-20
date_updated: 2026-05-20
coverage: 1
---

Foundational monograph unifying probabilistic and causal reasoning through Structural Causal Models (SCMs). Pearl constructs a formal language for causal inference — the do-calculus — that bridges observational data, interventional experiments, and counterfactual reasoning. Central contribution: the Ladder of Causation (association → intervention → counterfactuals), which structures causal queries into three levels of increasing expressive power and shows what each level requires to answer.

## Key Knowledge Objects

- [[structural-causal-models]] — functional-equation DAGs; the book's central formal system linking probability, intervention, and counterfactuals
- [[do-calculus]] — three-rule interventional calculus for identifying causal effects from observational data
- [[d-separation]] — graphical criterion for reading off conditional independence from a DAG; Pearl's core contribution to Bayesian network theory
- [[counterfactuals]] — potential outcomes formalized via SCM: Y_x(u) = outcome of Y when X is set to x in unit u
- [[confounding]] — causal definition via back-door and front-door criteria; distinguishes from mere statistical association
- [[directed-graphical-models]] — probabilistic DAGs; Pearl's prior work; SCMs extend these to the interventional layer

## Key Extractions

1. **do-operator**: `P(Y | do(X=x))` is interventional distribution — fundamentally different from observational `P(Y | X=x)`. The do-operator formalizes the act of setting a variable by external intervention, severing its incoming edges in the graph.
2. **d-separation rules**: Chain (X→Z→Y blocked by Z), Fork (X←Z→Y blocked by Z), Collider (X→Z←Y unblocked only when conditioning on Z or its descendants). These three patterns determine all conditional independence relations implied by a DAG.
3. **Ladder of Causation**: Level 1 (Association) — seeing/observational; Level 2 (Intervention) — doing/do-calculus; Level 3 (Counterfactuals) — imagining/potential outcomes. Each level requires strictly more than the previous.
4. **Back-door criterion**: A set Z satisfies the back-door criterion for (X,Y) if it blocks all back-door paths from X to Y and contains no descendant of X — sufficient condition to identify causal effects from observational data as `P(Y | do(X=x)) = Σ_z P(Y | X=x, Z=z) P(Z=z)`.
5. **Simpson's paradox resolution**: Pearl shows the paradox dissolves when causal structure is made explicit — whether to aggregate or stratify depends on which variable is the confounder vs. the collider, not on any purely statistical criterion.

## Chapters

| # | Title | Stub |
|---|-------|------|
| 1 | Introduction to Probabilities, Graphs, and Causal Models | [[pearl-causality-ch01]] |
| 2 | A Theory of Inferred Causation | [[pearl-causality-ch02]] |
| 3 | Causal Diagrams and the Identification of Causal Effects | [[pearl-causality-ch03]] |
| 4 | Actions, Plans, and Direct Effects | [[pearl-causality-ch04]] |
| 5 | Causality and Structural Models in Social Science and Economics | [[pearl-causality-ch05]] |
| 6 | Simpson's Paradox, Confounding, and Collapsibility | [[pearl-causality-ch06]] |
| 7 | The Logic of Structure-Based Counterfactuals | [[pearl-causality-ch07]] |
| 8 | Imperfect Experiments: Bounding Effects and Counterfactuals | [[pearl-causality-ch08]] |
| 9 | Probability of Causation: Interpretation and Identification | [[pearl-causality-ch09]] |
| 10 | The Actual Cause | [[pearl-causality-ch10]] |
| 11 | Reflections, Elaborations, and Discussions with Readers | [[pearl-causality-ch11]] |
| — | Epilogue: The Art and Science of Cause and Effect | [[pearl-causality-epilogue]] |
