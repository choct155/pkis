"""
paths.py — canonical filesystem paths for tools/scripts (B4).

Locks the contract the scripts rely on: REPO_ROOT points at the code repo (holds
app.py), the code/graph paths are the SAME objects config exposes (so paths.py never
drifts from the server's authority), bootstrap() is idempotent, and the operational
paths honour their env overrides.
"""

from pathlib import Path

import pytest

import paths
import config


@pytest.mark.unit
def test_repo_root_holds_app_py():
    assert (paths.REPO_ROOT / "app.py").exists()
    assert (paths.REPO_ROOT / "config.py").exists()


@pytest.mark.unit
def test_code_paths_match_config():
    # paths re-exports config's authoritative values verbatim.
    assert paths.WIKI_DIR == config.WIKI_DIR
    assert paths.REPO_DIR == config.REPO_DIR
    assert paths.USAGE_DB_PATH == config.USAGE_DB_PATH


@pytest.mark.unit
def test_bootstrap_is_idempotent():
    import sys
    paths.bootstrap()  # ensure present once
    before_count = sys.path.count(str(paths.REPO_ROOT))
    before = list(sys.path)
    paths.bootstrap()
    paths.bootstrap()
    # Already-present root is never re-added (the env may legitimately carry it more
    # than once via pytest rootdir + editable install; bootstrap must not grow it).
    assert sys.path.count(str(paths.REPO_ROOT)) == before_count
    # bootstrap only ever prepends; existing entries are preserved.
    assert set(before).issubset(set(sys.path))


@pytest.mark.unit
def test_operational_paths_are_paths():
    for p in (paths.PROPOSALS_DIR, paths.DOCS_BOOKS_DIR, paths.USAGE_DIR,
              paths.DISCOVERY_INBOX_PATH, paths.ENV_FILE, paths.INBOX_MD):
        assert isinstance(p, Path)


@pytest.mark.unit
def test_env_override(monkeypatch):
    import importlib
    monkeypatch.setenv("PKIS_PROPOSALS_DIR", "/tmp/custom-proposals")
    importlib.reload(paths)
    assert str(paths.PROPOSALS_DIR) == "/tmp/custom-proposals"
    # Restore module state for any later test importing paths.
    monkeypatch.delenv("PKIS_PROPOSALS_DIR")
    importlib.reload(paths)
