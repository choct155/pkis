---
aliases: []
also_type: []
applies:
- value-of-information
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- agentic-systems
- bayesian-stats
id: pkis:principle:off-switch-deference
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch16
tags:
- ai-safety
- decision-theory
- value-of-information
- corrigibility
- human-ai-collaboration
- deference
title: Off-Switch Deference Under Preference Uncertainty
understanding: 0
---

## Definition
## Definition
The **off-switch deference** result states that a machine that is *uncertain about the human's utility function* has a positive incentive to let the human switch it off, rather than acting unilaterally — and this incentive vanishes exactly when the machine becomes certain of the human's preferences (R&N Section 16.7.2, adapted from Hadfield-Menell et al., 2017; central to Russell's 2019 framework for beneficial AI).

### The off-switch game
Robot Robbie can (a) act now on a plan whose value $u$ to human Harriet is uncertain (prior density $P(u)$), (b) switch itself off (value 0), or (c) defer: explain the plan and let Harriet switch it off or approve it. A rational Harriet approves iff $u>0$. Comparing the value of acting versus deferring:
$$ EU(a)=\int_{-\infty}^{\infty}\!P(u)\,u\,du, \qquad EU(d)=\int_{0}^{\infty}\!P(u)\,u\,du, $$
so $EU(d)\ge EU(a)$ because deferring *zeroes out the negative-utility region*. Equality holds only when $P(u<0)=0$ — i.e. the machine is already certain Harriet approves.

### Why it matters
The incentive is a direct instance of the nonnegativity of the **value of information**: Harriet's switch-off decision is informative about her preferences precisely when the machine is uncertain. Elaborations: charging a cost for Harriet's time makes the robot less eager to interrupt; allowing for human *error* makes the robot less willing to defer to an irrational human (it should not let a toddler switch off a self-driving car mid-highway). The result formalizes a *corrigibility* incentive arising endogenously from preference uncertainty rather than imposed by hand.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[value-of-information]] — applies: the deference incentive is the nonnegative value of the human's switch-off decision
- A direct application of the nonnegative value of information.
- Motivated by uncertainty over the human's utility (a gap in expected-utility theory's usual assumption of a known U).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]