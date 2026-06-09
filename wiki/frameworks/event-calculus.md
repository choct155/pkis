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
- discrete-event-systems
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
id: pkis:framework:event-calculus
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch10
specializes:
- upper-ontology-categories-objects
tags:
- event-calculus
- fluents
- reified-events
- temporal-reasoning
- actions
- situation-calculus
- first-order-logic
- frame-problem
title: Event Calculus
understanding: 0
uses:
- temporal-interval-logic
---

## Definition
Event calculus (Kowalski & Sergot, 1986) is a first-order formalism for reasoning about actions, events, and change over continuous time, designed to overcome the limitations of successor-state axioms in domains with continuous, simultaneous, or extended-duration actions. Its objects are **events**, **fluents** (reified facts whose truth can change, e.g. At(Shankar, Berkeley)), and **time points**.

## Core predicates
- T(f, t1, t2): fluent f is true throughout the interval [t1, t2]
- Happens(e, t1, t2): event e occurs from t1 to t2
- Initiates(e, f, t) / Terminates(e, f, t): event e makes fluent f true / false at t
- Initiated / Terminated (existential over an intervening initiating/terminating event)
- t1 < t2: temporal ordering of time points

A distinguished Start event sets the initial state. Persistence axioms (analogous to successor-state axioms) say a fluent retains its value across an interval if no intervening event changed it.

## Key moves
- **Reification of events** as objects (E1 ∈ Flyings ∧ Flyer(E1, Shankar) …) allows arbitrary extra information to be attached (Bumpy(E1)) — impossible with fixed-arity event predicates, which do not scale.
- **Physical objects as generalized events**: an object is a chunk of space–time (USA as an event begun in 1776); state fluents (Population(USA), President(USA)) describe changing properties, using a function Equals inside T rather than logical identity (which cannot change over time).
- Extends to simultaneous, exogenous, continuous, and nondeterministic events.

## Relation to other formalisms
Alternative to situation calculus and to the fluent calculus (Thielscher); James Allen's interval algebra arose for the same reason. Closely tied to Davidson's philosophical analysis of events.

## Reading Path
- [[russell-norvig-aima-ch10]] — §10.3: events, processes, time intervals, fluents, objects as space–time chunks

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[discrete-event-systems]] — contrasts-with: both model events over time; event calculus is a logical KR formalism, DES a state-transition systems-theory model
- [[temporal-interval-logic]] — uses: event calculus reasons over time points and Allen interval relations
- [[upper-ontology-categories-objects]] — specializes: events/time are the event-calculus portion of the upper ontology; objects are generalized events
[To be populated during integration]