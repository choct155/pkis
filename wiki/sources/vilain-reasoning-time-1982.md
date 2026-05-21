---
title: "A System for Reasoning About Time"
authors: "Marc B. Vilain"
year: 1982
type: paper
domain: [knowledge-representation]
tags: [temporal-reasoning, interval-algebra, constraint-propagation, qualitative-reasoning, ai-planning, consistency-maintenance]
source_url: ""
drive_id: "1S_lHdg5bMEUaJf70ZVPA1lslFsKxOe3H"
drive_path: "PKIS/sources/papers/A System for Reasoning About Time.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[interval-algebra]]", "[[constraint-propagation]]", "[[temporal-interval-logic]]"]
---

## Summary

This 1982 AAAI proceedings paper describes one of the earliest formal computational systems for temporal reasoning. Vilain proposes representing time primarily in terms of intervals (rather than time points, which were common in prior systems such as Bruce 1972 and Kahn & Gorry 1977), with relations between intervals described by a logic of 13 primitive relational operators. These 13 primitives cover all possible ways two intervals can be related: before/after, during/contains, begins/begun-by, ends/ended-by, overlaps/overlapped-by, and equals. Relational vectors (disjunctions over primitives) represent partial knowledge about interval relationships.

The system performs deductions through constraint propagation: given that interval A relates to B by R1, and B to C by R2, composition rules derive A's relation to C. This is formalized as a semiring-like algebraic structure over relational vectors, enabling transitive closure computation in polynomial time (O(n³), attributed to Kleene). The system maintains consistency using a technique inspired by Doyle's (1978) truth maintenance systems and Kahn & Gorry's time specialist — when contradictions are detected, the system backtracks and isolates the exact set of mutually inconsistent assertions.

The paper also extends the interval logic to handle time points (defined as boundaries of intervals), with additional primitive relations for point-point, point-interval, and interval-point relationships. Finally, it describes a method for handling absolute dates by mapping calendar assertions to generated time points, unifying dated and undated information under the same constraint propagation mechanism. This work is a direct predecessor to Allen's (1983) more comprehensive interval temporal logic, which Vilain explicitly anticipates.

## Key Knowledge Objects

- [[interval-algebra]] (framework, high) — a formal system for representing and reasoning about temporal relationships between intervals using 13 primitive relations and composition rules; precursor to Allen's interval algebra
- [[constraint-propagation]] (technique, high) — a computational method for maintaining consistency and deducing new information by applying composition rules transitively across a network of known relations
- [[temporal-interval-logic]] (concept, moderate — could be framework) — the logic of interval-based temporal relations; this paper presents an early version; the concept straddles concept (a formal language) and framework (an organizing system for temporal reasoning)

## Key Extractions

1. "The system represents time primarily — though not exclusively — in terms of intervals, and performs deductions on this representation. It has a mechanism for maintaining consistency in the representation and discovering the origin of inconsistencies."

2. The 13 primitive interval relations are: before/after, during/contains, begins/begun-by, ends/ended-by, overlaps/overlapped-by, equals. "The relational primitives can be joined into relational vectors; a relational vector describes a composite relation between two time intervals."

3. "The rules are used to define the composition properties of the primitive relations of the logic; there is thus one composition rule for each pair of primitive relations (169 rules in total)."

4. "The composition rules [can be formulated] in terms of a multiplication and an addition over relation vectors. These operations, along with the appropriate identity elements, define an algebraic structure over relation vectors that is very close to being a semiring. The resemblance to a semiring is sufficiently good that we can compute the transitive closure operation using a modification of a polynomial time algorithm … operating in n³ time and n² space."

5. On consistency maintenance: "Whenever a new set of assertions is added by the user, the transitive closure operation is recomputed. During this operation, the system monitors partial computations to discover contradictions. If one is found, the system … backtracks … and isolates the exact set of mutually inconsistent assertions."

6. Absolute dates are handled by "mapping them into the logic of intervals and points … generating a time point to correspond to the date … The system performs this automatically by simply adding a few new statements to its store of assertions." This obviates the need for separate mechanisms for dated vs. undated information.

## Connection Candidates

- [[temporal-logic]] — extends: this paper provides a computational realization of interval-based temporal logic; it extends the concept by providing an inference system and consistency maintenance mechanism
- [[constraint-propagation]] — uses: the core deduction mechanism is constraint propagation over a semiring of relational vectors; this node should link to or from the technique node
- [[directed-graphical-models]] — contrasts-with: interval algebra uses constraint networks rather than probabilistic graphical models; both are formalisms for reasoning about relational structure, but with different semantics
- [[discourse-representation-theory]] — prerequisite-of: temporal interval reasoning of this kind underlies temporal semantics in DRT; DRT's temporal reference system draws on interval-based reasoning
