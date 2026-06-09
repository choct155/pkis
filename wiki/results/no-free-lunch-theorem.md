---
aliases: []
also_type: []
analogous-to:
- bias-variance-tradeoff
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:result:no-free-lunch-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch19
tags: []
title: No Free Lunch (No Representation Efficient for All Functions)
understanding: 0
---

## Definition
There is no representation -- and no learning algorithm -- that is efficient for all possible functions. The combinatorial root, as R&N present it: considering only Boolean functions of n Boolean attributes, the truth table has 2^n rows and each can independently output true or false, so there are 2^{2^n} distinct functions. With n=20 that is roughly 10^{300,000} functions; a million-bit representation cannot even name them all. Hence any compact representation (decision trees, polynomials, etc.) is concise for some functions and exponentially large for others -- decision trees, for instance, need exponentially many nodes for parity and majority functions.

The same fact appears in learning theory: with H the class of all Boolean functions, for any set of N observed examples the consistent hypotheses split evenly between those predicting the next example positive and those predicting it negative, so observing data tells you nothing about unseen inputs. Real generalization therefore requires restricting (biasing) the hypothesis space, accepting the risk of excluding the true function. This is the formal underpinning of why inductive bias is not optional but necessary for learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bias-variance-tradeoff]] — analogous-to
[To be populated during integration]