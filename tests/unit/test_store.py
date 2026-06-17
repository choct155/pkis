"""
WikiStore — the option-C dependency-injected state container (B2 split).

Locks the cache-ownership + invalidation contract that the rest of the C
increments build on: the node/alias caches live on the injected instance, and
invalidate_nodes() actually clears them (the behavior the ~7 rewired clear-sites
in app.py now rely on instead of rebinding module globals).
"""

import pytest


@pytest.mark.unit
def test_app_store_is_an_injected_wikistore(appmod):
    assert isinstance(appmod.STORE, appmod.WikiStore)


@pytest.mark.unit
def test_wikistore_caches_then_invalidates(appmod, isolated_wiki):
    s = appmod.WikiStore(isolated_wiki.wiki)
    p = s.find_node_path("entropy")
    assert p is not None

    s.load_node(p)
    assert str(p) in s._node_cache            # populated on load
    s.get_alias_registry()
    assert s._alias_registry                  # populated lazily

    s.invalidate_nodes()
    assert s._node_cache == {}                # cleared
    assert s._alias_registry == {}

    # Re-load still works (rebuilds from disk) — invalidation isn't destructive.
    assert s.load_node(p)["slug"] == "entropy"


@pytest.mark.unit
def test_wikistore_is_injected_not_global(appmod, isolated_wiki):
    """A fresh WikiStore pointed at a different wiki is independent of app.STORE —
    the whole point of DI (no shared module-global cache)."""
    s = appmod.WikiStore(isolated_wiki.wiki)
    s.load_node(s.find_node_path("entropy"))
    assert s._node_cache and s is not appmod.STORE


@pytest.mark.unit
def test_wikistore_graph_caches_then_invalidates(appmod, isolated_wiki):
    """C-1b: the graph cache lives on the store and invalidate_graph() clears it,
    then get_graph() rebuilds from disk (non-destructive)."""
    s = appmod.WikiStore(isolated_wiki.wiki)
    g = s.get_graph()
    assert s._graph is not None and g.number_of_nodes() >= 1
    s.invalidate_graph()
    assert s._graph is None
    assert s.get_graph().number_of_nodes() >= 1
