import { useState } from 'react'
import type { View, NodeType, SearchResult } from './types'
import TopBar from './components/TopBar'
import FilterStrip from './components/FilterStrip'
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

export default function App() {
  const [view, setView]               = useState<View>('browse')
  const [selectedIri, setSelectedIri] = useState<string | null>(null)
  const [captureOpen, setCaptureOpen] = useState(false)
  const [editIri, setEditIri]         = useState<string | null>(null)
  const [typeFilter, setTypeFilter]   = useState<NodeType | 'all'>('all')
  const [searchResults, setSearchResults] = useState<SearchResult[] | null>(null)

  const handleSelectNode = (iri: string) => setSelectedIri(iri)

  const handleNavigateToGraph = () => {
    setView('graph')
    setSelectedIri(null)
  }

  // Search is global: when there are results, show them over any view.
  const showSearch = searchResults !== null
  // The type filter is only meaningful for Browse and search results.
  const showFilter = view === 'browse' || showSearch

  return (
    <>
      <TopBar
        onResults={setSearchResults}
        onNavigate={setView}
        activeView={view}
      />
      {showFilter && <FilterStrip active={typeFilter} onChange={setTypeFilter} />}

      <div className={view === 'graph' && !showSearch ? 'main main-graph' : 'main'}>
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
                onSelectNode={handleSelectNode}
                onNavigate={setView}
              />
            )}
            {view === 'clusters' && (
              <ClustersView onSelectNode={handleSelectNode} />
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
          </>
        )}
      </div>

      <BottomNav active={view} onNavigate={setView} />
      <Fab onClick={() => setCaptureOpen(true)} />

      {selectedIri && (
        <DetailSheet
          iri={selectedIri}
          onClose={() => setSelectedIri(null)}
          onNavigate={(iri) => setSelectedIri(iri)}
          onEdit={() => setEditIri(selectedIri)}
          onGraph={handleNavigateToGraph}
        />
      )}

      {captureOpen && (
        <CaptureSheet onClose={() => setCaptureOpen(false)} />
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
