"""
Seam D — write ↔ cache freshness (ARCHITECTURE_AUDIT.md §7 Seam D).

Contract: a committing write changes the git-HEAD content signature, and
ensure_fresh() rebuilds the per-worker caches off that signature — so an edit is
searchable in the same worker without a restart. A staged-only create (no commit)
must NOT bump the signature (staged work stays invisible to search until promoted).
"""

import pytest


@pytest.mark.integration
def test_edit_is_searchable_in_same_worker(appmod, isolated_wiki):
    appmod.ensure_fresh()  # baseline: establish _cache_gen + build indexes
    appmod.tool_edit_node(
        slug="entropy",
        section_updates={"Definition": "Contains the rare marker token ZQXJWORDMARK."},
        commit_message="test: add searchable token",
    )
    appmod.ensure_fresh()  # the commit changed HEAD → caches rebuild off disk
    hits = appmod.hybrid_search("ZQXJWORDMARK", max_results=10)
    assert "pkis:concept:entropy" in {h["iri"] for h in hits}


@pytest.mark.integration
def test_content_signature_changes_on_commit(appmod, isolated_wiki):
    before = appmod._content_signature()
    appmod.tool_edit_node(slug="entropy",
                          section_updates={"Definition": "changed body"},
                          commit_message="test: bump signature")
    assert appmod._content_signature() != before


@pytest.mark.integration
def test_staged_only_create_does_not_bump_signature(appmod, isolated_wiki):
    before = appmod._content_signature()
    appmod.tool_create_node_stub(knowledge_type="concept", title="Staged Only",
                                 suggest_sources=False)
    assert appmod._content_signature() == before  # staging doesn't commit
