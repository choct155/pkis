import type { View } from '../types'

export interface NavItem {
  view: View
  icon: string
  label: string
  group: 'primary' | 'secondary'
  admin?: boolean   // owner-only (administrative) — hidden unless role === 'owner'
}

// Shared by BottomNav (mobile) and Sidebar (desktop) so the nav set stays DRY.
// `group` drives the mobile split: primary items sit in the bottom bar, secondary
// items fold into the "more" menu. The desktop Sidebar shows them all (NAV_ITEMS).
export const NAV_ITEMS: NavItem[] = [
  { view: 'browse',     icon: '◈', label: 'browse',   group: 'primary' },
  { view: 'clusters',   icon: '◎', label: 'clusters', group: 'primary' },
  { view: 'priority',   icon: '▲', label: 'priority', group: 'primary' },
  { view: 'graph',      icon: '⬡', label: 'graph',    group: 'primary' },
  { view: 'staged',     icon: '⊞', label: 'staged',   group: 'secondary' },
  { view: 'explainers', icon: '▦', label: 'explain',  group: 'secondary' },
  { view: 'discover',   icon: '✦', label: 'discover', group: 'secondary' },
  { view: 'docs',       icon: '▤', label: 'docs',     group: 'secondary' },
  { view: 'inbox',      icon: '✉', label: 'inbox',    group: 'secondary', admin: true },
]

export const PRIMARY_NAV = NAV_ITEMS.filter((n) => n.group === 'primary')
export const SECONDARY_NAV = NAV_ITEMS.filter((n) => n.group === 'secondary')

// Nav items visible to the current user — admin (owner-only) items hidden otherwise.
export const navFor = (isOwner: boolean) => NAV_ITEMS.filter((n) => !n.admin || isOwner)
