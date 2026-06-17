"""
PKIS store layer — extraction in progress (B2 split).

The first functions carved out of the app.py monolith: pure IRI / slug helpers
with no module-global dependencies, so they move verbatim and app.py re-imports
them (the thin-shim pattern keeps `import app` and gunicorn `app:app` valid).
app.py inserts its own real directory on sys.path before importing this, so the
import resolves under the server's gunicorn context too (CWD=/home/pkis).
Node loading + alias resolution (which depend on the mutable WIKI_DIR) move here
in a later increment, once the canonical paths are relocated to share one source.
"""

from pathlib import Path


def slug_from_path(path: Path) -> str:
    return path.stem


def iri_from_slug(node_type: str, slug: str) -> str:
    """Generate a stable IRI from node type and slug."""
    return f"pkis:{node_type}:{slug}"


def parse_iri(iri: str) -> tuple:
    """Parse IRI into (namespace, node_type, slug)."""
    parts = iri.split(":")
    if len(parts) >= 3:
        return parts[0], parts[1], parts[2]
    return None, None, None
