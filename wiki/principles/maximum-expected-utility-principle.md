---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- agentic-systems
id: pkis:principle:maximum-expected-utility-principle
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch16
tags:
- decision-theory
- rationality
- utility
- rational-agent
- performance-measure
title: Maximum Expected Utility Principle
understanding: 0
---

## Definition
## Definition
The **principle of maximum expected utility (MEU)** states that a rational agent should choose the action that maximizes its expected utility:
$$ \text{action} = \arg\max_a EU(a), \qquad EU(a) = \sum_{s'} P(\text{RESULT}(a)=s')\,U(s'), $$
where $P(\text{RESULT}(a)=s') = \sum_s P(s)P(s'\mid s,a)$ folds the agent's uncertainty about its current state $s$ into uncertainty about the outcome $s'$, and $U(s')$ is the utility of the outcome. MEU is the basic principle of decision theory (R&N Section 16.1).

### Why MEU and not some other rule
MEU is not the *only* conceivable decision rule — one could maximize the weighted sum of cubes of utilities, or minimize the worst-case loss (minimax). MEU is singled out because it is the rule that, averaged over all environments consistent with the agent's percept history, achieves the highest expected score against the external **performance measure**. This is the central justification of MEU: it effects a transition from a *retrospective* performance measure applied to whole histories to an *internal* utility function applied to the very next state, so that it can guide action step by step. The von Neumann–Morgenstern axioms supply the complementary justification: an agent whose preferences satisfy them *must* act as if maximizing expected utility.

### A framework, not a solution
MEU formalizes the notion that an intelligent agent should "do the right thing" but does not operationalize it. Estimating $P(s)$ requires perception, learning, knowledge representation, and inference; computing $P(\text{RESULT}(a)=s')$ requires a causal world model; and computing $U(s')$ may itself require further search or planning. An agent acting for a human may not even know the true $U$. MEU therefore defines the AI problem rather than solving it.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- Uses expected-utility-theory as its underlying scoring rule.
- Realized computationally by the decision-network evaluation algorithm.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]