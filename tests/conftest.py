"""
PKIS test harness — fixture wiki + fixture git repo, fully hermetic.

Phase-2 scaffold (see ARCHITECTURE_AUDIT.md §7, §9). This file is the prerequisite
the audit calls out: it builds a throwaway wiki + git repo in a tmp dir and points
app.py's WIKI_DIR / REPO_DIR / STAGING_DIR at it BEFORE importing app, so the whole
suite runs without touching /home/pkis or the live pkis.dev server.

Two import-time facts about app.py this harness has to work around (both recorded
in the audit):

  1. app.py reads its paths from env into MODULE-LEVEL constants at import
     (WIKI_DIR = Path(os.environ.get("WIKI_DIR", ...)), etc.). So env must be set
     before `import app`. We do that here, at conftest module top.
  2. app.py constructs `Anthropic(api_key=...)` at import (app.py:204). The
     Anthropic SDK builds an httpx client that honours proxy env vars; any
     environment with an *_PROXY / ALL_PROXY set (CI sandboxes, corp networks)
     makes the import fail unless socksio is installed. We neutralize proxy vars
     here. Harmless on the VPS (none set there).
"""

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import frontmatter
import pytest

# --------------------------------------------------------------------------- #
# 1. Normalize the import environment BEFORE app.py is imported.
# --------------------------------------------------------------------------- #

# Strip proxy vars so the import-time Anthropic() client construction succeeds
# (see module docstring, point 2).
for _k in list(os.environ):
    if "proxy" in _k.lower() or "socks" in _k.lower():
        os.environ.pop(_k, None)

# Session fixture root. Module-level (not a pytest tmp_path) because env must be
# set before import; cleaned up via the session-scoped finalizer below.
_SESSION_ROOT = Path(tempfile.mkdtemp(prefix="pkis-test-"))
_SESSION_REPO = _SESSION_ROOT / "repo"
_SESSION_WIKI = _SESSION_REPO / "wiki"

os.environ["WIKI_DIR"] = str(_SESSION_WIKI)
os.environ["REPO_DIR"] = str(_SESSION_REPO)
os.environ["DOCS_REPO_DIR"] = str(_SESSION_REPO)
os.environ["STAGING_DIR"] = str(_SESSION_WIKI / "staging")
os.environ["ANTHROPIC_API_KEY"] = "sk-test-not-a-real-key"
# Comptroller usage store: point at the session tmp dir so log_usage (best-effort)
# never writes to /home/pkis during tests.
os.environ["PKIS_USAGE_DB"] = str(_SESSION_ROOT / "usage" / "usage.sqlite")
# Force BM25-only: deterministic, and avoids pulling torch into the test env.
os.environ["PKIS_SEMANTIC_SEARCH"] = "0"
# Ensure auth subsystems are DORMANT for the default suite (Seam E tests opt in
# by setting these explicitly via monkeypatch).
for _k in ("PKIS_OAUTH_ISSUER", "PKIS_OAUTH_JWKS_URL", "WORKOS_API_KEY",
           "PKIS_MCP_WRITE_KEY", "PKIS_TRUSTED_TOKEN"):
    os.environ.pop(_k, None)


# --------------------------------------------------------------------------- #
# 2. Fixture-building helpers (used by the session fixture and isolated_wiki).
# --------------------------------------------------------------------------- #

# Folder -> a couple of representative knowledge dirs we seed. The full set lives
# in app.KNOWLEDGE_DIRS; we create them all so load_all_nodes() never trips.
_ALL_DIRS = [
    "concepts", "techniques", "results", "frameworks", "problems",
    "principles", "sources", "hypotheses", "clusters", "assets",
    "bridge-notes", "staging",
]


def write_node(wiki_dir: Path, folder: str, slug: str, *, body: str = "", **fm) -> Path:
    """Write a wiki node file with frontmatter, matching app.py's on-disk format.

    Returns the path. `fm` keys become frontmatter fields; pass e.g.
    title=..., id="pkis:concept:foo", domain=[...], coverage=3.
    """
    fm.setdefault("title", slug.replace("-", " ").title())
    post = frontmatter.Post(body or f"## Definition\n\n{slug} placeholder.\n", **fm)
    d = wiki_dir / folder
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{slug}.md"
    p.write_text(frontmatter.dumps(post))
    return p


def init_git_repo(repo_dir: Path, *, with_remote: bool = True) -> Path | None:
    """git init `repo_dir`, set a local identity, make an initial commit, and
    (optionally) add a *bare* remote named origin and push to it so that the
    push step in the write tools succeeds. Returns the remote path (or None).

    Seam-C push-failure tests can re-point origin at a bad URL to exercise the
    'local commit retained, git_pushed=False' contract.
    """
    subprocess.run(["git", "init", "-q", str(repo_dir)], check=True)
    subprocess.run(["git", "-C", str(repo_dir), "config", "user.email", "test@pkis.local"], check=True)
    subprocess.run(["git", "-C", str(repo_dir), "config", "user.name", "PKIS Test"], check=True)
    subprocess.run(["git", "-C", str(repo_dir), "add", "-A"], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(repo_dir), "commit", "-q", "-m", "fixture: initial"],
                   check=True, capture_output=True)
    remote = None
    if with_remote:
        remote = repo_dir.parent / (repo_dir.name + "-remote.git")
        subprocess.run(["git", "init", "-q", "--bare", str(remote)], check=True)
        subprocess.run(["git", "-C", str(repo_dir), "remote", "add", "origin", str(remote)], check=True)
        # Match the branch the push step targets.
        subprocess.run(["git", "-C", str(repo_dir), "push", "-q", "-u", "origin", "HEAD"],
                       check=True, capture_output=True)
    return remote


def _seed_fixture_wiki(wiki_dir: Path) -> None:
    """Create the dir skeleton + a handful of canonical nodes used by read tests."""
    for d in _ALL_DIRS:
        (wiki_dir / d).mkdir(parents=True, exist_ok=True)
    write_node(wiki_dir, "concepts", "bayesian-inference",
               id="pkis:concept:bayesian-inference", title="Bayesian Inference",
               domain=["bayesian-statistics"], aliases=["Bayes inference"],
               coverage=4, understanding=3,
               body="## Definition\n\nUpdating beliefs with evidence via Bayes' rule.\n")
    write_node(wiki_dir, "concepts", "entropy",
               id="pkis:concept:entropy", title="Entropy",
               domain=["information-theory"], coverage=3, understanding=2,
               body="## Definition\n\nExpected surprise of a distribution.\n")
    write_node(wiki_dir, "concepts", "sourceless-example",
               id="pkis:concept:sourceless-example", title="Sourceless Example",
               domain=["test"], coverage=1, needs_canonical_source=True,
               body="## Definition\n\nA stub with no canonical source.\n")
    write_node(wiki_dir, "sources", "mackay-itila",
               id="pkis:source:mackay-itila", title="Information Theory, Inference, and Learning Algorithms",
               domain=["information-theory"], coverage=5,
               body="## Summary\n\nMacKay's textbook.\n")


# --------------------------------------------------------------------------- #
# 3. Build the session fixture environment, then import app exactly once.
# --------------------------------------------------------------------------- #

_SESSION_WIKI.mkdir(parents=True, exist_ok=True)
_seed_fixture_wiki(_SESSION_WIKI)
init_git_repo(_SESSION_REPO, with_remote=True)

import app as _app  # noqa: E402  (must follow env setup + fixture build)


# Force LLM-using tools (e.g. detect_concepts) down their deterministic fallback
# path so the hermetic suite never touches the Anthropic API. Those tools catch
# broad exceptions and degrade to BM25, so raising here keeps the contract intact
# while guaranteeing no network call.
class _NoNetworkAnthropic:
    class messages:
        @staticmethod
        def create(*_a, **_k):
            raise RuntimeError("anthropic disabled in tests")


_app.anthropic_client = _NoNetworkAnthropic()


@pytest.fixture(scope="session", autouse=True)
def _cleanup_session_root():
    yield
    shutil.rmtree(_SESSION_ROOT, ignore_errors=True)


@pytest.fixture(scope="session")
def appmod():
    """The imported app module (app.py), bound to the session fixture wiki."""
    return _app


@pytest.fixture()
def client(appmod):
    """Flask test client. Reset per-test caches so reads reflect current disk."""
    appmod.STORE.invalidate_nodes()  # node + alias caches (option-C WikiStore)
    appmod.STORE.invalidate_graph()
    appmod.STORE.invalidate_search()
    return appmod.app.test_client()


@pytest.fixture()
def isolated_wiki(appmod, monkeypatch, tmp_path):
    """Function-scoped fresh wiki + git repo (+ bare remote), with app's path
    globals monkeypatched to point at it and all caches cleared. Use for any
    test that WRITES (git round-trip, staging→commit, edit_node), so tests don't
    mutate each other's fixture state.

    Yields a namespace with: .repo, .wiki, .remote, and .write_node(folder, slug, **fm).
    """
    repo = tmp_path / "repo"
    wiki = repo / "wiki"
    _seed_fixture_wiki(wiki)
    remote = init_git_repo(repo, with_remote=True)

    monkeypatch.setattr(appmod, "WIKI_DIR", wiki)
    monkeypatch.setattr(appmod, "REPO_DIR", repo)
    monkeypatch.setattr(appmod, "DOCS_REPO_DIR", repo)
    monkeypatch.setattr(appmod, "STAGING_DIR", wiki / "staging")
    # Option-C DI payoff: give this test its OWN store pointed at the fixture —
    # a fresh instance has empty caches + _cache_gen=None, so no monkeypatch-and-
    # invalidate dance. app.py functions resolve appmod.STORE at call time, so they
    # transparently use it. (Tools still read the app/config WIKI_DIR globals for
    # write-paths, hence those monkeypatches above remain.)
    monkeypatch.setattr(appmod, "STORE", appmod.WikiStore(wiki, repo_dir=repo, semantic_enabled=False))

    class _Env:
        pass
    env = _Env()
    env.repo, env.wiki, env.remote = repo, wiki, remote
    env.write_node = lambda folder, slug, **fm: write_node(wiki, folder, slug, **fm)
    yield env
