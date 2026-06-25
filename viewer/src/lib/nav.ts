import type { View } from '../types'

export interface NavItem {
  view: View
  icon: string
  label: string
  admin?: boolean   // owner-only (administrative) — hidden unless role === 'owner'
}

// The view set, shared by the desktop Sidebar and the mobile NavDrawer so nav
// stays DRY. `ask` is intentionally NOT here — it lives as a quick icon in the
// TopBar (next to search), since it's the most-reached action.
export const NAV_ITEMS: NavItem[] = [
  { view: 'browse',     icon: '◈', label: 'browse',   },
  { view: 'clusters',   icon: '◎', label: 'clusters', },
  { view: 'priority',   icon: '▲', label: 'priority', },
  { view: 'graph',      icon: '⬡', label: 'graph',    },
  { view: 'explainers', icon: '▦', label: 'assets',   },
  { view: 'docs',       icon: '▤', label: 'docs',     },
  { view: 'inbox',      icon: '✉', label: 'inbox',    admin: true },
  { view: 'lab',        icon: '⚗', label: 'lab',      admin: true },
]

// Nav items visible to the current user — admin (owner-only) items hidden otherwise.
export const navFor = (isOwner: boolean) => NAV_ITEMS.filter((n) => !n.admin || isOwner)
