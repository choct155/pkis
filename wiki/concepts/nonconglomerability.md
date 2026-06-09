---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:nonconglomerability
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch15
tags:
- jaynes
- de-finetti
- infinite-sets
- weighted-average
- paradox
- finite-additivity
title: Conglomerability and Nonconglomerability
understanding: 0
---

## Definition
Following de Finetti (1972), a probability P(A|I) is **conglomerable in a partition** {C_i} of mutually exclusive, exhaustive propositions if it lies within the bounds of the conditional probabilities it averages: if L <= P(A|C_i I) <= U for all i, then L <= P(A|I) <= U. For a finite partition this is the elementary theorem that a weighted average of real numbers cannot lie outside their range, since the sum/product rules give P(A|I) = sum_i P(A|C_i I) P(C_i|I). **Nonconglomerability** is the claimed violation of this bound.

## Jaynes's resolution
Jaynes argues nonconglomerability is not a phenomenon of probability theory but an artifact of violating the finite-sets policy: it cannot arise from a correct finite-set calculation, and therefore cannot occur in any infinite set approached as a well-defined limit of finite sets. The standard manufacturing recipe (e.g. the uniform rectangular MxN array; Kadane-Schervish-Seidenfeld 1986) passes to M,N -> infinity *first*, then evaluates conditional probabilities by counting directly on the infinite set ('infinitely many points where A holds, finitely many where it fails, ergo P=1'). The same fallacy produces opposite nonconglomerabilities from a single partition merely by relabeling indices, and it discards the crucial ratio R = M/N on which the unconditional probability actually depends. Done correctly (arithmetic on finite sets, limit last), the bounds are always respected. Jaynes regards 'nonconglomerability' and 'finite additivity' as red herrings concealing the real issue: whether uniform probability distributions on infinite sets are admitted as legitimate objects.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]