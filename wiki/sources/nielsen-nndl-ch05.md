---
id: "pkis:source:nielsen-nndl-ch05"
aliases: []
title: "Ch. 5 — Why are deep neural networks hard to train?"
authors: "Michael A. Nielsen"
year: 2015
type: book-chapter
domain: [deep-learning, optimization]
tags: [vanishing-gradient, exploding-gradient, sigmoid, training-dynamics]
drive_id: "1OvaRAM8W_QPmYOVaeZDMVbNTBBI-7txZ"
drive_path: "PKIS/sources/books/Neural Networks and Deep Learning"
parent_book: "[[nielsen-nndl]]"
chapter: 5
status: unread
date_added: 2026-05-20
concepts:
  - "[[vanishing-gradient-problem]]"
  - "[[backpropagation]]"
---

Diagnoses the vanishing gradient problem in deep networks: because gradients involve products of bounded sigmoid derivatives (≤1/4) and small weights, early-layer gradients shrink exponentially with depth, causing early layers to learn far slower than later ones.
