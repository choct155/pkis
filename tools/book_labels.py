#!/usr/bin/env python3
"""Shared labeling helpers for book/chapter source nodes.

Single source of truth for the `[ABBREV Author]` title tag used by both the
bulk migration (relabel_books.py) and the ingest generator (book_setup.py),
so the naming convention can't drift between them.

Title format produced:
    book:    [ITILA MacKay] Information Theory, Inference, and Learning Algorithms
    chapter: [ITILA MacKay] Ch. 29 — Monte Carlo Methods

Author stand-in rule:  1 -> surname; 2 -> "A & B"; 3+ -> "First et al".
"""

# slug -> book abbreviation. Keep in sync when ingesting a new book (or pass an
# explicit `abbrev` to title_prefix / the book_setup config).
ABBREV = {
    "mackay-itila": "ITILA",
    "bishop-prml": "PRML",
    "gelman-bda3": "BDA3",
    "hastie-esl": "ESL",
    "russell-norvig-aima": "AIMA",
    "goodfellow-deeplearning": "DLB",
    "murphy-pml1-intro": "PML1",
    "murphy-pml2-advanced": "PML2",
    "deisenroth-mml": "MML",
    "jaynes-probability": "PTLoS",
    "nielsen-nndl": "NNDL",
    "cunningham-causal-inference-mixtape": "Mixtape",
    "resnick-stochastic-processes": "ASP",
    "allemang-semantic-web": "SWWO",
    "cimiano-ontology-nlp": "OBI",
    "cassandras-des-intro": "DES",
    "carrell-groups-matrices-vectors": "GMVS",
    "benzi-hidden-structure-matrices": "HSMC",
    "kroese-statistical-modeling": "SMC",
    "lange-applied-probability": "AppProb",
    "tanner-tools-statistical-inference": "TSI",
    "gulli-agentic-design-patterns": "ADP",
    "pearl-causality": "Causality",
    "sutton-reinforcement-2018": "RL",
}


def _author_list(authors):
    """Normalize a frontmatter authors value (YAML list or comma string) to names."""
    if isinstance(authors, (list, tuple)):
        names = [str(a).strip() for a in authors]
    else:
        names = [a.strip() for a in str(authors or "").split(",")]
    return [n for n in names if n]


def _surname(name):
    parts = name.strip().split()
    return parts[-1] if parts else name.strip()


def short_author(authors):
    """1 author -> surname; 2 -> 'A & B'; 3+ -> 'First et al'."""
    names = _author_list(authors)
    if not names:
        return ""
    if len(names) == 1:
        return _surname(names[0])
    if len(names) == 2:
        return f"{_surname(names[0])} & {_surname(names[1])}"
    return f"{_surname(names[0])} et al"


def abbrev_for(slug, abbrev=None):
    return abbrev or ABBREV.get(slug, "")


def title_prefix(slug, authors, abbrev=None):
    """Return '[ABBREV Author] ' (trailing space) or '' if nothing to show."""
    tag = f"{abbrev_for(slug, abbrev)} {short_author(authors)}".strip()
    return f"[{tag}] " if tag else ""
