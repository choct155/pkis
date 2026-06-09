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
- causal-analysis
id: pkis:concept:causal-submodel
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- counterfactuals
related_concepts: []
sources:
- pearl-causality-ch07
specializes:
- structural-causal-models
tags:
- structural-causal-models
- do-operator
- interventions
- counterfactuals
- causality
title: Causal Submodel
understanding: 0
---

## Definition
The formal object (Pearl, Definition 7.1.2) that gives the do-operator and counterfactuals their semantics. Given a causal model $M = \langle U, V, F\rangle$, a set $X \subseteq V$, and a value $x$, the submodel $M_x$ is

$$M_x = \langle U, V, F_x\rangle, \qquad F_x = \{f_i : V_i \notin X\} \cup \{X = x\}.$$

That is, $F_x$ deletes the structural equations for the variables in $X$ and replaces them with the constant assignment $X = x$, leaving every other mechanism intact.

*Intuition:* an action is a minimal, local surgery on the assembly of mechanisms—respecify only the few equations the action perturbs, then let the rest run their natural course.

### Role in the framework
The effect of the action $do(X=x)$ is *defined* to be $M_x$ (Definition 7.1.3); the **potential response** $Y_x(u)$ is the solution for $Y$ in $F_x$; and the counterfactual "$Y$ would be $y$ had $X$ been $x$" is the equality $Y_x(u) = y$ (Definition 7.1.5). Because only mechanisms—not background conditions $U$—are altered, $x$ may contradict the actual value $X(u)$ without logical inconsistency, and abductive backtracking from the antecedent is suppressed.

### Why it matters
The submodel is the precise replacement for Lewis's vague "miracles": minisurgery instead of a similarity metric over possible worlds. It is the single device from which actions, causal effects, and counterfactuals are all derived, and it grounds the slogan that actions are *local in the space of mechanisms*, not in the space of variables. A degenerate submodel with $P(u)=1$ is a **causal world** $\langle M, u\rangle$ (Definition 7.1.2'), the atomic unit of a causal theory.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[structural-causal-models]] — specializes
- [[counterfactuals]] — prerequisite-of
[To be populated during integration]