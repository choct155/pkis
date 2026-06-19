import { useState, useEffect } from 'react'
import type { View, NodeType, SearchResult } from './types'
import { useAuth } from './lib/useAuth'
import TopBar from './components/TopBar'
import FilterStrip from './components/FilterStrip'
import DomainStrip from './components/DomainStrip'
import Sidebar from './components/Sidebar'
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
import StagedView from './views/StagedView'
import ExplainersView from './views/ExplainersView'
import DiscoverView from './views/DiscoverView'
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
  const { auth, canWrite, isOwner, signIn, signOut } = useAuth()

  // Owner-only views: if the inbox is open and the user isn't (or is no longer) the
  // owner — e.g. they signed out — fall back to browse.
  useEffect(() => { if (view === 'inbox' && !isOwner) setView('browse') }, [view, isOwner])

  const openExplainer = (slug: string, title?: string) => setExplainer({ slug, title })

  const handleSelectNode = (iri: string) => setSelectedIri(iri)

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

  return (
    <>
      <div className="app-shell">
        <Sidebar
          view={view}
          onNavigate={setView}
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
            onNavigate={setView}
            activeView={view}
            auth={auth}
            onSignIn={signIn}
            onSignOut={signOut}
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

          <div className={
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
                    onNavigate={setView}
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
                {view === 'staged' && (
                  <StagedView onSelectNode={handleSelectNode} />
                )}
                {view === 'explainers' && (
                  <ExplainersView onSelectNode={handleSelectNode} onOpenExplainer={openExplainer} />
                )}
                {view === 'discover' && (
                  <DiscoverView onSelectNode={handleSelectNode} />
                )}
                {view === 'docs' && <DocsView />}
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

      <BottomNav active={view} onNavigate={setView} isOwner={isOwner} />
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
