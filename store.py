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

import hashlib
import logging
import re
from pathlib import Path

import frontmatter
import networkx as nx
import numpy as np
from rank_bm25 import BM25Okapi

import config

logger = logging.getLogger(__name__)


def rrf_score(rank, k: int = 60) -> float:
    """Reciprocal-rank fusion weight (pure)."""
    return 1.0 / (k + rank)


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

    def __init__(self, wiki_dir, repo_dir=None, semantic_enabled=False):
        self.wiki_dir = Path(wiki_dir)
        # repo_dir is injected (tests monkeypatch it) — content_signature reads its
        # git HEAD. Defaults to the wiki's parent (prod layout: repo/wiki).
        self.repo_dir = Path(repo_dir) if repo_dir is not None else Path(wiki_dir).parent
        self._cache_gen = None
        self._node_cache: dict = {}
        self._alias_registry: dict = {}
        self._graph = None
        # Search layer (C-1c). semantic_enabled is injected (config.SEMANTIC_SEARCH
        # AND the app-level sentence-transformers probe) so the store needn't reach
        # back into app for _ST_AVAILABLE.
        self._semantic = bool(semantic_enabled)
        self._bm25_index = None
        self._bm25_corpus: list = []
        self._bm25_slugs: list = []
        self._embed_model = None
        self._embed_matrix = None
        self._embed_slugs: list = []

    def invalidate_nodes(self):
        """Drop the node + alias caches — call after any write that changes nodes."""
        self._node_cache = {}
        self._alias_registry = {}

    def invalidate_graph(self):
        """Drop the cached graph — call after a write that changes typed edges."""
        self._graph = None

    def invalidate_search(self):
        """Drop the BM25 + dense indexes (rebuilt lazily / on refresh). Keeps the
        loaded embedding model, which is expensive to re-load."""
        self._bm25_index = None
        self._bm25_corpus = []
        self._bm25_slugs = []
        self._embed_matrix = None
        self._embed_slugs = []

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

    def build_graph(self):
        """Build NetworkX graph from wiki wikilinks and typed edges."""
        G = nx.DiGraph()
        nodes = self.load_all_nodes()

        for node in nodes:
            G.add_node(node["iri"], **{
                "slug": node["slug"],
                "title": node["title"],
                "node_type": node["node_type"],
                "domain": node["domain"],
                "coverage": node["coverage"],
            })

        wikilink_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
        for node in nodes:
            content = node.get("content", "")
            fm = node.get("frontmatter", {})

            for edge_type in config.EDGE_WEIGHTS.keys():
                targets = fm.get(edge_type.replace("-", "_"), []) or \
                          fm.get(edge_type, [])
                if isinstance(targets, str):
                    targets = [targets]
                for target in targets:
                    target_slug = target.strip("[]").split("|")[0]
                    target_path = self.find_node_path(target_slug)
                    if target_path:
                        target_node = self.load_node(target_path)
                        if target_node:
                            G.add_edge(
                                node["iri"],
                                target_node["iri"],
                                edge_type=edge_type,
                                weight=config.EDGE_WEIGHTS[edge_type],
                            )

            for match in wikilink_pattern.finditer(content):
                target_slug = match.group(1).strip()
                target_path = self.find_node_path(target_slug)
                if target_path:
                    target_node = self.load_node(target_path)
                    if target_node and target_node["iri"] != node["iri"]:
                        if not G.has_edge(node["iri"], target_node["iri"]):
                            G.add_edge(
                                node["iri"],
                                target_node["iri"],
                                edge_type="related",
                                weight=0.3,
                            )
        return G

    def get_graph(self):
        if self._graph is None:
            self._graph = self.build_graph()
        return self._graph

    def structural_candidates(self, seed_iri, edge_types=None, max_hops=2):
        """Return structurally connected nodes with weighted scores."""
        G = self.get_graph()
        if seed_iri not in G:
            return []
        candidates = []
        visited = {seed_iri}

        def traverse(node_iri, depth):
            if depth > max_hops:
                return
            for neighbor in G.successors(node_iri):
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                edge_data = G.get_edge_data(node_iri, neighbor) or {}
                etype = edge_data.get("edge_type", "related")
                if edge_types and etype not in edge_types:
                    continue
                weight = config.EDGE_WEIGHTS.get(etype, 0.3)
                effective_weight = weight * (0.7 ** (depth - 1))
                candidates.append({
                    "iri": neighbor,
                    "edge_type": etype,
                    "weight": effective_weight,
                    "hop_count": depth,
                })
                traverse(neighbor, depth + 1)

        traverse(seed_iri, 1)
        return sorted(candidates, key=lambda x: x["weight"], reverse=True)

    # ── Search: BM25 + dense (C-1c) ─────────────────────────────────────────

    def _semantic_enabled(self):
        return self._semantic

    def _get_embed_model(self):
        """Lazy-load the sentence-transformer once per worker (CPU)."""
        if self._embed_model is None:
            from sentence_transformers import SentenceTransformer
            logger.info(f"Loading embedding model {config.EMBED_MODEL_NAME} ...")
            self._embed_model = SentenceTransformer(config.EMBED_MODEL_NAME, device="cpu")
        return self._embed_model

    @staticmethod
    def _index_meta(node):
        """Searchable bibliographic metadata (abbrev, authors, year) from
        frontmatter. Lets queries like 'mackay monte carlo' or 'gelman 2013'
        match source nodes whose title shows only a short author tag."""
        fm = node.get("frontmatter", {}) or {}
        authors = fm.get("authors", "") or ""
        if isinstance(authors, (list, tuple)):
            authors = " ".join(str(a) for a in authors)
        parts = [str(fm.get("abbrev", "") or ""), str(authors), str(fm.get("year", "") or "")]
        return " ".join(p for p in parts if p).strip()

    @staticmethod
    def _embed_text(node):
        title = node.get("title", "") or ""
        aliases = " ".join(node.get("aliases", []) or [])
        meta = WikiStore._index_meta(node)
        content = node.get("content", "") or ""
        return f"{title}\n{meta}\n{aliases}\n{content}".strip()

    def _load_embed_cache(self):
        if not config.EMBED_CACHE_PATH.exists():
            return {}
        try:
            data = np.load(config.EMBED_CACHE_PATH, allow_pickle=False)
            hashes, vectors = data["hashes"], data["vectors"]
            return {str(h): vectors[i] for i, h in enumerate(hashes)}
        except Exception as e:
            logger.warning(f"embed cache load failed ({e}); rebuilding from scratch")
            return {}

    def _save_embed_cache(self, cache, current_hashes):
        keep = list(dict.fromkeys(current_hashes))
        if not keep:
            return
        try:
            np.savez(
                config.EMBED_CACHE_PATH,
                hashes=np.array(keep),
                vectors=np.vstack([cache[h] for h in keep]).astype(np.float32),
            )
        except Exception as e:
            logger.warning(f"embed cache save failed: {e}")

    def build_bm25_index(self):
        nodes = self.load_all_nodes()
        corpus, slugs = [], []
        for node in nodes:
            text = f"{node['title']} {self._index_meta(node)} {node.get('content', '')} {' '.join(node.get('aliases', []))}"
            corpus.append(text.lower().split())
            slugs.append(node["iri"])
        self._bm25_index = BM25Okapi(corpus)
        self._bm25_corpus = corpus
        self._bm25_slugs = slugs

    def build_embedding_index(self):
        """Dense index over all nodes, reusing cached vectors. No-op when semantic
        search is disabled or the ML dep is absent."""
        if not self._semantic_enabled():
            self._embed_matrix, self._embed_slugs = None, []
            return
        nodes = self.load_all_nodes()
        texts = [self._embed_text(n) for n in nodes]
        hashes = [hashlib.sha1(t.encode("utf-8")).hexdigest() for t in texts]
        iris = [n["iri"] for n in nodes]
        cache = self._load_embed_cache()
        missing = [i for i, h in enumerate(hashes) if h not in cache]
        if missing:
            model = self._get_embed_model()
            vecs = model.encode(
                [texts[i] for i in missing],
                normalize_embeddings=True, batch_size=64, show_progress_bar=False,
            )
            for j, i in enumerate(missing):
                cache[hashes[i]] = np.asarray(vecs[j], dtype=np.float32)
            logger.info(f"Embedded {len(missing)} new/changed nodes "
                        f"({len(nodes) - len(missing)} reused from cache)")
        self._embed_matrix = np.vstack([cache[h] for h in hashes]).astype(np.float32)
        self._embed_slugs = iris
        self._save_embed_cache(cache, hashes)

    def vector_search(self, query, max_results=30):
        if not self._semantic_enabled() or self._embed_matrix is None or not self._embed_slugs:
            return []
        model = self._get_embed_model()
        q = model.encode([config.EMBED_QUERY_PREFIX + query], normalize_embeddings=True)[0]
        sims = self._embed_matrix @ np.asarray(q, dtype=np.float32)
        top = np.argsort(-sims)[:max_results]
        return [(self._embed_slugs[i], float(sims[i])) for i in top]

    def hybrid_search(self, query, domains=None, node_types=None, max_results=10):
        """Hybrid BM25 + dense search with RRF fusion."""
        if self._bm25_index is None:
            self.build_bm25_index()
        if self._semantic_enabled() and self._embed_matrix is None:
            self.build_embedding_index()

        tokens = query.lower().split()
        bm25_scores = self._bm25_index.get_scores(tokens)
        bm25_ranked = sorted(enumerate(bm25_scores), key=lambda x: x[1], reverse=True)[:max_results * 3]

        rrf_scores = {}
        for rank, (idx, _score) in enumerate(bm25_ranked):
            iri = self._bm25_slugs[idx]
            rrf_scores[iri] = rrf_scores.get(iri, 0) + rrf_score(rank)
        for rank, (iri, _sim) in enumerate(self.vector_search(query, max_results=max_results * 3)):
            rrf_scores[iri] = rrf_scores.get(iri, 0) + rrf_score(rank)

        node_map = {n["iri"]: n for n in self.load_all_nodes()}
        results, seen = [], set()
        for iri, score in sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True):
            if iri in seen:
                continue
            seen.add(iri)
            node = node_map.get(iri)
            if not node:
                continue
            if domains and not any(d in node.get("domain", []) for d in domains):
                continue
            if node_types and node.get("node_type") not in node_types:
                continue
            node_type_key = config.FOLDER_TO_TYPE.get(node["node_type"], node["node_type"])
            components = config.COMPONENT_SCORES_BY_TYPE.get(node_type_key)
            anatomy_total = len(components) if components else 0
            anatomy_assessed = 0
            if components:
                cs = node.get("frontmatter", {}).get("component_scores") or {}
                anatomy_assessed = sum(1 for c in components if cs.get(c) is not None)
            results.append({
                "iri": iri,
                "canonical_title": node["title"],
                "node_type": config.FOLDER_TO_TYPE.get(node["node_type"], node["node_type"]),
                "domain": node["domain"],
                "score": score,
                "excerpt": node["content"][:300] if node.get("content") else "",
                "coverage": node["coverage"],
                "understanding": node["understanding"],
                "anatomy_assessed": anatomy_assessed,
                "anatomy_total": anatomy_total,
            })
            if len(results) >= max_results:
                break
        return results

    # ── Freshness: git-HEAD-signature cross-worker cache invalidation (C-1d) ──

    def content_signature(self):
        """Live-content signature = git HEAD sha of repo_dir (changes on every
        committed write). Empty string if unreadable — caller leaves caches as-is."""
        try:
            head = (self.repo_dir / ".git" / "HEAD").read_text().strip()
            if head.startswith("ref:"):
                ref = head.split(" ", 1)[1].strip()
                ref_path = self.repo_dir / ".git" / ref
                if ref_path.exists():
                    return ref_path.read_text().strip()
                packed = self.repo_dir / ".git" / "packed-refs"
                if packed.exists():
                    for line in packed.read_text().splitlines():
                        parts = line.split()
                        if len(parts) == 2 and parts[1] == ref:
                            return parts[0]
                return ""
            return head  # detached HEAD: the line itself is the sha
        except Exception:
            return ""

    def refresh(self):
        """Invalidate and rebuild all caches."""
        self.invalidate_nodes()
        self.invalidate_graph()
        self.invalidate_search()
        g = self.get_graph()
        self.build_bm25_index()
        self.build_embedding_index()
        aliases = self.get_alias_registry()
        logger.info(f"Caches refreshed: {len(aliases)} aliases, "
                    f"{g.number_of_nodes()} nodes, "
                    f"{g.number_of_edges()} edges, "
                    f"semantic={'on' if self._semantic_enabled() else 'off'}")

    def ensure_fresh(self):
        """Rebuild this worker's caches if live content changed since it last built
        (cross-worker invalidation via the git HEAD signature). Cheap when unchanged."""
        sig = self.content_signature()
        if sig and sig != self._cache_gen:
            try:
                self.refresh()
                self._cache_gen = sig
            except Exception as e:
                logger.warning(f"ensure_fresh rebuild failed: {e}")
