import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

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
    <App />
  </React.StrictMode>,
)
