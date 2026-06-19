---
aliases: []
authors: Herbert A. Simon
concepts:
- '[[bounded-rationality]]'
- '[[satisficing]]'
- '[[evocation-attention]]'
- '[[programmed-vs-unprogrammed-decisions]]'
- '[[decision-premise]]'
date_added: 2026-05-20
domain:
- organizational-theory
drive_id: 1GbkhgO-n6zKerFY6X53ocdVgfqRM83iL
drive_path: PKIS/sources/papers/Administrative Decision Making.pdf
id: pkis:source:simon-admin-decision-making-1965
source_url: ''
status: unread
tags:
- bounded-rationality
- satisficing
- decision-theory
- operations-research
- heuristics
- computer-simulation
- organizational-behavior
title: Administrative Decision Making
type: paper
year: 1965
---

## Summary

Reprinted from *Public Administration Review* (Vol. XXV, No. 1, March 1965), this paper by Herbert Simon surveys twenty-five years of progress in the scientific study of administrative decision making, presenting findings from what would today be called behavioral organization theory and cognitive science. Simon surveys three main developments.

First, operations research and management science have formalized large classes of administrative decisions using tools like linear programming, queuing theory, dynamic programming, and combinatorial mathematics — enabling optimal solutions where well-structured problems can be precisely specified. However, Simon notes that real-world decision environments are often too complex for classical rationality: the information costs and computational demands of true optimization are prohibitive.

Second, he distinguishes heuristic (satisficing) methods from optimizing techniques. Heuristic approaches grapple with the need to design and discover alternatives (not just choose among given ones), accept "good-enough" solutions when optimal solutions are unknowable, and cannot guarantee solution quality. The satisficing concept — settling for a solution meeting an aspiration level rather than maximizing — is Simon's core contribution to behavioral decision theory.

Third, Simon introduces the distinction between persuasion and evocation in organizational influence. Persuasion concerns changing what premises a decision-maker holds; evocation concerns activating latent premises already held. Timing, attention, and institutional structure shape whose premises get evoked — a finding confirmed by Bauer, Pool, and Dexter's study of congressional voting on trade legislation.

The paper also introduces the decision-premise metaphor (drawing from earlier AI/computer-science thinking): each organizational member takes premises as inputs and produces conclusions/decisions as outputs, which become premises for others. Computer simulation is offered as a new tool for constructing and testing theories of organizational decision making.

## Key Knowledge Objects

- [[bounded-rationality]] (concept, high) — Simon's foundational concept: real decision makers operate under constraints on information, attention, and computation; classical rationality is descriptively false
- [[satisficing]] (concept, high) — choosing the first alternative that meets an aspiration threshold rather than exhaustively searching for the global optimum
- [[decision-premise]] (concept, moderate — could be concept or technique) — the metaphor of decisions as conclusions drawn from premises, where organizational influence works by shaping which premises are activated
- [[evocation-attention]] (concept, high) — organizational influence via activating latent decision premises already held by the actor, as distinguished from persuasion (changing premises)
- [[programmed-vs-unprogrammed-decisions]] (concept, high) — the distinction between well-structured, repetitive decisions amenable to algorithmic treatment and ill-structured, novel decisions requiring judgment and creativity

## Key Extractions

1. "A normative theory, to be useful, must call only for information that can be obtained and only for calculations that can be performed. The classical theory of rational choice has generally ignored these information-processing limitations."
2. Heuristic methods differ from optimizing methods in three respects: they must design/discover alternatives (not just choose); they satisfice rather than optimize; they cannot guarantee solution quality.
3. "We can view each member of an organization as 'inputting' certain premises, and 'outputting' certain conclusions, or decisions. But each member's conclusions become, in turn, the inputs, that is to say, the premises, for other members."
4. On evocation vs. persuasion: "When we want someone to carry out a particular action, we may think of our task as one of inducing him to accept latent decision premises favorable to the action that he already possesses." Bauer et al.'s trade study shows institutional structure shapes which premises get evoked.
5. "The modern digital computer... has provided both a language for expressing our theories of decision making and an engine for calculating their empirical implications." Early simulations of department store buyers and bank trust officers demonstrated feasibility.
6. Simon distinguishes the normative theory (how to make better decisions) from the descriptive science (how decisions are actually made), advocating progress on both simultaneously.

## Connection Candidates

- [[gavetti-behavioral-theory-firm-2012]] (source) — Gavetti builds directly on the Simon/Cyert/March tradition; this paper is a primary source for the bounded-rationality and behavioral-theory foundations Gavetti updates
- [[markov-decision-processes]] (framework) — MDPs are the formal framework for sequential decision making under uncertainty that emerged partly from the operations research tradition Simon surveys here; Simon's emphasis on heuristics anticipates challenges that MDP-based planning still faces in high-dimensional state spaces
- [[agentic-systems]] (framework) — Simon's framing of organizational members as information processors taking premises as inputs and producing decisions as outputs is an intellectual precursor to modern architectures of autonomous agents
- [[multi-agent-systems]] (framework) — the premise-passing model of organizational decision making is structurally similar to multi-agent coordination via message passing
- [[identification-strategy]] (concept) — Simon's discussion of computer simulation as a theory-testing tool raises identification questions: how do we know a simulation model is correct?
- [[coase-nature-firm-1937]] (source) — Coase's theory of the firm and Simon's theory of organizational decision making are complementary: Coase explains why organizations exist; Simon explains how they make decisions internally
