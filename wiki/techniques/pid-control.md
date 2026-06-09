---
aliases: []
also_type: []
applies:
- trajectory-tracking-control
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- robotics
- systems-theory
id: pkis:technique:pid-control
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- control
- feedback
- stability
title: PID Control
understanding: 0
---

## Definition
A feedback control law that sets the command as a sum of three terms in the tracking error e(t) = ξ(t) − q_t: proportional (K_P e, 'try harder the farther off you are'), integral (K_I ∫ e dt, 'try harder if you've made no progress for a long time', correcting systematic offsets), and derivative (K_D ė, 'try even harder if error is growing', adding damping). A pure P controller behaves like a spring and oscillates indefinitely without friction (stable but not strictly stable); adding the derivative term yields a PD controller that achieves strict stability; adding the integral term removes steady-state error from unmodeled forces. PID is the workhorse of industrial control. Computed torque control combines a model-based feedforward inverse-dynamics term with a PD feedback term whose gains scale with the configuration-dependent inertia matrix.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[trajectory-tracking-control]] — applies: PID corrects deviations between actual and reference state during tracking
[To be populated during integration]