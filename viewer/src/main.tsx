import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import ShareView from './views/ShareView'
import './index.css'

// Lightweight routing via query params (no router dep, no nginx change — the same
// /app/ index serves every variant). A `?s=<token>` link renders the public,
// read-only ShareView instead of the app.
const shareToken = new URLSearchParams(window.location.search).get('s')

// Service workers are DISABLED: a previous cache-first SW poisoned the app shell
// (served a stale index.html pointing at removed asset hashes -> blank screen).
// Unregister any SW that remains so the app always loads fresh from the network.
// (Offline caching for the reader will return later via a correctly-scoped SW.)
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.getRegistrations()
    .then((regs) => regs.forEach((r) => r.unregister()))
    .catch(() => {})
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    {shareToken ? <ShareView token={shareToken} /> : <App />}
  </React.StrictMode>,
)
