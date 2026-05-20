# PKIS Wiki Log

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
