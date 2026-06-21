import { useState, useEffect, useRef } from 'react'
import type { View, NodeType, SearchResult, DocMeta } from './types'
import { resolveSlug, getDocs } from './lib/api'
import { useAuth } from './lib/useAuth'
import TopBar from './components/TopBar'
import FilterStrip from './components/FilterStrip'
import DomainStrip from './components/DomainStrip'
import Sidebar from './components/Sidebar'
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
  // Back-gesture integration: a stack of "closers" for the currently-open
  // dismissible layers (sheets, overlays, drawer), top = last. Each open pushes
  // a browser history entry; the system back gesture / button pops the top one.
  const backStack = useRef<Array<() => void>>([])
  const { auth, canWrite, isOwner, signIn, signOut } = useAuth()

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

  // Open a dismissible layer: run `setState` to show it and push a history entry
  // whose closer reverses it, so the back gesture pops it. Skips the push if the
  // layer is already open (avoids a stray "dead" back press).
  const openLayer = (alreadyOpen: boolean, show: () => void, close: () => void) => {
    show()
    if (!alreadyOpen) {
      backStack.current.push(close)
      window.history.pushState({ d: backStack.current.length }, '')
    }
  }

  // Dismiss the top layer from a UI control (close button / backdrop) by routing
  // through history.back(), so the popstate handler does the actual close — the
  // exact same path as a real back gesture. No-op if nothing is open.
  const back = () => { if (backStack.current.length) window.history.back() }

  // The system back gesture / button fires popstate: close the top layer.
  useEffect(() => {
    const onPop = () => { backStack.current.pop()?.() }
    window.addEventListener('popstate', onPop)
    return () => window.removeEventListener('popstate', onPop)
  }, [])

  // Node permalink: /app/?n=<slug> opens that node's detail on load (public — no
  // auth needed; the graph is read-open). This is what a shared node link hits.
  useEffect(() => {
    const slug = new URLSearchParams(window.location.search).get('n')
    if (slug) resolveSlug(slug).then((iri) => {
      if (iri) openLayer(false, () => setSelectedIri(iri), () => setSelectedIri(null))
    }).catch(() => {})
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const openExplainer = (slug: string, title?: string) =>
    openLayer(!!explainer, () => setExplainer({ slug, title }), () => setExplainer(null))

  const handleSelectNode = (iri: string) =>
    openLayer(!!selectedIri, () => setSelectedIri(iri), () => setSelectedIri(null))

  // Navigate to a top-level view: collapse every open layer (closing them and
  // rewinding their history entries in one step) so the view changes cleanly and
  // the back stack stays in sync, then switch.
  const navigate = (v: View) => {
    const depth = backStack.current.length
    backStack.current = []
    setSelectedIri(null); setEditIri(null); setExplainer(null)
    setReaderSlug(null); setCaptureOpen(false); setDrawerOpen(false)
    setSearchResults(null)
    setView(v)
    if (depth) window.history.go(-depth)
  }

  const handleNavigateToGraph = () => navigate('graph')

  // Selecting a domain or cluster (from the sidebar or a cluster cross-link)
  // applies it as a browse facet and surfaces the faceted browse.
  const browseWith = (apply: () => void) => { apply(); navigate('browse') }
  const handleDomain = (d: string) => browseWith(() => setDomainFilter(d))
  const handleCluster = (slug: string) => browseWith(() => setClusterFilter(slug))

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
          onClusterAgenda={() => setView('clusters')}
        />

        <div className="content-col">
          <TopBar
            onResults={setSearchResults}
            onNavigate={navigate}
            auth={auth}
            onSignIn={signIn}
            onSignOut={signOut}
            onMenu={() => openLayer(drawerOpen, () => setDrawerOpen(true), () => setDrawerOpen(false))}
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

      {view !== 'ask' && (
        <Fab onClick={() => openLayer(captureOpen, () => setCaptureOpen(true), () => setCaptureOpen(false))} />
      )}

      {selectedIri && (
        <DetailSheet
          iri={selectedIri}
          onClose={back}
          onNavigate={(iri) => setSelectedIri(iri)}
          onEdit={() => openLayer(!!editIri, () => setEditIri(selectedIri), () => setEditIri(null))}
          onGraph={handleNavigateToGraph}
          onListen={(slug) => openLayer(!!readerSlug, () => setReaderSlug(slug), () => setReaderSlug(null))}
          onOpenExplainer={openExplainer}
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
