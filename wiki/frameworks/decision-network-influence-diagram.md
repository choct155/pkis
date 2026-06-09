---
aliases: []
also_type: []
applies:
- maximum-expected-utility-principle
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
contrasts-with:
- decision-tree-analysis
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- agentic-systems
extends:
- bayesian-networks
id: pkis:framework:decision-network-influence-diagram
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch16
tags:
- decision-theory
- graphical-models
- bayesian-networks
- utility
- rational-agent
title: Decision Network (Influence Diagram)
understanding: 0
---

## Definition
## Definition
A **decision network** (Howard and Matheson's **influence diagram**, 1984) is a graphical formalism that extends a Bayesian network with two additional node types so as to represent and solve a decision problem (R&N Section 16.5):
- **Chance nodes** (ovals): random variables with conditional distributions indexed by their parents; parents may include decision nodes.
- **Decision nodes** (rectangles): points where the agent chooses an action.
- **Utility nodes** (diamonds): the agent's utility function, with all outcome-affecting variables as parents.

It provides the substrate for a utility-based agent: it captures the current state, possible actions, resulting state, and outcome utility in one diagram.

### Two forms
The general form has explicit outcome-state chance nodes feeding the utility node. A **simplified (action-utility) form** omits those future-state nodes and connects the utility node directly to current-state and decision nodes; it then represents the **action-utility function** $EU(a)$ — the reinforcement-learning **Q-function**. Because outcome-state nodes describe future states they can never be set as evidence, so the simplified form is always usable where the general form is, though it is less flexible to changing circumstances.

### Evaluation algorithm
To choose an action: (1) set the evidence variables for the current state; (2) for each value of the decision node, set it (it now behaves like an evidence chance node), run standard probabilistic inference to get the posterior over the utility node's parents, and compute the resulting utility; (3) return the highest-utility action. Shachter (1986) gave a method operating directly on the network without expanding the exponential decision tree.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[decision-tree-analysis]] — contrasts-with: decision networks avoid building the exponential decision tree
- [[maximum-expected-utility-principle]] — applies: network evaluation implements MEU as inference
- [[bayesian-networks]] — extends: decision networks add decision and utility nodes to a Bayesian network
- Extends Bayesian networks with decision and utility nodes.
- Implements the maximum-expected-utility principle as an inference procedure.
- Its action-utility form is the Q-function used in reinforcement learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]