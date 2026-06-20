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
import BottomNav from './components/BottomNav'
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

  // Node permalink: /app/?n=<slug> opens that node's detail on load (public — no
  // auth needed; the graph is read-open). This is what a shared node link hits.
  useEffect(() => {
    const slug = new URLSearchParams(window.location.search).get('n')
    if (slug) resolveSlug(slug).then((iri) => { if (iri) setSelectedIri(iri) }).catch(() => {})
  }, [])

  const openExplainer = (slug: string, title?: string) => setExplainer({ slug, title })

  const handleSelectNode = (iri: string) => setSelectedIri(iri)

  // Navigating must also dismiss any open overlay (a node detail sheet or active
  // search results) — otherwise the view changes UNDERNEATH the sheet, which keeps
  // covering the screen, and the nav button looks like it failed.
  const navigate = (v: View) => {
    setSelectedIri(null)
    setSearchResults(null)
    setView(v)
  }

  const handleNavigateToGraph = () => {
    setView('graph')
    setSelectedIri(null)
  }

  // Selecting a domain or cluster (from the sidebar or a cluster cross-link)
  // applies it as a browse facet and surfaces the faceted browse.
  const browseWith = (apply: () => void) => { apply(); setView('browse'); setSearchResults(null) }
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
            onMenu={() => setDrawerOpen(true)}
            hidden={topHidden}
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
        onClose={() => setDrawerOpen(false)}
        view={view}
        domainFilter={domainFilter}
        onDomain={handleDomain}
        clusterFilter={clusterFilter}
        onCluster={handleCluster}
        onClusterAgenda={() => { setView('clusters'); setSearchResults(null) }}
        docManifest={docManifest}
        docKey={docKey}
        onDocSelect={setDocKey}
      />

      <BottomNav active={view} onNavigate={navigate} isOwner={isOwner} />
      {view !== 'ask' && <Fab onClick={() => setCaptureOpen(true)} />}

      {selectedIri && (
        <DetailSheet
          iri={selectedIri}
          onClose={() => setSelectedIri(null)}
          onNavigate={(iri) => setSelectedIri(iri)}
          onEdit={() => setEditIri(selectedIri)}
          onGraph={handleNavigateToGraph}
          onListen={(slug) => setReaderSlug(slug)}
          onOpenExplainer={openExplainer}
        />
      )}

      {readerSlug && (
        <ReaderView slug={readerSlug} onClose={() => setReaderSlug(null)} />
      )}

      {explainer && (
        <ExplainerOverlay slug={explainer.slug} title={explainer.title} onClose={() => setExplainer(null)} />
      )}

      {captureOpen && (
        <CaptureSheet onClose={() => setCaptureOpen(false)} canWrite={canWrite} onSignIn={signIn} />
      )}

      {editIri && (
        <EditSheet
          iri={editIri}
          onClose={() => setEditIri(null)}
        />
      )}
    </>
  )
}
