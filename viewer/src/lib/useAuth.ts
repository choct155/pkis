import { useState, useEffect, useCallback } from 'react'
import { getAuth, logout as apiLogout, signInUrl, type AuthState } from './api'

// Web sign-in state. The backend refreshes the sealed session transparently, so
// the frontend never handles tokens — it just reflects /auth/me and offers a
// (silent-SSO) sign-in redirect. The user authenticates at most once.
export function useAuth() {
  const [auth, setAuth] = useState<AuthState>({ authenticated: false, role: 'reader' })
  const [loaded, setLoaded] = useState(false)

  const refresh = useCallback(async () => {
    setAuth(await getAuth())
    setLoaded(true)
  }, [])

  useEffect(() => { refresh() }, [refresh])

  const signIn = useCallback(() => {
    window.location.href = signInUrl(window.location.pathname || '/app/')
  }, [])

  const signOut = useCallback(async () => {
    await apiLogout()
    await refresh()
  }, [refresh])

  const canWrite = auth.authenticated && (auth.role === 'owner' || auth.role === 'writer')
  return { auth, loaded, canWrite, refresh, signIn, signOut }
}
