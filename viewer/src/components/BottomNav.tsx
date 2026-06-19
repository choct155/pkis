import { useState } from 'react'
import type { View } from '../types'
import { PRIMARY_NAV, SECONDARY_NAV } from '../lib/nav'

interface Props {
  active: View
  onNavigate: (v: View) => void
  isOwner: boolean
}

// Mobile bottom bar: the four primary views, plus a "more" button that reveals the
// secondary views in a popover (keeps the bar from crowding as views are added).
export default function BottomNav({ active, onNavigate, isOwner }: Props) {
  const [moreOpen, setMoreOpen] = useState(false)
  // Admin (owner-only) items — e.g. the inbox — are hidden unless signed in as owner.
  const secondary = SECONDARY_NAV.filter((n) => !n.admin || isOwner)
  const secondaryActive = secondary.some((n) => n.view === active)

  const go = (v: View) => { onNavigate(v); setMoreOpen(false) }

  return (
    <>
      {moreOpen && <div className="more-backdrop" onClick={() => setMoreOpen(false)} />}
      {moreOpen && (
        <div className="more-menu">
          {secondary.map(({ view, icon, label }) => (
            <div
              key={view}
              className={`more-item${active === view ? ' active' : ''}`}
              onClick={() => go(view)}
            >
              <span className="more-icon">{icon}</span>
              <span className="more-label">{label}</span>
            </div>
          ))}
        </div>
      )}
      <nav className="bottom-nav">
        {PRIMARY_NAV.map(({ view, icon, label }) => (
          <div
            key={view}
            className={`nav-item${active === view ? ' active' : ''}`}
            onClick={() => go(view)}
          >
            <div className="nav-icon">{icon}</div>
            <div className="nav-label">{label}</div>
          </div>
        ))}
        <div
          className={`nav-item${moreOpen || secondaryActive ? ' active' : ''}`}
          onClick={() => setMoreOpen((o) => !o)}
        >
          <div className="nav-icon">⋯</div>
          <div className="nav-label">more</div>
        </div>
      </nav>
    </>
  )
}
