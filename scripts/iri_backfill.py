#!/usr/bin/env python3
"""
IRI Backfill Script
===================
Adds `id` and `aliases` fields to the frontmatter of all wiki nodes that lack them.

- `id` is derived deterministically: pkis:{singular_type}:{slug}
- `aliases` is populated from:
    1. Parenthetical abbreviations in the title (e.g. "Markov Chain Monte Carlo (MCMC)" → ["MCMC"])
    2. Expansions when the title IS the abbreviation (e.g. "OWL (Web Ontology Language)" → ["Web Ontology Language"])
    3. A hand-curated KNOWN_ALIASES dict for well-known source works

Files that already have an `id:` field are skipped (idempotent).

Usage:
    python3 scripts/iri_backfill.py [--dry-run]
"""

import re
import sys
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent / "wiki"

FOLDER_TO_TYPE = {
    "concepts":   "concept",
    "techniques": "technique",
    "results":    "result",
    "frameworks": "framework",
    "problems":   "problem",
    "principles": "principle",
    "sources":    "source",
}

# Hand-curated aliases for well-known source works (slug → alias list).
# Chapter-level stubs inherit the book's drive_id but don't need book-level aliases.
KNOWN_SOURCE_ALIASES: dict[str, list[str]] = {
    "hastie-esl":                           ["ESL", "Elements of Statistical Learning"],
    "pearl-causality":                      ["Causality (Pearl)", "Pearl Causality"],
    "deisenroth-mml":                       ["MML", "Mathematics for Machine Learning"],
    "nielsen-nndl":                         ["NNDL", "Neural Networks and Deep Learning"],
    "cunningham-causal-inference-mixtape":  ["Causal Inference: The Mixtape", "Mixtape"],
    "lange-applied-probability":            ["Applied Probability (Lange)"],
    "cassandras-des-intro":                 ["Introduction to Discrete Event Systems", "Cassandras DES"],
    "carrell-groups-matrices-vectors":      ["Groups, Matrices, and Vector Spaces"],
    "gulli-agentic-design-patterns":        ["Agentic Design Patterns"],
    "kroese-statistical-modeling":          ["Statistical Modeling and Simulation (Kroese)"],
    "allemang-semantic-web":                ["Semantic Web for the Working Ontologist"],
    "cimiano-ontology-nlp":                 ["Ontology-Based Interpretation of Natural Language"],
    "hamilton-graphsage":                   ["GraphSAGE paper"],
    "blei-vi-review":                       ["Blei VI review", "Variational Inference Review"],
    "scott-varian-bsts-2014":               ["BSTS paper", "Scott-Varian 2014"],
    "domingos-useful-things":               ["A Few Useful Things to Know About Machine Learning"],
}


def extract_aliases_from_title(title: str) -> list[str]:
    """
    Extract candidate aliases from a node title based on parenthetical patterns.

    Two patterns:
      1. "Full Name (ABBREV)"  → ABBREV if it looks like a true abbreviation
         (2+ chars, starts uppercase, mostly uppercase, e.g. MCMC, EM, VAE, KANs)
         Guard: skip if the main title (outside the parens) is a single word —
         that indicates a domain qualifier like "Controllability (DES)" where
         "(DES)" means "in the DES domain", not that DES is an alias for Controllability.
      2. "ABBREV (Full Expansion)"  → Full Expansion if ABBREV is all-caps and
         the expansion is a meaningful phrase (> 4 chars)
    """
    aliases = []

    # Strip parentheticals to get the "main title" for the single-word guard
    main_title = re.sub(r'\s*\([^)]+\)', '', title).strip()
    main_words = [w for w in re.split(r'[\s\-]+', main_title) if w]

    parentheticals = re.findall(r'\(([^)]+)\)', title)

    for paren in parentheticals:
        paren = paren.strip()
        # Pattern 1: parenthetical looks like a true abbreviation
        # Matches: MCMC, EM, CAVI, GMM, VAE, KANs, PINNs, ELBO, KGQA, IES, CAPM, NMF...
        # Requires: starts with uppercase, rest uppercase/digits/hyphens, optional trailing s
        if not re.fullmatch(r'[A-Z][A-Z0-9\-]{1,9}s?', paren):
            continue
        # Guard: single-word main titles pair with domain qualifiers, not aliases.
        # e.g. "Controllability (DES)" — DES is a domain context, not a synonym.
        if len(main_words) <= 1:
            continue
        aliases.append(paren)

    # Pattern 2: title STARTS with an all-caps abbreviation
    # e.g. "OWL (Web Ontology Language)", "OLAP (Online Analytical Processing)"
    m = re.match(r'^([A-Z][A-Z0-9\-]{1,9})\s+\((.+)\)\s*$', title)
    if m:
        abbrev, expansion = m.group(1), m.group(2).strip()
        # Only add expansion as alias if it's a meaningful phrase (not already captured)
        # and doesn't look like a domain qualifier (single short word or author name)
        if (
            len(expansion) > 4
            and expansion not in aliases
            and not re.fullmatch(r'[A-Z][A-Z0-9\-]{1,9}s?', expansion)  # not another abbrev
        ):
            aliases.append(expansion)

    return aliases


def get_title_from_frontmatter(fm_text: str) -> str:
    """Extract raw title value from frontmatter text."""
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
    return m.group(1).strip().strip('"\'') if m else ""


def format_aliases_yaml(aliases: list[str]) -> str:
    """Format aliases list as a YAML inline array."""
    if not aliases:
        return "[]"
    inner = ", ".join(f'"{a}"' for a in aliases)
    return f"[{inner}]"


def process_file(filepath: Path, node_type: str, dry_run: bool = False) -> tuple[bool, str]:
    """
    Add `id` and `aliases` to the file's frontmatter if missing.

    Returns (was_modified, summary_line).
    """
    content = filepath.read_text(encoding="utf-8")

    if not content.startswith("---"):
        return False, f"  SKIP (no frontmatter): {filepath.name}"

    parts = content.split("---", 2)
    if len(parts) < 3:
        return False, f"  SKIP (malformed frontmatter): {filepath.name}"

    fm_text = parts[1]
    body = parts[2]

    # Already has id → skip (idempotent)
    if re.search(r"^id:", fm_text, re.MULTILINE):
        return False, f"  SKIP (id exists): {filepath.name}"

    slug = filepath.stem
    iri = f"pkis:{node_type}:{slug}"

    # Determine aliases
    if node_type == "source" and slug in KNOWN_SOURCE_ALIASES:
        aliases = KNOWN_SOURCE_ALIASES[slug]
    elif node_type == "source":
        aliases = []
    else:
        title = get_title_from_frontmatter(fm_text)
        aliases = extract_aliases_from_title(title)

    aliases_yaml = format_aliases_yaml(aliases)

    # Prepend id and aliases to frontmatter, preserving everything else verbatim
    new_fm = f'id: "{iri}"\naliases: {aliases_yaml}\n' + fm_text.lstrip("\n")
    new_content = f"---\n{new_fm}---{body}"

    summary = f"  ADD {iri}  aliases={aliases_yaml}"

    if not dry_run:
        filepath.write_text(new_content, encoding="utf-8")

    return True, summary


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=== DRY RUN — no files will be written ===\n")
    else:
        print("=== IRI Backfill ===\n")

    total_modified = 0
    total_skipped = 0
    total_errors = 0

    for folder_name, node_type in FOLDER_TO_TYPE.items():
        folder = WIKI_DIR / folder_name
        if not folder.exists():
            print(f"[{folder_name}/] MISSING — skipping")
            continue

        files = sorted(folder.glob("*.md"))
        folder_modified = 0

        print(f"[{folder_name}/]  ({len(files)} files)")
        for filepath in files:
            try:
                modified, summary = process_file(filepath, node_type, dry_run=dry_run)
                if modified:
                    folder_modified += 1
                    total_modified += 1
                    if dry_run:
                        print(summary)
                else:
                    total_skipped += 1
            except Exception as e:
                total_errors += 1
                print(f"  ERROR {filepath.name}: {e}")

        if not dry_run:
            print(f"  → {folder_modified} files updated")
        print()

    print(f"{'[DRY RUN] ' if dry_run else ''}Done: {total_modified} modified, "
          f"{total_skipped} already had id, {total_errors} errors")


if __name__ == "__main__":
    main()
