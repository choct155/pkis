import type { CapacitorConfig } from '@capacitor/cli'

// PKIS native shell config. The React/Vite UI is built to `app/dist/` (webDir)
// and bundled into the APK; the Flask backend is reached over the network
// (LAN/emulator in dev, VPN/HTTPS in prod) via VITE_API_BASE_URL — not served
// from here. Build the web bundle for native with `CAP_BUILD=1 npm run build`
// so Vite emits relative asset paths (base '') instead of the web '/app/' base.
const config: CapacitorConfig = {
  appId: 'com.pkis.app',
  appName: 'PKIS',
  webDir: 'app/dist',
  plugins: {
    // The UI is served from https://localhost inside the WebView, but the API may
    // be plain HTTP on the LAN — a mixed-content + cross-origin request the WebView
    // blocks. CapacitorHttp patches window.fetch to make the call from native code,
    // sidestepping both. Cleartext (HTTP) is still gated by the Android network
    // security config; prod should use HTTPS.
    CapacitorHttp: {
      enabled: true,
    },
  },
}

export default config
