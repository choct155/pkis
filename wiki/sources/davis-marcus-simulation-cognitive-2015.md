---
id: "pkis:source:davis-marcus-simulation-cognitive-2015"
aliases: []
title: "The Scope and Limits of Simulation in Cognitive Models"
authors: "Ernest Davis, Gary Marcus"
year: 2015
type: paper
domain: [symbolic-subsymbolic, knowledge-representation]
tags: [physical-reasoning, simulation, cognitive-models, intuitive-physics, commonsense-reasoning, bayesian-cognition, mental-models]
source_url: ""
drive_id: "1kxUhv40pk9M2Bgl-HSMsAavSB3lU4LHf"
drive_path: "PKIS/sources/papers/The Scope and Limits of Simulation in Cognitive Models - Davis, Marcus.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[intuitive-physics-engine]]", "[[noisy-newton-model]]", "[[qualitative-physical-reasoning]]", "[[mental-simulation]]"]
---

## Summary

Davis and Marcus argue against the strong "physics engine in the head" hypothesis — the proposal that human physical reasoning consists mainly of probabilistic simulation using approximately Newtonian mechanics ("noisy Newton" models). They examine two strands of cognitive science literature: (1) depictive models from the 1990s (Hegarty, Schwartz & Black) that study pulley systems and gear rotation, and (2) more recent probabilistic simulation models (Battaglia, Hamrick & Tenenbaum; Sanborn, Mansinghka & Griffiths; Smith & Vul) using towers of blocks and bouncing balls.

The paper identifies six inherent challenges to simulation as a cognitive mechanism: finding an appropriate physical model, choosing an appropriate idealization, rapid approximate inference, handling extra-physical information, dealing with incomplete information, and supporting tasks other than prediction. Beyond these inherent limitations, Davis and Marcus document that simulation-based theories are simultaneously too weak (they predict better performance than humans exhibit on many tasks, given the pervasive systematic errors in physical reasoning) and too strong (they cannot account for the wide variation in accuracy across tasks involving identical physics).

The authors propose that non-simulative mechanisms — qualitative reasoning, rule-based heuristics, analogy, causal reasoning, symbolic inference, and memory retrieval — are not optional supplements but central to human physical cognition. They conclude that if simulation plays any role, it is one component of a much larger heterogeneous cognitive system, and that setting up and interpreting a simulation itself requires non-simulative reasoning, making pure simulation models circular.

## Key Knowledge Objects

- [[intuitive-physics-engine]] (concept, high) — the hypothesis that humans reason about physical scenes using an approximate internal simulation similar to computational physics engines; the paper's central target
- [[noisy-newton-model]] (concept, high) — a specific probabilistic simulation framework positing that human physical reasoning follows Newtonian mechanics plus perceptual noise (sampling uncertainty)
- [[qualitative-physical-reasoning]] (concept, moderate — could be technique) — non-numerical, non-simulative inference about physical systems using rules, ordering, and topological constraints
- [[mental-simulation]] (concept, high) — the general class of cognitive processes involving constructing and running internal representations of dynamic scenarios; distinguished from strict physics-engine simulation

## Key Extractions

1. "Simulation-based theories of physical reasoning are both too weak and too strong. They are too weak in that there are many forms of physical reasoning that people carry out where simulation is either extremely inefficient or entirely inapplicable. They are too strong … because in many tasks they predict much higher levels of performance than people exhibit."

2. On systematic errors: tasks with well-documented errors include "predicting the trajectory of an object that has been moving in a circular path and is now released" (McCloskey 1983) and "drawing the predicted trajectory of bob on a pendulum that is cut" (Smith & Vul 2013) — the latter showing that drawing vs. bucket-placement tasks yield dramatically different accuracy despite identical physics.

3. On incomplete information: "If we are to solve this problem by probabilistic simulation [of an eel in a fish tank], we would need, first to understand how an eel swims, and second to simulate all kinds of possible motions … Clearly, this is not psychologically plausible."

4. "In many situations, the machinery of memory per se is too impoverished to yield clear answers, without significant support from other mechanisms" — critiquing memory-based simulation as an alternative.

5. On non-simulative alternatives: "Objects in a closed container remain in the container — a single simple rule suffices … [while] simulating the motion of the objects will become rapidly more complicated as the number of objects increases."

6. "If there is indeed a physics engine in the head, it is likely to be only a small part of a larger system that encompasses a wide range of additional cognitive processes, such as learning, memory-based reasoning, causal reasoning, qualitative reasoning, rule-based heuristics, analogy, and abstraction."

7. "Setting up and interpreting a simulation requires modes of physical reasoning that are not themselves simulation" — the circularity argument against pure simulation accounts.

## Connection Candidates

- [[directed-graphical-models]] — grounds: causal reasoning about physical scenes (identifying causes vs. effects) requires representations beyond simulation; Bayesian networks offer a complementary framework
- [[structural-causal-models]] — contrasts-with: noisy Newton models are probabilistic but non-causal; SCMs offer a richer causal structure for physical reasoning
- [[marcus-dl-critical-appraisal-2018]] — extends: this 2015 paper makes the same structural argument (simulation/deep learning is not enough; you need hybrid approaches) in the specific domain of physical reasoning
- [[neurosymbolic-ai]] — grounds: the paper's call for hybrid approaches combining simulation with qualitative/symbolic reasoning is a physical-reasoning motivation for neuro-symbolic AI
- intuitive-physics-engine (new node) — primary source introducing and critiquing this concept
