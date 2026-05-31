import { useState, useCallback, useRef } from 'react'
import { searchWiki } from '../lib/api'
import type { SearchResult, View } from '../types'

interface Props {
  onResults: (results: SearchResult[] | null) => void
  onNavigate: (view: View) => void
  activeView: View
}

export default function TopBar({ onResults, onNavigate, activeView }: Props) {
  const [query, setQuery] = useState('')
  const [searching, setSearching] = useState(false)
  const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null)

  const handleChange = useCallback(
    (val: string) => {
      setQuery(val)
      if (debounceRef.current) clearTimeout(debounceRef.current)
      if (!val.trim()) {
        onResults(null)
        return
      }
      debounceRef.current = setTimeout(async () => {
        setSearching(true)
        try {
          const results = await searchWiki(val.trim(), { max_results: 20 })
          onResults(results)
        } catch {
          onResults([])
        } finally {
          setSearching(false)
        }
      }, 300)
    },
    [onResults]
  )

  return (
    <div className="topbar">
      <div className="topbar-logo">PKIS</div>
      <div className="search-wrap">
        <span className="search-icon">{searching ? '⟳' : '⌕'}</span>
        <input
          className="search-input"
          type="search"
          placeholder="search nodes…"
          value={query}
          onChange={(e) => handleChange(e.target.value)}
          onKeyDown={(e) => e.key === 'Escape' && handleChange('')}
        />
      </div>
      <div
        className={`icon-btn${activeView === 'graph' ? ' active' : ''}`}
        onClick={() => onNavigate(activeView === 'graph' ? 'browse' : 'graph')}
        title="Graph view"
      >
        ⬡
      </div>
    </div>
  )
}
