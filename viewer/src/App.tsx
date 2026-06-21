import { useState, useEffect, useRef } from 'react'
import type { View, NodeType, SearchResult, DocMeta } from './types'
import { resolveSlug, getDocs } from './lib/api'
import { useAuth } from './lib/useAuth'
import TopBar from './components/TopBar'
import FilterStrip from './components/FilterStrip'
import DomainStrip from './components/DomainStrip'
import Sidebar from './components/Sidebar'
import RightRail from './components/RightRail'
import { useRecent } from './lib/useRecent'
import NavDrawer from './components/NavDrawer'
import FacetBar from './components/FacetBar'
import Fab from './components/Fab'
import DetailSheet from './components/DetailSheet'
import CaptureSheet from './components/CaptureSheet'
import EditSheet from './components/EditSheet'
import SearchResults from './components/SearchResults'
import BrowseView from './views/BrowseView'
import ClustersView from './views/ClustersView'
import PriorityView from './views/PriorityView'
import GraphView from './views/GraphView'
import ExplainersView from './views/ExplainersView'
import DocsView from './views/DocsView'
import InboxView from './views/InboxView'
import AskView from './views/AskView'
import ReaderView from './views/ReaderView'
import ExplainerOverlay from './components/ExplainerOverlay'

export default function App() {
  const [view, setView]               = useState<View>('browse')
  const [selectedIri, setSelectedIri] = useState<string | null>(null)
  const [captureOpen, setCaptureOpen] = useState(false)
  const [editIri, setEditIri]         = useState<string | null>(null)
  const [typeFilter, setTypeFilter]   = useState<NodeType | 'all'>('all')
  const [domainFilter, setDomainFilter] = useState<string>('all')
  const [clusterFilter, setClusterFilter] = useState<string>('all')
  const [searchResults, setSearchResults] = useState<SearchResult[] | null>(null)
  const [readerSlug, setReaderSlug] = useState<string | null>(null)
  const [explainer, setExplainer] = useState<{ slug: string; title?: string } | null>(null)
  // Mobile nav drawer + docs state (lifted so the drawer can host the doc tree).
  const [drawerOpen, setDrawerOpen] = useState(false)
  const [docManifest, setDocManifest] = useState<DocMeta[] | null>(null)
  const [docKey, setDocKey] = useState<string | null>(null)
  const [topHidden, setTopHidden] = useState(false)   // auto-hide TopBar on scroll
  const lastScroll = useRef(0)
  // Back-gesture integration. PKIS is an SPA, so we mirror navigation into the
  // browser history: every forward step snapshots the prior navigable state and
  // pushes a history entry; the back gesture/button pops it and restores that
  // snapshot. Back thus retraces the path — node→node, view→view, search — and
  // only exits the app once the stack is empty.
  const histStack = useRef<Array<() => void>>([])  // restorers, top = last
  const sheetBase = useRef<number | null>(null)    // stack depth when the node sheet opened
  const popTarget = useRef<number | null>(null)    // target depth for a chained "close sheet" unwind
  const { auth, canWrite, isOwner, signIn, signOut } = useAuth()
  const recent = useRecent()

  // Load the docs manifest once; default to the first doc so Docs never opens empty.
  useEffect(() => {
    getDocs().then((m) => {
      setDocManifest(m)
      setDocKey((k) => k ?? (m.length ? m[0].key : null))
    }).catch(() => {})
  }, [])

  // Owner-only views: if the inbox is open and the user isn't (or is no longer) the
  // owner — e.g. they signed out — fall back to browse.
  useEffect(() => { if (view === 'inbox' && !isOwner) setView('browse') }, [view, isOwner])

  // Capture the current navigable state as a restorer. Running it returns the app
  // to exactly this state (closing/reopening sheets, restoring view + node + search).
  // The nav drawer is excluded — it's transient and always restored closed.
  const snapshot = () => {
    const s = { view, selectedIri, readerSlug, explainer, editIri, captureOpen, search: searchResults }
    return () => {
      setView(s.view); setSelectedIri(s.selectedIri); setReaderSlug(s.readerSlug)
      setExplainer(s.explainer); setEditIri(s.editIri); setCaptureOpen(s.captureOpen)
      setSearchResults(s.search); setDrawerOpen(false)
    }
  }

  // A forward step: remember how to return to the current state, then apply the
  // change. When the drawer is open, reuse its history entry instead of stacking a
  // new one — picking from the drawer is one logical step, not two.
  const advance = (apply: () => void, reuseDrawerEntry = false) => {
    if (!(reuseDrawerEntry && drawerOpen && histStack.current.length)) {
      histStack.current.push(snapshot())
      window.history.pushState({ d: histStack.current.length }, '')
    }
    apply()
  }

  // The back gesture/button (or a programmatic unwind) fires popstate: pop one
  // entry. During a chained "close whole sheet" unwind we skip the intermediate
  // restores and only apply the final one.
  useEffect(() => {
    const onPop = () => {
      const restore = histStack.current.pop()
      if (popTarget.current != null && histStack.current.length > popTarget.current) {
        window.history.back()   // keep unwinding
        return
      }
      popTarget.current = null
      restore?.()
    }
    window.addEventListener('popstate', onPop)
    return () => window.removeEventListener('popstate', onPop)
  }, [])

  // Clear the node-sheet marker once the sheet is fully closed.
  useEffect(() => { if (!selectedIri) sheetBase.current = null }, [selectedIri])

  // Dismiss the top layer via history (shared by close buttons and the gesture).
  const back = () => { if (histStack.current.length) window.history.back() }

  // Fully close the node sheet, collapsing its entire node-path back to the view.
  const closeSheet = () => {
    if (sheetBase.current == null || histStack.current.length <= sheetBase.current) { back(); return }
    popTarget.current = sheetBase.current
    sheetBase.current = null
    window.history.back()
  }

  // Node permalink: /app/?n=<slug> opens that node's detail on load (public — no
  // auth needed; the graph is read-open). This is what a shared node link hits.
  useEffect(() => {
    const slug = new URLSearchParams(window.location.search).get('n')
    if (slug) resolveSlug(slug).then((iri) => {
      if (iri) { sheetBase.current = histStack.current.length; advance(() => setSelectedIri(iri)) }
    }).catch(() => {})
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const openExplainer = (slug: string, title?: string) =>
    advance(() => setExplainer({ slug, title }))

  // Open a node, or follow a link within the sheet — each is a forward step, so
  // the back gesture retraces the node path. Mark where a fresh sheet began.
  const handleSelectNode = (iri: string) => {
    if (!selectedIri) sheetBase.current = histStack.current.length
    advance(() => setSelectedIri(iri))
  }

  // Navigate to a top-level view; back returns to the previous view. Skip the
  // no-op case (tapping the current view with nothing open) to avoid dead entries.
  const navigate = (v: View) => {
    if (v === view && !drawerOpen && !selectedIri && !searchResults
        && !readerSlug && !explainer && !editIri && !captureOpen) return
    advance(() => {
      setView(v); setSelectedIri(null); setEditIri(null); setExplainer(null)
      setReaderSlug(null); setCaptureOpen(false); setDrawerOpen(false); setSearchResults(null)
    }, true)
  }

  const handleNavigateToGraph = () => navigate('graph')

  // Selecting a domain or cluster applies it as a browse facet (a forward step).
  const browseWith = (apply: () => void) =>
    advance(() => {
      apply(); setView('browse'); setSelectedIri(null); setSearchResults(null); setDrawerOpen(false)
    }, true)
  const handleDomain = (d: string) => browseWith(() => setDomainFilter(d))
  const handleCluster = (slug: string) => browseWith(() => setClusterFilter(slug))

  // Search results are a layer too: the first results push an entry (back clears
  // search); clearing the box consumes it; subsequent keystrokes just update.
  const handleResults = (r: SearchResult[] | null) => {
    if (r !== null && searchResults === null) advance(() => setSearchResults(r))
    else if (r === null && searchResults !== null) back()
    else setSearchResults(r)
  }

  // Search is global: when there are results, show them over any view.
  const showSearch = searchResults !== null
  // The type filter is only meaningful for Browse and search results.
  const showFilter = view === 'browse' || showSearch
  const facetActive = typeFilter !== 'all' || domainFilter !== 'all' || clusterFilter !== 'all'
  const showFacetBar = view === 'browse' && !showSearch && facetActive

  // The Docs view runs a three-pane (tree / article / TOC) layout that wants more
  // room than the app's default body clamp. Widen the shell only while docs is up.
  useEffect(() => {
    document.body.classList.toggle('body-docs', view === 'docs' && !showSearch)
    return () => document.body.classList.remove('body-docs')
  }, [view, showSearch])

  // Switching view (or surfacing search) should always re-reveal the TopBar.
  useEffect(() => { setTopHidden(false); lastScroll.current = 0 }, [view, showSearch])

  // Auto-hide the TopBar while scrolling down inside the main column; reveal it on
  // any upward scroll. Mobile-only in effect — the CSS no-ops it at ≥900px.
  const onMainScroll = (e: React.UIEvent<HTMLDivElement>) => {
    const y = e.currentTarget.scrollTop
    if (y > lastScroll.current && y > 72) setTopHidden(true)
    else if (y < lastScroll.current) setTopHidden(false)
    lastScroll.current = y
  }

  return (
    <>
      <div className="app-shell">
        <Sidebar
          view={view}
          onNavigate={navigate}
          isOwner={isOwner}
          domainFilter={domainFilter}
          onDomain={handleDomain}
          clusterFilter={clusterFilter}
          onCluster={handleCluster}
          onClusterAgenda={() => navigate('clusters')}
        />

        <div className="content-col">
          <TopBar
            onResults={handleResults}
            onNavigate={navigate}
            auth={auth}
            onSignIn={signIn}
            onSignOut={signOut}
            onMenu={() => advance(() => setDrawerOpen(true))}
            hidden={topHidden}
            view={view}
          />
          {showFilter && <FilterStrip active={typeFilter} onChange={setTypeFilter} />}
          {view === 'browse' && !showSearch && (
            <DomainStrip active={domainFilter} onChange={setDomainFilter} />
          )}
          {showFacetBar && (
            <FacetBar
              typeFilter={typeFilter}
              domainFilter={domainFilter}
              clusterFilter={clusterFilter}
              onClearType={() => setTypeFilter('all')}
              onClearDomain={() => setDomainFilter('all')}
              onClearCluster={() => setClusterFilter('all')}
            />
          )}

          <div
            onScroll={onMainScroll}
            className={
              !showSearch && view === 'graph' ? 'main main-graph'
              : !showSearch && view === 'ask' ? 'main main-ask'
              : 'main'
            }>
            {showSearch ? (
              <SearchResults
                results={searchResults!}
                typeFilter={typeFilter}
                onSelectNode={handleSelectNode}
              />
            ) : (
              <>
                {view === 'browse' && (
                  <BrowseView
                    typeFilter={typeFilter}
                    domainFilter={domainFilter}
                    clusterFilter={clusterFilter}
                    onSelectNode={handleSelectNode}
                    onNavigate={navigate}
                    isOwner={isOwner}
                  />
                )}
                {view === 'clusters' && (
                  <ClustersView
                    onSelectNode={handleSelectNode}
                    onDomain={handleDomain}
                    onBrowseCluster={handleCluster}
                  />
                )}
                {view === 'priority' && (
                  <PriorityView onSelectNode={handleSelectNode} />
                )}
                {view === 'graph' && (
                  <GraphView focusIri={selectedIri} onSelectNode={handleSelectNode} />
                )}
                {view === 'explainers' && (
                  <ExplainersView onSelectNode={handleSelectNode} onOpenExplainer={openExplainer} />
                )}
                {view === 'docs' && (
                  <DocsView manifest={docManifest} selected={docKey} onSelect={setDocKey} />
                )}
                {view === 'ask' && (
                  <AskView
                    onSelectNode={handleSelectNode}
                    signedIn={auth.authenticated}
                    onSignIn={signIn}
                  />
                )}
                {view === 'inbox' && isOwner && <InboxView onSelectNode={handleSelectNode} />}
              </>
            )}
          </div>
        </div>

        <RightRail
          recent={recent.items}
          onSelectNode={handleSelectNode}
          onCluster={handleCluster}
          onAgenda={() => navigate('clusters')}
        />
      </div>

      <NavDrawer
        open={drawerOpen}
        onClose={back}
        view={view}
        onNavigate={navigate}
        isOwner={isOwner}
        domainFilter={domainFilter}
        onDomain={handleDomain}
        clusterFilter={clusterFilter}
        onCluster={handleCluster}
        onClusterAgenda={() => navigate('clusters')}
        docManifest={docManifest}
        docKey={docKey}
        onDocSelect={setDocKey}
      />

      {canWrite && view !== 'ask' && (
        <Fab onClick={() => advance(() => setCaptureOpen(true))} />
      )}

      {selectedIri && (
        <DetailSheet
          iri={selectedIri}
          onClose={closeSheet}
          onNavigate={handleSelectNode}
          onEdit={() => advance(() => setEditIri(selectedIri))}
          onGraph={handleNavigateToGraph}
          onListen={(slug) => advance(() => setReaderSlug(slug))}
          onOpenExplainer={openExplainer}
          onView={recent.record}
        />
      )}

      {readerSlug && (
        <ReaderView slug={readerSlug} onClose={back} />
      )}

      {explainer && (
        <ExplainerOverlay slug={explainer.slug} title={explainer.title} onClose={back} />
      )}

      {captureOpen && (
        <CaptureSheet onClose={back} canWrite={canWrite} onSignIn={signIn} />
      )}

      {editIri && (
        <EditSheet
          iri={editIri}
          onClose={back}
        />
      )}
    </>
  )
}
