import { useState, useEffect, useCallback } from 'react'
import { getAuth, logout as apiLogout, signInUrl, type AuthState } from './api'
import { isNative, signInNative, restoreNativeSession, initNativeAuthListener } from './nativeAuth'

// Sign-in state. On web the backend refreshes the sealed session transparently and
// the frontend just reflects /auth/me. On native (Capacitor APK) the same /auth/me
// reflects the PKIS bearer token: we restore a stored session on launch and drive
// sign-in through the system-browser PKCE flow (see nativeAuth.ts).
export function useAuth() {
  const [auth, setAuth] = useState<AuthState>({ authenticated: false, role: 'reader' })
  const [loaded, setLoaded] = useState(false)

  const refresh = useCallback(async () => {
    setAuth(await getAuth())
    setLoaded(true)
  }, [])

  useEffect(() => {
    let cancelled = false
    async function boot() {
      if (isNative()) {
        // Deep-link handler fires after a fresh sign-in; restore any stored session
        // before reflecting state so a returning user lands signed-in.
        initNativeAuthListener(() => { void refresh() })
        await restoreNativeSession()
      }
      if (!cancelled) await refresh()
    }
    void boot()
    return () => { cancelled = true }
  }, [refresh])

  const signIn = useCallback(() => {
    if (isNative()) {
      void signInNative()   // completion arrives via the deep-link listener → refresh()
    } else {
      window.location.href = signInUrl(window.location.pathname || '/app/')
    }
  }, [])

  const signOut = useCallback(async () => {
    await apiLogout()
    await refresh()
  }, [refresh])

  const canWrite = auth.authenticated && (auth.role === 'owner' || auth.role === 'writer')
  const isOwner = auth.authenticated && auth.role === 'owner'   // gates the admin inbox
  return { auth, loaded, canWrite, isOwner, refresh, signIn, signOut }
}
