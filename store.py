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

import logging
from pathlib import Path

import frontmatter

import config

logger = logging.getLogger(__name__)


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


class WikiStore:
    """Owns the node + alias caches and the node-loading layer (B2 split / option C
    dependency injection). The wiki directory is INJECTED, so tests construct a
    fresh store pointed at a fixture wiki rather than monkeypatching module globals.
    app.py holds one module-level STORE instance and exposes thin wrappers so its
    ~95 existing call sites are unchanged; cache-clear sites call STORE.invalidate*().
    Static config (KNOWLEDGE_DIRS / TYPE_TO_FOLDER) is read live from config."""

    def __init__(self, wiki_dir):
        self.wiki_dir = Path(wiki_dir)
        self._node_cache: dict = {}
        self._alias_registry: dict = {}

    def invalidate_nodes(self):
        """Drop the node + alias caches — call after any write that changes nodes."""
        self._node_cache = {}
        self._alias_registry = {}

    def find_node_path(self, slug):
        """Find the file path for a slug, searching all knowledge dirs."""
        for kdir in config.KNOWLEDGE_DIRS:
            p = self.wiki_dir / kdir / f"{slug}.md"
            if p.exists():
                return p
        return None

    def find_node_path_by_iri(self, iri):
        """Resolve an IRI to a file path."""
        _, node_type, slug = parse_iri(iri)
        if not slug:
            return None
        folder = config.TYPE_TO_FOLDER.get(node_type, node_type) if node_type else None
        if folder:
            p = self.wiki_dir / folder / f"{slug}.md"
            if p.exists():
                return p
        return self.find_node_path(slug)

    def load_node(self, path):
        """Load and parse a wiki node file (cached by path)."""
        if str(path) in self._node_cache:
            return self._node_cache[str(path)]
        try:
            post = frontmatter.load(str(path))
            node_type = path.parent.name
            slug = path.stem
            iri = post.metadata.get("id") or iri_from_slug(node_type, slug)
            result = {
                "iri": iri,
                "slug": slug,
                "node_type": node_type,
                "path": str(path),
                "frontmatter": dict(post.metadata),
                "content": post.content,
                "title": post.metadata.get("title", slug),
                "domain": post.metadata.get("domain", []),
                "aliases": post.metadata.get("aliases", []),
                "coverage": post.metadata.get("coverage", 0),
                "understanding": post.metadata.get("understanding", 0),
                "confidence": post.metadata.get("confidence", 0),
                "date_updated": post.metadata.get("date_updated", ""),
            }
            self._node_cache[str(path)] = result
            return result
        except Exception as e:
            logger.error(f"Error loading {path}: {e}")
            return {}

    def load_all_nodes(self):
        """Load all wiki nodes across all knowledge directories."""
        nodes = []
        for kdir in config.KNOWLEDGE_DIRS:
            dir_path = self.wiki_dir / kdir
            if not dir_path.exists():
                continue
            for md_file in dir_path.glob("*.md"):
                node = self.load_node(md_file)
                if node:
                    nodes.append(node)
        return nodes

    def build_alias_registry(self):
        """Build flat alias → IRI registry from all node frontmatter."""
        registry = {}
        for node in self.load_all_nodes():
            iri = node["iri"]
            title = node.get("title", "")
            if title:
                registry[title.lower()] = iri
            registry[node["slug"].lower()] = iri
            for alias in node.get("aliases", []):
                registry[alias.lower()] = iri
        return registry

    def get_alias_registry(self):
        if not self._alias_registry:
            self._alias_registry = self.build_alias_registry()
        return self._alias_registry
