---
id: "pkis:source:forbus-qp-motion-1982"
aliases: []
title: "Modeling Motion with Qualitative Process Theory"
authors: "Kenneth D. Forbus"
year: 1982
type: paper
domain: [knowledge-representation, symbolic-subsymbolic]
tags: [qualitative-reasoning, naive-physics, physical-simulation, common-sense-reasoning, symbolic-ai, knowledge-representation, process-theory, oscillators]
source_url: ""
drive_id: "1fgXRoYGemfUNkNgjmm_cf9qnoW5zHmNq"
drive_path: "PKIS/sources/papers/Modeling Motion with Qualitative Process Theory.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[qualitative-process-theory]]", "[[qualitative-reasoning]]", "[[naive-physics]]", "[[quantity-spaces]]", "[[qualitative-simulation]]"]
---

## Summary

This AAAI-82 paper by Forbus at MIT AI Lab presents Qualitative Process Theory (QP theory) as an alternative to Qualitative State representations for modeling motion in naive physics. The problem: prior qualitative simulation approaches (de Kleer's Qualitative States) model motion via symbolic states linked by simulation rules, but struggle with compound systems (continuously interacting objects) and questions requiring richer notions of process and time — such as determining whether a pumped oscillator will exhibit stable behavior (limit cycle existence). QP theory extends the ontology of common-sense physical models by introducing the concept of a *physical process* (flowing, boiling, stretching) as the primary causal agent of change. A process is specified by five parts: *individuals* (entities the process acts between), *preconditions* (non-physics conditions for activation), *quantity conditions* (physics-deducible conditions for activation), *relations* (relationships holding when active), and *influences* (descriptions of quantity changes). Quantities consist of an amount and a derivative, each with sign and magnitude. The *Quantity Space* is a partially ordered set of numbers and quantities that constrains possible values qualitatively. The paper demonstrates QP theory by analyzing a spring-mass oscillator to (1) derive the process history (sequences of processes), and (2) determine limit cycle existence for a pumped-with-friction oscillator — the latter being a qualitative proof of what requires non-linear differential equations analytically. The paper shows that Qualitative States can be derived as a compiled, simplified special case of QP theory, establishing QP as the more fundamental representation.

## Key Knowledge Objects

- [[qualitative-process-theory]] (framework, high) — QP theory: formal ontology for physical processes, quantities, and causal relations; Forbus's foundational contribution
- [[qualitative-reasoning]] (concept, high) — reasoning about physical systems using symbolic, order-of-magnitude representations rather than numerical simulation
- [[naive-physics]] (concept, high) — Hayes's program of formalizing everyday physical knowledge; QP theory as a contribution to the naive physics program
- [[quantity-spaces]] (concept, high) — partially ordered collections of values (numbers and quantities) defining the qualitative state of a system
- [[qualitative-simulation]] (technique, high) — envisionment: deriving all qualitatively possible states and transitions from initial conditions
- [[limit-analysis]] (technique, moderate — could be concept) — QP theory's procedure for determining what process changes (new processes starting/stopping) can occur

## Key Extractions

1. **Process definition**: "A process is specified by five parts: individuals (descriptions of entities the process acts between), preconditions (statements that must be true for the process to act, but not deducible solely within QP theory), quantity conditions (statements that must be true for the process to act, but are deducible within QP theory), relations (the relationships between the individuals which hold when the process is active), influences (descriptions of what quantities are affected)."
2. **Causal primacy of processes**: "A principle tenet of QP theory is that only processes cause changes, so only processes impose influences."
3. **Quantity representation**: A quantity consists of an amount and a derivative, each with sign (positive, negative, zero) and magnitude. Quantity Spaces are partially ordered, primarily determined by the domain's process vocabulary.
4. **Qualitative States as special case**: Qualitative State representations of motion can be derived by "compiling" the QP limit analysis onto a motion vocabulary that includes kinematic information — making QP theory the more fundamental representation.
5. **Limit cycle proof**: For a pumped oscillator with friction, QP theory derives that there exists a unique E(stable) such that the oscillator's energy converges to it regardless of initial conditions — a qualitative proof of limit cycle existence and stability.

## Connection Candidates

- [[qualitative-process-theory]] — uses: this paper introduces and instantiates QP theory for the domain of motion
- [[qualitative-reasoning]] — uses: QP theory is a formal system for qualitative physical reasoning
- [[naive-physics]] — extends: QP theory contributes a process-based ontology to the naive physics program
- [[common-sense-reasoning]] — uses: motion and physical processes are a core domain of common-sense knowledge
- [[formal-ontology]] — specializes: QP theory is a domain-specific formal ontology for physical processes and quantities
- [[neurosymbolic-ai]] — grounds: qualitative reasoning provides the historical symbolic foundation that modern NSAI seeks to combine with neural learning

## Awaiting Classification

- **limit-analysis** — candidate types: technique or concept
  - Case for technique: limit analysis is a procedure applied to QP descriptions to derive possible state transitions
  - Case for concept: it is also a theoretical notion about the structure of QP change-event analysis
  - What makes this hard: Forbus uses it as both a named procedure and a conceptual property of QP theory
