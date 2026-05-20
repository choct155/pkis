# PKIS Wiki Log

## [2026-05-20] ingest | GraphRAG / KR / Neurosymbolic cluster (6 papers)
- Created wiki/sources/: banf-tripartite-graphrag, barron-legal-rag-nmf, cheng-cograg, hamilton-graphsage, baldazzi-soft-ontological-reasoning, liu-symagent
- Created stubs: [[node-embedding]] (concept), [[inductive-representation-learning]] (technique), [[graph-sage]] (technique), [[neurosymbolic-ai]] (framework), [[ontology-reasoning]] (technique), [[non-negative-matrix-factorization]] (technique), [[knowledge-graph-question-answering]] (problem)
- Updated existing nodes: [[graph-rag]] (coverage 2→5), [[retrieval-augmented-generation]] (coverage 2→6), [[knowledge-graph]] (coverage 2→5), [[multi-hop-reasoning]] (coverage 1→4), [[graph-neural-networks]] (coverage 1→2), [[knowledge-graph-construction]] (coverage 1→3), [[agentic-systems]] (coverage 1→2)

## [2026-05-20] ingest | Variational Inference cluster (4 papers)
- Created wiki/sources/: ganguly-intro-vi, sjolund-parametric-vi, yellapragada-variational-bayes, blei-vi-review
- Created stubs: [[variational-inference]] (technique+framework), [[elbo]] (concept), [[mean-field-approximation]] (technique), [[variational-autoencoder]] (technique+framework), [[amortized-inference]] (technique), [[reparameterization-trick]] (technique), [[coordinate-ascent-vi]] (technique), [[stochastic-vi]] (technique), [[normalizing-flows]] (technique), [[kl-divergence]] (concept), [[bayesian-neural-networks]] (concept), [[intractable-posterior]] (problem)
- Updated existing nodes: [[em-algorithm]] (coverage 3→8), [[gaussian-mixture-models]] (coverage 1→3), [[directed-graphical-models]] (coverage 2→3)

## [2026-05-20] ingest | Bayesian forecasting / macroeconometrics / time-series cluster (7 papers)
- Created wiki/sources/: duncan-mskf-seemingly-unrelated-1993, steel-bma-forecasting-2011, scott-varian-nowcasting-2013a, sargent-sims-business-cycle-1977, lee-structural-breaks-2007, stock-watson-leading-indicators-1992, scott-varian-bsts-2014
- Created stubs: [[kalman-filter]] (technique), [[bayesian-model-averaging]] (technique), [[spike-and-slab]] (technique), [[structural-time-series]] (framework), [[state-space-models]] (framework), [[var-models]] (framework), [[dynamic-factor-models]] (framework), [[structural-breaks]] (concept), [[nowcasting]] (problem)
- Introduced domain tags: time-series, forecasting
- Updated existing nodes: [[model-selection-problem]] (coverage 1→2), [[bayesian-linear-regression]] (coverage 1→3), [[em-algorithm]] (coverage 2→3 per agent; merged in VI update above)

## [2026-05-20] ingest | Model selection / rule ensembles / structured matrices / Bayesian computation cluster (4 papers)
- Created wiki/sources/: castle-model-selection-algorithms (paper), friedman-rulefit-2005 (paper), benzi-hidden-structure-matrices (book) + ch01–ch05, tanner-tools-statistical-inference (book) + ch01–ch06
- Created stubs: [[information-criteria]] (concept), [[general-to-specific-modeling]] (technique), [[model-averaging]] (technique+framework), [[rule-ensembles]] (technique), [[partial-dependence]] (technique), [[structured-matrices]] (concept), [[tensor-decompositions]] (technique), [[hierarchical-low-rank-matrices]] (concept), [[toeplitz-matrices]] (concept), [[data-augmentation]] (technique), [[gibbs-sampler]] (technique), [[metropolis-algorithm]] (technique), [[importance-sampling]] (technique), [[laplace-approximation]] (technique)
- Updated existing nodes: [[model-selection-problem]] (coverage 2→3), [[bias-variance-tradeoff]] (coverage 2→3, also fixed duplicate related_concepts key), [[gradient-boosting]] (coverage 1→2), [[decision-trees]] (coverage 1→2), [[lasso]] (coverage 1→2), [[ensemble-learning]] (coverage 2→4), [[matrix-decompositions]] (coverage 1→2), [[singular-value-decomposition]] (coverage 1→2)

## [2026-05-20] ingest | A Few Useful Things to Know About Machine Learning (Domingos, 2012)
- Created wiki/sources/domingos-useful-things.md (Drive ID: 1bCkseO06512PFQyuBevRIAPy8BU3APCc)
- Created concept stub: [[inductive-bias]] (high) — no free lunch; the knowledge lever
- Created technique stub: [[feature-engineering]] (high) — most important factor in ML project success
- Updated existing nodes: [[bias-variance-tradeoff]] (sources +1, coverage 1→2, Reading Path added), [[curse-of-dimensionality]] (sources +1, coverage 1→2, Reading Path added), [[ensemble-learning]] (sources +1, coverage 1→2, Reading Path added), [[empirical-risk-minimization]] (sources +1, coverage 1→2, Reading Path added, related_concepts expanded)
- No chapter stubs (paper, not book); source added directly to queue as Normal
- Updated: wiki/index.md, wiki/queue.md

## [2026-05-20] ingest | Causality: Models, Reasoning, and Inference (Pearl, 2009)
- Created wiki/sources/pearl-causality.md (Drive ID: 1PK_71YU0x1o_j9uTCjYhgDdTY7crj4Pi)
- Created framework stub: [[structural-causal-models]] (high) — functional-equation DAGs; book's central formal system
- Created technique stubs: [[do-calculus]] (high, also_type: result), [[d-separation]] (high, also_type: result)
- Created concept stubs: [[counterfactuals]] (high), [[confounding]] (high)
- Updated existing node: [[directed-graphical-models]] (sources +1, coverage 1→2, Reading Path added, related_concepts expanded)
- Created 12 chapter stubs: [[pearl-causality-ch01]] through [[pearl-causality-ch11]] and [[pearl-causality-epilogue]] (toc_source: manual)
- Introduced first entries in `causal-analysis` domain
- Note: OpenLibrary had no ToC for this ISBN; Google Books 429; ToC extracted from PDF via read_file_content
- Updated: wiki/index.md, wiki/queue.md

## [2026-05-20] ingest | Agentic Design Patterns (Gullí, 2025)
- Created wiki/sources/gulli-agentic-design-patterns.md (Drive ID: 1BRC09kdXT7AtbhsUrTBTsRanXWw2Yx41)
- Created framework stubs: [[agentic-systems]] (high, also_type: concept), [[multi-agent-systems]] (high, also_type: technique)
- Created technique stubs: [[prompt-chaining]] (high), [[tool-use]] (high), [[human-in-the-loop]] (moderate, also_type: principle)
- Updated existing nodes: [[retrieval-augmented-generation]] (sources +1, coverage 1→2, Reading Path added), [[graph-rag]] (sources +1, coverage 1→2, Reading Path added)
- Created 29 chapter stubs: [[gulli-agentic-design-patterns-ch01]] through [[gulli-agentic-design-patterns-ch29]] (toc_source: manual)
- Note: Google Books returned 429; OpenLibrary returned 404 (book too new); ToC extracted directly from PDF via read_file_content
- Updated: wiki/index.md, wiki/queue.md

## [2026-05-20] toc-enrichment | Chapter stub source files for ESL and MML
- Created 18 chapter stubs: [[hastie-esl-ch01]] through [[hastie-esl-ch18]] (toc_source: manual)
- Created 12 chapter stubs: [[deisenroth-mml-ch01]] through [[deisenroth-mml-ch12]] (toc_source: manual)
- Updated [[hastie-esl]] and [[deisenroth-mml]]: `## Chapters` tables now use wikilinks; `toc_source: "manual"` set
- Updated wiki/index.md: 30 chapter stubs added to Sources section
- Updated wiki/queue.md: all chapter references updated to chapter-level wikilinks

## [2026-05-20] schema-update | Reading status, ToC enrichment, Reading Path convention
- Updated SCHEMA.md: added `isbn`, `toc_source`, `parent_book`, `chapter` to source entry template; added `## Reading Path Convention` section
- Updated LIBRARIAN.md: Step 2 now creates individual chapter stub source files with ToC API enrichment (OpenLibrary/Google Books by ISBN); Step 3 frontmatter template updated; Step 4 stubs now include `## Reading Path`; updated existing nodes now append to `## Reading Path`
- Updated SYNTHESIZER.md: Mode 1 Step 1 now includes reading gap check before deepening; `## Reading Path` section added to all 6 deepening templates
- Added `isbn` and `toc_source` fields to `wiki/sources/hastie-esl.md` (ISBN: 978-0-387-84857-0) and `wiki/sources/deisenroth-mml.md` (ISBN: 978-1-108-47004-9)
- Chapter stub source files and ToC enrichment for existing books are pending (next ingest session)

## [2026-05-20] ingest | A Survey of Graph Retrieval-Augmented Generation for Customized Large Language Models (Zhang et al.)
- Created wiki/sources/zhang-graphrag-survey.md (Drive ID: 1HNUSufv7AQek6Qcl6Js5AFXxQ5lf3vpg)
- Created technique stubs: [[retrieval-augmented-generation]] (high, also_type: framework), [[graph-rag]] (high, also_type: framework), [[graph-neural-networks]] (high), [[knowledge-graph-construction]] (high), [[in-context-learning]] (moderate, also_type: concept)
- Created concept stub: [[multi-hop-reasoning]] (high)
- Updated existing node: [[knowledge-graph]] (sources list, coverage 1→2)
- Updated: wiki/index.md, wiki/queue.md

## [2026-05-20] ingest | A Brief Survey of Methods for Analytics over RDF Knowledge Graphs (Papadaki, Tzitzikas, Mountantonakis)
- Created wiki/sources/papadaki-rdf-analytics-survey.md (paper-level entry, 6 sections cataloged)
- Created concept stubs: [[knowledge-graph]] (high, also_type: framework), [[rdf]] (high, also_type: framework), [[linked-open-data]] (high)
- Created technique stubs: [[sparql]] (high), [[olap]] (high, also_type: framework), [[faceted-search]] (moderate)
- Introduced first entries in `knowledge-representation` domain
- Key contribution: 5-category taxonomy (C1-C5) of RDF analytics approaches; two query categories (domain-specific A, quality-related B)
- Copied source to PKIS/sources/papers/ in Drive (ID: 1YPg3QWPUsEdauty_2akC_aNZR_ln6Kt7)
- Updated: wiki/index.md

## [2026-05-20] ingest | The Elements of Statistical Learning (Hastie, Tibshirani, Friedman)
- Created wiki/sources/hastie-esl.md (book-level entry, 18 chapters cataloged)
- Created concept stubs: [[bias-variance-tradeoff]] (high), [[regularization]] (high), [[curse-of-dimensionality]] (high)
- Created technique stubs: [[lasso]] (high), [[gradient-boosting]] (high), [[random-forests]] (high), [[support-vector-machines]] (high, also_type: framework), [[cross-validation]] (high), [[em-algorithm]] (high)
- Created framework stubs: [[ensemble-learning]] (moderate, also_type: concept)
- Created problem stubs: [[model-selection-problem]] (moderate, also_type: concept)
- Introduced new domain tag: `statistical-learning`
- Updated: wiki/index.md, wiki/queue.md
- Queue: 5 chapter-level reading items added (2 High, 3 Normal)

## [2026-05-20] ingest | Mathematics for Machine Learning (Deisenroth, Faisal, Ong)
- Created wiki/sources/deisenroth-mml.md (book-level entry, 12 chapters cataloged)
- Graduated tags to concept nodes: [[linear-algebra]], [[analytic-geometry]], [[matrix-decompositions]], [[vector-calculus]], [[probability-theory]], [[gaussian-distribution]], [[conjugate-prior]], [[continuous-optimization]], [[convex-optimization]]
- Created technique stubs: [[singular-value-decomposition]] (high, also_type: result), [[eigendecomposition]] (high, also_type: result), [[automatic-differentiation]] (high), [[gradient-descent]] (high), [[lagrange-multipliers]] (high, also_type: result), [[bayesian-linear-regression]] (high), [[gaussian-mixture-models]] (high, also_type: framework)
- Created framework stubs: [[empirical-risk-minimization]] (high), [[directed-graphical-models]] (high)
- Updated existing nodes: [[backpropagation]] (coverage 1→2, new related_concepts), [[principal-component-analysis]] (coverage 1→2, new related_concepts), [[support-vector-machines]] (coverage 1→2, new related_concepts), [[em-algorithm]] (coverage 1→2)
- Copied source to PKIS/sources/books/ in Drive (ID: 1pd0ziFWZBYPaAGefEewmYZqhGcD5udYV)
- Updated: wiki/index.md, wiki/queue.md

## [2026-05-20] ingest-update | ESL — additional stubs
- Created technique stubs: [[neural-networks]] (high, also_type: framework), [[backpropagation]] (high), [[logistic-regression]] (high), [[decision-trees]] (high), [[principal-component-analysis]] (high)
- Created framework stub: [[undirected-graphical-models]] (high)
- Updated wiki/sources/hastie-esl.md concepts list and Key Knowledge Objects
- Updated: wiki/index.md
