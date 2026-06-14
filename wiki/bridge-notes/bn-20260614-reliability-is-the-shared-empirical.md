---
date_created: '2026-06-14'
id: pkis:bridge-note:bn-20260614-reliability-is-the-shared-empirical
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- coverage-driven-graph-traversal
- continuous-hardening-mixture-framework
- bn-20260613-the-existing-coveragepertoken-efficiency-formali
- bn-20260613-beyond-whether-a-concept-is
origin: conversation
proposed_edge_type: bridges
rationale: 'Reliability(τ) is the shared empirical primitive connecting coverage-driven
  traversal and the continuous hardening amortization framework.


  Formal definition:


  Reliability(τ) = E_{q, c1, c2}[I(q; c2 | c1, τ) − I(q; c2)]


  The lift in mutual information between query q and node c2 provided by knowing both
  the source node c1 and the edge type τ, averaged across all traversals of that edge
  type. Estimated empirically from traversal logs as average information gain lift
  per τ-typed traversal.


  Two roles in the architecture:


  Role 1 — Traversal ranking weight (Candidate A): Reliability(τ) is the base rate
  prior used to rank frontier candidates in R(F, S, q). High-reliability edge types
  are traversed by default; low-reliability types are traversed only when query signal
  warrants. This is the prospective use — Reliability(τ) informs the next traversal
  decision.


  Role 2 — Hardening rate signal (continuous hardening framework): λ(e, t) for an
  edge of type τ should be a function of accumulated Reliability(τ) evidence. High-reliability
  types harden faster because each traversal generates stronger evidence that τ is
  load-bearing. This is the retrospective use — Reliability(τ) calibrates confidence
  in the hardened edge.


  Critical separation: Reliability(τ) is a property of the edge type, not of the node
  content. It answers "should I traverse this edge?" — a relevance gate. It says nothing
  about how completely c2 covers the concept it represents once retrieved. That is
  the instantiation depth problem (H(c|node)), which is orthogonal and lives at the
  node level.


  Conflation risk: A scalar traversal outcome conflates both failure modes — τ was
  a poor relevance predictor, or τ was accurate but c2 was shallowly instantiated.
  Separating these requires the two-tier measurement strategy: traversal frequency
  gives a blended signal; periodic attribution analysis separates edge reliability
  from node instantiation quality.'
source_context: Conversation on Candidate B edge formalization — Reliability(τ) as
  bridge between traversal ranking and amortization hardening
status: unreviewed
title: Reliability(τ) — shared empirical primitive bridging traversal ranking and
  amortization hardening
---

## Connection
Reliability(τ) is the shared empirical primitive connecting coverage-driven traversal and the continuous hardening amortization framework.

Formal definition:

Reliability(τ) = E_{q, c1, c2}[I(q; c2 | c1, τ) − I(q; c2)]

The lift in mutual information between query q and node c2 provided by knowing both the source node c1 and the edge type τ, averaged across all traversals of that edge type. Estimated empirically from traversal logs as average information gain lift per τ-typed traversal.

Two roles in the architecture:

Role 1 — Traversal ranking weight (Candidate A): Reliability(τ) is the base rate prior used to rank frontier candidates in R(F, S, q). High-reliability edge types are traversed by default; low-reliability types are traversed only when query signal warrants. This is the prospective use — Reliability(τ) informs the next traversal decision.

Role 2 — Hardening rate signal (continuous hardening framework): λ(e, t) for an edge of type τ should be a function of accumulated Reliability(τ) evidence. High-reliability types harden faster because each traversal generates stronger evidence that τ is load-bearing. This is the retrospective use — Reliability(τ) calibrates confidence in the hardened edge.

Critical separation: Reliability(τ) is a property of the edge type, not of the node content. It answers "should I traverse this edge?" — a relevance gate. It says nothing about how completely c2 covers the concept it represents once retrieved. That is the instantiation depth problem (H(c|node)), which is orthogonal and lives at the node level.

Conflation risk: A scalar traversal outcome conflates both failure modes — τ was a poor relevance predictor, or τ was accurate but c2 was shallowly instantiated. Separating these requires the two-tier measurement strategy: traversal frequency gives a blended signal; periodic attribution analysis separates edge reliability from node instantiation quality.

## Nodes Involved
- [[coverage-driven-graph-traversal]]
- [[continuous-hardening-mixture-framework]]
- [[bn-20260613-the-existing-coveragepertoken-efficiency-formali]]
- [[bn-20260613-beyond-whether-a-concept-is]]

## Integration Notes
Pending review.