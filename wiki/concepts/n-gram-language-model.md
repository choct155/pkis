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
- deep-learning
- information-theory
id: pkis:concept:n-gram-language-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
specializes:
- language-model
tags:
- nlp
- markov
- language-model
- smoothing
title: N-gram Language Model
understanding: 0
uses:
- markov-chains
---

## Definition
A language model that factorizes the probability of a sequence using a Markov assumption: the probability of each word depends only on the n-1 preceding words, P(w_{1:N}) = prod_j P(w_j | w_{j-n+1:j-1}), giving unigram (n=1), bigram (n=2), and trigram (n=3) special cases. The full chain rule P(w_{1:N}) = prod_j P(w_j | w_{1:j-1}) is exact but intractable (a 40-word sentence over a 100,000-word vocabulary would need ~10^200 parameters); the n-gram approximation trades fidelity for estimability via corpus counts. N-grams may be defined over words or over characters (character-level models handle unknown words, agglutinative languages, and language identification at >99% accuracy). The model is atomic -- each word is a distinct symbol with no internal structure -- so it cannot generalize across syntactically or semantically similar words (it knows 'a black cat' only by having counted it, and misses the article-adjective-noun pattern). As n grows the model becomes more fluent but increasingly reproduces verbatim passages from training data rather than generating novel text. Practical n-gram models require handling unknown/out-of-vocabulary words (e.g. an <UNK> token) and smoothing of unseen n-grams.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-chains]] — uses
- [[language-model]] — specializes
[To be populated during integration]