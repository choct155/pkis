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

import copy
import hashlib
import logging
import re
import time
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


# Baseline search profile — reproduces the pre-pipeline hybrid_search behavior
# exactly (lexical + dense, RRF k=60, 3x candidate pool, no rerankers/transforms).
# app.py layers named/user profiles on top via search_profiles.json; partial
# profiles are shallow-merged over this default by merge_search_profile().
DEFAULT_SEARCH_PROFILE = {
    "name": "default",
    "transforms": {"hyde": False, "alias_expansion": False},
    "retrievers": {"lexical": True, "dense": True},
    "fusion": {"method": "rrf", "k": 60},
    "rerankers": [],            # ordered: e.g. ["cross_encoder", "graph"]
    "filters": {"domains": None, "node_types": None},
    "candidate_multiplier": 3,  # candidate pool = max_results * this, per retriever
    "deep_metrics": False,
}


def merge_search_profile(profile):
    """Shallow-merge a (possibly partial) profile over DEFAULT_SEARCH_PROFILE.
    Nested dicts (transforms/retrievers/fusion/filters) merge per-key; everything
    else replaces. Returns a fresh dict — never mutates the default or the input."""
    base = copy.deepcopy(DEFAULT_SEARCH_PROFILE)
    if not profile:
        return base
    for key, val in profile.items():
        if isinstance(val, dict) and isinstance(base.get(key), dict):
            base[key].update(val)
        else:
            base[key] = val
    return base


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
        self._cross_encoder = None
        self._cross_encoder_name = None
        self._ppr_out = None  # cached row-normalized out-adjacency for graph rerank

    def invalidate_nodes(self):
        """Drop the node + alias caches — call after any write that changes nodes."""
        self._node_cache = {}
        self._alias_registry = {}

    def invalidate_graph(self):
        """Drop the cached graph — call after a write that changes typed edges."""
        self._graph = None
        self._ppr_out = None

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

    # ── Staged, profile-driven search pipeline (C-1e) ──
    # transform → retrieve (lexical/dense) → fuse (RRF) → rerank → filter+assemble.
    # Each stage is independently toggled by a SearchProfile and timed into `trace`,
    # so the lab can compare capabilities and measure their efficiency cost.

    def _timed(self, trace, name, kind, fn):
        """Run fn(), append a {name,kind,ms,n_out} record to trace.stages."""
        t0 = time.perf_counter()
        out = fn()
        ms = (time.perf_counter() - t0) * 1000.0
        if trace is not None:
            n_out = len(out) if hasattr(out, "__len__") else None
            trace.setdefault("stages", []).append(
                {"name": name, "kind": kind, "ms": round(ms, 3), "n_out": n_out}
            )
        return out

    def _retrieve_lexical(self, query, k):
        if self._bm25_index is None:
            self.build_bm25_index()
        scores = self._bm25_index.get_scores(query.lower().split())
        ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:k]
        return [(self._bm25_slugs[i], float(s)) for i, s in ranked]

    def _retrieve_dense(self, query, k):
        if self._semantic_enabled() and self._embed_matrix is None:
            self.build_embedding_index()
        return self.vector_search(query, max_results=k)

    @staticmethod
    def _fuse_rrf(candidate_lists, k=60):
        rrf = {}
        for lst in candidate_lists:
            for rank, (iri, _s) in enumerate(lst):
                rrf[iri] = rrf.get(iri, 0.0) + rrf_score(rank, k)
        return sorted(rrf.items(), key=lambda x: x[1], reverse=True)

    def _apply_reranker(self, name, query, fused, node_map, prof):
        """Dispatch to _rerank_<name>(query, fused, node_map, prof). Each reranker
        takes and returns a [(iri, score), ...] list. Unknown names are skipped."""
        fn = getattr(self, f"_rerank_{name}", None)
        if fn is None:
            logger.warning(f"unknown reranker '{name}'; skipping")
            return fused
        return fn(query, fused, node_map, prof)

    def _get_cross_encoder(self, model_name):
        if self._cross_encoder is None or self._cross_encoder_name != model_name:
            from sentence_transformers import CrossEncoder  # lazy: optional dep
            logger.info(f"Loading cross-encoder {model_name} ...")
            self._cross_encoder = CrossEncoder(model_name, device="cpu")
            self._cross_encoder_name = model_name
        return self._cross_encoder

    def _rerank_cross_encoder(self, query, fused, node_map, prof):
        """Re-score the top-N fused candidates with a cross-encoder (query+doc read
        jointly — far more precise than bi-encoder cosine), reorder them, and keep
        the un-reranked tail beneath. Head scores become the cross-encoder logit;
        order (not absolute score) is what the assembler consumes."""
        params = (prof.get("reranker_params") or {}).get("cross_encoder", {})
        model_name = params.get("model", config.CROSS_ENCODER_MODEL)
        top_n = int(params.get("top_n", 30))
        head = fused[:top_n]
        if not head:
            return fused
        try:
            ce = self._get_cross_encoder(model_name)
        except Exception as ex:  # dep missing / load failure → degrade to fused order
            logger.warning(f"cross-encoder unavailable ({ex}); skipping rerank")
            return fused
        pairs, iris = [], []
        for iri, _s in head:
            node = node_map.get(iri)
            if not node:
                continue
            pairs.append((query, f"{node.get('title', '')} {(node.get('content') or '')[:500]}"))
            iris.append(iri)
        scores = ce.predict(pairs)
        reranked = sorted(zip(iris, (float(s) for s in scores)), key=lambda x: x[1], reverse=True)
        return reranked + fused[top_n:]

    def _ppr_adjacency(self, G):
        """Row-normalized, edge-weighted out-adjacency {u: [(v, p), ...]} cached
        off the graph (rebuilt only when the graph is invalidated)."""
        if self._ppr_out is None:
            out = {}
            for u in G.nodes():
                ws = [(v, float((G.get_edge_data(u, v) or {}).get("weight", 1.0))) for v in G.successors(u)]
                s = sum(w for _, w in ws)
                out[u] = [(v, w / s) for v, w in ws] if s else []
            self._ppr_out = out
        return self._ppr_out

    def _personalized_pagerank(self, G, pers, alpha=0.85, iters=50, tol=1e-6):
        """Edge-weighted personalized PageRank by power iteration — pure dict, no
        scipy. `pers` is the teleport distribution (seed → weight, summing to 1).
        Dangling nodes redistribute mass to the teleport set. Returns {node: score}."""
        out = self._ppr_adjacency(G)
        nodes = list(out.keys())
        dangling = [n for n in nodes if not out[n]]
        r = {n: pers.get(n, 0.0) for n in nodes}
        for _ in range(iters):
            dmass = alpha * sum(r[n] for n in dangling)
            nr = {n: (1 - alpha + dmass) * pers.get(n, 0.0) for n in nodes}
            for u in nodes:
                ru = r[u]
                if ru and out[u]:
                    a_ru = alpha * ru
                    for v, w in out[u]:
                        nr[v] += a_ru * w
            if sum(abs(nr[n] - r[n]) for n in nodes) < tol:
                return nr
            r = nr
        return r

    def _rerank_graph(self, query, fused, node_map, prof):
        """Spreading-activation rerank: run personalized PageRank over the typed
        graph, teleporting back to the fused candidates (weighted by their fused
        score). A candidate well-connected to the other strong hits gets boosted
        even if its own text matched weakly. Blend PPR with the first-stage score
        (rank-normalized, scale-free) and reorder; un-ranked tail kept beneath."""
        params = (prof.get("reranker_params") or {}).get("graph", {})
        alpha = float(params.get("alpha", 0.85))
        beta = float(params.get("blend", 0.5))   # weight on PPR vs first-stage
        top_n = int(params.get("top_n", 50))
        if not fused:
            return fused
        head = fused[:top_n]
        G = self.get_graph()
        seeds = {iri: sc for iri, sc in head if G.has_node(iri) and sc > 0}
        if not seeds:
            return fused
        tot = sum(seeds.values()) or 1.0
        pers = {i: s / tot for i, s in seeds.items()}
        try:
            ppr = self._personalized_pagerank(G, pers, alpha=alpha)
        except Exception as e:  # degrade to fused order on any failure
            logger.warning(f"graph rerank failed ({e}); skipping")
            return fused
        fmax = max((sc for _, sc in head), default=1.0) or 1.0
        pmax = max((ppr.get(iri, 0.0) for iri, _ in head), default=1.0) or 1.0
        blended = [(iri, beta * (ppr.get(iri, 0.0) / pmax) + (1 - beta) * (sc / fmax))
                   for iri, sc in head]
        blended.sort(key=lambda x: x[1], reverse=True)
        return blended + fused[top_n:]

    def _assemble(self, fused, node_map, domains, node_types, max_results):
        results = []
        for iri, score in fused:
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
                "node_type": node_type_key,
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

    def search(self, query, profile=None, trace=None, domains=None,
               node_types=None, max_results=10):
        """Profile-driven staged search. `profile` is a (possibly partial) dict;
        `trace` (if a dict is passed) accumulates per-stage timing. Explicit
        domains/node_types args override the profile's filters (back-compat)."""
        prof = merge_search_profile(profile)
        f_domains = domains if domains is not None else prof["filters"].get("domains")
        f_node_types = node_types if node_types is not None else prof["filters"].get("node_types")
        k = max_results * int(prof.get("candidate_multiplier", 3))

        eff_query = query  # query transforms (HyDE / expansion) land here in a later phase

        cand_lists = []
        if prof["retrievers"].get("lexical", True):
            cand_lists.append(self._timed(trace, "retrieve:lexical", "retriever",
                                          lambda: self._retrieve_lexical(eff_query, k)))
        if prof["retrievers"].get("dense", True):
            cand_lists.append(self._timed(trace, "retrieve:dense", "retriever",
                                          lambda: self._retrieve_dense(eff_query, k)))

        fused = self._timed(trace, "fuse:rrf", "fusion",
                            lambda: self._fuse_rrf(cand_lists, prof["fusion"].get("k", 60)))

        node_map = {n["iri"]: n for n in self.load_all_nodes()}
        for rname in prof.get("rerankers", []):
            fused = self._timed(trace, f"rerank:{rname}", "reranker",
                                lambda rn=rname, fl=fused: self._apply_reranker(rn, eff_query, fl, node_map, prof))

        results = self._timed(trace, "assemble", "assemble",
                              lambda: self._assemble(fused, node_map, f_domains, f_node_types, max_results))
        if trace is not None:
            trace["profile"] = prof.get("name", "custom")
            trace["query"] = query
        return results

    def hybrid_search(self, query, domains=None, node_types=None, max_results=10):
        """Back-compat shim — the default profile reproduces the original
        BM25 + dense → RRF behavior exactly. Existing call sites are unchanged."""
        return self.search(query, profile=None, trace=None, domains=domains,
                           node_types=node_types, max_results=max_results)

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
