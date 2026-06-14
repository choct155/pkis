"""
Seam D — write ↔ cache freshness (ARCHITECTURE_AUDIT.md §7 Seam D).

Per-worker in-memory caches (_node_cache, _graph, _bm25_*, _embed_*) are
invalidated via a git-HEAD content signature (_content_signature / ensure_fresh /
_cache_gen). tool_edit_node ALSO manually zeroes _node_cache/_graph. The subtle
contract: after a write, a search in the same worker must find the new/edited
content without a restart. The audit flags this dual mechanism (manual zeroing +
signature-driven rebuild) as fragile.
"""

import pytest


@pytest.mark.integration
def test_edit_is_searchable_in_same_worker(appmod, isolated_wiki):
    """STUB: edit a node's searchable text via tool_edit_node, then search_wiki for
    the new term in the SAME process and assert it's found — i.e. the write
    invalidated/rebuilt the BM25 index, not just _node_cache. This is the exact
    'writes invisible until restart' regression the signature mechanism fixed."""
    pytest.skip("Phase-2 stub — assert post-edit search_wiki surfaces the new content")


@pytest.mark.integration
def test_content_signature_changes_on_commit(appmod, isolated_wiki):
    """STUB: _content_signature() (git HEAD sha) must change after a committing
    write, which is what makes other workers rebuild lazily via ensure_fresh()."""
    pytest.skip("Phase-2 stub — capture signature before/after a committing write")


@pytest.mark.integration
def test_staged_only_create_does_not_bump_signature(appmod, isolated_wiki):
    """STUB: a staged-only create (no commit) must NOT change the content
    signature — staged work is deliberately invisible to search until promoted."""
    pytest.skip("Phase-2 stub — confirm staging write leaves HEAD (and signature) unchanged")
