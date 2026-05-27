---
id: "pkis:concept:homogeneous-risk-class"
aliases: []
title: "Homogeneous Risk Class"
knowledge_type: concept
also_type: [framework]
domain: [corporate-finance]
tags: [arbitrage, capital-structure, valuation, risk-classification]
related_concepts: [modigliani-miller-theorem, cost-of-capital, no-arbitrage-pricing, capital-structure-irrelevance]
sources: [modigliani-miller-cost-capital-1958]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: historical
---

## Definition

A homogeneous risk class is a set of firms whose earnings streams are perfectly correlated — differing only by a scalar multiple. Firms within the same class are perfect substitutes from an investor's perspective: they represent the same underlying economic risk packaged in different quantities. The risk class partitions the universe of firms into groups, and Modigliani and Miller prove their irrelevance propositions *within* a class, not across classes.

MM use the concept as the analog of the Marshallian industry: just as the perfectly competitive industry defines the competitive unit in product markets, the risk class defines the substitution set in capital markets. The no-arbitrage proof relies on the assumption that investors can freely substitute between firms in the same class, making leverage-based price discrepancies unsustainable — "homemade leverage" closes the gap.

## Type Ambiguity

The classification straddles concept and framework:

- **As a concept**: it names a property — identical-risk membership — that applies to firms and enables substitution. The definition is precise.
- **As a framework**: it provides the analytic apparatus within which Propositions I and II are proved. Without the risk-class partitioning, the arbitrage argument cannot be stated in its original 1958 form.

The `also_type: [framework]` flag captures this: the risk class is definitionally a concept but functions structurally as the organizing scaffold for MM's theory.

## Status in Modern Finance

Pagano (2005) calls the risk-class device "clumsy" — a scaffold that works for the 1958 proof but was superseded by the cleaner no-arbitrage pricing argument. Modern restatements of MM rely on the linearity of pricing operators: firm value equals the value of total cash flow regardless of how it is split between debt and equity. This formulation requires no partitioning of firms into risk classes. The concept is therefore historical infrastructure for the original proof rather than a live analytic tool.

## Connections

- [[modigliani-miller-theorem]] — prerequisite-of: the 1958 proof is stated within a risk class; the concept is a structural prerequisite for the original arbitrage argument
- [[no-arbitrage-pricing]] — uses: the arbitrage proof exploits perfect substitutability of firms within a risk class to rule out leverage-based price discrepancies
- [[cost-of-capital]] — uses: the capitalization rate ρ_k is defined at the level of the risk class, not the individual firm
- [[capital-structure-irrelevance]] — grounds: Proposition I holds because within-class firms are perfect substitutes regardless of leverage

## Reading Path

- [[modigliani-miller-cost-capital-1958]] (unread) — primary source; defines and deploys the concept throughout the proofs of Propositions I and II
