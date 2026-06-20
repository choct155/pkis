import { useState, useCallback, useRef } from 'react'
import { searchWiki, type AuthState } from '../lib/api'
import type { SearchResult, View } from '../types'

interface Props {
  onResults: (results: SearchResult[] | null) => void
  onNavigate: (view: View) => void
  auth: AuthState
  onSignIn: () => void
  onSignOut: () => void
}

export default function TopBar({ onResults, onNavigate, auth, onSignIn, onSignOut }: Props) {
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
          let results
          try {
            results = await searchWiki(val.trim(), { max_results: 20 })
          } catch {
            // one retry — a transient blip shouldn't masquerade as "no results"
            await new Promise((r) => setTimeout(r, 400))
            results = await searchWiki(val.trim(), { max_results: 20 })
          }
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

  const handleHome = () => {
    setQuery('')
    if (debounceRef.current) clearTimeout(debounceRef.current)
    onResults(null)
    onNavigate('browse')
  }

  return (
    <div className="topbar">
      <div className="topbar-logo" onClick={handleHome} title="Home" role="button">PKIS</div>
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
      {auth.authenticated ? (
        <div
          className="account-btn"
          onClick={onSignOut}
          title={`Signed in (${auth.role}) — click to sign out`}
        >
          <span className="account-dot" /> {auth.role}
        </div>
      ) : (
        <div className="account-btn signin" onClick={onSignIn} title="Sign in to write">
          sign in
        </div>
      )}
    </div>
  )
}
