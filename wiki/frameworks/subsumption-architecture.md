---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
contrasts-with:
- motion-planning
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- robotics
id: pkis:framework:subsumption-architecture
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
specializes:
- robotics-decision-making
tags:
- robotics
- reactive-control
- finite-state-machine
- behavior-based
title: Subsumption Architecture (Reactive Robot Control)
understanding: 0
---

## Definition
A framework (Brooks, 1986) for building reactive robot controllers by composing augmented finite state machines (AFSMs)—finite state machines whose nodes test sensor variables, whose arcs emit messages to motors or other machines, and which carry internal clocks (the 'augmentation'). Controllers are assembled bottom-up: low-level reflexes (e.g., per-leg gait control for a hexapod, with a simple rule to retract-lift-retry when a leg is blocked) are layered under higher-level behaviors like collision avoidance. This reflex-agent (reactive) approach often succeeds where deliberative configuration-space planning fails—e.g., walking a 18-DOF hexapod over rough terrain with poor sensors. Its weaknesses: AFSMs driven by raw sensor input cannot integrate information over time, fixed wiring makes goal-switching hard, and complex conditional policies (e.g., nuanced highway merging) do not scale, motivating the deliberative–reactive debate.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[robotics-decision-making]] — specializes: the reactive (reflex-agent) pole of the deliberative-vs-reactive design space
- [[motion-planning]] — contrasts-with: reactive AFSM control vs deliberative configuration-space planning; succeeds where planning is intractable (high-DOF rough terrain)
[To be populated during integration]