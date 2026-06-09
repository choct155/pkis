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
- optimization
- knowledge-representation
id: pkis:concept:evaluation-function-games
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch05
tags:
- adversarial-search
- games
- heuristic
- cutoff-test
- quiescence
- horizon-effect
title: Heuristic Evaluation Function (Games)
understanding: 0
---

## Definition
A function EVAL(s,p) that estimates the expected utility (probability-of-winning-related value) of a nonterminal game state s to player p, used to cut off game-tree search before reaching terminal states when the full tree is too large to explore. It replaces UTILITY in heuristic minimax: H-MINIMAX(s,d) applies EVAL when a *cutoff test* IS-CUTOFF(s,d) fires (true for all terminal states, otherwise free to stop based on depth or state properties), recursing with depth+1 otherwise. A good EVAL must (i) be cheap to compute, (ii) be strongly (not necessarily linearly) correlated with the actual chances of winning, and (iii) satisfy UTILITY(loss,p) <= EVAL(s,p) <= UTILITY(win,p), agreeing with UTILITY at terminal states. Conceptually, features partition states into equivalence categories whose value is the expected outcome over win/draw/loss proportions; in practice this is approximated by a *weighted linear function* EVAL(s) = sum_i w_i f_i(s) over features f_i (e.g. chess material: pawn 1, knight/bishop 3, rook 5, queen 9; king safety; pawn structure), with weights normalized into [0,1]. Linear combination assumes feature independence, so strong programs add nonlinear terms (e.g. a bishop pair, or a bishop worth more in the endgame). Two characteristic pathologies: the *quiescence* problem -- EVAL should be applied only to quiescent positions with no pending swing (e.g. an imminent capture), so the cutoff test continues searching through nonquiescent positions via a *quiescence search* restricted to e.g. captures; and the *horizon effect* -- an unavoidable loss can be pushed past the search depth by delaying tactics, partially countered by *singular extensions*. Search reaches expert play at ~14 ply (alpha-beta + transposition tables) and grandmaster play with tuned EVAL plus endgame databases; opening books and retrograde-computed endgame tables replace search where lookup is feasible.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]